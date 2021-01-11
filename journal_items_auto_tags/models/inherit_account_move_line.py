# -*- coding: utf-8 -*-
from odoo import api, fields, models


class InheritAccountMoveLineAuto(models.Model):
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

    # @api.model_create_multi
    # def create(self, vals_list):
    #     print('ml create ======> ', vals_list)
    #     return super(InheritAccountMoveLineAuto, self).create(vals_list)

    # def write(self, vals):
    #     print(vals)
    #     for line in self:
    #         print("ml write ======> ", vals)
    #         return super(InheritAccountMoveLineAuto, line).write(vals)

    @api.onchange('analytic_account_id', 'analytic_tag_ids')
    def _onchange_mark_recompute_taxes_analytic(self):
        ''' Trigger tax recomputation only when some taxes with analytics
        '''
        for line in self:
            if not line.tax_repartition_line_id and any(tax.analytic for tax in line.tax_ids):
                line.recompute_tax_line = True

            # parent_ids = []
            # for tag_id in line.analytic_tag_ids[0:-1]:
            #     tagid= tag_id.id.origin if type(tag_id.id) != int else tag_id.id
            #     domain = [
            #         ('analytic_tag_ids','=',tagid),                             
            #         ]
            #     parent_tag_ids = self.env['account.analytic.default'].search(domain).mapped('child_analytic_tag_ids').ids
            #     parent_ids += parent_tag_ids

            # if len(line.analytic_tag_ids) > 1:
            #     newtag = line.analytic_tag_ids[-1]
            #     tagid = newtag.id.origin if type(tag_id.id) != int else newtag.id
            #     domain = [
            #         ('analytic_tag_ids','=',tagid),                             
            #         ]
            #     parent_new = self.env['account.analytic.default'].search(domain).mapped('child_analytic_tag_ids').ids
            #     for item in parent_new:
            #         if item in parent_ids:
            #             raise UserError("You cannot select more than one child tag for same parent tag")

            for tag_id in line.analytic_tag_ids.ids:
                print('mv ln 1st tag ====> ', tag_id)
                matched_analytics_default_rule = self.env['account.analytic.default'].search([('analytic_tag_ids', '=', tag_id)])
                print('mv ln matched_analytics_default_rule ===> ', matched_analytics_default_rule)
                if matched_analytics_default_rule:
                    if matched_analytics_default_rule.dimension_name:
                        dimension_name = matched_analytics_default_rule.dimension_name
                        # print('dimension_dict =====> ', dimension_dict['dimension_name'])
                        # print('dimension_name =====> ', dimension_name)
                        if dimension_name:
                            analytic_tag_id = self.env['account.analytic.tag'].search([('id', '=', tag_id)])
                            # print('analytic_tag_id ===> ', analytic_tag_id)
                            if dimension_name == 'travel_policy':
                                line.travel_policy_id = analytic_tag_id.id
                            if dimension_name == 'thematic':
                                line.thematic_id = analytic_tag_id.id
                            if dimension_name == 'cra_category':
                                line.cra_category_id = analytic_tag_id.id
                            if dimension_name == 'activity':
                                line.activity_id = analytic_tag_id.id
                            if dimension_name == 'partners':
                                line.partners_id = analytic_tag_id.id
                            if dimension_name == 'employee':
                                line.employee_id = analytic_tag_id.id
                            if dimension_name == 'budget':
                                line.budget_id = analytic_tag_id.id
                            if dimension_name == 'department':
                                line.department_id = analytic_tag_id.id
                            if dimension_name == 'funding_stream':
                                line.funding_stream_id = analytic_tag_id.id
                            