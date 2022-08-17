from distutils.log import error
from django import forms
from .models import UserBase
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm


class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(label="Enter Username", min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
                             'required': 'Sorry, your email is required'})
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email')

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken'
            )
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {
                'class': 'form-control mb-3',
                'placeholder': 'Username'
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'class': 'form-control mb-3',
                'placeholder': 'E-mail',
                'name': 'email'
            }
        )
        self.fields['password'].widget.attrs.update(
            {
                'class': 'form-control mb-3',
                'placeholder': 'Password'
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'class': 'form-control mb-3',
                'placeholder': 'Repeat Password'
            }
        )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Username',
            'id': 'login-user'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd'
        }
    ))


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Account email',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Email',
                'id': 'form-email'
            }
        )
    )
    user_name = forms.CharField(
        label='Username (cannot be changed)',
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Username',
                'id': 'form-username',
                'readonly': 'readonly'
            }
        )
    )
    first_name = forms.CharField(
        label='First Name',
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'First Name',
                'id': 'form-firstname'
            }
        )
    )

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name'].lower()
        email = self.cleaned_data['email']
        r = UserBase.objects.get(email=email)
        if r.user_name != user_name:
            raise forms.ValidationError("You can't change the username")
        return user_name

    class Meta:
        model = UserBase
        fields = ('email', 'user_name', 'first_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['email'].required = True


class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Email',
            'id': 'form-email'
        }
    ))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = UserBase.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                "We cannot find that email address"
            )
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'New Password',
                'id': 'form-new-passowrd1'
            }
        )
    )
    new_password2 = forms.CharField(
        label='Repeat Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Repeat New Password Password',
                'id': 'form-new-passowrd1'
            }
        )
    )
