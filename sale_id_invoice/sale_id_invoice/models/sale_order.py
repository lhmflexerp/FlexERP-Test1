# -*- coding: utf-8 -*-

from odoo import models, api


class Sale(models.Model):
    _inherit = 'sale.order'

    @api.multi #Pass value of client to pay in create invoice.
    def _prepare_invoice(self):
       res = super(Sale, self)._prepare_invoice()
       vals = {
           'custom_sale_id': self.id,
       }
       res.update(vals)
       return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
