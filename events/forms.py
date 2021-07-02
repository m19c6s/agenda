from django import forms
from django.forms import formset_factory

from bootstrap_datepicker_plus import DatePickerInput

from events.models import Event

from django.utils.datastructures import MultiValueDict

import datetime

class InputForm(forms.Form):
    # id do evento
    id = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput()
    )

    # nome do evento
    event_name = forms.CharField(
        label='Nome do evento',
        max_length=80,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    # data do evento
    date = forms.DateField(
        label='Informe a data do evento',
        required=False,
        input_formats=['%d/%m/%Y'],
        widget=DatePickerInput(format='%d/%m/%Y')
    )

    def clean_date(self):
        # data digitada no formulario
        date = self.cleaned_data['date']

        # verifica se a data está no passado
        if date < datetime.date.today():
            raise forms.ValidationError('Data inválida')

        # verfica se esta data já existe no banco
        result = Event.objects.filter(date=date)

        # caso já exista um evento igual no banco emite um alerta
        if result:
            raise forms.ValidationError("A data " + date.strftime('%d/%m/%Y') + " já existe, altere a data do seu evento.")

        return date

    # previsao de inicio do evento
    expected_start = forms.TimeField(
        label='Previsao de inicio',
        required=False,
        widget=DatePickerInput(format='%I:%M %p')
    )

    # previsao de encerramento do evento
    expected_end = forms.TimeField(
        label='Previsao de encerramento',
        required=False,
        widget=DatePickerInput(format='%I:%M %p')
    )


class UpdateForm(forms.Form):
    # id do evento
    id = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput()
    )

    # nome do evento
    event_name = forms.CharField(
        label='Nome do evento',
        max_length=80,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    # data do evento
    date = forms.DateField(
        label='Informe a data do evento',
        required=False,
        input_formats=['%d/%m/%Y'],
        widget=DatePickerInput(format='%d/%m/%Y')
    )

    def clean_date(self):
        # data do evento vinda do formulario
        date = self.cleaned_data['date']

        # id do evento vindo do formulario
        id = self['id'].value()

        # verifica se a data está no passado
        if date < datetime.date.today():
            raise forms.ValidationError('Data inválida')

        # verfica excluindo o registro atual, se esta data já tem no banco
        evento = Event.objects.exclude(id=id).filter(date=date)

        # caso já exista um evento igual no banco emite um alerta
        if evento:
            raise forms.ValidationError("A data " + date.strftime('%d/%m/%Y') + " já existe, altere a data do seu evento.")

        return date

    # previsao de inicio do evento
    expected_start = forms.TimeField(
        label='Previsao de inicio',
        required=False,
        widget=DatePickerInput(format='%I:%M %p')
    )

    # previsao de encerramento do evento
    expected_end = forms.TimeField(
        label='Previsao de encerramento',
        required=False,
        widget=DatePickerInput(format='%I:%M %p')
    )
