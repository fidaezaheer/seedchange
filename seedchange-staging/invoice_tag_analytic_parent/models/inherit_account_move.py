from odoo import api, fields, models, _
from odoo.exceptions import UserError


class accountMoveInherit(models.Model):
    _inherit = "account.move"

    @api.model
    def create(self, vals):
        if vals.get('line_ids'):
            print('crt 1st entry!!!')
            for lines in vals.get('line_ids'):
                print(lines[-1].get('analytic_tag_ids'))
                if lines[-1].get('analytic_tag_ids'):
                    existing_tags = lines[-1].get('analytic_tag_ids')[0][-1]
                    print('---------------------------------------------')
                    print(existing_tags)
                    # if len(existing_tags) > 0:
                    print("enters ========================> ")
                    for tags_sel in existing_tags:
                        domain=[
                            ('analytic_tag_ids','=',tags_sel),                             
                            ]
                        child_tag_ids = self.env['account.analytic.default'].search(domain).mapped('child_analytic_tag_ids').ids
                        existing_tags += child_tag_ids

        obj = super(accountMoveInherit, self).create(vals)
        return obj
    
    def write(self, vals):
        print("vals ^^^^^^^^^^^^^^^^^^^ ", vals)
        # domain=[('analytic_tag_ids','=',tags_sel),]
        # child_tag_ids = self.env['account.analytic.default'].search(domain).mapped('child_analytic_tag_ids').ids
        try:
            vals['line_ids'] = vals.pop('invoice_line_ids')

            if vals.get('line_ids'):
                print('wrt 1st entry!!!')
                for lines in vals.get('line_ids'):
                    if lines[-1] and type(lines[-1]) == dict:
                        if lines[-1].get('analytic_tag_ids'):
                            existing_tags = lines[-1].get('analytic_tag_ids')[0][-1]
                            ex_ids = self.env['account.analytic.tag'].search([('id','in',existing_tags)])
                            print('---------------------------------------------')
                            print(existing_tags)
                            # if len(existing_tags) > 0:
                            print('entersssssssssssssssssssssssssssssssssssssss')
                            for tags_sel in existing_tags:
                                domain=[
                                    ('analytic_tag_ids','=',tags_sel),                             
                                    ]
                                child_tag_ids = self.env['account.analytic.default'].search(domain).mapped('child_analytic_tag_ids').ids
                                # # for child in child_tag_ids:
                                # #     print(self.env['account.analytic.default'].search([('id', '=', child)]).child_analytic_tag_ids.name)
                                existing_tags += child_tag_ids
                                # domain2 = [
                                #     ('child_analytic_tag_ids','=',tags_sel),                             
                                #     ]
                                # parent_tag_ids = self.env['account.analytic.default'].search(domain2).mapped('child_analytic_tag_ids').ids
                                # existing_tags += parent_tag_ids


            # vals['line_ids'] = vals.pop('invoice_line_ids')
        except Exception as e:
            print(e.args)

        obj = super(accountMoveInherit, self).write(vals)
        # print (vals)
        return obj
