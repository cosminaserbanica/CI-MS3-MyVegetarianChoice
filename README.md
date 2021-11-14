# My Vegetarian Choice

![My Vegetarian Choice Mockup Images](/static/images/mockup.PNG)

[View the live project here](https://my-vegetarian-choice.herokuapp.com/)

### Table of contents
1. [UX](#UX)
     1. [Project Goals](#Project-Goals)
     2. [User Stories](#User-Stories)
     3. [Development Planes](#Development-Planes)
2. [Database Info](#Database-Info)
     1. [Users Collection](#Users-Collection)
     2. [Recipes Collection](#Recipes-Collection)
3. [Design Features](#Design-Features)
4. [Technologies Used](#Technologies-Used)
     1. [Languages](#Languages)
     2. [Tools](#Tools)
     3. [Libraries](#Libraries)
     4. [Database Management](#Database-Management)
5. [Testing](#Testing)
     1. [Testing.md](testing.md)
6. [Deployment](#Deployment)
     1. [1. Database Creation](#1-Database-Creation)
     2. [2. Local Copy Creation](#2-Local-Copy-Creation)
     3. [3. Heroku App Creation](#3-Heroku-App-Creation)
7. [Credits](#Credits)
8. [Acknowledgements](#Acknowledgements)
***

## UX 
### Project Goals
The main goal of **My Vegetarian Choice** is to provide a web-based application, that is simplistic and intuitive in design, which allows users to **create**, **search**, **update** and share their **favourite** vegetarian recipes.

This is the third of four Milestone Projects that the developer must complete during their Full Stack Web Development Program at The Code Institute. 

The main requirements were to build a full-stack web application that allows users to manage a common dataset (in this instance, vegetarian recipes) using **HTML5**, **CSS3**, **JavaScript**, **Python**, **Flask** and **MongoDB**.

#### User Goals
The user is looking for:
- A database where the user can find recipes.
- An easy-to-use user management system with **CRUD** conventions to:

    - Create a user account.
    - View user account.
    - Update their passord.
    - Delete their user account.

- An easy-to-use dataset management system with **CRUD** conventions to:

    - Create recipes.
    - Read recipes.
    - Update their own recipes.
    - Delete their own recipes.

- A simple and easy to navigate design.

#### Developer Goals
As a developer, I am looking to:

- Create an application where users can post, edit and delete their own recipes.
- Add a new application to my portfolio.
- Improve my newly learned languages and skills.

### User Stories
**As a General User, I want to:**

1. Easily find recipes on the database. 
2. View the details of each recipe.

**As a Non-Registered User, I want to:**

1. Register an account.

**As a Registered User, I want to:**

1. Log into my account to be able to create, edit and delete recipes.
2. Navigate to my user profile to change my password.
3. Navigate to my account settings to delete my account.
4. Navigate to my recipes page to view my uploaded recipes.
6. Navigate to my own recipes to edit recipe as needed.
7. Navigate to my own recipes to delete recipe.

**As an Administrative Account holder, I want to:**

1. Edit **any** recipes created by users.
2. Delete **any** recipes from the dashboard.

### Development Planes

In order to develop and promote an interactive web application, My Vegetarian Choice has been created based on::

#### Strategy
The targeted audience:
- New Users **(Non-Registered)**
- Returning Users **(Registered)**
- Individuals who want to find a recipe.
- Individuals who want to create a recipe.
- Age group: suitable for any age group

The website needs to enable the **user** to:
- Register/Login to an account
- Edit their account
- Delete their account
- Search Recipe database by:
    - Name/Phrase
    - Ingredient
- View Recipe Dashboard with the following information:
    - Name
    - Image
    - Category
    - Serving Size
    - Time
    - Ingredients
    - Cooking method
    - The user who created the recipe
- Upload and access their own recipes

#### Scope
After defining the strategy, the scope was developed based on the following requirements:
- **User Requirements**
     - The user will be looking for:
        - Customisable and Editable account:
            - Custom Username/Password
            - Manage their account
            - Upload their own recipes
            - Manage their own recipes
        - Easy Navigation
        - Recipe dashboard:
            - Name
            - Image URL
            - Category
            - Serving Size
            - Time
            - Who created the recipe
            - Ingredients
            - Cooking method
        - Searchable database system

- **How the user requirements have been met**
     - The user will be able to:
        - Register/Login to account
        - Edit their profile:
            - Edit Password
            - Delete their account
            - Upload their own recipes
            - Edit and delete their recipes
        - Navigate to recipes:
            - Search by name or ingredient
            - My Recipes Page
        - Create their recipes, providing:
            - Name
            - Image URL
            - Category
            - Serving Size
            - Time
            - Ingredients
            - Cooking Method

#### Structure
With the previously identified strategy and scope, the ideal structure was agreed to match the following diagram:
![Site structure](static/images/structure.PNG)

#### Skeleton
**Skeleton** has been put together using [Balsamiq wireframes](https://balsamiq.com/ "Link to Balsamiq wireframes"):
![](static/images/wireframes.PNG)

#### Surface

- <strong>Colour Scheme</strong>

     - The developer has chosen to use blue for navbar and orange for links and buttons.
     
     ![](static/images/colours.PNG)


- <strong>Typography</strong>

    - The font used for the LOGO is 'Pacifico', with cursive as fallback.
    - The font used for Menu is 'Roboto', with sans-serif as fallback.

## Database info

For this project, the NoSQL database [MongoDB](https://www.mongodb.com/ "Link to MongoDB") was used to store the dataset. For this, two collections were created:

### Users Collection
- When registering an account, the user provides:
     - Username (unique identifier)
     - Password (hashed)

### Recipes Collection
- When creating a recipe, the user provides:
     - Recipe Name
     - Recipe Image (via URL)
     - Category
     - Serving
     - Time
     - Ingredients
     - Method
- The Ingredients and Method are arrays, allowing data to be entered dynamically.

## Design Features

Each page of the website features a consistently responsive and intuitive navigational system:
- There is a conventionally placed **navbar** on the top of each page with easily accessible and identifiable navigation links with a clickable logo, redirecting users back to the home page.
     - On mobile and tablet screens, the navbar is located in a conventionally placed 'hamburger' menu.
- The **Footer** displays the information regarding the use of copyrighted material on the website.
- [Jinja](http://jinja.pocoo.org/docs/2.10/ "Link to Jinja information") was used to extend the `base.html` page, allowing functionality across all pages. The extended block elements created the same basic layout for each page:

     ```
     <nav>
          <!-- Navigational content -->
     </nav>

     <section>

          {% block header %}
               <!-- Page Banner Image and Title -->
          {% endblock %}

          {% block flash %}
               <!-- Appropriate flash messages -->
          {% endblock %}

          {% block content %}
               <!-- Content unique to each page -->
          {% endblock %}

     </section>

     <footer>
          <!-- Footer content -->
     </footer>
     ```

- If the user is in session, there will be additional links added to the `navbar`:
     - Profile
     - Add a Recipe
     - Logout

- On mobile and tablet screens, the extra buttons will appear on the navigation (hamburger) menu in order to provide quick access.


- Recipe **Cards** are used throughout the website, providing users with a snapshot of the recipe, name category and who created it, before they view the entire recipe page. Each card is designed the same for consistency purposes and allows the user to click on the recipe name in order to be directed to the recipe page.

## Technologies Used
### Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")
- [Python](https://www.python.org/ "Link to Python Homepage")

### Tools
- [Visual Studio Code Insiders](https://code.visualstudio.com/insiders/ "Link to download Visual Studio Code Insiders") 
     - VSCode was used as the preferred IDE.
- [Git](https://git-scm.com/ "Link to Git homepage")
     - Git was used for version control to commit to Git and push to Heroku.
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project repository, after pushing.
- [Heroku](https://id.heroku.com/login "Link to Heroku login page")
     -  Heroku was used in order to deploy the website.
- [Balsamiq](https://www.balsamiq.com/ "Link to balsamiq homepage")
     - Figma was used to create the wireframes during the design phase of the project.
- [Font Awesome](https://fontawesome.com/ "Link to Font Awesome site")
     - Font Awesome was used in conjunction with Iconify for icons used throughout the website.

### Libraries
- [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/ "Link to Bootstrap page")
     - Bootstrap was used to implement the responsiveness of the site, using bootstrap classes.
- [jQuery](https://jquery.com/ "Link to jQuery page")
     - jQuery was used to simplify the JavaScript code used.
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")
    - Google fonts was used to import the fonts **"Pacifico"** and **"Roboto"** into the style.css file. These fonts were used throughout the project.
- [Bootstrap Themes](https://themes.getbootstrap.com/ "Link to Bootstrap Themes page")
     - The website was build using one of the bootstrap themes.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/ "Link to Flask Homepage")
     - Flask was used as the web framework for the application.
- [PyMongo](https://pypi.org/project/pymongo/ "Link to PyMongo information")
     - `flask_pymongo` was used a communication line between the MongoDB database and Python.
- [Pagination](https://flask-paginate.readthedocs.io/en/master/ "Link to flask-paginate documentation")
     - `flask_paginate` extension was used to implement pagination functionality on select pages.
- [BSON](https://bsonspec.org/ "Link to BSon documentation")
     - `bson.objectid` is a required dependency for MongoDB management system.
- [Jinja](http://jinja.pocoo.org/docs/2.10/ "Link to Jinja information")
     - Jinja templating language was used to simplify and display backend data in html.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/ "Link to Werkzeug information")
     - Werkzeug was used for password hashing and authentication.

### Database Management
- [MongoDB](https://www.mongodb.com/ "Link to MongoDB site")
     - MongoDB was the chosen NoSQL database for this website.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas "Link to MongoDB Atlas site")
     - MongoDB Atlas was the cloud database service used to host the database.

## Testing

Testing information can be found in a separate testing [file](TESTING.md "Link to testing file")

## Deployment
To further develop this project, a clone can be made using the following steps:
### 1. Database Creation
The application is connected to a [MongoDB Atlas](https://mongodb.com/ "Link to MongoDB Homeapage") Cluster. A Project database can be created using the following steps:

1. Log into [MongoDB](https://account.mongodb.com/account/login "Link to MongoDB login page") or [create an account](https://account.mongodb.com/account/register "Link to MongoDB sign-up page").
2. Locate and select the `New Project` button on the right side of the page, and give your project a name. Navigate to the project page.
3. Locate and select the `Create a New Cluster` button on the right side of the page. Once selected:
     - Choose **Shared Cluster** which is a free option.
     - Select your **Cloud Provider** and **Region** (in this instance: **AWS** and **Ireland**).
     - Click on **Cluster Tier** and select tier of preference (in this instance: **Basic M0 tier**).
     - Click on **Cluster Name** and create your cluster name.
4. Locate and select `Database Access` on the left side of the page. Once selected, click `Add New Database User`:
     - Choose `Password` for the **Authentication Method**
     - Enter a username and password of your choosing
     - Ensure `Read and write to any database` is selected in **Database User Privileges**
     - Add User
5. Locate and select `Network Access` under `Database Access` on the left side of the page. Once selected, click `Add IP Address`:
     - Select `Allow Access from anywhere` (This is not recommended for full-production applications).
     - Select `Confirm`.
6. Locate and select `Clusters` on the left side of the page (must be provisioned first).
7. Click `Collections`, then `+ Create Database` to start adding documents to your database collections:
     - Enter chosen `Database Name`
     - Enter chosen `Collection Name`
     - Select `Create`
8. Click `Create Collection` and create the necessary collections. See [Data Schema](#Data-Schema) for reference of the collections created for this project.

### 2. Local Copy Creation
A Local Clone of the repository can be made in two ways:

- **Forking the Repository:**

     By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

     1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
     2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/bake-it-til-you-make-it "Link to GitHub Repo").
     3. At the top of the repository, on the right side of the page, select "Fork".
     4. You should now have a copy of the original repository in your GitHub account.

-  **Creating a Clone**

     How to run this project locally:
     1. Install the [GitPod Browser](https://www.gitpod.io/docs/browser-extension/ "Link to Gitpod Browser extension download") Extension for Chrome.
     2. After installation, restart the browser.
     3. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
     2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/bake-it-til-you-make-it "Link to GitHub Repo").
     5. Click the green "GitPod" button in the top right corner of the repository.
     This will trigger a new gitPod workspace to be created from the code in github where you can work locally.

     How to run this project within a local IDE, such as VSCode:

     1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
     2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/bake-it-til-you-make-it "Link to GitHub Repo").
     3. Under the repository name, click "Clone or download".
     4. In the Clone with HTTPs section, copy the clone URL for the repository.
     5. In your local IDE open the terminal.
     6. Change the current working directory to the location where you want the cloned directory to be made.
     7. Type 'git clone', and then paste the URL you copied in Step 3.
     ```
     git clone https://github.com/USERNAME/REPOSITORY
     ```
     8. Press Enter. Your local clone will be created.

     (Further reading and troubleshooting on cloning a repository from GitHub [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository "Link to GitHub troubleshooting"))

Once a local clone is created, the environment variables have to be set:

1. Create a `.gitignore` file in the project's root directory.
2. In the terminal window, type `touch env.py` to create the file that will contain the environment variables. 
3. Add `env.py` to the `.gitignore` file.
4. Within the `env.py` file, enter the project's environment variables:
```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", <your_secret_key>)
os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority" )
os.environ.setdefault("MONGO_DBNAME", <your_mongo_db_name>)
```
For the `MONGO_URI` ensure to replace `<username>`, `<password>`, `<cluster_name>` and `<database_name>` with the appropriate alternatives.



### 3. Heroku App Creation
The website requires back-end technology, including a server, application and database. It is because of this that the project was deployed on **Heroku**, a container-based cloud Platform as a Service. There are two ways to deploy on Heroku:

- Using the Heroku Command Line Interface
- Connect to GitHub Repository (the developer recommends this method)

Before deployment can be carried out on Heroku, the following steps must be carried out:

1. Create a `requirements.txt` file to install all requirements. In the terminal window, type the following command:
```
pip3 install -r requirements.txt
```
2. Create a `Procfile` file so that Heroku knows which file runs the app. In the terminal window, type the following command:
```
echo web: python app.py > Procfile
```
*Remove the blank line that may occur at the end of the Procfile to avoid any issues*


3. Push the two files to the repository:
```
git add requirements.txt
git commit -m "Add requirements.txt"

git add Procfile 
git commit -m "Add Procfile"

git push
```
Once these steps are completed, continue with the process:

1. Log into [Heroku](https://id.heroku.com/login "Link to Heroku login page") or [create an account](https://signup.heroku.com/login "Link to Heroku sign-up page").
2. Select the `New` button on the top-right of the page, and choose `Create New App`. Give your app a unique name and set the region (in this instance: **Europe**). Then click `Create App`.
3. Navigate to the `Deploy` tab on the dashboard and select `Connect to GitHub`.
4. Search for the repository name (ensuring it is spelled correctly). Once located, click `Connect`. 
5. Navigate to the `Setting` tab on the dashboard and select `Reveal Config Vars`, entering the necessary key/values as below:

| Key | Value |
 --- | ---
IP | 0.0.0.0
PORT | 5000
SECRET_KEY | `<your_secret_key>`
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority`
MONGO_DBNAME | `<your_mongo_db_name>`

6. Navigate back to the `Deploy` tab and scroll down to `Automatic Deploys`.
7. Ensure that the `master` branch is selected, then select `Enable Automatic Deploys`.

Heroku will receive the pushed code from the GitHub repository and host the application with the required packages set out. 

The deployed version can now be viewed by selecting `View App` in the top-right of the page.

## Credits 
During the production of the application, multiple sources were accessed, such as: 

The [Code Institute Task Manager Mini Project](https://github.com/Code-Institute-Solutions/TaskManagerAuth) mini project was used as a starting point in the develpment of the **CRUD** functionality.

References for code that was copied and edited:
- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page")
- [Rebecca Tracey- Timoney](https://github.com/rebeccatraceyt/bake-it-til-you-make-it/ "Link to Rebecca's repo")

## Acknowledgements
The developer would like to thank the following:
- Fellow student Rebecca, for all the support.
- Their mentor Brian, for her consistent guidance and advice.