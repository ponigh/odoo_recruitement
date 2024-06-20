# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.addons.account.tests.common import AccountTestInvoicingCommon
from odoo.tests import tagged, Form
from odoo.exceptions import ValidationError


@tagged('-at_install', 'post_install')
class TestMaterial(AccountTestInvoicingCommon):

    def test_material_created(self):
        company = self.env.user.company_id
        po = Form(self.env['material'])
        po.name = "name"
        po.code = "code"
        po.type = "fabric"
        po.buy_price = 120
        po.partner_id = self.partner_a
        po.save()

    def test_material_constraint(self):
        company = self.env.user.company_id
        with self.assertRaises(ValidationError):
            self.env['material'].create({
                'name': 'name',
                'code': "code",
                'type': 'fabric',
                'buy_price': 90,
                'partner_id': self.partner_a.id,
                'currency_id': 1,
                'company_id': 1
            })

