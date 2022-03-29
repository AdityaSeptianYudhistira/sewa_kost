from odoo import api, fields, models


class Accounting(models.Model):
    _name = 'kost.accounting'
    _description = 'New Description'
    _order = 'id asc'

    name = fields.Char(string='Name')
    id_ak = fields.Char(string='Kode')
    date = fields.Datetime('Date', default=fields.Datetime.now())
    debit = fields.Integer(string='Debit')
    kredit = fields.Integer(string='Kredit')
    saldo = fields.Float(compute='_compute_saldo', string='Saldo')
    
    @api.depends('debit', 'kredit')
    def _compute_saldo(self):
        for record in self:
            prev = self.search_read([('id', '<', record.id)], ['saldo'], limit=1, order='date desc')
            prev_saldo = prev[0]['saldo'] if prev else 0
            record.saldo = prev_saldo + record.kredit - record.debit
