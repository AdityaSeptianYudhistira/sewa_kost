from odoo import api, fields, models


class Tipe_Kamar(models.Model):
    _name = 'kost.tipe_kamar'
    _description = 'Jenis Kamar yang Tersedia'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga Sewa')
    
    
