from django import forms
from .models import *
# class FeedbackForm(forms.Form):
#     name = forms.CharField(label='Имя', max_length=7, min_length=2, error_messages={
#         'max_length': 'Слиском много символов',
#         'min_length': 'Слиском мало символов',
#         'required': 'Не должно быть пустое',
#     })
#     surname = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs={"cols": 20, "rows": 2}))
#     rating = forms.IntegerField(label='Рейтинг', max_value=5, min_value=1)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        # exclude = ['name']
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг',
        }
        error_messages = {
            'name': {
                'max_length': 'Слиском много символов',
                'min_length': 'Слиском мало символов',
                'required': 'Не должно быть пустое',
            },
        }
