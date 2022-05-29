from django.contrib.auth.forms import (
  AuthenticationForm, PasswordChangeForm, UserCreationForm
)
from django.forms import CharField, Textarea, Select


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'email']

    biography = CharField(
        label='Biography',
        widget=Textarea(attrs={'Placeholder': 'Tell us your story with movies'}),
        min_length=20
    )
    gender = CharField(
        widget=Select(
            choices=[
                ("M", 'Male'),
                ("F", 'Female')
            ]
        )
    )

    def save(self, commit=True):
        self.instance.is_active = False
        return super().save(commit)
