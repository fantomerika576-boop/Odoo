from odoo import models, fields


class MyPartner(models.Model):
    _name = "my.partner"
    _description = "My Partner"

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone")