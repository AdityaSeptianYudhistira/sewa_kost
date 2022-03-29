from odoo import api, fields, models


class CheckOut(models.Model):
    _name = 'kost.checkout'
    _description = 'Check Out penyewa kamar'

    name = fields.Char(compute='_compute_penyewa', string='Penyewa')
    order_id = fields.Many2one('kost.order', string='Order')
    tgl_checkout = fields.Date(
        string='Tanggal Check Out',
        default=fields.Date.today(),
    )
    
    tagihan = fields.Char(compute='_compute_tagihan', string='Tagihan')
    
    @api.depends('order_id')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.order_id.total

    @api.depends('order_id')
    def _compute_penyewa(self):
        for record in self:
            record.name = self.env['kost.order'].search([('id', '=', record.order_id.id)]).mapped('penyewa_id').name

    @api.model
    def create(self, vals):
        record = super(CheckOut, self).create(vals)
        if record.tgl_checkout:
            self.env['kost.order'].search([('id', '=', record.order_id.id)]).write({'checkouted': True})
            self.env['kost.accounting'].create({'kredit': record.tagihan, 'name' :record.name})
            return record

    def unlink(self):
        for r in self:
            self.env['kost.order'].search([('id', '=', r.order_id.id)]).write({'checkouted': False})
        record = super(CheckOut, self).unlink()
        return record
