"""Library Imports."""

import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# ------- Flask App Configuration -------

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# ------- Pagination -------

"""
Pagination adapted from:
    https://github.com/Sharon-B/Recipe-Box/blob/master/app.py
"""


PER_PAGE = 4


def paginated(recipes):
    """Pagination config."""
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    offset = page * PER_PAGE - PER_PAGE

    return recipes[offset: offset + PER_PAGE]


def pagination_args(recipes):
    """Pagination config."""
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    total = len(recipes)

    return Pagination(page=page, per_page=PER_PAGE,
                      css_framework='bootstrap5', total=total)


# ------- Check User Login Function -------
def login_required(f):
    """
    Login_required decorator adapted from TravelTimN.

    https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/#login-required-decorator
    https://github.com/TravelTimN/flask-task-manager-project/blob/demo/app.py
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):

        # User NOT logged in
        if "user" not in session:
            flash("Please log in to view this page!")
            return redirect(url_for("login"))

        # User IS logged in
        return f(*args, **kwargs)

    return decorated_function


# ------- Home Page -------


@app.route("/")
def index():
    """Home page displays  the 4 latest recipes."""
    latest_recipes = mongo.db.recipes.find().sort("_id", -1).limit(3)
    return render_template("index.html", recipes=latest_recipes)


# ------- Get Recipes Page -------

@app.route("/get_recipes")
def get_recipes():
    """Get recipes page  all recipes with pagination and search function."""
    recipes = list(mongo.db.recipes.find())
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)

    return render_template('recipes.html',
                           recipes=recipes_paginated,
                           pagination=pagination)


'#global variable'

search_term = ''


# ------- Search Function -------


@app.route("/search", methods=['GET', 'POST'])
def search():
    """Search function to allow users to search recipes or ingredients."""
    global search_term
    query = request.form.get("query")

    '#check if query is present or use previously saved search term'
    if query:
        search_term = query
    else:
        query = search_term

    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    results_count = len(recipes)

    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)

    return render_template('search.html',
                           recipes=recipes_paginated,
                           query=query,
                           results_count=results_count,
                           pagination=pagination)


# ------- Register Function -------


@app.route("/register", methods=["GET", "POST"])
def register():
    """Allow user to register an account."""
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
          {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("register"))
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration succesful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# ------- Login Function -------


@app.route("/login", methods=["GET", "POST"])
def login():
    """Allow registered users to login."""
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matched the password the user has input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                                        session["user"] = request.form.get(
                                                            "username").lower()
                                        flash("Welcome, {}".format(
                                            request.form.get("username")))
                                        return redirect(url_for("profile",
                                                        username=session[
                                                                    "user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("User doesn't exist")
            return redirect(url_for("login"))

    return render_template("login.html")


# ------- User Profile Page -------


@app.route("/profile", methods=["GET", "POST"])
def profile():
    """Allow user to view profile."""
    if "user" in session:
        return render_template("profile.html", username=session["user"])

    return redirect(url_for("login"))


# ------- Log out Function -------


@app.route("/logout")
def logout():
    """Allow user to log out."""
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# ------- Edit Profile Function -------


@app.route("/edit_profile/<username>", methods=["GET", "POST"])
@login_required
def edit_profile(username):
    """
    Allow user to edit their account settings.

        - Change Password
        - Delete Account
    """
    user = mongo.db.users.find_one_or_404(
        {"username": session["user"]})

    if session["user"] == username:

        # Update profile function
        if request.method == "POST":

            mongo.db.users.update_one({'username': session['user']},
                                      {'$set': {
                                          'password': generate_password_hash(
                                              request.form.get("password"))
                                      }})

            flash("Account Updated! Log back in to confirm changes.".format(
                    request.form.get("username")))
            session.pop("user")
            return render_template("login.html",
                                   title="Login")

        return render_template("edit_profile.html",
                               user=user,
                               title="Edit Account")

    else:
        # if wrong user
        flash("You do not have permission to view this page")
        return redirect(url_for("recipes",
                                username=session["user"]))


# ------- Delete User Profile -------


@app.route("/delete_profile/<username>")
@login_required
def delete_profile(username):
    """Allow user to delete profile."""
    if session["user"] == username:
        mongo.db.users.remove(
            {"username": username.lower()})
        flash("Profile Deleted")
        session.pop("user")

        return redirect(url_for("register"))

    else:
        # if wrong user
        flash("You do not have permission to do that!")
        return redirect(url_for("recipes",
                                username=session["user"]))


# ------- Add recipe function -------

@app.route("/add_recipe", methods=["GET", "POST"])
@login_required
def add_recipe():
    """Users can upload new recipe."""
    user = mongo.db.users.find_one(
        {"username": session["user"]})

    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_image": request.form.get("recipe_image"),
            "category": request.form.get("category"),
            "serving": request.form.get("serving"),
            "time": request.form.get("time"),
            "recipe_ingredients": request.form.getlist("recipe_ingredients"),
            "method": request.form.getlist("method"),
            "created_by": session["user"]
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Added!")
        return redirect(url_for("get_recipes"))

    return render_template("add_recipe.html", user=user)


# ------- Recipe Page -------

@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    """Display the full recipe."""
    recipe = mongo.db.recipes.find_one_or_404(
        {"_id": ObjectId(recipe_id)})

    return render_template("recipe.html", recipe=recipe)


# ------- User recipes Page -------


@app.route("/my_recipes/<username>", methods=["GET", "POST"])
@login_required
def my_recipes(username):
    """Allow users to view the recipes they have added."""
    if session["user"] == username:

        # user variable for user image
        user = mongo.db.users.find_one(
            {"username": session["user"]})

        recipes = list(
            mongo.db.recipes.find(
                {"created_by": username.lower()}))

        recipes_paginated = paginated(recipes)
        pagination = pagination_args(recipes)

    else:
        # if wrong user
        flash("You cannot view this page!")
        return redirect(url_for("recipes",
                                username=session["user"]))

    return render_template("my_recipes.html",
                           user=user,
                           recipes=recipes_paginated,
                           pagination=pagination)


# ------- Edit recipe function -------

@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
        """Allow users to edit their own recipes."""
        user = mongo.db.users.find_one(
                {"username": session["user"]})

        recipe = mongo.db.recipes.find_one(
                 {"_id": ObjectId(recipe_id)})

        if session["user"] == recipe["created_by"] or user["is_admin"]:

            if request.method == "POST":
                mongo.db.recipes.update_one(
                    {"_id": ObjectId(recipe_id)}, {
                        '$set': {
                                "recipe_name": request.form.get("recipe_name"),
                                "recipe_image": request.form.get(
                                                    "recipe_image"),
                                "category": request.form.get("category"),
                                "serving": request.form.get("serving"),
                                "time": request.form.get("time"),
                                "recipe_ingredients": request.form.getlist(
                                                     "recipe_ingredients"),
                                "method": request.form.getlist("method"),
                                "created_by": session["user"]
                            }
                    })

                flash("{} Recipe Updated!".format(
                            request.form.get("recipe_name")))

                return redirect(url_for("recipe", recipe_id=recipe_id))

            return render_template("edit_recipe.html",
                                   recipe=recipe, user=user)

        else:
            # if wrong user
            flash("You do not have permission to view this page")
            return redirect(url_for('recipe', recipe_id=recipe_id))


# ------- Delete recipe function -------

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """Allow users to delete their recipes."""
    user = mongo.db.users.find_one(
        {"username": session["user"]})

    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})

    if session["user"] == recipe["created_by"] or "admin":

        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})

        flash("Recipe Deleted")
        return redirect(url_for("my_recipes",
                                username=session["user"]))

    else:
        # if wrong user
        flash("You cannot view this page")
        return redirect(url_for('recipe',
                                recipe_id=recipe_id))


# ------- Declaration of special variables -------


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
