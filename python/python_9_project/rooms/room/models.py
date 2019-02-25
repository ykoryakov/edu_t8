from django.db import models
from .validators import validate_duration


class Room(models.Model):
    number = models.PositiveIntegerField(verbose_name='номер', unique=True)
    name = models.CharField(max_length=50, verbose_name='название')
    capacity = models.PositiveIntegerField(verbose_name='вместимость')
    has_projector = models.BooleanField(verbose_name='наличие проектора')

    class Meta:
        verbose_name = 'Переговорка'
        verbose_name_plural = 'Переговорки'

    def __str__(self):
        return '{}, {}'.format(
            self.number,
            self.name)


class Reserve(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='переговорка')
    reserve_date = models.DateField(verbose_name='дата начала')
    reserve_time = models.TimeField(verbose_name='время начала')
    duration = models.PositiveSmallIntegerField(verbose_name='продолжительность', validators=[validate_duration])
    name = models.CharField(max_length=100, verbose_name='имя')

    class Meta:
        verbose_name = 'Резерв переговорки'
        verbose_name_plural = 'Резервы переговорок'

    def __str__(self):
        return '{}, {}, {}, {}'.format(
            self.room,
            self.reserve_date,
            self.reserve_time,
            self.name)

