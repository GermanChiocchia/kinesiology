# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


class KinesiologyTreatments(models.Model):
    _name = 'kinesiology.treatments'
    _description = 'Treatments'

    codigo = fields.Integer(string='Codigo')
    descripcion = fields.Char(string='Descripcion')
    precio = fields.Float(string='Precio')