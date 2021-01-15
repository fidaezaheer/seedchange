# -*- coding: utf-8 -*-
# from odoo import http


# class InvoiceTagAnalyticParent(http.Controller):
#     @http.route('/invoice_tag_analytic_parent/invoice_tag_analytic_parent/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_tag_analytic_parent/invoice_tag_analytic_parent/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_tag_analytic_parent.listing', {
#             'root': '/invoice_tag_analytic_parent/invoice_tag_analytic_parent',
#             'objects': http.request.env['invoice_tag_analytic_parent.invoice_tag_analytic_parent'].search([]),
#         })

#     @http.route('/invoice_tag_analytic_parent/invoice_tag_analytic_parent/objects/<model("invoice_tag_analytic_parent.invoice_tag_analytic_parent"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_tag_analytic_parent.object', {
#             'object': obj
#         })
