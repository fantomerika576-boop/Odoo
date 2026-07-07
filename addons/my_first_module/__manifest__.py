{
    "name": "My First Module",
    "version": "1.0",
    "summary": "My first Odoo module",
    "author": "Anna",
    "category": "Tools",
    "depends": ["base", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "views/partner_views.xml",
    ],
    "installable": True,
    "application": True,
}