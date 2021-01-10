# -*- coding: utf-8 -*-
from odoo import api, fields, models


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

    @api.model_create_multi
    def create(self, vals_list):
        print('ml create ======> ', vals_list)
        if vals_list[0].get('analytic_tag_ids'):   #    [[6, False, [2, 196]]]
            ids_to_browse = vals_list[0].get('analytic_tag_ids')[0][2]
            
            if ids_to_browse:
                ids_to_append = []
                for tag_id in ids_to_browse:
                    target_tag_id = self.env['account.analytic.tag'].browse(tag_id)
                    print(target_tag_id)
                    if target_tag_id:
                        matched_analytics_default_id = self.env['account.analytic.default'].search([('analytic_tag_ids', '=', target_tag_id.id)])
                        print(matched_analytics_default_id)
                        if matched_analytics_default_id:
                            dimension_name = matched_analytics_default_id.dimension_name
                            target_tag_parent_id = matched_analytics_default_id.parent_tag_id

                            if target_tag_parent_id:            #   1st rule
                                ids_to_append.append(matched_analytics_default_id.parent_tag_id.id)
                            else:
                                pass

                            if dimension_name:                  #   2nd Rule
                                if dimension_name == 'travel_policy':
                                    vals_list[0]['travel_policy_id'] = target_tag_id.id
                                if dimension_name == 'thematic':
                                    vals_list[0]['thematic_id'] = target_tag_id.id
                                if dimension_name == 'cra_category':
                                    vals_list[0]['cra_category_id'] = target_tag_id.id
                                if dimension_name == 'activity':
                                    vals_list[0]['activity_id'] = target_tag_id.id
                                if dimension_name == 'partners':
                                    vals_list[0]['partners_id'] = target_tag_id.id
                                if dimension_name == 'employee':
                                    vals_list[0]['employee_id'] = target_tag_id.id
                                if dimension_name == 'budget':
                                    vals_list[0]['budget_id'] = target_tag_id.id
                                if dimension_name == 'department':
                                    vals_list[0]['department_id'] = target_tag_id.id
                                if dimension_name == 'funding_stream':
                                    vals_list[0]['funding_stream_id'] = target_tag_id.id
                            else:
                                pass
      
                ids_to_browse = ids_to_browse + ids_to_append
                vals_list[0]['analytic_tag_ids'] = ids_to_browse

            else:
                pass

        return super(InheritAccountMoveLineTag, self).create(vals_list)

    def write(self, vals):
        for line in self:
            print("ml write =======================================")
            if vals.get('analytic_tag_ids'):   #    [[6, False, [2, 196]]]
                ids_to_browse = vals.get('analytic_tag_ids')[0][2]
                
                if ids_to_browse:
                    ids_to_append = []

                    for tag_id in ids_to_browse:
                        target_tag_id = self.env['account.analytic.tag'].browse(tag_id)
                        print(target_tag_id)
                        if target_tag_id:
                            matched_analytics_default_id = self.env['account.analytic.default'].search([('analytic_tag_ids', '=', target_tag_id.id)])
                            print(matched_analytics_default_id)
                            if matched_analytics_default_id:
                                dimension_name = matched_analytics_default_id.dimension_name
                                target_tag_parent_id = matched_analytics_default_id.parent_tag_id

                                if target_tag_parent_id:            #   1st rule
                                    ids_to_append.append(matched_analytics_default_id.parent_tag_id.id)
                                else:
                                    pass

                                if dimension_name:                  #   2nd Rule
                                    if dimension_name == 'travel_policy':
                                        vals['travel_policy_id'] = target_tag_id.id
                                    if dimension_name == 'thematic':
                                        vals['thematic_id'] = target_tag_id.id
                                    if dimension_name == 'cra_category':
                                        vals['cra_category_id'] = target_tag_id.id
                                    if dimension_name == 'activity':
                                        vals['activity_id'] = target_tag_id.id
                                    if dimension_name == 'partners':
                                        vals['partners_id'] = target_tag_id.id
                                    if dimension_name == 'employee':
                                        vals['employee_id'] = target_tag_id.id
                                    if dimension_name == 'budget':
                                        vals['budget_id'] = target_tag_id.id
                                    if dimension_name == 'department':
                                        vals['department_id'] = target_tag_id.id
                                    if dimension_name == 'funding_stream':
                                        vals['funding_stream_id'] = target_tag_id.id
                                else:
                                    pass
        
                    ids_to_browse = ids_to_browse + ids_to_append
                    vals['analytic_tag_ids'] = ids_to_browse

                else:
                    pass

            return super(InheritAccountMoveLineTag, line).write(vals)