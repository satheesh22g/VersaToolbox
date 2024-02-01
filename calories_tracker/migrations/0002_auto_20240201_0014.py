from django.db import migrations

def populate_data(apps, schema_editor):
    Food = apps.get_model('calories_tracker', 'Food')
    Consume = apps.get_model('calories_tracker', 'Consume')

    # Add your data here

    food_data = [
        {'name': 'Apple', 'carbs': 25.0, 'protein': 1.0, 'fats': 0.3, 'calories': 95},
        {'name': 'Banana', 'carbs': 27.0, 'protein': 1.3, 'fats': 0.4, 'calories': 105},
        {'name': 'Chicken Breast', 'carbs': 0.0, 'protein': 31.0, 'fats': 3.6, 'calories': 165},
        {'name': 'Broccoli', 'carbs': 11.2, 'protein': 2.8, 'fats': 0.6, 'calories': 55},
        {'name': 'Salmon', 'carbs': 0.0, 'protein': 25.0, 'fats': 13.0, 'calories': 206},
        {'name': 'Brown Rice', 'carbs': 45.0, 'protein': 5.0, 'fats': 1.6, 'calories': 215},
        {'name': 'Oats', 'carbs': 54.0, 'protein': 13.0, 'fats': 6.0, 'calories': 303},
        {'name': 'Almonds', 'carbs': 6.0, 'protein': 21.0, 'fats': 14.0, 'calories': 160},
        {'name': 'Greek Yogurt', 'carbs': 6.0, 'protein': 15.0, 'fats': 10.0, 'calories': 150},
        {'name': 'Spinach', 'carbs': 6.7, 'protein': 2.9, 'fats': 0.4, 'calories': 23},
        {'name': 'Carrot', 'carbs': 12.0, 'protein': 0.6, 'fats': 0.3, 'calories': 50},
        {'name': 'Quinoa', 'carbs': 39.0, 'protein': 8.0, 'fats': 2.5, 'calories': 222},
        {'name': 'Avocado', 'carbs': 12.0, 'protein': 2.0, 'fats': 15.0, 'calories': 160},
        {'name': 'Egg', 'carbs': 1.0, 'protein': 6.0, 'fats': 5.0, 'calories': 68},
        {'name': 'Sweet Potato', 'carbs': 26.0, 'protein': 1.6, 'fats': 0.1, 'calories': 112},
    ]

    for data in food_data:
        food = Food(**data)
        food.save()




class Migration(migrations.Migration):

    dependencies = [
        ('calories_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_data),
    ]
