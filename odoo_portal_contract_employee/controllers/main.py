# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website_portal.controllers.main import website_account

class website_account(website_account):

    @http.route()
    def account(self, **kw):
        """ Add return documents to main account page """
        response = super(website_account, self).account(**kw)
        employee = request.env['hr.employee'].sudo().search([('user_id', '=', request.env.user.id)])
        response.qcontext.update({
        'contract_count': employee.contracts_count,
        })
        return response
        
    @http.route(['/my/contracts', '/my/contracts/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_contract(self, page=1, **kw):
        if request.env.user.has_group('odoo_portal_contract_employee.group_employee_contract'):
            values = self._prepare_portal_layout_values()
            employee = request.env['hr.employee'].sudo().search([('user_id', '=', request.env.user.id)])
            if employee:
                contract = request.env['hr.contract'].sudo().search([('employee_id', '=', employee.id)])
                contracts_count = employee.contracts_count
                # count for pager
                # pager
                pager = request.website.pager(
                    url="/my/contracts",
                    total=contracts_count,
                    page=page,
                    step=self._items_per_page
                )
                values.update({
                    'contracts': contract,
                    'page_name': 'contract',
                    'pager': pager,
                    'default_url': '/my/contracts',
                })
                return request.render("odoo_portal_contract_employee.display_contracts", values)
                
    @http.route(['/my/contract/<int:contract>'], type='http', auth="user", website=True)
    def contract_print(self, contract=None, **kw):
        if request.env.user.has_group('odoo_portal_contract_employee.group_employee_contract'):
            pdf = request.env['report'].sudo().get_pdf([contract], 'print_employee_contract.employee_contract_report_id', data=None)
            pdfhttpheaders = [('Content-Type', 'application/pdf'), ('Content-Length', len(pdf))]
            return request.make_response(pdf, headers=pdfhttpheaders)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
