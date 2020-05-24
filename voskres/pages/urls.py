from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>/', views.BlogPostDetailView.as_view(), name='blogpost-detail'),
]
