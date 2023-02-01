# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Vehicle_Odometer(models.Model):
    _name = "vehicle.odometer"
    _description = "Fleet Odometer value Model"

    vehicle = fields.Char(string = 'Vehicle Model',required=True)