from django.db import models

from albums.models import Album

from AWS import rename_file
from AWS import delete_mediafile

class ImageManager(models.Manager):

    def delete_by_aws(self, id):
        image = self.filter(id=id).first()

        if image and delete_mediafile(image.bucket, image.key):
            image.delete()
            
            return id

class Image(models.Model):
    key = models.CharField(max_length=100, null=False, blank=False)
    bucket = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    content_type = models.CharField(max_length=20, null=False, blank=False)
    size = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ImageManager()

    def __str__(self):
        return self.name

    @property
    def url(self):
        return f"https://{self.bucket}.s3.amazonaws.com/{self.key}"

    @property
    def title(self):
        return self.name.split('.')[0]

    @property
    def extension(self):
        return self.name.split('.')[-1]
    
    def set_name(self, new_name):
        new_name = new_name + '.' + self.extension
        new_key = self.album.key + new_name

        if rename_file(self.bucket, new_key, self.key):
            self.key = new_key
            self.name = new_name

            self.save()
