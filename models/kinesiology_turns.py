# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


class KinesiologyTurns(models.Model):
    _name = 'kinesiology.turns'
    _description = 'Turns'

    paciente_id = fields.Many2one(string='Paciente', comodel_name='kinesiology.patients', ondelete='restrict')
    ficha_id = fields.Many2one(string='Ficha', comodel_name='kinesiology.records', ondelete='restrict')
    inicio = fields.Date(string='Fecha inicio')
    cantidad = fields.Integer(string='Cantidad')
    horario = fields.Datetime(string='Horario')
    dia = fields.Char(string='Dia')
    estado = fields.Selection(string='Estado', selection=[('pendiente', 'Pendiente'),('realizado', 'Realizado')], default='pendiente')