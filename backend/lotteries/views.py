import json

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Event, Participant, Ballot
from datetime import datetime, timedelta


# get today's date as string
def getTodaysDate():
    return datetime.today().strftime('%Y-%m-%d')

# get yesterday's date as string
def getYesterdaysDate():
    yesterday = datetime.now() - timedelta(1)
    return yesterday.strftime('%Y-%m-%d')


class EventListView(ListView):
    model = Event
    def index(self, request):
        event_list = Event.objects.order_by('-date')
        context = {'event_list': event_list,}
        return render(request, 'lotteries/event_list.html', context)

class EventDetailView(DetailView):
    model = Event
    template_name = 'lotteries/detail.html'



def participants(request):
    participant_list = Participant.objects.order_by('register_date')
    output = ',\n '.join([p.id for p in participant_list])
    return HttpResponse(output)



# Register as a Lottery Participant
def register(request):
    response = "Wrong request method!"
    # Check if request method is correct
    if request.method == 'POST':
        # Check if event exists
        try:
            event = Event.objects.get(date=getTodaysDate())
        except Event.DoesNotExist:
            response = "There is no Event available today!"
            return HttpResponseNotFound(response)

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        id = body['id']
        name = body['name']
        password = ['password']

        # Check if Participant already exists
        if Participant.objects.filter(pk=id).exists():
            response = "Participant already exists!"
            return HttpResponse(response)
        else:
            p = Participant(id=id, name=name, lottery_event=event, password=password)
            p.save()
            response = "Participant with ID: " + id + " has been registered."
            return HttpResponse(response)
    else:
        return HttpResponseBadRequest(response)

# Submit lottery ballot for the event of the day
def submit(request):
    response = "Wrong request method!"
    # Check if request method is correct
    if request.method == 'POST':
        # Check if Event exists
        try:
            event = Event.objects.get(date=getTodaysDate())
        except Event.DoesNotExist:
            response = "There is no Event available today!"
            return HttpResponseNotFound(response)

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        numbers = body['numbers']
        participant_id = body['id']

        if event.is_finished is not True:
            # Check if Participant exists
            try:
                participant = Participant.objects.get(id=participant_id)
            except Participant.DoesNotExist:
                response = "Participant does not exist!"
                return HttpResponseNotFound(response)


            # check if Ballot already exists
            if Ballot.objects.filter(numbers=numbers).exists():
                response = "Ballot already exists! Choose different numbers."
                return HttpResponse(response)
            else:
                b = Ballot(numbers=numbers, participant=participant, lottery_event=event)
                b.save()
                response = "Ballot with numbers: " + numbers + " has been submitted."
                return HttpResponse(response)
        else:
            response = "You cannot submit a ballot to closed event!"
            return HttpResponse(response)

    else:
        return HttpResponse(response)

