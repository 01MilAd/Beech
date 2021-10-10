from django import forms

from profiles.models import Profile


class EditProfileForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField()
    firstname = forms.CharField()
    lastname = forms.CharField()

    class Meta:
        model = Profile
        fields = ('phone', 'avator', 'bio', 'age', 'gender', 'birthday')


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'avator', 'bio', 'age', 'gender', 'birthday')