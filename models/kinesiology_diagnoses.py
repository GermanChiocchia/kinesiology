# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


class KinesiologyDiagnoses(models.Model):
    _name = 'kinesiology.diagnoses'
    _description = 'Diagnoses'

    name = fields.Char(string=u'Nombre')