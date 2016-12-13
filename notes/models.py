from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

from django.utils.text import slugify

from django.contrib.auth.models import User



class Classes(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True)


    def save(self, *args, **kwargs):
                # Uncomment if you don't want the slug to change every time the name changes
                #if self.id is None:
                        #self.slug = slugify(self.name)
            x = self.title
            self.title = x.capitalize()
            super(Classes, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Notes(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200,null=True, blank=True)
    note_text = models.TextField(max_length=2000)
    pub_date = models.DateTimeField('date published', null=True)
    classname = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True,)
    note_image = models.FileField(null=True, blank=True)    # add image field to this later
    slug = models.SlugField(unique=True,null=True,blank=True,max_length=255);
    

    def save(self, *args, **kwargs):
                # Uncomment if you don't want the slug to change every time the name changes
                #if self.id is None:
                        #self.slug = slugify(self.name)
            self.slug = slugify(self.title)
            x = self.title
            self.title = x.title()
            super(Notes, self).save(*args, **kwargs)

    def __str__(self):
        return self.title




