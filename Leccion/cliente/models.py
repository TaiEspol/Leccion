# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Ticket (models.Model):
	fecha_emision = models.DateField()
	ciudad1 = 'Guayaquil'	
	ciudad2 = 'Quito'
	ciudad3 = 'Cuenca'
	ciudad4 = 'Quevedo'
	ciudad5 = 'Manabi'
	origen = (
		(ciudad1, 'Guayaquil'),
		(ciudad2, 'Quito'),
		(ciudad3, 'Cuenca'),
		(ciudad4, 'Quevedo'),
		(ciudad5, 'Manabi'),
	)

	ciudad11 = 'Guayaquil'	
	ciudad22 = 'Quito'
	ciudad33 = 'Cuenca'
	ciudad44 = 'Quevedo'
	ciudad55 = 'Manabi'
	destino = (
		(ciudad11, 'Guayaquil'),
		(ciudad22, 'Quito'),
		(ciudad33, 'Cuenca'),
		(ciudad44, 'Quevedo'),
		(ciudad55, 'Manabi'),
	)
	precio = models.IntegerField(max_digits = 8)
	adquiriente = models.IntegerField(max_length=10)
	puesto = models.IntegerField(max_length=2)
	
	

