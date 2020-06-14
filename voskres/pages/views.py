from django.utils import timezone
from django.views.generic import FormView, TemplateView
from django.views.generic.detail import DetailView, View
from django.views.generic.list import ListView
from django.shortcuts import render

from .models import BlogPost
from .forms import FeedbackForm


class HomePageView(View):
    def get(self, request):
        return render(request, 'pages/home.html')


class BlogPostDetailView(DetailView):
    model = BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    paginate_by = 10
    context_object_name = 'blogposts'

    def get_queryset(self):
        return BlogPost.objects.filter(post_type=self.kwargs['category'].rstrip('s'))


class ContactsFormView(FormView):
    template_name = 'pages/contacts.html'
    success_url = '/contacts/thankyou/'
    form_class = FeedbackForm

    def form_valid(self, form, **kwargs):
        form.save()
        form.send_email()
        return super().form_valid(form)


class ContactsThankYouView(TemplateView):
    template_name = 'pages/thankyou.html'


def translation(request):
    return render(request, 'pages/translation.html')
