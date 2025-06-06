from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tracker.models import UserProfile, DailyWeightEntry
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Creates a test user with a profile and multiple weight entries.'

    def handle(self, *args, **kwargs):
        if User.objects.filter(username='testuser').exists():
            self.stdout.write(self.style.WARNING('User "testuser" already exists.'))
            return

        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='Test1234'
        )

        UserProfile.objects.create(
            user=user,
            height_cm=180,
            birth_date=date(2000, 1, 1),
            gender='M',
            goal='Gain muscle mass'
        )

        base_date = date.today()
        weights = [75.0, 75.5, 76.0, 76.2, 76.4, 76.0, 75.8]
        notes = [
            'Initial weight',
            'Slight increase',
            'Good progress',
            'Post-leg day',
            'Peak weight',
            'Dropped a bit',
            'Stable'
        ]
        
        for i in range(len(weights)):
            DailyWeightEntry.objects.create(
                user=user,
                weight_kg=weights[i],
                date=date.today() - timedelta(days=10 - i),
                note=notes[i]
            )

        self.stdout.write(self.style.SUCCESS('Test user, profile, and multiple weight entries created.'))
