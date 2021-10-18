from odoo import models,fields

class Personal(models.Model):
    _name = "mod.personal"

    name = fields.Char("Nombre")
    status = fields.Selection(selection=[("borrador","Borrador"),("hecho","Hecho")])