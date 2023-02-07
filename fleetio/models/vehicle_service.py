# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Vehicle_Service(models.Model):
    _name = "vehicle.service"
    _description = "Fleet Service Model"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name="service_type"

    description = fields.Char('Description')
    service_type_id = fields.Many2one(
        'vehicle.service', 'Service Type',
        default=lambda self: self.env.ref('vehicle.service', raise_if_not_found=False),
    )
    date = fields.Date(help='Date when the cost has been executed', default=fields.Date.context_today)
    amount = fields.Float('Cost')
    vendor_id = fields.Many2one('res.partner', 'Vendor')
    vehicle_id = fields.Many2one('vehicle.detail', 'Vehicle')
    manager_id = fields.Many2one('res.users', 'Fleet Manager', store=True)
    odometer_value = fields.Float(
        string='Odometer Value',
        help='Odometer measure of the vehicle at the moment of this log')
    service_type=fields.Char(string='Service')

    # company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company)
    # currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    # inv_ref = fields.Char('Vendor Reference')
    
    driver = fields.Many2one('res.partner', string="Driver", readonly=False, store=True)
    notes = fields.Text()
    state = fields.Selection([
        ('new', 'New'),
        ('running', 'Running'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='new', string='Stage', group_expand='_expand_states')

