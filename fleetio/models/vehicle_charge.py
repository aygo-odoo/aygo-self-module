# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Vehicle_Charge(models.Model):
    _name = "vehicle.charge"
    _description = "Fleet Charge value Model"

    vehicle = fields.Char(string = 'Vehicle Model',required=True)