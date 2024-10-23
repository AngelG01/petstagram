from django.shortcuts import render, redirect

from petstagram_project.common.forms import CommentForm
from petstagram_project.pets.forms import PetBaseForm, PetDeleteForm
from petstagram_project.pets.models import Pet


# Create your views here.
def add_pet(request):
    form = PetBaseForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)

    context = {
        'form': form
    }

    return render(request, 'pets/pet-add-page.html', context)


def pet_details_page(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()

    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
    }

    return render(request, 'pets/pet-details-page.html', context=context)


def edit_pet(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetBaseForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetBaseForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)

    context = {
        'form': form
    }

    return render(request, 'pets/pet-edit-page.html', context)


def delete(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)

    form = PetDeleteForm(initial=pet.__dict__)
    context = {
        'form': form
    }

    return render(request, 'pets/pet-delete-page.html', context)
