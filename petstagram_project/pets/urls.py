from django.urls import path, include

from petstagram_project.pets import views

urlpatterns = [
    path('add_pet/', views.add_pet, name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.pet_details_page, name='pet-details'),
        path('edit/', views.edit_pet, name='edit-pet'),
        path('delete_pet/', views.delete, name='delete-pet'),
    ]))
]
