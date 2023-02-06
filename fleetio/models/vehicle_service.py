# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Vehicle_Service(models.Model):
    _name = "vehicle.service"
    _description = "Fleet Service Model"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    service_type =fields.Char(string="Service Type")
    description = fields.Char(string="Description")
    date = fields.Date(string="Date")
    cost = fields.Integer(string="Cost")
    vendor = fields.Char(string="Vendor")
    vehicle = fields.Char(string="Vehicle")
    driver = fields.Char(string="Driver")
    odometer_value = fields.Integer(string="Odometer")
    notes = fields.Text()

