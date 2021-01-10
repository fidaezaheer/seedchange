# -*- coding: utf-8 -*-
from odoo import api, fields, models


class InheritAccountMoveLineTag(models.Model):
    _inherit = "account.move.line"

    @api.model_create_multi
    def create(self, vals_list):
        print('ml create ======> ', vals_list)
        if vals_list[0].get('analytic_tag_ids'):   #    [[6, False, [2, 196]]]
            ids_to_browse = vals_list[0].get('analytic_tag_ids')[0][2]
            print(ids_to_browse)
            if ids_to_browse:
                ids_to_append = []
                for tag_id in ids_to_browse:
                    target_tag_id = self.env['account.analytic.tag'].browse(tag_id)
                    print(target_tag_id)
                    if target_tag_id:
                        target_tag_parent_id = self.env['account.analytic.default'].search([('analytic_tag_ids', '=', target_tag_id.id)]).parent_tag_id
                        print(target_tag_parent_id)
                        if target_tag_parent_id:
                            ids_to_append.append(target_tag_parent_id.id)
                        else:
                            pass
                print(ids_to_append)        
                ids_to_browse = ids_to_browse + ids_to_append
                print(ids_to_browse)
                vals_list[0]['analytic_tag_ids'] = ids_to_browse

        return super(InheritAccountMoveLineTag, self).create(vals_list)

    def write(self, vals):
        print(vals)
        for line in self:
            print("ml write ======> ", vals)
            return super(InheritAccountMoveLineTag, line).write(vals)