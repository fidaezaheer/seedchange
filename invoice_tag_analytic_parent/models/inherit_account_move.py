from odoo import api, fields, models, _
from odoo.exceptions import UserError


class accountMoveInherit(models.Model):
    _inherit = "account.move"

    @api.model
    def create(self, vals):
        for lines in vals.get('line_ids'):
            if lines[-1].get('analytic_tag_ids'):
                existing_tags = lines[-1].get('analytic_tag_ids')[0][-1]
                if len(existing_tags) >0:
                    for tags_sel in existing_tags:
                        domain=[
                            ('analytic_tag_ids','=',tags_sel),                             
                            ]
                        child_tag_ids = self.env['account.analytic.default'].search(domain).mapped('child_analytic_tag_ids').ids
                        existing_tags += child_tag_ids

        obj = super(accountMoveInherit, self).create(vals)
        # import pdb; pdb.set_trace()
                

        return obj

    
    def write(self, vals):
        # import pdb; pdb.set_trace()
        if vals.get('line_ids'):
            for lines in vals.get('line_ids'):
                # import pdb; pdb.set_trace()
                if lines[-1] and type(lines[-1]) == dict:
                    if lines[-1].get('analytic_tag_ids'):
                        existing_tags = lines[-1].get('analytic_tag_ids')[0][-1]
                        if len(existing_tags) >0:
                            for tags_sel in existing_tags:
                                domain=[
                                    ('analytic_tag_ids','=',tags_sel),                             
                                    ]
                                child_tag_ids = self.env['account.analytic.default'].search(domain).mapped('child_analytic_tag_ids').ids
                                existing_tags += child_tag_ids



        obj = super(accountMoveInherit, self).write(vals)
        # if values.get('line_ids')[0][2].get('requisition_line_id'):
        #     
        return obj