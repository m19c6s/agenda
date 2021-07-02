from django.db import models

# Create your models here.


class Event(models.Model):
	# id do evento
	id = models.AutoField(primary_key=True)

	# nome do evento
	event_name = models.CharField(max_length=80)

	# dia do evento
	date = models.DateField('Dia do Evento', blank=True, null=True, unique=True)

	# previsao de inicio do evento
	expected_start = models.TimeField('Previsão Início', blank=True, null=True)

	# previsao de encerramento do evento
	expected_end = models.TimeField('Previsão Fim', blank=True, null=True)

	def __str__(self):
		return str(self.event_name)