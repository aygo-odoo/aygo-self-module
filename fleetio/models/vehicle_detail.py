# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Vehicle_Detail(models.Model):
    _name = "vehicle.detail"
    _description = "fleet Model"

    vehicle = fields.Char(string = 'Vehicle',required=True)
    licence_plate = fields.Char(string = 'Licence Plate', required = True)
    fleet_cost = fields.Float(string = 'Fleet cost',required = True)
    transportation = fields.Selection(
        string = 'Transportation',
        selection = [('two_wheeler','Two Wheeler'),('four_wheeler','Four Wheeler'),('heavy_vechiles','Heavy Vehicle')]
    )