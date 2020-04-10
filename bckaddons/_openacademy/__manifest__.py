# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings
          - training courses o
          - training sessions o
          - attendes registration o
    """,

    'author': "My Company olp",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
	'security/ir.model.access.csv',
        'views/templates.xml',
	'views/openacademy.xml',
	'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
