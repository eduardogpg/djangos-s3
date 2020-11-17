from django.db import models
from django.db.models import Sum

from AWS import create_folder

class AlbumMananger(models.Manager):

    def create_by_aws(self, bucket, title, description):
        
        key = title.replace(' ', '_').lower()
        key = create_folder(bucket, key)
        
        if key:
            return self.create(title=title, description=description,
                                bucket=bucket, key=key)

class Album(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    bucket = models.CharField(max_length=100, null=False, blank=False)
    key = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = AlbumMananger()

    def __str__(self):
        return self.title

    @property
    def images(self):
        return self.image_set.all()

    @property
    def size(self):
        if self.images:
            return self.images.aggregate(Sum('size'))['size__sum']
        else:
            return 0