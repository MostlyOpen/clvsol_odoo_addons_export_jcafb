# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Export (customizations for CLVhealth-JCAFB Solution)',
    'summary': 'Export Module customizations for CLVhealth-JCAFB Solution.',
    'version': '15.0.6.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_export',
        'clv_base_jcafb',
    ],
    'data': [
        'data/export_seq.xml',
        'data/file_system.xml',
        'data/global_settings.xml',
        'views/model_export_template_code_view.xml',
        'views/model_export_code_view.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
