# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from cliente.models import Ticket
from cliente.forms import TicketForm
from django.contrib import messages


# Create your views here.

def index_ticket(request):
    ticket = Ticket.objects.all()
    return render(request,'tickets/factura_listaPendiente.html',{'tickets':ticket})

def editarTicket(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method =='GET':
        form = TicketForm(instance=ticket)
    else:
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
        return redirect('ticket:index')
    return render(request, 'tickets/factura_formulario.html',{'form':form})

def eliminarTicket(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('ticket:index')
    return render(request, 'tickets/factura_eliminar.html', {'ticket': ticket})

def create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Ticket creada con exito!')
        return redirect('ticket:index')
    else:
        form = TicketForm()
        messages.add_message(request, messages.SUCCESS, 'Error al crear Factura!')
    return render(request, 'facturas/factura_formulario.html',{'form':form})



