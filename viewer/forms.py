import re
from datetime import date

from django.core.exceptions import ValidationError
from django.forms import (
    CharField, Form, ModelChoiceField, DateField, Textarea, IntegerField, ModelForm)


from viewer.models import Genre, Movie


# A validator that is not related to a certain Filed type nor a certain field
def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


def no_special_char_validator(value):
    forbidden = "%¤#+=/()"
    if any(c in value for c in forbidden):
        raise ValidationError("You can't use special characters.")


# We will create our own field type
class PastMonthField(DateField):

    def validate(self, value):
        # The usual validation for the field DateField
        # If you write a date that is not valid, an exception will be raised
        super().validate(value)

        # Then if the date you write is valid, we do our own validations
        # Then the added customised validation we want to have
        if value >= date.today():
            raise ValidationError('Only past dates allowed here.')

    def clean(self, value):
        result = super().clean(value)

        # Change the date value to the first day of the month
        return date(year=result.year, month=result.month, day=1)


# class MovieForm(Form):
#     title = CharField(max_length=128, validators=[capitalized_validator, no_special_char_validator])
#     genre = ModelChoiceField(queryset=Genre.objects)
#     rating = IntegerField(min_value=1, max_value=10)
#     released = PastMonthField()
#     description = CharField(widget=Textarea, required=False)
#
#     def clean_description(self):
#         """
#         This cleans the field description after it has been validated
#         :return:
#         """
#         initial = self.cleaned_data['description']
#         sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
#         return '. '.join(sentence.capitalize() for sentence in sentences)
#
#     def clean(self):
#         result = super().clean()
#         if result['genre'].name == 'Horror' and result['rating'] > 5:
#             # Raise validation error
#             self.add_error('genre' "The genre can't be horror")
#             self.add_error('rating' "The rating of a horror can't be more than 5")
#             raise ValidationError("Horror movies aren't so good to be rated over 5.")
#         return result

#---
class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = []

    # This overriding the fields that were automatically generated
    title = CharField(validators=[capitalized_validator, no_special_char_validator])
    rating = IntegerField(min_value=1, max_value=10)
    released = PastMonthField()

    def clean_description(self):
        # Force each sentence of the description to be capitalized.
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        cleaned = '. '.join(sentence.capitalize() for sentence in sentences)
        self.cleaned_data['description'] = cleaned
        return cleaned

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'Horror' and result['rating'] > 5:
            raise ValidationError(
                "Horror movies are usually bad. And they don't deserve more than 5 points"
            )
        return result

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"
