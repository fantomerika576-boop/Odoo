{
    'name': 'Custom Extensions: Дни рождения + Автозакупка',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': 'Поздравления с ДР клиентов + пример автоматической закупки при недостатке товара',
    'description': """
Модуль-пример для демонстрации двух возможностей:

1. Дата рождения контакта (res.partner) + автоматическая отправка поздравления
   в день рождения (email или сообщение в чаттере).

2. Упрощённый пример автозакупки: если остаток товара падает ниже заданного
   минимума — создаётся (или дополняется) черновик заказа на закупку у поставщика.

ВАЖНО: для реальной автозакупки в Odoo уже есть встроенный механизм
"Правила пополнения" (Reordering Rules, stock.warehouse.orderpoint) —
он покрывает 90% таких задач без единой строки кода. Этот модуль — учебный
пример, как сделать похожую логику руками, если нужна нестандартная логика.
    """,
    'author': 'Custom',
    'depends': ['base', 'contacts', 'sale', 'purchase', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/product_views.xml',
        'data/mail_template_birthday.xml',
        'data/ir_cron_data.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
