from django import forms
from main.models import Category, User, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    author = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.RadioSelect
    )
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'input mb-4', 'placeholder': 'your post title'})
    )
    text = forms.CharField(
        max_length=99999999,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'your post text'})
        
    )