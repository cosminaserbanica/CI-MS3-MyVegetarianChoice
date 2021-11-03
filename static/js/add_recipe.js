// Dynamic functionality was inspired by fellow student Rebecca 
//  https://github.com/rebeccatraceyt/bake-it-til-you-make-it

$(document).ready(function () {
  // Declare Variables
  var max_ingredients = 30;
  var ingredient_row = $(".ingredient-row");
  var add_ingredient = $(".add-ing-btn");
  var ingredient = 1;

  var max_methods = 30;
  var method_row = $(".method-row");
  var add_method = $(".add-met-btn");
  var method = 1;

// Append New Ingredient
  $(add_ingredient).click(function (e) {
    e.preventDefault();
    if (ingredient < max_ingredients) {
        ingredient++;
        $(ingredient_row).append('<div class="col-12 form-group ing-input"><input id="recipe_ingredients" class="form-control" type="text" name="recipe_ingredients"/><label for="recipe_ingredients" required></label><a href="#" class="remove_field"><i class="fas fa-trash-alt"></i> Delete</a></div>');
    }
  });

// Delete New Ingredient
  $(ingredient_row).on("click", ".remove_field", function (e) {
      e.preventDefault();
      $(this).parent('div').remove();
      ingredient--;
    });

// Append New Method
  $(add_method).click(function (e) {
      e.preventDefault();
      if (method < max_methods) {
          method++;
          $(method_row).append('<div class="col-12 form-group met-input"><textarea id="method" class="form-control" type="text" name="method" maxlength="300" rows="2" required/></textarea><label for="method"></label><a href="#" class="remove_field"><i class="fas fa-trash-alt"></i> Delete</a></div>');
      }
    });

// Delete New Method
  $(method_row).on("click", ".remove_field", function (e) {
      e.preventDefault();
      $(this).parent('div').remove();
      method--;
    });

});
