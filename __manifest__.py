{
    'name': 'kinesiology',
    'summary': 'kinesiology Module Project',
    'version': '1.0',

    'description': """
kinesiology Module Project.
==============================================


    """,

    'author': 'Adrian Borella',
    'website': 'https://github.com/adriannborella',
    'license': 'AGPL-3',
    
    'category': 'Uncategorized',

    'depends': [
        'base',
    ],
    'external_dependencies': {
        'python': [
        ],
    },
    'data': [
        'views/kinesiology_cash_movements_views.xml',
        'views/kinesiology_diagnoses_views.xml',
        'views/kinesiology_health_insurance_views.xml',
        'views/kinesiology_localities_views.xml',
        'views/kinesiology_medical_offices_views.xml',
        'views/kinesiology_patients_views.xml',
        'views/kinesiology_professionals_views.xml',
        'views/kinesiology_records_views.xml',
        'views/kinesiology_referral_doctors_views.xml',
        'views/kinesiology_treatments_views.xml',
        'views/kinesiology_turns_views.xml',
        'views/res_company_views.xml',
        'views/kinesiology_menu.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    'js': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'images': [
    ],
    'test': [
    ],

    'installable': True
}
