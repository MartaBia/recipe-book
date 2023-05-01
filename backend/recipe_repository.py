import psycopg2
from recipe import Recipe

class RecipeRepository:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def get_all(self):
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM recipes")
                rows = cur.fetchall()
                recipes = [Recipe(*row) for row in rows]
                return recipes
    
    def get_from_id(self, recipe_id):
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM recipes WHERE id=%s", (recipe_id,))
                row = cur.fetchone()
                if row:
                    return Recipe(*row)
                else:
                    return None
                
    def add(self, name, ingredients, process):
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO recipes (name, ingredients, process) VALUES (%s, %s, %s) RETURNING id", (name, ingredients, process))
                recipe_id = cur.fetchone()[0]
                return Recipe(recipe_id, name, ingredients, process)
    

      