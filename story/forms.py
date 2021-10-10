from ckeditor.widgets import CKEditorWidget
from django import forms

from story.models import Story


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'sound', 'cover', 'caption')
        help_texts = {
            'caption':' Max 1000 char'
        }
        widgets = {
            'caption': CKEditorWidget()
        }

