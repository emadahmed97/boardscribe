from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


class Classes(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True)


    def __str__(self):
        return self.title


class Notes(models.Model):
    title = models.CharField(max_length=200)
    note_text = models.TextField(max_length=2000)
    pub_date = models.DateTimeField('date published', null=True)
    _class = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True,)
    note_image = models.FileField(null=True, blank=True)    # add image field to this later

    def __str__(self):
        return self.title
