from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from theatre.models import Ticket, Performance, Reservation, TheatreHall, Play


class TicketModelTests(TestCase):
    def test_ticket_str(self):
        theatre_hall = TheatreHall.objects.create(
            name="Test Theatre", rows=5, seats_in_row=10
        )
        play = Play.objects.create(title="Test Play")
        performance = Performance.objects.create(
            play=play,
            theatre_hall=theatre_hall,
            show_time=datetime(2023, 7, 21, 19, 30)
        )
        user = get_user_model().objects.create_user(
            email="user@test.com", password="testpassword"
        )
        reservation = Reservation.objects.create(user=user)
        ticket = Ticket.objects.create(
            row=2, seat=5, performance=performance, reservation=reservation
        )

        expected_str = f"{str(performance)} (row: 2, seat: 5)"
        self.assertEqual(str(ticket), expected_str)
