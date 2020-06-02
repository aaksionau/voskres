from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('<int:id>/', views.BlogPostDetailView.as_view(), name='blogpost-detail'),
]
