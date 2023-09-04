from rest_framework import serializers

from book.models import Book, Author, ReviewBook, BookInstance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']
    # first_name = serializers.CharField(max_length=150)
    # last_name = serializers.CharField(max_length=150)
    # email = serializers.EmailField


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'genre', 'author', 'copies']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewBook
        fields = ['reviewer_name', 'description']

    def create(self, validated_data):
        return ReviewBook.objects.create(book_id=self.context['book_id'], **validated_data)


class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = ['book', 'user', 'date_returned', 'price']

    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(),
    #     view_name="author-detail"
    # )

    # title = serializers.CharField(max_length=200)
    # isbn = serializers.CharField(max_length=13)
    # genre = serializers.CharField(max_length=8)


class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'genre', 'copies', 'author']


class CreateAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'email']


class CreateBookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewBook
        fields = ['id', 'reviewer_name', 'date_and_time', 'book', 'description']

# class CreateBorrowBookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BorrowBookModel
#         fields = ['id', 'book_instance', 'borrower_name']
