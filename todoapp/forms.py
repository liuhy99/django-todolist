from django.forms import ModelForm
from todoapp.models import Post
from django import forms

class TodoappForm(ModelForm):
    class Meta:
        model=Post
        fields="__all__"
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(TodoappForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False