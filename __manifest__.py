# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Material Module',
    'version': '1.2',
    'category': 'Test',
    'sequence': 100,
    'summary': 'Material Module for recruitment',
    'description': "",
    'website': 'https://www.linkedin.com/in/faris-ponighzwa-8b5a33146/',
    'depends': ['account'],
    'data': [
        'security/material_security.xml',
        'security/ir.model.access.csv',
        'data/material_data.xml',
        'views/material_views.xml',
        'views/material_menu.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
