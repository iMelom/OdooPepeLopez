# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Prestado(models.Model):
    _name = 'biblioteca.prestado'
    _description = "Diagnostico"
    _rec_name = 'id'
    
    socio = fields.Many2one('biblioteca.socio', string="Medico")
    comic = fields.Many2one('biblioteca.comic',string='Paciente')
    inicio = fields.Char(string='Sintomas')

