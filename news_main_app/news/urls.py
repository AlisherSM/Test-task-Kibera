from django.urls import path, include
from . import views



urlpatterns = [
  path('news', views.NewsViews.as_view(), name='news'),
  path('news-reversed', views.NewsViewsReversed.as_view(), name='news-reversed'),
  path('add-news', views.NewsCreateView.as_view(), name='add-news'),
  path('delete-news/<int:pk>', views.NewsDeleteView.as_view(), name='delete-news'),
  path('update-news/<int:pk>', views.NewsUpdateView.as_view(), name='update-news')
]