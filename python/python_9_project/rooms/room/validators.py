from django.core.exceptions import ValidationError


def validate_duration(value):
    if value < 1:
        raise ValidationError('Минимальная продолжительность бронирования - 1 час',
                              params={'value': value})
    elif value > 10:
        raise ValidationError('Максимальная продолжительность бронирования - 10 часов',
                              params={'value': value})