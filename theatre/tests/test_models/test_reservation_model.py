from django.contrib.auth import get_user_model
from django.test import TestCase

from theatre.models import Reservation


class ReservationModelTests(TestCase):
    def test_reservation_str(self):
        user = get_user_model().objects.create_user(
            email="user@test.com", password="testpassword"
        )
        reservation = Reservation.objects.create(user=user)

        expected_str = str(reservation.created_at)
        self.assertEqual(str(reservation), expected_str)
