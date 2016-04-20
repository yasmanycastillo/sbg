# -*- coding: utf-8 -*-
from openerp import models, fields, api, _

class sbg_subscription_services(models.Model):
    _name = 'sbg.subscription.services'
    _description = 'Subscription services'

    name = fields.Char(string="Name")
    ref = fields.Char(string="Internal reference")
    duration_type = fields.Selection(string="Duration type", selection=[('permanent', 'Permanent'),('period','Defined period')], default='permanent')
    start_date = fields.Date(string="Start date", default=fields.Date.today)
    end_date = fields.Date(string="End date", default=fields.Date.today)
    periodicity = fields.Selection(string="Fee periodicity", selection=[('m','Monthly'), ('b','Bimonthly'), ('q','Quarterly'), ('s','Semiannually'), ('a','Annually')], default='m')
    fee = fields.Float(string="Fee",default=0)
    statement_description = fields.Char(string="Statement description")
    product_ids = fields.Many2many("product.product", string="Related products")
    sbg_subscription_ids = fields.One2many('sbg.subscriptions', 'subscription_service_id', string='Subscriptions')
    active = fields.Boolean(string="Active", default=True)