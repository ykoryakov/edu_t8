from datetime import timedelta
from django import forms
from .models import Reserve


class ReserveForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.__room = kwargs.pop('room')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Reserve
        fields = ('reserve_date', 'reserve_time', 'duration', 'name',)
        widgets = {
            'reserve_date': forms.SelectDateWidget()
        }

    def clean(self):
        reserve_date = self.cleaned_data['reserve_date']
        reserve_time = self.cleaned_data['reserve_time']
        duration = self.cleaned_data['duration']

        _our_start = reserve_time.hour
        _our_end = reserve_time.hour + duration

        all_reserves = Reserve.objects.filter(room=self.__room, reserve_date=reserve_date)
        for reserve in all_reserves:
            _start = reserve.reserve_time.hour
            _end = reserve.reserve_time.hour + reserve.duration
            if not (_our_start > _end or _our_end < _start):
                self.add_error('reserve_time', 'Кто-то успел до тебя')

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == 'Коля':
            self.add_error('name', 'Извини, приятель, тебе нельзя забронировать')
        return name