from django.contrib import admin
from .models import Room, Reserve


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'capacity', 'has_projector')


@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display = ('room', 'name', 'reserve_date', 'reserve_time', 'duration')
