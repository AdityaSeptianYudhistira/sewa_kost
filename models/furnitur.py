from odoo import api, fields, models


class Furnitur(models.Model):
    _name = 'kost.furnitur'
    _description = 'New Description'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga Sewa')
