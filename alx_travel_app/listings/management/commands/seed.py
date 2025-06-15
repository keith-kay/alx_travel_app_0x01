from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing, Booking
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample listings and bookings'

    def handle(self, *args, **kwargs):
        # Create a user if not exists
        user, created = User.objects.get_or_create(
            username='demo_user',
            defaults={'email': 'demo@example.com'}
        )
        if created:
            user.set_password('password123')
            user.save()

        # Create sample listings
        for i in range(1, 4):
            listing, _ = Listing.objects.get_or_create(
                title=f"Sample Listing {i}",
                defaults={
                    'description': f"Description for listing {i}",
                    'location': f"City {i}",
                    'price_per_night': 100.0 * i,
                    'owner': user,
                }
            )

            # Create a booking for each listing
            Booking.objects.get_or_create(
                listing=listing,
                user=user,
                start_date=timezone.now().date() + timedelta(days=i),
                end_date=timezone.now().date() + timedelta(days=i+2),
                guests=2
            )

        self.stdout.write(self.style.SUCCESS('Database seeded with sample listings and bookings.'))