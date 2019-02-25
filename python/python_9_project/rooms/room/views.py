from datetime import datetime, date, time
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import reverse
from .models import Room
from .forms import ReserveForm


def index(request):
    template = loader.get_template('home.html')
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return HttpResponse(template.render(context, request))


def reserve(request, room_id):
    try:
        room = Room.objects.get(id=room_id)
    except Room.DoesNotExist:
        raise Http404('Room not found')

    if request.POST:
        form = ReserveForm(request.POST, room=room)
        if form.is_valid():
            _reserve = form.save(commit=False)
            _reserve.room = room
            _reserve.save()
            return HttpResponseRedirect(reverse('index', args=()))
    else:
        _time = time(datetime.now().time().hour + 1, 0)
        form = ReserveForm(initial={
            'room': room,
            'reserve_date': date.today(),
            'reserve_time': _time,
            'duration': 2
        }, room=room)

    template = loader.get_template('reserve.html')
    context = {
        'room': room,
        'form': form
    }
    return HttpResponse(template.render(context, request))

