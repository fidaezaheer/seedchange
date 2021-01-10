# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritAccountAnalyticDefault(models.Model):
    _inherit = "account.analytic.default"

    # child_analytic_tag_ids = fields.Many2many('account.analytic.tag',relation="child_analytic_tag_ids", string='Child Tags')
    parent_tag_id = fields.Many2one('account.analytic.tag', string='Parent Tag')

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

