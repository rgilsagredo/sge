from odoo import models, fields

class libreria_categoria(models.Model):
    # mandatory
    _name = "libreria.categoria"


    name = fields.Char(string="Nombre Categría", required=True, help="Ayuda para saber que info lleva este campo")
    descripcion = fields.Text(string="Description")
    libros = fields.One2many("libreria.libro","categoria",string="libros")