from DjangoExamProject.patients.models import Patients


def get_pet_by_name_and_username(pet_slug, username):
    return Patients.objects.filter(
        slug=pet_slug,
        user__username=username).get()
