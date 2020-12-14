import django.forms as forms
from authapp.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control {name}'


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'password1', 'password2', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control {name}'
            item.help_text = ''

    def save(self, commit=True):
        user = super().save(commit=commit)  # call native method
        UserProfile.objects.create(user=user)
        return user


class ChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control {name}'
            item.help_text = ''
            if name == 'password':
                item.widget = forms.HiddenInput()

    def save(self, commit=True):
        user = super().save(commit=commit)
        user.userprofile.save()
        return user
