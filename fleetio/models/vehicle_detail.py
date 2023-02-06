# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Vehicle_Detail(models.Model):
    _name = "vehicle.detail"
    _description = "fleet Model"
    _rec_name="vehicle"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    vehicle = fields.Char(string = 'Vehicle Model',required=True)
    licence_plate = fields.Char(string = 'Licence Plate', required = True)
    vehicle_type = fields.Selection(
        string = 'Vechicle Type',
        selection = [('two_wheeler','Two Wheeler'),('four_wheeler','Four Wheeler'),('heavy_vechiles','Heavy Vehicle')]
    )
    location = fields.Char(string = 'Location')
    #driver
    driver_name = fields.Char(string = 'Driver Name')
    avaliable = fields.Boolean(string = 'Avaliable')
    #vehicle
    fleet_manager = fields.Char(string = 'Fleet Manager')
    category = fields.Char(string = 'Category')
    #model
    model_year = fields.Integer(string = 'Model Year')
    colour = fields.Char(string = 'Colour')
    transmission = fields.Selection(
        string = 'Transmission',
        selection = [('automatic','Automatic'),('manual','Manual')]
    )
    #engine
    horsepower = fields.Integer(string ='HorsePower')
    fuel_type = fields.Selection(
        string = 'Fuel Type',
        selection = [('diesel','Diesel'),('petrol','Petrol'),('cng','CNG'),('electric','Electric')]
    )
    #description
    description = fields.Char(string ='Description')



