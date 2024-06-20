# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _name = "material"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = "Material"
    _order = 'id desc'

    @api.model
    def _get_default_code(self):
        ''' Get the default journal.
        It could either be passed through the context using the 'default_journal_id' key containing its id,
        either be determined by the default type.
        '''
        return_value = self.env['ir.sequence'].next_by_code('material.sequence') or '/'

        return return_value

    @api.constrains('buy_price')
    def _check_rule_minimum_buy_price(self):
        if self.filtered(lambda self_object: self_object.buy_price < 100):
            raise ValidationError(_('Buy Price must be greater than 100'))

    name = fields.Char('Order Reference', required=True, index=True, copy=False, default='New')
    code = fields.Char('Order Reference', readonly=True, required=True, index=True, copy=False,
                       default=_get_default_code)
    type = fields.Selection(
        [('fabric', 'Fabric'), ('jeans', 'Jeans'), ('  ', 'Cotton')], 'Type', default='fabric',
        index=True, required=True)
    buy_price = fields.Monetary(string='Buy Price', default=0.0,  currency_field='currency_id')
    partner_id = fields.Many2one('res.partner', string='Vendor', required=True,
                                 change_default=True, tracking=True,
                                 domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")

    currency_id = fields.Many2one('res.currency', 'Currency', required=True, readonly=True,
                                  invisible=True, default=lambda self: self.env.company.currency_id.id)
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, readonly=True,
                                 default=lambda self: self.env.company.id)
