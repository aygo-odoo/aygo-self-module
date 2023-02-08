# -*- coding: utf-8 -*-

from odoo import fields, models


class Vehicle_Tag(models.Model):
    _name = 'vehicle.tag'
    _description = 'Vehicle Tag'

    name = fields.Char('Tag Name', required=True, translate=True)
    color = fields.Integer('Color')

    _sql_constraints = [('name_uniq', 'unique (name)', "Tag name already exists !")]
