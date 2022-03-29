from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    is_pegawai_kost = fields.Boolean(string='Pegawai', default=False)
    is_customer_kost = fields.Boolean(string='Customer', default=False)

    
