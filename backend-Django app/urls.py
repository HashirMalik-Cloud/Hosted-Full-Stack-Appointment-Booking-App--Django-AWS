from django.urls import path
from .views import home, book_slot

urlpatterns = [
    path('', home, name='home'),
    path('book/<int:slot_id>/', book_slot, name='book_slot'),
]
