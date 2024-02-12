from odoo import models, fields, api

class libreria_libro(models.Model):
    _name = "libreria.libro"

    name = fields.Char(string="Nombre Libro")
    precio = fields.Float(string="Precio")
    num_ejemplares = fields.Integer(string="Numero Ejemplares")
    fecha_compra = fields.Date(string="fecha de compra")
    segunda_mano = fields.Boolean(string="2ª mano")
    estado = fields.Selection([('0','Nuevo'),('1','Usado')],string="estado",default='0')
    categoria = fields.Many2one("libreria.categoria",string="Categoria",required=True,ondelete="restrict")
    precio_total = fields.Float(string="Importe total",compute="_importe_total",store=True)


    @api.depends('precio','num_ejemplares')
    def _importe_total(self):
        for row in self:
            row.precio_total = row.precio*row.num_ejemplares