from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Tasklist


class TasklistList(ListView):
    model = Tasklist
    template_name = "task_list.html"
    ordering = ["is_done", "timestamp_create"]


class TaskCreate(CreateView):
    model = Tasklist
    success_url = reverse_lazy("index")
    fields = ["text"]
    success_message = "Задача создана"
    template_name = "task_create.html"


class TaskUpdate(UpdateView):
    model = Tasklist
    success_url = reverse_lazy("index")
    template_name = "task_update.html"
    fields = ["text", "is_done"]
    success_message = "Изменения сохранены"


class TaskDelete(DeleteView):
    model = Tasklist
    success_url = reverse_lazy("index")
    template_name = "task_delete.html"
    success_message = "Задача удалена"
