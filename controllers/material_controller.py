# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import base64
from collections import OrderedDict
from datetime import datetime

from odoo import http
from odoo.exceptions import AccessError, MissingError
from odoo.http import content_disposition, request, Response, Controller, request, route
from odoo.tools import image_process
from odoo.tools.translate import _
from odoo.addons.portal.controllers.portal import pager as portal_pager, CustomerPortal
from odoo.addons.web.controllers.main import Binary
import json



class MaterialController(Controller):

    @http.route(['/material'], type='http',  methods=['GET'], auth="api_key")
    def material_index(self):
        list=[]
        for material_obj in request.env['material'].search([]):
            list.append({
                "id": material_obj.id,
                "name": material_obj.name,
                "code": material_obj.code,
                "buy_price": material_obj.buy_price,
                "partner_id": material_obj.partner_id.name
            })
        response = {
            "data": list
        }
        mime = 'application/json'
        body = json.dumps(response)
        return Response(
            body, status=200,
            headers=[('Content-Type', mime), ('Content-Length', len(body))]
        )

    @route(['/material'], type='json',  methods=['POST'], auth="api_key")
    def material_post(self):
        res = request.jsonrequest and request.jsonrequest or {}

        return_id = request.env['material'].create({
            "name": res["name"],
            "buy_price": res["buy_price"],
            "partner_id": res["partner_id"],
        })

        response = {
            "id": return_id.id
        }
        mime = 'application/json'
        body = json.dumps(response)
        return Response(
            body, status=200,
            headers=[('Content-Type', mime), ('Content-Length', len(body))]
        )

    @route(['/material/<int:material_id>'], type='json', methods=['PUT'], auth="api_key")
    def material_put(self, material_id=None):
        res = request.jsonrequest and request.jsonrequest or {}

        request.env['material'].browse(material_id).write({
            "name": res["name"],
            "code": res["code"],
            "buy_price": res["buy_price"],
            "partner_id": res["partner_id"],
        })

        response = {
            "id": "null"
        }
        mime = 'application/json'
        body = json.dumps(response)
        return Response(
            body, status=200,
            headers=[('Content-Type', mime), ('Content-Length', len(body))]
        )

    @http.route(['/material/<int:material_id>'], type='http', methods=['DELETE'], auth="api_key", csrf=False)
    def material_delete(self, material_id=None):
        request.env['material'].browse(material_id).unlink()
        response = {
            "id": "null"
        }
        mime = 'application/json'
        body = json.dumps(response)
        return Response(
            body, status=200,
            headers=[('Content-Type', mime), ('Content-Length', len(body))]
        )