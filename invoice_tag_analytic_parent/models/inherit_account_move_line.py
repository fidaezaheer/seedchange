# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


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
        # print('ml create ======> ', len(vals_list))
        # print('ml create ======> ', vals_list)
        for vals_elem in vals_list:
            # print(vals_elem)
            if vals_elem.get('analytic_tag_ids'):   #    [[6, False, [2, 196]]]
                ids_to_browse = vals_elem.get('analytic_tag_ids')[0][2]
                
                if ids_to_browse:               #   1st Rule
                    ids_to_append = []
                    for tag_id in ids_to_browse:
                        target_tag_id = self.env['account.analytic.tag'].browse(tag_id)
                        # print(target_tag_id)
                        if target_tag_id:
                            matched_analytics_default_id = self.env['account.analytic.default'].search([('analytic_tag_ids', '=', target_tag_id.id)])
                            # print(matched_analytics_default_id)
                            if matched_analytics_default_id and len(matched_analytics_default_id) == 1:
                                # print(matched_analytics_default_id, len(matched_analytics_default_id))
                                target_tag_parent_id = matched_analytics_default_id.parent_tag_id
                                # print(target_tag_parent_id, len(target_tag_parent_id))
                                if target_tag_parent_id:
                                    ids_to_append.append(matched_analytics_default_id.parent_tag_id.id)
                                else:
                                    pass
                            
                            else:
                                raise UserError(_('There are multiple account Analytic Defaults Rules ralated with the tag - %s',target_tag_id.name))
                            
        
                    new_ids_to_browse = ids_to_browse + ids_to_append
                    vals_elem['analytic_tag_ids'] = new_ids_to_browse

                    if new_ids_to_browse:                   #   2nd Rule
                        for tag_id in new_ids_to_browse:
                            target_tag_id = self.env['account.analytic.tag'].browse(tag_id)
                            # print(target_tag_id)
                            if target_tag_id:
                                matched_analytics_default_id = self.env['account.analytic.default'].search([('analytic_tag_ids', '=', target_tag_id.id)])
                                # print(matched_analytics_default_id)
                                if matched_analytics_default_id:
                                    dimension_name = matched_analytics_default_id.dimension_name

                                    if dimension_name:                  
                                        if dimension_name == 'travel_policy':
                                            vals_elem['travel_policy_id'] = target_tag_id.id
                                        if dimension_name == 'thematic':
                                            vals_elem['thematic_id'] = target_tag_id.id
                                        if dimension_name == 'cra_category':
                                            vals_elem['cra_category_id'] = target_tag_id.id
                                        if dimension_name == 'activity':
                                            vals_elem['activity_id'] = target_tag_id.id
                                        if dimension_name == 'partners':
                                            vals_elem['partners_id'] = target_tag_id.id
                                        if dimension_name == 'employee':
                                            vals_elem['employee_id'] = target_tag_id.id
                                        if dimension_name == 'budget':
                                            vals_elem['budget_id'] = target_tag_id.id
                                        if dimension_name == 'department':
                                            vals_elem['department_id'] = target_tag_id.id
                                        if dimension_name == 'funding_stream':
                                            vals_elem['funding_stream_id'] = target_tag_id.id
                                    else:
                                        pass

                else:
                    pass

        return super(InheritAccountMoveLineTag, self).create(vals_list)

    def write(self, vals):
        # print(vals)
        for line in self:
            # print("ml write =======================================")
            if vals.get('analytic_tag_ids'):   #    [[6, False, [2, 196]]]
                ids_to_browse = vals.get('analytic_tag_ids')[0][2]
                
                if ids_to_browse:           #   1st rule
                    ids_to_append = []

                    for tag_id in ids_to_browse:
                        target_tag_id = self.env['account.analytic.tag'].browse(tag_id)
                        # print(target_tag_id)
                        if target_tag_id:
                            matched_analytics_default_id = self.env['account.analytic.default'].search([('analytic_tag_ids', '=', target_tag_id.id)])
                            # print(matched_analytics_default_id)
                            if matched_analytics_default_id and len(matched_analytics_default_id) == 1:
                                target_tag_parent_id = matched_analytics_default_id.parent_tag_id

                                if target_tag_parent_id:            
                                    ids_to_append.append(matched_analytics_default_id.parent_tag_id.id)
                                else:
                                    pass
                            
                            else:
                                raise UserError(_('There are multiple account Analytic Defaults Rules ralated with the tag - %s',target_tag_id.name))
        
                    new_ids_to_browse = ids_to_browse + ids_to_append
                    vals['analytic_tag_ids'] = new_ids_to_browse

                    if new_ids_to_browse:               #   2nd Rule
                        for tag_id in new_ids_to_browse:
                            target_tag_id = self.env['account.analytic.tag'].browse(tag_id)
                            # print(target_tag_id)
                            if target_tag_id:
                                matched_analytics_default_id = self.env['account.analytic.default'].search([('analytic_tag_ids', '=', target_tag_id.id)])
                                # print(matched_analytics_default_id)
                                if matched_analytics_default_id:
                                    dimension_name = matched_analytics_default_id.dimension_name

                                    if dimension_name:                  
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

                else:
                    pass

            return super(InheritAccountMoveLineTag, line).write(vals)