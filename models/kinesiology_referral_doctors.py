# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


class KinesiologyReferralDoctors(models.Model):
    _name = 'kinesiology.referral.doctors'
    _description = 'Referral doctors'

    name = fields.Char(string=u'Nombre')