# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


class KinesiologyInstitutions(models.Model):
    _name = 'kinesiology.institutions'
    _description = 'Institutions'

    name = fields.Char(string = u'Nombre')
    direccion = fields.Char(string = u'Direccion')
    telefono = fields.Char(string = u'Telefono')
    web = fields.Char(string = u'Web')