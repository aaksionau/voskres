from django.utils import timezone
from django.views.generic.detail import DetailView, View
from django.shortcuts import render

from .models import BlogPost


class HomePageView(View):
    def get(self, request):
        blogposts = BlogPost.objects.all()[:7]
        return render(request, 'pages/home.html', {'blogposts': blogposts})


class BlogPostDetailView(DetailView):

    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
