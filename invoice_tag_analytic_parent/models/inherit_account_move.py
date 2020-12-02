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
        return obj

    
    
    def write(self, vals):
        print("==============================================")
        print("vals")
        print(vals)
        existing_tags = []
        print("line_ids")
        if vals.get('line_ids'):
            for lines in vals.get('line_ids'):
                if lines[-1] and type(lines[-1]) == dict:
                    if lines[-1].get('analytic_tag_ids'):
                        existing_tags = lines[-1].get('analytic_tag_ids')[0][-1]
                        vals.get('line_ids')[-1][-1].get('analytic_tag_ids')[-1][-1] = []
                        print("Existing Tags")
                        print(existing_tags)
                        ex_ids = self.env['account.analytic.tag'].search([('id','in',existing_tags)])
                        for ex_id in ex_ids:
                            print(ex_id.name)

                        # existing_tags = []
                        # if len(existing_tags) >0:
                        #     for tags_sel in existing_tags:
                        #         domain=[
                        #             ('analytic_tag_ids','=',tags_sel),                             
                        #             ]
                        #         child_tag_ids = self.env['account.analytic.default'].search(domain).mapped('child_analytic_tag_ids').ids
                        #         for child in child_tag_ids:
                        #             print(self.env['account.analytic.default'].search([('id', '=', child)]).child_analytic_tag_ids.name)
                        #         existing_tags += child_tag_ids
                        #         domain2 = [
                        #             ('child_analytic_tag_ids','=',tags_sel),                             
                        #             ]
                        #         parent_tag_ids = self.env['account.analytic.default'].search(domain2).mapped('child_analytic_tag_ids').ids
                        #         existing_tags += parent_tag_ids
        print("invoice_line_ids")
        existing_tags = []
        if vals.get('invoice_line_ids'):
            for lines in vals.get('invoice_line_ids'):
                if lines[-1] and type(lines[-1]) == dict:
                    if lines[-1].get('analytic_tag_ids'):
                        invoice_tags = lines[-1].get('analytic_tag_ids')[0][-1]
                        try:
                            existing_tags += invoice_tags
                            print("invoice_tags")
                            print(invoice_tags)
                            if len(invoice_tags) >0:
                                # domain=[
                                #         ('analytic_tag_ids','in',invoice_tags) ,                          
                                #         ]
                                # print(domain)
                                # child_tag_ids = self.env['account.analytic.default'].search(domain)#.mapped('analytic_tag_ids').ids
                                # for c_tag in child_tag_ids:
                                #     if c_tag.id not in existing_tags:
                                #         existing_tags += [c_tag.id]
                                for tag in invoice_tags:
                                    if tag not in existing_tags:
                                        existing_tags += [tag]
                                    domain=[
                                        ('analytic_tag_ids','=',tag),                             
                                        ]
                                    child_tag_ids = self.env['account.analytic.default'].search(domain)#.mapped('analytic_tag_ids').ids
                                    if len(child_tag_ids) == 1:
                                        print("ID",child_tag_ids.id ,str(child_tag_ids.analytic_tag_ids.name))
                                        print("ID",child_tag_ids.child_analytic_tag_ids.id ,str(child_tag_ids.child_analytic_tag_ids.name))
                                    for c_tag in child_tag_ids:
                                        if c_tag.id not in existing_tags:
                                            existing_tags += [c_tag.id]
                                    # domain2 = [
                                    #     ('analytic_tag_ids','=',tag),                             
                                    #     ]
                                    # parent_tag_ids = self.env['account.analytic.default'].search(domain2)#.mapped('child_analytic_tag_ids').ids
                                    # if self.env['account.analytic.default'].search(domain2):
                                    #     print(self.env['account.analytic.default'].search(domain2).analytic_tag_ids.name)
                                    #     print(self.env['account.analytic.default'].search(domain2).child_analytic_tag_ids.name)
                                    # for p_tag in parent_tag_ids:
                                    #     if p_tag.id not in existing_tags:
                                    #         existing_tags += [p_tag.id]
                                    
                                    # existing_tags += parent_tag_ids
                                    # if len(child_tag_ids) == 0 and tag not in existing_tags:
                                    #     existing_tags += [tag]
                                    # if len(parent_tag_ids) == 0 and tag not in existing_tags:
                                            #     existing_tags += [tag]

                        except Exception as e:
                            print(e.args)
        if not vals.get('invoice_line_ids'):
            try:
                existing_tags = []
            except Exception as e:
                pass
                     
                      
        try:
            # if vals.get('line_ids')[-1][-1].get('analytic_tag_ids')[-1][-1]:
                # for tagi in existing_tags:
                #     if tagi not in vals.get('line_ids')[-1][-1].get('analytic_tag_ids')[-1][-1]:
                #         vals['line_ids'][-1][-1]['analytic_tag_ids'][-1][-1] += [tagi]

                # for idd in line_ids:
                #     if idd not in existing_tags:
                #         line_ids.remove(idd)
            vals['line_ids'][-1][-1]['analytic_tag_ids'][-1][-1] = existing_tags


        except Exception as e:
            print(e.args)

            # import pdb; pdb.set_trace()
            # if len(vals.get('invoice_line_ids')[0][-1].get('analytic_tag_ids')[0][-1]) == 0:
            #     existing_tags = []
        print("Writing Tags")
        print(existing_tags)
        print(vals.get('line_ids'))
        # print("new Vals")
        # print(vals)
        print("==============================================")
        # import pdb; pdb.set_trace()
        obj = super(accountMoveInherit, self).write(vals)
        return obj


class accountMoveLinesInherit(models.Model):
    _inherit = "account.move.line"
    @api.onchange('analytic_tag_ids')
    def _onchange_analytic_tag_ids(self):
        import pdb; pdb.set_trace()
        parent_ids = []
        for tag_id in self.analytic_tag_ids[0:-1]:
            tagid= tag_id.id.origin if type(tag_id.id) != int else tag_id.id
            domain = [
                ('analytic_tag_ids','=',tagid),                             
                ]
            parent_tag_ids = self.env['account.analytic.default'].search(domain).mapped('child_analytic_tag_ids').ids
            parent_ids += parent_tag_ids

        if len(self.analytic_tag_ids) > 1:
            newtag = self.analytic_tag_ids[-1]
            tagid = newtag.id.origin if type(tag_id.id) != int else newtag.id
            domain = [
                ('analytic_tag_ids','=',tagid),                             
                ]
            parent_new = self.env['account.analytic.default'].search(domain).mapped('child_analytic_tag_ids').ids
            for item in parent_new:
                if item in parent_ids:
                    raise UserError("You cannot select more than one child tag for same parent tag")
