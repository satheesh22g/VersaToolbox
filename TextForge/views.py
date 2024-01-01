# views.py

from django.shortcuts import render
from faker import Faker

def generate_profile(request):
    profile = None
    print(0)
    if request.method == 'POST':
        print(2)
        profile_fake = Faker('en_IN') if request.POST.get('profileType') == 'indian' else Faker()
        profile = {
            'name': profile_fake.name(),
            'email': profile_fake.email(),
            'phone_number': profile_fake.phone_number(),
            'date_of_birth': profile_fake.date_of_birth(),
            'job': profile_fake.job(),
            'company': profile_fake.company(),
            'username': profile_fake.user_name(),
            'website': profile_fake.url(),
            'favorite_color': profile_fake.color_name(),
            'favorite_movie': profile_fake.random_element(elements=('The Shawshank Redemption', 'The Godfather', 'The Dark Knight')),
            'favorite_food': profile_fake.random_element(elements=('Pizza', 'Sushi', 'Chocolate', 'Burgers')),
            'blood_group': profile_fake.random_element(elements=('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')),
            'height': profile_fake.random_int(min=150, max=200),  # in cm
            'weight': profile_fake.random_int(min=50, max=120),  # in kg
            'eye_color': profile_fake.color_name(),
            'hair_color': profile_fake.color_name(),
            'education': profile_fake.random_element(elements=('High School', 'Bachelor\'s Degree', 'Master\'s Degree', 'PhD')),
            'religion': profile_fake.random_element(elements=('Christianity', 'Islam', 'Hinduism', 'Buddhism', 'Judaism', 'Atheism')),
            'political_views': profile_fake.random_element(elements=('Conservative', 'Liberal', 'Moderate', 'Socialist', 'Anarchist')),
            # Add more fake profile data fields as needed
        }

    return render(request, 'generate_profile.html', {'profile': profile})


def generate_address(request):
    address = None
    address_fake = Faker('en_IN') if request.POST.get('addressType') == 'indian' else Faker()
    address = {
        'street_address': address_fake.street_address(),
        'city': address_fake.city(),
        'state': address_fake.state(),
        'country': address_fake.country(),
        'phone_number': address_fake.phone_number(),
        'email': address_fake.email(),
        # Add more fake address data fields as needed
    }

    return render(request, 'generate_profile.html', {'address': address})
