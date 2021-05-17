from django.db import models
from django.urls import reverse

class ProjectName(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    postdate = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])
