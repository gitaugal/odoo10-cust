# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Product Secondary UOM",
    "summary": "Extends product to give a second UOM",
    "version": "10.0.1.0.0",
    "category": "Sales",
    "website": "",
    "author": "FNG",
    "license": "",
    "application": False,
    "installable": True,
    "post_init_hook": "_trigger_onchange_price_discount",
    "depends": [
        "sales",
    ],
    "data": [
        "views/product_uos_view.xml",
    ],
}
