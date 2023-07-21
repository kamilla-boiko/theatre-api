from datetime import datetime

from django.test import TestCase

from theatre.models import Performance, Play, TheatreHall


class PerformanceModelTests(TestCase):
    def test_performance_str(self):
        play = Play.objects.create(title="Test Play")
        theatre_hall = TheatreHall.objects.create(
            name="Test Hall", rows=10, seats_in_row=10
        )
        performance = Performance.objects.create(
            play=play,
            theatre_hall=theatre_hall,
            show_time=datetime(2023, 7, 21, 19, 30)
        )

        expected_str = f"{play.title} 2023-07-21 19:30:00"
        self.assertEqual(str(performance), expected_str)
