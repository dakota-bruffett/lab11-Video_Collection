from django.db import models
from urllib import parse
from django.core.exceptions import ValidationError

class Video(models.Model):
    name = models.CharField(max_length= 200)
    url = models.CharField(max_length=400)
    notes = models.TextField(blank=True, null= False)
    video_id = models.CharField(max_length=50, unique=True)





def save(self, *args, **kwargs):
    try:
        url_componantes = parse.urlparse(self.url)
        if url_componantes.scheme != 'http'or url_componantes.netloc != 'www.youtube.com' or url_componantes.path != '/watch':
            raise ValidationError(f'Invalid url{self.url}')
        query_string = url_componantes.query
        if not query_string:
            raise ValidationError(f'Invalid url{self.url}')
        parameters = parse.parse_qs(query_string,strict_parsing=True)
        parameters_list = parameters.get('v')
        if not parameters_list:
            raise ValidationError(f'Invalid url{self.url}')
        self.video_id = parameters_list[0]
    except ValueError as e:
        raise ValidationError(f'Invalid url{self.url}') from e
    super().save(*args , **kwargs )





def __str__(self):
    return (f'id:{self.pk}, Name: {self.name} , url: {self.url} ,NOTES: {self.notes}(:200), '
            f'Video_id: {self.video_id},')

# Create your models here.
