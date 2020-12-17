# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


class KinesiologyMedicalOffices(models.Model):
    _name = 'kinesiology.medical.offices'
    _description = 'Medical offices'

    name = fields.Char(string = u'Nombre')
    direccion = fields.Char(string = u'Direccion')
    telefono = fields.Char(string = u'Telefono')