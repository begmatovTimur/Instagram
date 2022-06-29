from django import forms
from main.models import Comment, User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


    author = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.RadioSelect()
    )
    text = forms.CharField(
        max_length=99999999,
        widget=forms.TextInput(attrs={'class': 'textarea', 'placeholder': 'Add a comment...'})
    )
    