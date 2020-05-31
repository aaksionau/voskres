from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.BlogPostDetailView.as_view(), name='blogpost-detail'),
]
