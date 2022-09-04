# -*- coding: utf-8 -*-

from odoo import models, fields, api

class teacher(models.Model):
    _name = 'students.teacher'

    name = fields.Char(string="Teacher Name")
    classes = fields.Many2one("students.class")
    national_id = fields.Char("National ID")
    subject_taught = fields.Many2many("students.subject", "subject_id", "teacher_id")

class student(models.Model):
    _name = 'students.student'

    name = fields.Char(string="Students Name")
    contact_user = fields.Many2one("res.partner", string="Related Contact")
    national_id = fields.Char("National ID")
    student_class = fields.Many2one("students.class", string="Related Class")
    dob = fields.Integer(string="Date of birth")
    age = fields.Char(compute="_compute_age")

    @api.depends("dob")
    def _compute_age(self):

        for record in self:
            record.age = 2022 - record.dob


class subject(models.Model):
    _name = 'students.subject'

    name = fields.Char("Subject Name")


    @api.model
    def create(self, values):
        id = super(subject, self).create(values)

        raise Warning(f"Dp rest call")

        return id

    # @api.model
    # def write(self, values):
    #     raise Warning(f"Ukuda kutasei")

    #     return super(subject, self).write(values)

    # @api.model
    # def unlink(self):
        
    #     return self