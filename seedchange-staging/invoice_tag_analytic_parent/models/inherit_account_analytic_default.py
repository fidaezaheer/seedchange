# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritAccountAnalyticDefault(models.Model):
    _inherit = "account.analytic.default"

    child_analytic_tag_ids = fields.Many2many('account.analytic.tag',relation="child_analytic_tag_ids", string='Child Tags')


    travel_or_policy = fields.Many2one('account.analytic.tag',relation="child_analytic_tag_ids", string='Travel/Policy')
    activity = fields.Many2one('account.analytic.tag',relation="child_analytic_tag_ids", string='Activity')
    partners = fields.Many2one('account.analytic.tag',relation="child_analytic_tag_ids", string='Partners')
    employee = fields.Many2one('account.analytic.tag',relation="child_analytic_tag_ids", string='Employee')
    budget = fields.Many2one('account.analytic.tag',relation="child_analytic_tag_ids", string='Budget')
    thematic = fields.Many2one('account.analytic.tag',relation="child_analytic_tag_ids", string='Thematic')
    department = fields.Many2one('account.analytic.tag',relation="child_analytic_tag_ids", string='Department')
    ora_category = fields.Many2one('account.analytic.tag',relation="child_analytic_tag_ids", string='ORA Category')
    funding_stream = fields.Many2one('account.analytic.tag',relation="child_analytic_tag_ids", string='Funding Stream')
