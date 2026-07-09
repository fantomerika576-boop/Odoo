# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    custom_reorder_min = fields.Float(
        string='Мин. остаток',
        help='Если фактический остаток товара опустится ниже этого значения — '
             'система создаст (или дополнит) черновик заказа на закупку',
    )
    custom_reorder_qty = fields.Float(
        string='Заказывать по',
        default=10,
        help='Сколько единиц заказывать у поставщика при срабатывании автозакупки',
    )

    def action_check_and_create_po(self):
        """Пример упрощённой автозакупки.
        В реальном проекте эту логику обычно закрывают штатные
        'Правила пополнения' (Inventory > Configuration > Reordering Rules) —
        они умеют работать по складам, срокам поставки и т.д.
        Здесь — минимальный пример 'руками', чтобы показать принцип."""
        Purchase = self.env['purchase.order']

        for product in self:
            if not product.custom_reorder_min:
                continue

            qty_available = product.qty_available
            if qty_available >= product.custom_reorder_min:
                continue

            seller = product.seller_ids[:1]
            if not seller:
                # нет поставщика в карточке товара — некого заказывать
                continue
            vendor = seller.partner_id

            # ищем открытый (черновой) заказ у этого поставщика,
            # чтобы не плодить по заказу на каждый товар
            po = Purchase.search([
                ('partner_id', '=', vendor.id),
                ('state', '=', 'draft'),
            ], limit=1)
            if not po:
                po = Purchase.create({'partner_id': vendor.id})

            po.write({
                'order_line': [(0, 0, {
                    'product_id': product.product_variant_id.id,
                    'product_qty': product.custom_reorder_qty,
                    'price_unit': seller.price or 0,
                    'name': product.name,
                })]
            })
        return True

    @api.model
    def _cron_check_stock_and_reorder(self):
        """Раз в день (см. ir.cron) проходит по всем товарам,
        у которых задан мин. остаток, и вызывает проверку."""
        products = self.search([('custom_reorder_min', '>', 0)])
        products.action_check_and_create_po()
