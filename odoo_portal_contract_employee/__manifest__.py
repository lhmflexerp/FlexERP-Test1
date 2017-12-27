# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': 'Employee Contract from Web-My Account using Portal User as Employee',
    'version': '1.0',
    'price': 49.0,
    'depends': [
                'hr_contract',
                #'website_portal',
                'website',
                'portal',
                'print_employee_contract',
                ],
    'currency': 'EUR',
    'license': 'Other proprietary',
    'summary': """This module allow your portal employee to view and print employee contract from my account""",
    'description': """
Odoo Portal Contract Employee
Odoo Portal Contract Employee
Portal Contract Employee
Odoo Portal Contract
Odoo Contract Employee
Odoo Employee Contract Self Service Portal
employee contract portal
self service portal contract
self service employee contract portal
contract employee portal self service
employee self service
ESS
ess
self service odoo
portal
self service
self portal
odoo self service employee
employee portal
employee job portal
self service odoo employee
employee details
employee leave
employee contract
employee holidays
self service portal​

Odoo contract Portal User Employee
Contract Portal User
Odoo contracts
Your contracts
My contracts
Project contract
User contracts
Employee contracts
Portal user contracts
portal contract
website contract
enterprise user contract
enterprise contract user
enterprise employee contract
enterprise contract employee
contract for enterprise user
contract for enterprise employee
contract recording
contract entry for enterprise
contract entry employee enterprise
enterprise paid users
enterprise free users
enterprise employee user
enterprise user employee
contract user fill
contract employee fill
enterprise contract encoding
contract fill
enterprise contract
hr contract
hr contract enterprise employee
hr contract enterprise user
enterprise fill contract activities
contract activities
contract lines enterprise user
contract lines enterprise employee
contract work enterprise user
contract work user
contract work employee enterprise
portal contract enterprise
portal contract
website contract
contract data
odoo enterprise user
odoo enterprise employee
odoo external employee
odoo external user
external user contract
worker contract
This module allow you to employee(s) who are portal user and it will allow to record contract.
labour contract
external employee contract
external user contract
contract Entry from Web-My Account using Portal User as Employee
external contract employee
external contract user
Portal Users who are employee of system but not real users can fill/record contract Activities.
If your company using contract application but not purchased real users from Odoo Enterprise then your employee can fill contract as portal users.
No need to create real users in system if you are only using contract module to make contract entry for your all employees. So you can create portal users and set it on employee form and employee can use that portal user logged to fill contract activities.
Make sure you have set Portal Employee Contract group on portal user form on settings of users.
No need to purchase users from Odoo Enterprise only to fill contract any more.
For more details please watch Video or contact us before buy.​

    """,
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'http://www.probuse.com',
    'support': 'contact@probuse.com',
    'images': ['static/description/img1.jpg'],
    'live_test_url' : 'https://youtu.be/x4-xbX8dLRM',
    'category' : 'Website',

    'data':[
        'security/contract_security.xml',
        'views/contract_template.xml',
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
