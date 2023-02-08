# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Vehicle_Type(models.Model):
    _name = "vehicle.type"
    _description = 'Fleet Service Type'
    _order = 'name'

    name = fields.Char(required=True, translate=True)
    category = fields.Selection([
        ('contract', 'Contract'),
        ('service', 'Service')
        ], 'Category', required=True, help='Choose whether the service refer to contracts, vehicle services or both')