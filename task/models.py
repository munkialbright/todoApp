from django.db import models

# Create your models here.
class Task(models.Model):
    task_Id = models.AutoField(primary_key = True)
    task_title = models.CharField(max_length = 50, unique = True)
    task_description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length = 10, default='active')
    start_time = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_title + ' (' + self.status + ')'