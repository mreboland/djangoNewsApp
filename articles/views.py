# List view is to show many items (a list), detail view is used to show 1 item.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"
    

# will use Django’s generic class-based views for DetailView, UpdateView and DeleteView. We specify
# which fields can be updated–title and body–and where to redirect the user after deleting an
# article: article_list.

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"
    
class ArticleUpdateView(UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"
    
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")