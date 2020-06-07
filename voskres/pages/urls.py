from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('blogposts/<int:pk>/', views.BlogPostDetailView.as_view(),
         name='blogpost-detail'),
    path('blogposts/<str:category>', views.BlogPostListView.as_view(),
         name="blogpost-list"),
    path('contacts/', views.ContactsFormView.as_view(), name='contacts'),
    path('contacts/thankyou/', views.ContactsThankYouView.as_view(), name='thankyou'),
    path('translation', views.translation, name="translation"),

]
