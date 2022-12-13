from django import forms
from . import models

# Создание формы Университета(для изменения , удаления или Добавления)
class UniViewForm(forms.ModelForm):
    class Meta:
        model = models.Uni
        fields = "__all__"
