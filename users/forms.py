from django import forms
from .models import User, Urls, Numbers

class UrlsForm(forms.ModelForm):
    class Meta:
        model = Urls
        fields = ['url_name', 'url']


class NumbersForm(forms.ModelForm):
    class Meta:
        model = Numbers
        fields = ['number_name', 'number']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    url = forms.inlineformset_factory(User, Urls, form=UrlsForm, extra=1)
    number = forms.inlineformset_factory(User, Numbers, form=NumbersForm, extra=1)