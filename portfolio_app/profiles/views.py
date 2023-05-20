from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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
        print(f"Latitude: {user_profile.latitude}")
        print(f"Longitude: {user_profile.longitude}")

        # Save the updated user profile
        user_profile.save()

        return redirect('profile')

    return render(request, 'profiles/edit_profile.html', {'user_profile': user_profile})



