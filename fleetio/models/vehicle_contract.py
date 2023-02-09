# -*- coding: utf-8 -*-
from odoo import models,fields,api
from dateutil.relativedelta import relativedelta

class Vehicle_Contract(models.Model):
    _name = "vehicle.contract"
    _description = "Fleet Contract Model"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name="contract"

    contract = fields.Char()
    # offer_id = fields.Many2one('vehicle.detail')
    user_id = fields.Many2one('res.users', 'Responsible', default=lambda self: self.env.user)
    cost_subtype_id = fields.Many2one('vehicle.type', 'Type', help='Cost type purchased with this cost', domain=[('category', '=', 'contract')])
    insurer_id = fields.Many2one('res.partner', 'Vendor')
    ins_ref = fields.Char('Reference', size=64, copy=False)
    vehicle_id = fields.Many2one('vehicle.detail', 'Vehicle', required=True)
    # purchaser_id = fields.Many2one(related='vehicle_id.driver_id', string='Driver')
    amount = fields.Float('Cost', tracking=True)
    cost_generated = fields.Float('Recurring Cost', tracking=True)
    cost_frequency = fields.Selection([
        ('no', 'No'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')
        ], 'Recurring Cost Frequency', default='monthly', required=True)
    date = fields.Date(help='Date when the cost has been executed')
    start_date = fields.Date(
        'Contract Start Date', default=fields.Date.context_today,
        help='Date when the coverage of the contract begins')
    expiration_date = fields.Date(
        'Contract Expiration Date', default=lambda self:
        self.compute_next_year_date(fields.Date.context_today(self)),
        help='Date when the coverage of the contract expirates, one year after begin date)')
    state = fields.Selection(
        [('futur', 'Incoming'),
         ('open', 'In Progress'),
         ('expired', 'Expired'),
         ('closed', 'Closed')
        ], 'Status', default='open', readonly=True,
        help='Choose whether the contract is still valid or not',
        tracking=True,
        copy=False)
    notes = fields.Text()
    

    def compute_next_year_date(self, strdate):
        oneyear = relativedelta(years=1)
        start_date = fields.Date.from_string(strdate)
        return fields.Date.to_string(start_date + oneyear)