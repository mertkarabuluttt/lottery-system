import random
from datetime import datetime, timedelta
from lotteries.models import Event, Ballot


def chooseWinner(event_id):
    ballots = Ballot.objects.get(id=event_id)
    # choosing a random ballot
    winner_ballot = random.choice(ballots)
    return winner_ballot.numbers


def renewEvent():
    # Get yesterday's date as string
    yesterday = datetime.now() - timedelta(1)
    yesterday = yesterday.strftime('%Y-%m-%d')
    # get today's date as string
    today = datetime.today().strftime('%Y-%m-%d')

    # Get yesterday's event
    old_event = Event.objects.get(isFinished=False)
    old_event_id = old_event.id
    # Set yesterday's event winner
    old_event.winner = chooseWinner(old_event_id)
    # Close yesterday's event
    old_event.is_finished = True

    # Create new event
    if Event.objects.filter(date=today).exists():
        print("Event already exists.")
    else:
        new_event = Event(date=today)
        new_event.save()

