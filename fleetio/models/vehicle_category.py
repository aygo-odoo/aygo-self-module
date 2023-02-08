# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Vehicle_Category(models.Model):
    _name = "vehicle.category"
    _description = 'Category of the model'
    _order = 'sequence asc, id asc'
    _rec_name="name"
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'Category name must be unique')
    ]

    name = fields.Char(string = 'Category')
    sequence = fields.Integer()