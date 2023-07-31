
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from DjangoExamProject.common.forms import CommentForm
from DjangoExamProject.core.find_pet import get_pet_by_name_and_username
from DjangoExamProject.core.is_owner import is_owner
from DjangoExamProject.doctors.forms import DoctorCreateForm, DoctorDeleteForm, DoctorEditForm


@login_required
# pets/views.py
def add_doctor(request):
    if request.method == "GET":
        form = DoctorCreateForm()
    else:
        form = DoctorCreateForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('profile details', pk=request.user.pk)

    context = {
        'form': form,

    }

    return render(
        request,
        'doctors/doctor-add-page.html',
        context,
    )


def show_doctor_details(request, username, pet_slug):
    pet = get_pet_by_name_and_username(pet_slug, username)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()

    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
        'username': username,
        'pet_slug': pet_slug,
        'is_owner': pet.user == request.user,

    }

    return render(
        request,
        'doctors/doctor-details-page.html',
        context,
    )


# http://127.0.0.1:8000/pets/goto/pet/pesho-5/

def edit_doctor(request, username, pet_slug):
    pet = get_pet_by_name_and_username(pet_slug, username)

    if not is_owner(request, pet):
        return redirect('show pet details', username=username, pet_slug=pet_slug)

    if request.method == 'GET':
        form = DoctorEditForm(instance=pet)
    else:
        form = DoctorEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('show pet details', username=username, pet_slug=pet_slug)

    context = {
        'form': form,
        'pet': pet,
        'username': username,
        'pet_slug': pet_slug,
    }
    return render(
        request,
        'doctors/doctor-edit-page.html',
        context,
    )


def delete_doctor(request, username, pet_slug):
    pet = get_pet_by_name_and_username(pet_slug, username)
    profile = pet.user

    if request.method == 'GET':
        form = DoctorDeleteForm(instance=pet)
    else:
        form = DoctorDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk=profile.pk)

    context = {
        'form': form,
        'pet': pet,
        'pet_slug': pet_slug,
        'username': username,
    }

    return render(
        request,
        'doctors/doctor-delete-page.html',
        context,
    )

