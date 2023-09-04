from django.urls import path, include
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register('books', views.BookViewSet, basename='books')
router.register('authors', views.AuthorViewSet)
router.register('reviews', views.ReviewViewSet, basename='reviews')

# parent route
book_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
# child route
book_router.register('reviews', views.ReviewViewSet, basename='book-reviews')

# urlpatterns = router.urls + book_router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('', include(book_router.urls)),
    path('bookinstance/', views.BookInstanceAPIView.as_view())
]


# path('authors/', views.AuthorList.as_view()),
# path('authors/<int:pk>', views.AuthorDetails.as_view(), name="author-detail")

# path('authors/', views.author_list),
# path('authors/<int:pk>', views.author_detail, name="author-detail")
# path('welcome/', views.welcome),
# path('get-book/', views.get_books),
# path('welcomeH/', views.welcome_html),
# path('find_id/<int:pk>', views.find_by_id)

# ]
