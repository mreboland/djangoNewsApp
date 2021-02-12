from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
)

# Django automatically adds a primary key to each
# database. Therefore our first article with a primary key of 1 will be at articles/1/edit / and the
# delete route will be at articles/1/delete/.
urlpatterns = [
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("", ArticleListView.as_view(), name="article_list"),
]
