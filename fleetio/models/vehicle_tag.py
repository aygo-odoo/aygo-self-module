# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Vehicle_Tag(models.Model):
    _name = "vehicle.tag"
    _description = "Fleet tags Model"

    vehicle = fields.Char(string = 'Vehicle Model',required=True)