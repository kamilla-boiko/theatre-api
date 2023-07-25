from django.test import TestCase

from theatre.models import Actor


class ActorModelTests(TestCase):
    def test_actor_str(self):
        actor = Actor.objects.create(
            first_name="Test first", last_name="Test last"
        )

        self.assertEqual(str(actor), f"{actor.first_name} {actor.last_name}")
