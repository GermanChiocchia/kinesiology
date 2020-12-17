# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


class KinesiologyPatients(models.Model):
    _name = 'kinesiology.patients'
    _description = 'Patients'

    name = fields.Char(string=u'Nombre')
    apellido = fields.Char(string = u'Apellido')
    documento = fields.Char(string = u'Documento')
    nacimiento = fields.Date(string = u'Fecha de nacimiento')
    localidad_id = fields.Many2one(string='Localidad', comodel_name='kinesiology.localities', ondelete='restrict')
    domicilio = fields.Char(string='Domicilio')
    telefono = fields.Char(string='Telefono')
    social_id = fields.Many2one(string='Obra social', comodel_name='kinesiology.health.insurance', ondelete='restrict')
    profesional_id = fields.Many2one(string='Profesional', comodel_name='kinesiology.professionals', ondelete='restrict')