# -*- coding: utf-8 -*-
{
    'name': "Analytic tags Parent & Auto Fields",

    'summary': """
        All the tag related modifications for SeedChange""",

    'description': """
        All the tag related modifications for SeedChange (Rule 1 & Rule 2)
    """,

    'author': "Syncoria Inc",
    'website': "https://www.syncoria.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account','account_accountant'],

    # always loaded
    'data': [
        'views/inherit_account_move_line_views.xml',
        'views/inherit_view_account_analytic_default.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
