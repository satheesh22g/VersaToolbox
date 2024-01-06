import requests
from django.shortcuts import render
from .forms import RecipeForm

def generate_recipes(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            ingredients = form.cleaned_data.get('ingredients')
            
            # Make a request to TheMealDB API to fetch list of meals based on ingredients
            response = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php', params={'i': ingredients})
            
            if response.status_code == 200:
                meals = response.json().get('meals', [])
                
                # Fetch detailed information for each meal
                detailed_meals = []
                for meal in meals:
                    meal_id = meal.get('idMeal')
                    if meal_id:
                        meal_response = requests.get('https://www.themealdb.com/api/json/v1/1/lookup.php', params={'i': meal_id})
                        if meal_response.status_code == 200:
                            detailed_meal = meal_response.json().get('meals', [])[0]
                            
                            # Extract ingredients and measures into a list of tuples
                            ingredients = []
                            for i in range(1, 21):
                                ingredient = detailed_meal.get(f'strIngredient{i}')
                                measure = detailed_meal.get(f'strMeasure{i}')
                                if ingredient:
                                    ingredients.append((ingredient, measure))
                            
                            # Update the meal dictionary with ingredients
                            detailed_meal['ingredients'] = ingredients
                            
                            detailed_meals.append(detailed_meal)
                
                context = {'detailed_meals': detailed_meals}
                return render(request, 'recipe_list.html', context)
            else:
                error_message = f"Failed to fetch recipes. Status code: {response.status_code}"
                return render(request, 'error.html', {'error_message': error_message})
    else:
        form = RecipeForm()
    return render(request, 'generate_recipes.html', {'form': form})
