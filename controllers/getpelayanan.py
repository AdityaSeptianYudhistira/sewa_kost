from odoo import http, fields, models
from odoo.http import request
import json


class PelayananCon(http.Controller):
    @http.route(['/pelayanan/', '/pelayanan/<int:idnya>'], auth='public', methods=['GET'], csrf=True)
    def getPelayanan(self, idnya=None, **kwargs):
        value = []
        if not idnya:
            pelayanan = request.env['kost.pelayanan'].search([])
            for p in pelayanan:
                value.append({
                    'id': p.id,
                    'nama_pelayanan': p.name,
                    'deskripsi': p.deskripsi,
                    'stok': p.stok,
                    'harga': p.harga,
                })
            return json.dumps(value)
        else:
            pelayanan_id = request.env['kost.pelayanan'].search([('id', '=', idnya)])
            for p in pelayanan_id:
                value.append({
                    'id': p.id,
                    'nama_pelayanan': p.name,
                    'deskripsi': p.deskripsi,
                    'stok': p.stok,
                    'harga': p.harga,
                })
            return json.dumps(value)
    
    @http.route('/createpelayanan', auth='user', type='json', methods=['POST'], csrf=True)
    def createPelayanan(self, **kw):
        if request.jsonrequest:
            if kw['name']:
                vals ={
                    'name': kw['name'],
                    'deskripsi': kw['deskripsi'],
                    'stok': kw['stok'],
                    'harga': kw['harga'],
                }
                pelayanan_baru = request.env['kost.pelayanan'].create(vals)
                args = {
                    "succeed": True, 
                    "ID": pelayanan_baru.id, 
                    "message": "Pelayanan baru berhasil ditambahkan"}
                return args

