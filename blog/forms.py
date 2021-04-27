from django.contrib.auth import get_user_model

user = get_user_model(user)

class LoginForm(forms.Form):
    username = forms.CharField
    password = forms.CharField (
        widget = forms.PasswordInput(
            attrs = {'class', 'form-control', 'id': 'user_password'}
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username_iexact = username)
        if not qs.exists():
            raise forms.ValidationError('Invalid User')
            return username
        
class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(required=True)
    password1 = forms.CharField(
        label = 'password'
        widget = forms.PasswordInput(
            attrs = {
                'class', 'form-control', 'id': 'user_password'
            }
        )
    )

        password2 = forms.CharField(
        label = ' confirm password'
        widget = forms.PasswordInput(
            attrs = {
                'class', 'form-control', 'id': 'user_confirm_password'
            }
        )
    )        

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.object.filter(username_iexact = username)
        if qs.exists():
            raise forms.ValidationError ('User Already Exists')
            return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.object.filter(email__iexact=email)
        if qs exists ():
            raise forms.ValidationError('Email Already Exists')
            return email