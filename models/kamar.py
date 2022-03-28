from odoo import api, fields, models


class Kamar(models.Model):
    _name = 'kost.kamar'
    _description = 'Sewa Kamar Kost'

    name = fields.Char(
        string='Name', 
        required=True
        )
    tipe_kamar_id = fields.Many2one('kost.tipe_kamar', 
        string='tipe_kamar', 
        required=True,  
        #domain=[('harga','>','199')] #Memberi filter dengan kondisi tertentu
        )
    furnitur_id = fields.Many2one('kost.furnitur', 
        string='Furnitur',
        required=True
        )

    harga = fields.Char(
        compute='_compute_harga', 
        string='Harga'
        )
    
    @api.depends('tipe_kamar_id', 'furnitur_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.tipe_kamar_id.harga + record.furnitur_id.harga

    stok = fields.Integer(string='Kamar yang Tersedia')
    
    

