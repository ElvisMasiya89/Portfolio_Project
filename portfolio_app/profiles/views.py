from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.gis.db.models.functions import Transform
from django.shortcuts import redirect
from django.shortcuts import render
from .models import UserProfile


@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profiles/profile.html', {'user_profile': user_profile})


from django.contrib.auth.decorators import login_required


@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        # Update the user profile with the new data
        user_profile.home_address = request.POST['home_address']
        user_profile.phone_number = request.POST['phone_number']
        user_profile.set_location(request.POST['latitude'], request.POST['longitude'])

        # Display the data before saving
        print(f"Home Address: {user_profile.home_address}")
        print(f"Phone Number: {user_profile.phone_number}")
        print(f"Location: {user_profile.location}")

        # Save the updated user profile
        user_profile.save()

        return redirect('profile')

    return render(request, 'profiles/edit_profile.html', {'user_profile': user_profile})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm(request)
    return render(request, 'profiles/login.html', {'form': form})

@login_required
def user_map_view(request):
    user_profiles = get_user_profiles()
    return render(request, 'profiles/user_map.html', {'user_profiles': user_profiles})

def get_user_profiles():
    user_profiles = UserProfile.objects.all()
    return user_profiles.annotate(transformed_location=Transform('location', 4326))