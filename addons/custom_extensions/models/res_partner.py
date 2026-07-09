# -*- coding: utf-8 -*-
from datetime import date

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    date_of_birth = fields.Date(
        string='Дата рождения',
        help='Используется для автоматической отправки поздравлений',
    )
    birthday_greeting_sent_year = fields.Integer(
        string='Год последнего поздравления',
        help='Технич. поле — чтобы не поздравить дважды в один год',
        copy=False,
    )

    @api.model
    def _cron_send_birthday_greetings(self):
        """Запускается по расписанию (см. ir.cron) раз в день.
        Ищет контакты, у которых сегодня день рождения, и отправляет
        поздравление: письмо по шаблону (если есть email) либо
        сообщение в чаттере."""
        today = date.today()
        partners = self.search([('date_of_birth', '!=', False)])

        template = self.env.ref(
            'custom_extensions.email_template_birthday',
            raise_if_not_found=False,
        )

        for partner in partners:
            dob = partner.date_of_birth
            if dob.day != today.day or dob.month != today.month:
                continue
            # защита от повторной отправки в тот же год
            if partner.birthday_greeting_sent_year == today.year:
                continue

            if partner.email and template:
                template.send_mail(partner.id, force_send=True)
            else:
                partner.message_post(
                    body=f'🎉 С Днём Рождения, {partner.name}! Желаем всего наилучшего!'
                )

            partner.birthday_greeting_sent_year = today.year
