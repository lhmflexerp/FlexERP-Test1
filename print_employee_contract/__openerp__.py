# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Employee Contract Report',
    'version' : '1.0',
    'price' : 10.0,
    'currency': 'EUR',
    'category': 'Human Resources',
    'description': """
Employee Contract Report:
Print the contract report
print employee contract
print hr contract
print contract
print employee contract
contract employee
employee agreement
print employee agreement
employee data
contract print
hr contract
hr employee contract
odoo employee contract
contract details
report contract
report hr contract
            """,
    'summary' : 'Employee Contract Report - HR',
    'author' : 'Probuse Consulting Service Pvt. Ltd.',
    'website' : 'www.probuse.com',
        'images': ['static/description/123.jpg'],
    'depends' : ['hr_contract'],
    'data' : [
            'report/employee_contract_report.xml'
              ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
