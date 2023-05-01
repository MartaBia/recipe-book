from flask import Flask, render_template, redirect, url_for, request
from backend.recipe import Recipe
from backend.recipe_repository import RecipeRepository

app = Flask(__name__)

# Create a connection to the database
recipe_repository = RecipeRepository()

# Defining the routes


@app.route('/')
def homepage():
    # Get all the recipes from the database
    recipes = recipe_repository.get_all()

    return render_template('homepage.html', recipes=recipes)


@app.route('/add-recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        # Create a new recipe from the form data
        recipe = Recipe(name=request.form['name'],
                        ingredients=request.form['ingredients'],
                        process=request.form['ingredients'])

        # Save the new recipe in the database
        recipe_repository.add(recipe)

        return redirect(url_for('homepage'))
    else:
        return render_template('add_recipe_form.html')


@app.route('recipe_name')
def recipe_detail(recipe_name):
    # Get the recipe from the database
    recipe = recipe_repository.get_by_name(recipe_name)

    return render_template('recipe_detail.html', recipe=recipe)


if __name__ == '__main__':
    app.run(debug=True)
