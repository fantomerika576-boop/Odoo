from datetime import date

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    birthday = fields.Date(string="Birthday")

    birthday_message = fields.Char(
        string="Birthday Greeting",
        compute="_compute_birthday_message"
    )

    @api.depends("birthday")
    def _compute_birthday_message(self):
        today = date.today()
        for partner in self:
            if (
                partner.birthday
                and partner.birthday.month == today.month
                and partner.birthday.day == today.day
            ):
                partner.birthday_message = "Happy Birthday!"
            else:
                partner.birthday_message = ""
