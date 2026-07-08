{
    'name': 'Birthday Reminder',
    'version': '18.0.1.0.0',
    'category': 'Contacts',
    'summary': 'Birthday notifications for customers',

    'depends': [
        'base',
        'contacts',
        'mail',
    ],

    'data': [
        'views/res_partner_views.xml',
        'data/birthday_cron.xml',
    ],

    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}