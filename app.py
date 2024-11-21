from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_URL = "https://cosylab.iiitd.edu.in/recipe-search/recipesAdvanced?page=1&pageSize=10"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/output')
def output():
    return render_template('output.html')

@app.route('/generate-meal-plan', methods=['POST'])
def generate_meal_plan():
    # Get user input from frontend
    data = request.json
    protein_min = data.get("proteinMin", 0)
    protein_max = data.get("proteinMax", 0)
    carbs_min = data.get("carbsMin", 0)
    carbs_max = data.get("carbsMax", 0)
    energy_min = data.get("energyMin", 0)
    energy_max = data.get("energyMax", 0)

    # Payload to send to the API
    payload = {
        "continent": "",
        "region": "",
        "subRegion": "",
        "recipeTitle": "",
        "ingredientUsed": "",
        "ingredientNotUsed": "",
        "cookingProcess": "",
        "utensil": "",
        "energyMin": energy_min,
        "energyMax": energy_max,
        "carbohydratesMin": carbs_min,
        "carbohydratesMax": carbs_max,
        "fatMin": 0,
        "fatMax": 0,
        "proteinMin": protein_min,
        "proteinMax": protein_max
    }

    try:
        # Make API call
        response = requests.post(API_URL, json=payload)
        response_data = response.json()

        # Extract recipes from the response
        if response_data.get("success") == "true" and response_data["payload"]["data"]:
            recipes = []
            for recipe in response_data["payload"]["data"]:
                recipes.append({
                    "title": recipe["Recipe_title"],
                    "energy": recipe.get("Energy (kcal)", "N/A"),
                    "protein": recipe.get("Protein (g)", "N/A"),
                    "carbs": recipe.get("Carbohydrate, by difference (g)", "N/A"),
                    "link": recipe["url"]
                })

            # Send recipes to frontend
            return jsonify(recipes)

        else:
            # If no recipes are found or API fails
            return jsonify([])

    except Exception as e:
        print(f"Error: {e}")
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
