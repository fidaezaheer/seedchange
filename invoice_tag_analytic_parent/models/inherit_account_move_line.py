# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class InheritAccountMoveLineTag(models.Model):
    _inherit = "account.move.line"

    travel_policy_id = fields.Many2one('account.analytic.tag', string='Travel/Policy')
    activity_id = fields.Many2one('account.analytic.tag', string='Activity')
    partners_id = fields.Many2one('account.analytic.tag', string='Partners')
    employee_id = fields.Many2one('account.analytic.tag', string='Employee')
    budget_id = fields.Many2one('account.analytic.tag', string='Budget')
    thematic_id = fields.Many2one('account.analytic.tag', string='Thematic')
    department_id = fields.Many2one('account.analytic.tag', string='Department')
    cra_category_id = fields.Many2one('account.analytic.tag', string='CRA Category')
    funding_stream_id = fields.Many2one('account.analytic.tag', string='Funding Stream')

    @api.onchange('analytic_tag_ids')
    def _onchange_analytic_tags(self):
        analytic_rules = self.env['account.analytic.default'].search([('analytic_tag_ids', 'in', self.analytic_tag_ids.ids)])
        rules_parent_tag = self.env['account.analytic.tag']
        if analytic_rules:
            self.analytic_tag_ids = [(6, 0, analytic_rules.parent_tag_id.ids + self.analytic_tag_ids.ids or [])]
        for tag in self.analytic_tag_ids:
            rules = self.env['account.analytic.default'].search([('analytic_tag_ids', 'in', tag.ids)])
            if rules_parent_tag not in rules.parent_tag_id:
                rules_parent_tag |= rules.parent_tag_id
            else:
                return {'warning': {'title': _('Multiple Child Tag!'), 'message': ('There are multiple Child analytic tag %s' % ', '.join(analytic_rules.analytic_tag_ids.mapped('name')))}}
            if len(rules) > 1:
                return {'warning': {'title': _('Multiple Parent Tag!'), 'message': ('There are multiple parent analytic tag %s' % ', '.join(analytic_rules.parent_tag_id.mapped('name')))}}
        return {}

    @api.depends('product_id', 'account_id', 'partner_id', 'date')
    def _compute_analytic_account(self):
        print("_compute_analytic_account >>>>>>>>>>>>>", self)
        for record in self:
            print("record >>>>>>>>>>>>>>", record)
            if not record.exclude_from_invoice_tab or not record.move_id.is_invoice(include_receipts=True):
                rec = self.env['account.analytic.default'].account_get(
                    product_id=record.product_id.id,
                    partner_id=record.partner_id.commercial_partner_id.id or record.move_id.partner_id.commercial_partner_id.id,
                    account_id=record.account_id.id,
                    user_id=record.env.uid,
                    date=record.date,
                    company_id=record.move_id.company_id.id
                )
                print("rec >>>>>>>>>>>>", rec)
                if rec:
                    record.analytic_account_id = rec.analytic_id
                    analytic_rules = self.env['account.analytic.default'].search([('analytic_tag_ids', 'in', rec.analytic_tag_ids.ids)])
                    tag = analytic_rules.parent_tag_id and analytic_rules.parent_tag_id.ids or []
                    rec.analytic_tag_ids = [(6, 0, tag + rec.analytic_tag_ids.ids or [])]
