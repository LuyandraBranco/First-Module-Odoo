from odoo import models, fields

class MeuModelo(models.Model):
    _name = 'meu.modulo'
    _description = 'Descrição do Meu Modelo'

    name = fields.Char(string='Nome', required=True)
    descricao = fields.Text(string='Descrição')
