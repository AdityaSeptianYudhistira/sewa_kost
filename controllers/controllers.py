# -*- coding: utf-8 -*-
# from odoo import http


# class SewaKost(http.Controller):
#     @http.route('/sewa_kost/sewa_kost/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sewa_kost/sewa_kost/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sewa_kost.listing', {
#             'root': '/sewa_kost/sewa_kost',
#             'objects': http.request.env['sewa_kost.sewa_kost'].search([]),
#         })

#     @http.route('/sewa_kost/sewa_kost/objects/<model("sewa_kost.sewa_kost"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sewa_kost.object', {
#             'object': obj
#         })
