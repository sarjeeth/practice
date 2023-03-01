from odoo import models, fields

class Patline(models.Model):
    _name = "student.line"
    _description = "student detail"

    name = fields.Char(required = True)
    age = fields.Integer(string = "Age No")
    dob = fields.Date(string = "Date Of Birth")
    gender = fields.Selection([('male', 'Male'),
                            ('female', 'Female')], string = 'Gender')
    
    children_id = fields.Many2one("teacher.model")