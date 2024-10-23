from django.shortcuts import render


# Create your views here.
def register(request):
    return render(request, 'accounts/register-page.html')


def login(request):
    return render(request, 'accounts/login-page.html')


def show_profile_details(request, pk: int):
    return render(request, 'accounts/profile-details-page.html')


def edit_profile(request, pk: int):
    return render(request, 'accounts/profile-edit-page.html')


def delete_profile(request, pk: int):
    return render(request, 'accounts/profile-delete-page.html')