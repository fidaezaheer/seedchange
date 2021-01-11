# -*- coding: utf-8 -*-
{
    'name': "Auto Journal Items Tag",

    'summary': """
        Auto Journal Items Tag""",

    'description': """
        Auto journal items tagging.
    """,

    'author': "Syncoria", 
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        # 'security/security_groups.xml',
        # 'security/ir.model.access.csv',
        # 'views/lc_requisition_line_views.xml',
        # 'views/letter_of_credit_views.xml',
        # 'views/inherit_purchase_order_views.xml',
        # 'views/letter_of_credit_sequence.xml',
        # 'views/lc_related_menus.xml',
        # 'views/inherit_account_res_partner_views.xml',
        'views/inherit_account_move_line_views.xml',
        'views/inherit_account_analytic_default_views.xml',
    ],
}