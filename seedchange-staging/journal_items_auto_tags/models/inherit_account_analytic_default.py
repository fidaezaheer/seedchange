# -*- coding: utf-8 -*-
from odoo import api, fields, models


class InheritAccountAnalyticDefaultAuto(models.Model):
    _inherit = "account.analytic.default"

    dimension_name = fields.Selection([
        ('travel_policy', 'Travel/Policy'),
        ('activity', 'Activity'),
        ('partners', 'Partners'),
        ('employee', 'Employee'),
        ('budget', 'Budget'),
        ('thematic', 'Thematic'),
        ('department', 'Department'),
        ('cra_category', 'CRA Category'),
        ('funding_stream', 'Funding Stream')], string='Related Dimension')

