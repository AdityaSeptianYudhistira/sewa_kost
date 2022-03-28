from odoo import api, fields, models


class Pelayanan(models.Model):
    _name = 'kost.pelayanan'
    _description = 'Pelayanan tambahan untuk penyewa kamar'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    stok = fields.Integer(string='Ketersediaan')
    harga = fields.Integer(string='Harga Jasa')
