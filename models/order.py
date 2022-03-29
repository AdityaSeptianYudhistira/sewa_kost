from odoo import api, fields, models


class Order(models.Model):
    _name = 'kost.order'
    _description = 'New Description'

    orderkamardetail_ids = fields.One2many(
        string='Detail Kamar',
        comodel_name='kost.order_kamar_detail',
        inverse_name='order_id',
    )

    orderpelayanandetail_ids = fields.One2many(
        string='Detail Pelayanan',
        comodel_name='kost.order_pelayanan_detail',
        inverse_name='orderp_id',
    )
    
    name = fields.Char(string='Kode Order', required=True)
    tanggal_pesan = fields.Date('Tanggal Sewa', default=fields.Date.today())
    tanggal_pengiriman = fields.Date(string="Tanggal Mulai Sewa", default=fields.Date.today())
    total = fields.Char(compute='_compute_total', string='Total Harga', store=True)

    
    @api.depends('orderkamardetail_ids')
    def _compute_total(self):
        for record in self:
            # Mengambil harga dari order detail ke dalam bentuk array kemudian dijumlahkan menggunakan sum()
            sum_a = sum(self.env['kost.order_kamar_detail'].search([('order_id', '=', record.id)]).mapped('harga'))
            sum_b = sum(self.env['kost.order_pelayanan_detail'].search([('order_id', '=', record.id)]).mapped('harga'))
            record.total = sum_a + sum_b


class OrderKamarDetail(models.Model):
    _name = 'kost.order_kamar_detail'
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
    
    # Mengurangi stok berdasarkan qty
    @api.model
    def create(self, vals):
        record = super(OrderKamarDetail, self).create(vals)
        if record.qty:
            self.env['kost.kamar'].search([('id', '=', record.kamar_id.id)]).write({'stok': record.kamar_id.stok - record.qty})
            return record

class OrderPelayananDetail(models.Model):
    _name = 'kost.order_pelayanan_detail'
    _description = 'New Description'

    orderp_id = fields.Many2one('kost.order', string='Order')
    pelayanan_id = fields.Many2one('kost.pelayanan', string='Pelayanan')

    name = fields.Selection(
        string='Name', 
        selection=[('kamar', 'Kamar'), 
                  ('pelayanan', 'Pelayanan')])
    harga = fields.Integer(compute='_compute_harga', string='harga')
    qty = fields.Integer(string='Lama Sewa')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga Perbulan')
    
    @api.depends('pelayanan_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.pelayanan_id.harga
    
    @api.depends('qty', 'harga_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.harga_satuan * record.qty
    
    # Mengurangi stok berdasarkan qty
    @api.model
    def create(self, vals):
        record = super(OrderPelayananDetail, self).create(vals)
        if record.qty:
            self.env['kost.pelayanan'].search([('id', '=', record.pelayanan_id.id)]).write({'stok': record.pelayanan_id.stok - record.qty})
            return record
