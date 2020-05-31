from django.utils import timezone
from django.views.generic.detail import DetailView
from django.shortcuts import render

from .models import BlogPost


class HomePageView(View):
    def get(self, request):
        return render(request, 'pages/home.html')


class BlogPostDetailView(DetailView):

    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
