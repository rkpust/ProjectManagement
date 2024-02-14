from django.db import models

# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(unique=True, max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=100)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

