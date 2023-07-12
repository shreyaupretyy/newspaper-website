from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import request
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Articles


class ArticleListView(LoginRequiredMixin, ListView):
    model = Articles
    template_name = "CRUD/article_list.html"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Articles
    template_name = "CRUD/article_detail.html"


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    fields = (
        "title",
        "body",
    )
    template_name = "CRUD/article_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    template_name = "CRUD/article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Articles
    template_name = "CRUD/article_new.html"
    fields = (
        "title",
        "body",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
