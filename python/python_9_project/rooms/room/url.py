from django.urls import path
from .views import reserve

app_name = 'room'

urlpatterns = [
    path('reserve/<int:room_id>/', reserve, name='reserve')
]