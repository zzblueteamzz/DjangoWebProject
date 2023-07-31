from django.urls import path, include

from DjangoExamProject.patients.views import add_patient, show_patient_details, edit_pet, delete_pet

# pets/urls
# http://127.0.0.1:8000/pets/goto/pet/Buddy/ + edit/delete

urlpatterns = (
    path('add/', add_patient, name='add_patient'),
    path('<str:username>/pet/<slug:pet_slug>/', include(
        [
            path('', show_patient_details, name='show pet details'),
            path('edit/', edit_pet, name='edit pet'),
            path('delete/', delete_pet, name='delete pet'),
        ]
    )),
)
