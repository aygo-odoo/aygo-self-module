# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Vehicle_Type(models.Model):
    _name = "vehicle.type"
    _description = "Fleet type Model"

    vehicle = fields.Char(string = 'Vehicle Model',required=True)