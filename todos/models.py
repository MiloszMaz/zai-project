from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "do zrobienia", "Do zrobienia"
        DOING = "w trakcie", "W trakcie"
        DONE = "zrobione", "Zrobione"

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=12,
        choices=Status.choices,
        default=Status.TODO,
    )

    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="tasks",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
