from odoo import models,fields

class StudentModel(models.Model):
    _name = "student.model"
    _description = "students_details_from"

    name = fields.Char(required = True)
    id_number = fields.Integer(string = "Id Number")
    age = fields.Integer(string = "Age No")
    dob = fields.Date(string = "Date Of Birth")
    gender = fields.Selection([('male', 'Male'),
                            ('female', 'Female')], string = 'Gender')
    select = fields.Boolean(string = " OK or Not")
    example = fields.Image() 
    dattetime = fields.Integer(default = "432153245") 
    
                              
