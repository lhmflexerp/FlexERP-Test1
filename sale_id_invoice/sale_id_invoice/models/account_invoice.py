# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    custom_sale_id = fields.Many2one(
        'sale.order',
        string='Sale Order',
        readonly=True,
        copy=False,
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
