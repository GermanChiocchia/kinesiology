# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    timeframes_ids = fields.One2many(string=u'Horarios',comodel_name='kinesiology.timeframes',inverse_name='company_id')

class KinesiologyTimeFrames(models.Model):
    _name = 'kinesiology.timeframes'
    _description = 'Horarios'

    company_id = fields.Many2one(string=u'Compania',comodel_name='res.company',ondelete='set null')
    day = fields.Char(string=u'Dia')
    enabled = fields.Boolean(string=u'Habilitado')