from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Address(models.Model):
    house_number = models.CharField(max_length=30)
    street_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=203)
    country = models.CharField(max_length=50, default='Nigeria')


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    GENRE_CHOICES = [
        ('FICTION', 'Fiction'),
        ('ROMANCE', 'Romance'),
        ('FINANCE', 'Finance'),
        ('POLITICS', 'Politics'),

    ]
    title = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=8, choices=GENRE_CHOICES, default="Fiction")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_published = models.DateField(blank=True, null=True)
    copies = models.IntegerField()

    def __str__(self):
        return f"{self.title} {self.isbn} {self.genre} {self.author} {self.copies}"


class Meta:
    ordering = ['title']


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11)


class BookInstance(models.Model):
    book = models.OneToOneField(Book, on_delete=models.PROTECT, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    date_borrowed = models.DateField(auto_now=True)
    date_returned = models.DateTimeField()

    def __str__(self):
        return f"{self.book} {self.price} {self.date_borrowed} {self.date_returned}"


class ReviewBook(models.Model):
    DESCRIPTION_CHOICE = [
        ('LOVELY', 'Lovely'),
        ('GROSS', 'Gross'),
        ('EDUCATIVE', 'Educative'),
        ('EXCITING', 'Exciting')
    ]
    reviewer_name = models.CharField(max_length=100)
    date_and_time = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, choices=DESCRIPTION_CHOICE)

    def __str__(self):
        return f"{self.reviewer_name} {self.date_and_time} {self.book} {self.description}"

# class BorrowBookModel(models.Model):
#     book_instance = models.ForeignKey(BookInstance, on_delete=models.CASCADE)
#     borrower_name = models.CharField(max_length=100)
#     book_name = models.CharField(max_length=250)
#
#     def __str__(self):
#         return f"{self.borrower_name} {self.book_instance} {self.book_name}"
