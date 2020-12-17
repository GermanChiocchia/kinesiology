# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


class KinesiologyCashMovement(models.Model):
    _name = 'kinesiology.cash.movement'
    _description = 'Cash movement'

    fecha = fields.Date(string = u'Fecha'),
    motivo = fields.Char(string = u'Motivo'),
    monto = fields.Float(string = u'Monto'),
    tipo = fields.Selection(string = u'Tipo', selection= [('ingreso', 'Ingreso'),('egreso', 'Egreso')])