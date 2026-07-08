from odoo import models, fields
from datetime import date


class ResPartner(models.Model):

    _inherit = 'res.partner'


    birthday = fields.Date(
        string="Birthday"
    )


    def check_birthdays(self):

        today = date.today()

        partners = self.search([
            ('birthday', '!=', False)
        ])


        for partner in partners:

            if (
                partner.birthday.day == today.day
                and
                partner.birthday.month == today.month
            ):

                partner.message_post(
                    body=f"""
                    🎉 Happy Birthday, {partner.name}!<br/>
                    We wish you happiness and success!
                    """
                )