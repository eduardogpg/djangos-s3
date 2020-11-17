from django import forms

class UploadFileForm(forms.Form):
    album_id = forms.CharField(required=True, widget=forms.HiddenInput())
    file = forms.FileField(required=True, label='Imagen', 
                            widget=forms.FileInput(
                                attrs={'accept': 'image/*'}
                            ))

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)

        self.fields['file'].widget.attrs['class'] = 'form-control-file'
