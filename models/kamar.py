from odoo import api, fields, models


class Kamar(models.Model):
    _name = 'kost.kamar'
    _description = 'Sewa Kamar Kost'

    name = fields.Char(
        string='Name', 
        required=True
        )
    tipe_kamar_id = fields.Many2one('kost.tipe_kamar', 
        string='Tipe Kamar', 
        required=True,  
        # domain=[('harga','>','199')]
        )
    furnitur_id = fields.Many2one('kost.furnitur', 
        string='Furnitur Tambahan',
        required=True
        )
    orderkamardetail_ids = fields.One2many(
        string='Order Detail',
        comodel_name='kost.order_kamar_detail',
        inverse_name='kamar_id',
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

    des_tipe_kamar = fields.Char(compute='_compute_des_tipe_kamar', string='Deskripsi Tipe Kamar')
    
    @api.depends('tipe_kamar_id')
    def _compute_des_tipe_kamar(self):
        for record in self:
            record.des_tipe_kamar = record.tipe_kamar_id.deskripsi
    
    des_furnitur = fields.Char(compute='_compute_des_furnitur', string='Deskripsi Furnitur')
    
    @api.depends('furnitur_id')
    def _compute_des_furnitur(self):
        for record in self:
            record.des_furnitur = record.furnitur_id.deskripsi
    
    

