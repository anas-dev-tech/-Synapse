from django import forms
from .models import *




class ChatMessageCreateForm(forms.ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['content']
        widgets = {
            'content': forms.TextInput(
                attrs={
                    'placeholder': 'Add Message',
                    'class': 'p-4 text-black ',
                    'maxlength':'300',
                    'autofocus':True,
                }
            )
        }




