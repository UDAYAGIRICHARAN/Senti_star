from django import forms
from .models import Image, Audio

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ('image',)
        def __init__(self, *args, **kwargs):
            super(ImageUploadForm, self).__init__(*args, **kwargs)
            self.fields['image'].required = False
class AudioUploadForm(forms.ModelForm):
    class Meta:
        model = Audio
        audio = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ('audio',)
        def __init__(self, *args, **kwargs):
            super(AudioUploadForm, self).__init__(*args, **kwargs)
            self.fields['audio'].required = False
class UrlUploadForm(forms.Form):
    url = forms.CharField(label='url', max_length=100)
    def __init__(self, *args, **kwargs):
        super(UrlUploadForm, self).__init__(*args, **kwargs)
        self.fields['url'].required = False
class FileUploadForm(forms.Form):
    file = forms.FileField(label='file', max_length=100)
    def __init__(self, *args, **kwargs):
        super(FileUploadForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False
# Compare this snippet from main\api\viewsSentiSpeech.py:
            
# Compare this snippet from main\api\views.py:

