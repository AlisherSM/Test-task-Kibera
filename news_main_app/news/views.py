
from .models import News
from .forms import NewsForm
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q


class NewsView(ListView):
    template_name = "news/main_page.html"
    context_object_name = "news"
    paginate_by = 10

    def get_queryset(self):
        return News.objects.all()


class NewsViewReversed(ListView):
    template_name = "news/main_page.html"
    context_object_name = "news"

    def get_queryset(self):
        return News.objects.order_by('publish_date')


class NewsCreateView(CreateView):
    form_class = NewsForm
    template_name = "news/adding_form_page.html"

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, "Новость успешно добавлена")
        news = self.object
        news.save()
        return 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NewsDeleteView(DeleteView):

    context_object_name = 'news'
     
    def get_queryset(self):
        return News.objects.filter(pk=self.kwargs["pk"])
    
    def get_success_url(self):
        messages.success(self.request, "Новость успешно удалена !")
        return reverse('news')


class NewsUpdateView(UpdateView):
    form_class = NewsForm
    template_name = "news/adding_form_page.html"

    
    def get_queryset(self):  # Запрос в БД. Получить, который будет обновлять
        return News.objects.filter(pk=self.kwargs["pk"])
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse('news')


class NewsSearchView(NewsView):
    def get_queryset(self):
        search_news = self.request.GET["search_news"]
        return News.objects.filter(
            Q(title__icontains=search_news)
        )

    def get_context_data(self, **kwargs):
        search_news = self.request.GET["search_news"]
        context = super().get_context_data(**kwargs)
        return context
  
