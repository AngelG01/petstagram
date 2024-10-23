from django.urls import path, include

from petstagram_project.photos import views

urlpatterns = [
    path('add_photo/', views.add_photo, name='add-photo'),
    path('<int:pk>/', include([
        path('', views.photo_details_page, name='photo-details'),
        path('edit_photo/', views.edit_photo, name='edit-photo'),
        path('delete/', views.delete_photo, name='delete-photo'),
    ]))
]
