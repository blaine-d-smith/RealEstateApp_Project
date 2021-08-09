from django.urls import path
from . import views

urlpatterns = [
    path(
        'contacts',
        views.contacts,
        name='contacts'
    ),
    path(
        'delete/<listing_id>',
        views.delete,
        name='delete'
    ),
]
