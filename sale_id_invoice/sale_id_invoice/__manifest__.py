# -*- coding: utf-8 -*-

# Part of Alex Lyngsøe. See LICENSE file for full copyright and licensing details.

{
    'name': "Sale ID Invoice",
    'version': '1.0',
    'category': 'Sales',
    'license': 'Other proprietary',
    'summary': """Sale ID Invoice""",
    'description': """
  Sale ID Invoice
    """,
    'author': 'Alex Lyngsøe',
    'website': 'www.odoo.com',
    'depends': [
        'sale_management',
    ],
    'data':[
        'views/account_invoice_view.xml',
    ],
    'installable' : True,
    'application' : False,
    'auto_install' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
