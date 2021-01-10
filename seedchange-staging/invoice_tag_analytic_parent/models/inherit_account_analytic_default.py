# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritAccountAnalyticDefault(models.Model):
    _inherit = "account.analytic.default"

    # child_analytic_tag_ids = fields.Many2many('account.analytic.tag',relation="child_analytic_tag_ids", string='Child Tags')
    parent_tag_id = fields.Many2one('account.analytic.tag', string='Parent Tag')

