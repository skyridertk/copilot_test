from odoo import models, fields, api

class student_class(models.Model):
    _name = 'students.class'

    name = fields.Char("Class Name")
    level = fields.Char("Class Level")
    subjects =  fields.Many2many("students.subject", "class_id", "student_id")