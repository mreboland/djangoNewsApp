# We import a mixin, which is a special kind of multiple inheritance that django uses to avoid duplicate code and still allows customization.
# To clarify, for example, the built-in generic ListView needs a way to return a template. But so
# does DetailView and in fact almost every other view. Rather than repeat the same code in each big
# generic view, Django breaks out this functionality into a “mixin” known as
# TemplateResponseMixin170. Both ListView and DetailView use this mixin to render the proper
# template. LoginRequiredMixin is a powerful mixin that makes restricting access to logged in users easy.
# To restrict users so they can only modify their own articles, we will use another mixin, UserPassesTestMixin. We will add said mixing the the update, and delete views.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# List view is to show many items (a list), detail view is used to show 1 item.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
# reverse_lazy won't execute until the value is needed
# revers: It’s similar to the url template tag which use to convert namespaced url to real url pattern.
# It is useful because it prevent 'Reverse Not Found' exceptions when working with URLs that may not be immediately known.
from django.urls import reverse_lazy

from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"
    

# will use Django’s generic class-based views for DetailView, UpdateView and DeleteView. We specify
# which fields can be updated–title and body–and where to redirect the user after deleting an
# article: article_list.

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"
    

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"
    
    # The test_func methodis used by UserPassesTestMixin for our logic. We need to override it. We do so by setting the var obj to the current object returned by the view using get_object(). We then say if the author on the current object matches the current user on the webpage (whoever is logged in and trying to make the change), then allow it. If false, an error will be auto thrown.
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

# We added author to our fields as we want to specify who wrote it. However once it's written we do not want the author to be changed hence in the edit view it's not included
# At present the author on a new article can be set to any user. However we want it so it will automatically set to the current user.
# To do so, we'll remove author from fields and instead set it automatically via the form_valid method.
# We place the mixin before our view so it'll be read first. This tells CreateView that we intend to restrict access. Once placed, users will be sent to the account login page.
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        # "author"
    )
    
    # When we go to create a new article, author is now no longer a valid field. Author is now auto set to the logged in user.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
