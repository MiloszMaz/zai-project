from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task, Project
from .forms import TaskForm, ProjectForm
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    # def get_queryset(self):
    #     return Task.objects.exclude(status='zrobione')


class TaskDetailView(DetailView):
    model = Task
    # template_name = "todos/task_detail.html"
    context_object_name = "task"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    # template_name = "todos/task_form.html"
    success_url = reverse_lazy("task_list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    # template_name = "todos/task_form.html"
    success_url = reverse_lazy("task_list")


class TaskDeleteView(DeleteView):
    model = Task
    # template_name = "todos/task_confirm_delete.html"
    success_url = reverse_lazy("task_list")


class ProjectListView(ListView):
    model = Project
    # template_name = "todos/project_list.html"
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = Project
    # template_name = "todos/project_detail.html"
    context_object_name = "project"


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    # template_name = "todos/project_form.html"
    success_url = reverse_lazy("project_list")


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    # template_name = "todos/project_form.html"
    success_url = reverse_lazy("project_list")


class ProjectDeleteView(DeleteView):
    model = Project
    # template_name = "todos/project_confirm_delete.html"
    success_url = reverse_lazy("project_list")
