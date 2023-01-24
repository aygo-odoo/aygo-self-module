# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Vehicle_Service(models.Model):
    _name = "vehicle.service"
    _description = "Fleet Service Model"

    name=fields.Char()

