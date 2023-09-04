
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .filters import CustomFilter
from .pagination import CustomPagination
from .serializers import BookSerializer, AuthorSerializer, CreateBookSerializer, ReviewSerializer, \
    BookInstanceSerializer
from .models import Book, Author, ReviewBook, BookInstance


# Create your views here.


# def welcome(request):
#     return HttpResponse("Welcome to my library")
#
#
# def get_books(request):
#     return HttpResponse("We borrow you books")
#
#
# def welcome_html(request):
#     query_set = Author.objects.all()
#     return render(request, 'book/welcome.html', {"authors": list(query_set)})
#
#
# def find_by_id(request, user_id):
#     return HttpResponse(user_id)

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CustomFilter
    search_fields = ['genre', 'isbn']
    # ordering_fields = ['title']

    # def get_queryset(self):
    #     queryset = Book.objects.all()
    #     author_id = self.request.query_params.get('author_id')
    #     if author_id is not None:
    #         queryset = queryset.filter(author_id=author_id)
    #     return queryset


#
# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     # def get_queryset(self):
#     #     return Book.objects.all()
#     #
#     # def get_serializer_class(self):
#     #     return BookSerializer
#
#     def get_contest(self):
#         return {'request': self.request}
#
#     # def get(self, request):
#     #     queryset = Book.objects.all()
#     #     serializer = BookSerializer(queryset, many=True, context={'request': request})
#     #     return Response(serializer.data, status=status.HTTP_200_OK)
#     #
#     # def post(self, request):
#     #     serializer = CreateBookSerializer(data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save()
#     #     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get_serializer_context(self):
#         return {'request': self.request}

# def get(self, request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     serializer = BookSerializer(book)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# def put(self, request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     serializer = CreateBookSerializer(book, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# def delete(self, request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     book.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, DjangoModulePermission]

    def get_serializer_context(self):
        return {'request': self.request}


class BookInstanceAPIView(ListCreateAPIView):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return ReviewBook.objects.filter(book_id=self.kwargs['book_pk'])

    def get_serializer_context(self):
        return {'book_id': self.kwargs['book_pk']}

# class AuthorList(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#     # def get_queryset(self):
#     #     return Author.objects.all()
#
#     # def get_serializer_class(self):
#     #     return AuthorSerializer
#
#     def get_contest(self):
#         return {'request': self.request}
#
#     # def get(self, request):
#     #     query_set = Author.objects.all()
#     #     serializer = AuthorSerializer(query_set, many=True, context={'request': request})
#     #     return Response(serializer.data, status=status.HTTP_200_OK)
#     #
#     # def post(self, request):
#     #     serializer = CreateBookSerializer(data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save()
#     #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class AuthorDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#     def get_serializer_context(self):
#         return {'request': self.request}
#
#     # def get(self, request, pk):
#     #     author = get_object_or_404(Author, pk=pk)
#     #     serializer = AuthorSerializer(author, context={'request': request})
#     #     return Response(serializer.data, status=status.HTTP_200_OK)
#     #
#     # def put(self, request, pk):
#     #     author = get_object_or_404(Author, pk=pk)
#     #     serializer = CreateBookSerializer(author, data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save()
#     #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#     #
#     # def delete(self, request, pk):
#     #     author = get_object_or_404(Author, pk=pk)
#     #     author.delete()
#     #     return Response(status=status.HTTP_204_NO_CONTENT)
#     #
#
#
# # @api_view(['GET', 'POST'])
# # def book_list(request):
# #     if request.method == 'GET':
# #         queryset = Book.objects.select_related('author').all()
# #         serializer = BookSerializer(queryset, many=True, context={'request': request})
# #         return Response(serializer.data, status=status.HTTP_200_OK)
# #     elif request.method == 'POST':
# #         serializer = CreateBookSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# # @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# # def book_details(request, pk):
# #     book = get_object_or_404(Book, pk=pk)
# #     if request.method == 'GET':
# #         serializer = BookSerializer(book)
# #         return Response(serializer.data, status=status.HTTP_200_OK)
# #     elif request.method == 'PUT':
# #         serializer = CreateBookSerializer(book, data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data, status=status.HTTP_200_OK)
# #     elif request.method == 'DELETE':
# #         book.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def author_list(request):
#     if request.method == 'GET':
#         query_set = Author.objects.all()
#         serializer = AuthorSerializer(query_set, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CreateBookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def author_detail(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     if request.method == 'GET':
#         serializer = AuthorSerializer(author, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     if request.method == 'PUT':
#         serializer = CreateBookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     if request.method == 'DELETE':
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
