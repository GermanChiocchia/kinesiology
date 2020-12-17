# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


class KinesiologyRecords(models.Model):
    _name = 'kinesiology.records'
    _description = 'Records'

    name = fields.Char(string=u'Nombre')
    diagnostico_id = fields.Many2one(string='Diagnostico', comodel_name='kinesiology.diagnoses', ondelete='restrict')
    ingreso = fields.Date(string='Fecha ingreso')
    medico_id = fields.Many2one(string='Medico', comodel_name='kinesiology.professionals', ondelete='restrict')