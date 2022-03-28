from odoo import api, fields, models


class Order(models.Model):
    _name = 'kost.order'
    _description = 'New Description'

    orderdetail_ids = fields.One2many(
        string='Order Detail',
        comodel_name='kost.order_detail',
        inverse_name='order_id',
    )
    
    name = fields.Char(string='Kode Order', required=True)
    total = fields.Char(compute='_compute_total', string='Total Harga', store=True)
    
    @api.depends('orderdetail_ids')
    def _compute_total(self):
        for record in self:
            # Mengambil harga dari order detail ke dalam bentuk array kemudian dijumlahkan menggunakan sum()
            sum_harga = sum(self.env['kost.order_detail'].search([('order_id', '=', record.id)]).mapped('harga'))
            record.total = sum_harga


class OrderDetail(models.Model):
    _name = 'kost.order_detail'
    _description = 'New Description'

    order_id = fields.Many2one('kost.order', string='Order')
    kamar_id = fields.Many2one('kost.kamar', string='Kamar')

    name = fields.Selection(
        string='Name', 
        selection=[('kamar', 'Kamar'), 
                  ('pelayanan', 'Pelayanan')])
    harga = fields.Integer(compute='_compute_harga', string='harga')
    qty = fields.Integer(string='Lama Sewa')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga Perbulan')
    
    @api.depends('kamar_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.kamar_id.harga
    
    @api.depends('qty', 'harga_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.harga_satuan * record.qty
    


