# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


class KinesiologyHealthInsurance(models.Model):
    _name = 'kinesiology.health.insurance'
    _description = 'Health insurance'

    name = fields.Char(string=u'Nombre')