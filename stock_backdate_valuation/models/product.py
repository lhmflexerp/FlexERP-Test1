# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.tools.float_utils import float_round


class Product(models.Model):
    _inherit = "product.product"

    def _compute_quantities_dict(self, lot_id, owner_id, package_id, from_date=False, to_date=False):
        if not self._context.get('special'):
            return super(Product, self)._compute_quantities_dict(lot_id, owner_id, package_id, from_date, to_date) 
        else:
            domain_quant_loc, domain_move_in_loc, domain_move_out_loc = self._get_domain_locations()
            domain_quant = [('product_id', 'in', self.ids)] + domain_quant_loc
            dates_in_the_past = False
            if to_date and to_date < fields.Datetime.now(): #Only to_date as to_date will correspond to qty_available
                dates_in_the_past = True
    
            domain_move_in = [('product_id', 'in', self.ids)] + domain_move_in_loc
            domain_move_out = [('product_id', 'in', self.ids)] + domain_move_out_loc
            if lot_id:
                domain_quant += [('lot_id', '=', lot_id)]
            if owner_id:
                domain_quant += [('owner_id', '=', owner_id)]
                domain_move_in += [('restrict_partner_id', '=', owner_id)]
                domain_move_out += [('restrict_partner_id', '=', owner_id)]
            if package_id:
                domain_quant += [('package_id', '=', package_id)]
            if dates_in_the_past:
                domain_move_in_done = list(domain_move_in)
                domain_move_out_done = list(domain_move_out)
            if from_date:
                domain_move_in += [('date', '>=', from_date)]
                domain_move_out += [('date', '>=', from_date)]
            if to_date:
                domain_move_in += [('back_date', '<=', to_date)] 
                domain_move_out += [('back_date', '<=', to_date)] 
    
            Move = self.env['stock.move']
            Quant = self.env['stock.quant']
            domain_move_in_todo = [('state', 'not in', ('done', 'cancel', 'draft'))] + domain_move_in
            domain_move_out_todo = [('state', 'not in', ('done', 'cancel', 'draft'))] + domain_move_out
            moves_in_res = dict((item['product_id'][0], item['product_qty']) for item in Move.read_group(domain_move_in_todo, ['product_id', 'product_qty'], ['product_id'], orderby='id'))
            moves_out_res = dict((item['product_id'][0], item['product_qty']) for item in Move.read_group(domain_move_out_todo, ['product_id', 'product_qty'], ['product_id'], orderby='id'))
            quants_res = dict((item['product_id'][0], item['quantity']) for item in Quant.read_group(domain_quant, ['product_id', 'quantity'], ['product_id'], orderby='id'))
            if dates_in_the_past:
                # Calculate the moves that were done before now to calculate back in time (as most questions will be recent ones)
                domain_move_in_done = [('state', '=', 'done'), ('back_date', '>', to_date)] + domain_move_in_done 
                domain_move_out_done = [('state', '=', 'done'), ('back_date', '>', to_date)] + domain_move_out_done 
                moves_in_res_past = dict((item['product_id'][0], item['product_qty']) for item in Move.read_group(domain_move_in_done, ['product_id', 'product_qty'], ['product_id'], orderby='id'))
                moves_out_res_past = dict((item['product_id'][0], item['product_qty']) for item in Move.read_group(domain_move_out_done, ['product_id', 'product_qty'], ['product_id'], orderby='id'))
    
            res = dict()
            for product in self.with_context(prefetch_fields=False):
                res[product.id] = {}
                if dates_in_the_past:
                    qty_available = quants_res.get(product.id, 0.0) - moves_in_res_past.get(product.id, 0.0) + moves_out_res_past.get(product.id, 0.0)
                else:
                    qty_available = quants_res.get(product.id, 0.0)
                res[product.id]['qty_available'] = float_round(qty_available, precision_rounding=product.uom_id.rounding)
                res[product.id]['incoming_qty'] = float_round(moves_in_res.get(product.id, 0.0), precision_rounding=product.uom_id.rounding)
                res[product.id]['outgoing_qty'] = float_round(moves_out_res.get(product.id, 0.0), precision_rounding=product.uom_id.rounding)
                res[product.id]['virtual_available'] = float_round(
                    qty_available + res[product.id]['incoming_qty'] - res[product.id]['outgoing_qty'],
                    precision_rounding=product.uom_id.rounding)
            return res