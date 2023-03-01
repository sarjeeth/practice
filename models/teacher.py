from odoo import models,fields

class Teacher(models.Model):
    _name = "teacher.model"
    _description = "this school is for study"

    name = fields.Char(required = True)
    age = fields.Integer(string = "Age No")
    # stud_id = fields.Many2one(comodel_name="student.model")
    student_ids = fields.One2many("student.line","children_id")
    tution = fields.Many2many("student.model")