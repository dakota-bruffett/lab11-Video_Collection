from django.db import models


class video(models.model):
    name = models.CharField(max_length= 200)
    url = models.CharField(max_length=400)
    notes = models.TextField(blank=True, null= False)
def __str__(self):
    return f'id:{self.pk}, Name: {self.name} , url: {self.url} ,NOTES: {self.notes}(:200)'

# Create your models here.
