from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import HttpResponse, render, redirect


from .models import Event
from .forms import EventForm
# Create your views here. 

def index(request): 

	event_list = Event.objects.order_by("-date") 
	if request.method == "POST": 
		form = EventForm(request.POST) 
		if form.is_valid(): 
			form.save() 
			return redirect('event_app') 
	form = EventForm() 

	e_page = { 
			"forms" : form, 
			"list" : event_list, 
			"title" : "EVENT LIST", 
		} 
	return render(request, 'eventapp/events.html', e_page) 



### function to remove item ###
def remove(request, id): 
    item = get_object_or_404(Event, id = id)
    if request.method =="POST":
        item.delete()
    return render(request, 'eventapp/events.html') 

 