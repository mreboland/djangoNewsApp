# List view is to show many items (a list), detail view is used to show 1 item.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
# reverse_lazy won't execute until the value is needed
# revers: It’s similar to the url template tag which use to convert namespaced url to real url pattern.
# It is useful because it prevent 'Reverse Not Found' exceptions when working with URLs that may not be immediately known.
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

# We added author to our fields as we want to specify who wrote it. However once it's written we do not want the author to be changed hence in the edit view it's not included
# At present the author on a new article can be set to any user. However we want it so it will automatically set to the current user.
# To do so, we'll remove author from fields and instead set it automatically via the form_valid method.
class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        # "author"
    )
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)