from django.views.generic import TemplateView

# Using Django's TemplateView generic class-based view
class HomePageView(TemplateView):
    template_name = "home.html"