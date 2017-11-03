from django import forms
from django.core import validators
from home.models import UserProfileInfo
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User


gender_choices = [('male', 'Male'), ('female', 'Female')]

sec_questions = [("nickname", 'What was your childhood nickname?'),
                 ("bff", "What is the name of your favorite childhood friend?"),
                 ("city", "In what city or town did your mother and father meet?"),
                 ("middle", "What is the middle name of your oldest child?"),
                 ("team", "What is your favorite team?"),
                 ("movie", "What is your favorite movie?"),
                 ("sport", "What was your favorite sport in high school?"),
                 ("food", "What was your favorite food as a child?")
                 ]


class UserForm(forms.ModelForm):
    model = User
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-group-lg bg-transparent light',
            'placeholder': 'Enter your username.',
            'id':'place'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control input-group-lg bg-transparent light',
            'placeholder':'Enter your password.',
            'id':'place'
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class':'form-control input-group-lg bg-transparent light',
            'placeholder':'Enter your email.',
            'id':'place'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    portfolio = forms.URLField(widget=forms.URLInput(
        attrs={
            'class': 'form-control input-group-lg bg-transparent light',
            'placeholder':'Enter link to your profile.',
            'id':'place'
        }
    ))
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs= {
                'id':"drop_zone",
                'class':"FileUpload",
                'accept':'.jpg,.png,.gif',
                'onchange':'handleFileSelect(this)'
        }
    ))

    class Meta:
        model = UserProfileInfo
        fields = ('portfolio', 'picture')


#
# class LoginForm(forms.ModelForm):
#     first_name = forms.CharField(128, validators=[validators.MaxLengthValidator(20)])
#     last_name = forms.CharField(128)
#     username = forms.CharField(128)
#     email_ad = forms.EmailField(label="Email Address")
#     email_ver = forms.EmailField(label="Email Address Confirmation")
#     password = forms.CharField(widget=forms.PasswordInput(render_value=True))
#     password_ver = forms.CharField(widget=forms.PasswordInput(render_value=True))
#     gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect())
#     security_question = forms.ChoiceField(choices=sec_questions)
#     question_answer = forms.CharField(128)
#     terms_check = forms.BooleanField(required=True, label="I have read the terms!")
#     no_bot = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
#
#     class Meta:
#         model = UserData
#         fields = '__all__'
#
#     def clean(self):
#         all_clean = super().clean()
#         email_ad = all_clean.get('email_ad')
#         email_ver = all_clean.get('email_ver')
#
#         if email_ad != email_ver:
#             raise forms.ValidationError("Please correct to matching emails.")
#
#         try:
#             validate_email(email_ad)
#
#         except ValidationError as e:
#             print("oops! wrong email")
#
#         else:
#             print("hooray! email is valid")
