# ALX Travel App

This project is a simple travel booking application built with Django and Django REST Framework. It allows users to list properties, make bookings, and leave reviews.

## Features

- **Listings:** Users can create and view property listings.
- **Bookings:** Users can book available listings for specific dates.
- **Reviews:** Users can leave reviews and ratings for listings.

## Project Structure

- `listings/models.py`: Contains the `Listing`, `Booking`, and `Review` models.
- `listings/serializers.py`: Serializers for API representation of listings and bookings.
- `listings/management/commands/seed.py`: Management command to seed the database with sample data.

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Apply migrations:
    ```sh
    python manage.py migrate
    ```

3. Seed the database with sample data:
    ```sh
    python manage.py seed
    ```

4. Run the development server:
    ```sh
    python manage.py runserver
    ```

## API Endpoints

- `/api/listings/` - List and create property listings.
- `/api/bookings/` - List and create bookings.

## License

This project is for educational purposes.