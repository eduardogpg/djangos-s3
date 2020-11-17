from django.forms import ModelForm

from .models import Album

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'id': 'title',
            'placeholder': 'Título'
        })
        
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'id': 'description',
            'placeholder': 'Descripción'
        })