# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


class KinesiologyLocalities(models.Model):
    _name = 'kinesiology.localities'
    _description = 'Localities'

    name = fields.Char(string=u'Nombre')
    postal = fields.Integer(string = u'Codigo postal')