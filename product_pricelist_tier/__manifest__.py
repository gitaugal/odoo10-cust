# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Product Pricelist UOM",
    "summary": "Extends pricelists with specifiying UOM",
    "version": "10.0.1.0.0",
    "category": "Product",
    "website": "",
    "author": "FNG, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "post_init_hook": "_trigger_onchange_product_uom",
    "depends": [
        "product",
    ],
    "data": [
        "views/product_pricelist_item_view.xml",
    ],
    "demo": [
        "demo/product_template_demo.xml",
        "demo/product_pricelist_item_demo.xml",
    ],
}
