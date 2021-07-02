from django.shortcuts import render, redirect

from django import forms
from events.forms import InputForm
from events.forms import UpdateForm

from . import models
from events.models import Event

# views
# Lista de Eventos
def events(request):
	data = {}
	data["events"] = Event.objects.all()
	return render(request, "events.html", data)

# Novo Evento
def create(request):
	form = InputForm(request.POST or None)
	fields = ['event_name', 'date', 'expected_start', 'expected_end']

	if form.is_valid():
		event_name = form.cleaned_data["event_name"]
		date = form.cleaned_data["date"]
		expected_start = form.cleaned_data["expected_start"]
		expected_end = form.cleaned_data["expected_end"]
		saving_all = models.Event.objects.create(
			event_name=event_name,
			date=date,
			expected_start=expected_start,
			expected_end=expected_end
		)
		saving_all.save()
		# redirect to a new URL:
		return redirect("events")
	return render(request, "create.html", {"form": form, "events": events})

# update
def update(request, id):
	event = Event.objects.get(id=id)

	if request.method == 'POST':
		form = UpdateForm(request.POST)
		if form.is_valid():
			event.event_name = form.cleaned_data["event_name"]
			event.date = form.cleaned_data["date"]
			event.expected_start = form.cleaned_data["expected_start"]
			event.expected_end = form.cleaned_data["expected_end"]
			event.save()
			return redirect("events")
	else:
		initial_dict = {
			"id": event.id,
			"event_name": event.event_name,
			"date": event.date,
			"expected_start": event.expected_start,
			"expected_end": event.expected_end
		}
		form = InputForm(initial=initial_dict)
	return render(request, "create.html", {"form": form, "event": event})

# delete
# def delete(request, id):
# 	event = Event.objects.get(id=id)
# 	event.delete()
# 	return redirect("events")


# delete
def delete(request, id):
	event = Event.objects.get(id=id)
	if request.method == 'POST':
		event.delete()
		return redirect("events")
	return render(request, 'event_delete_confirm.html', {'object': event})
