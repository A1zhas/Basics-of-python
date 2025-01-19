from django.core.management.base import BaseCommand
from my_app.models import Author, Book
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        # Добавление авторов
        author1 = Author.objects.create(name="George Orwell", birth_date=date(1903, 6, 25))
        author2 = Author.objects.create(name="J.K. Rowling", birth_date=date(1965, 7, 31))

        # Добавление книг
        Book.objects.create(title="1984", author=author1, published_date=date(1949, 6, 8), isbn="1234567890123")
        Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author2, published_date=date(1997, 6, 26), isbn="9780747532743")

        self.stdout.write(self.style.SUCCESS('Database successfully populated with sample data.'))
