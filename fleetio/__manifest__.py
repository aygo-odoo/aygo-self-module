# -*- coding: utf-8 -*-
{
    'name': "Fleetio",
    'summary': "Module for trasportation",
    'author': "Ayushi Gorai(aygo)",
    'category': 'Category',
    'license': 'LGPL-3',
    'description': "fleet module",
    'installable':True,
    'application':True,
    'demo': [
      'demo/vehicle_detail_demo_data.xml',
     ],
     'data': [
        'security/ir.model.access.csv',
        'view/vehicle_detail_view.xml',
        'view/vehicle_service_view.xml',
        'view/vehicle_contract_view.xml',
        'view/vehicle_odometer_view.xml',
        'view/vehicle_menus.xml',
     ],
}