from odoo import api, fields, models, _
from odoo.exceptions import UserError


class accountMoveInherit(models.Model):
    _inherit = "account.move"

    @api.model
    def create(self, vals):
        if vals.get('line_ids'):
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
        existing_tags = []

        if vals.get('line_ids'):
            for lines in vals.get('line_ids'):
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
        
        if vals.get('invoice_line_ids'):
            for lines in vals.get('invoice_line_ids'):
                if lines[-1] and type(lines[-1]) == dict:
                    if lines[-1].get('analytic_tag_ids'):
                        invoice_tags = lines[-1].get('analytic_tag_ids')[0][-1]
                        if len(invoice_tags) >0:
                            for tag in invoice_tags:
                                domain=[
                                    ('analytic_tag_ids','=',tag),                             
                                    ]
                                child_tag_ids = self.env['account.analytic.default'].search(domain).mapped('child_analytic_tag_ids').ids
                                for c_tag in child_tag_ids:
                                    if c_tag not in existing_tags:
                                        existing_tags += child_tag_ids
                                if len(child_tag_ids) == 0 and tag not in existing_tags:
                                    existing_tags += [tag]


        print(existing_tags)
        obj = super(accountMoveInherit, self).write(vals)
        # if values.get('line_ids')[0][2].get('requisition_line_id'):
        #     
        return obj


# class accountMoveLinesInherit(models.Model):
#     _inherit = "account.move.line"
#     @api.onchange('analytic_tag_ids')
#     def _onchange_analytic_tag_ids(self):
#         print(self.analytic_tag_ids)
        
#         existing_tags = self.analytic_tag_ids.ids
#         for tags_sel in self.analytic_tag_ids.ids:
#             domain=[
#                 ('analytic_tag_ids','=',tags_sel),                             
#                 ]
#             child_tag_ids = self.env['account.analytic.default'].search(domain).mapped('child_analytic_tag_ids').ids
#             for child_tag in child_tag_ids:
#                 if child_tag not in existing_tags:
#                     existing_tags += child_tag_ids
#         import pdb; pdb.set_trace()
#         self.sudo().write({'analytic_tag_ids':existing_tags})

