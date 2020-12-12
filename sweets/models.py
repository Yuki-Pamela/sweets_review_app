from django.db import models
from django.core.validators import MaxValueValidator

class Sweet(models.Model):
    name = models.CharField(max_length=200)
    picture = models.URLField(max_length=900, default='https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png')
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
    notes = models.TextField(max_length=2000, default='')

    def __str__(self):
        return self.name

