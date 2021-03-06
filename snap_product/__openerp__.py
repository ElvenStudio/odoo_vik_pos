# -*- coding: utf-8 -*-
{
    'name': 'Snap product',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'WIC product for the Point of Sale ',
    'description': """

=======================

This module adds WIC product features to the Point of Sale:


""",
    'author': 'Viktor Vorobjov',
    'depends': ['point_of_sale'],
    'license': 'LGPL-3',
 	'website': 'https://straga.github.io',
 	'support': 'vostraga@gmail.com',
    'data': [
        'views/templates.xml',
        'views/views.xml',
    ],
    'qweb':[

        'static/src/xml/snap_product.xml',
    ],
    'installable': True,
    'auto_install': False,
}

