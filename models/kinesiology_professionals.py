# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


class KinesiologyProfessionals(models.Model):
    _name = 'kinesiology.professionals'
    _description = 'Professionals'

    name = fields.Char(string=u'Nombre')
    apellido = fields.Char(string='Apellido')
    matricula = fields.Integer(string='Matricula')
    localidad_id = fields.Many2one(string='Localidad', comodel_name='kinesiology.localities', ondelete='restrict')
    direccion = fields.Char(string='Direccion')
    telefono = fields.Char(string='Telefono')