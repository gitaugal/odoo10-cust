# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import ValidationError


class PricelistUOM(models.Model):
    _inherit = 'product.uom'
	# This is so as to select if the customer gets the product invoicing in Kgs or in Lbs, or in any other UOM that is not the default. This will work for all the products in the pricelist in the same category ID as chosen.
	# If empty, means default product UOM is used.
	uom_id = fields.Many2one('product.uom', 'Unit of Sale', help='Specify a unit of measure if different from the default unit of measure than inventory. Keep empty to use the default unit of measure.')
