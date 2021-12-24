# -*- coding: utf-8 -*-

from odoo import models, fields, api


class crystal_reservation(models.Model):
    _name = 'reservation.reservation'
    _rec_name = 'seq'

    seq = fields.Char("Sequence", default="New")
    first_name = fields.Char("First Name")
    lastname = fields.Char("Last Name")
    calendar = fields.Datetime("Calendar")
    email = fields.Char("Email")
    phone = fields.Char("phone")
    no_guest = fields.Char("Number Of Guests")
    no_children = fields.Char("Number Of Children")
    dome = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])

    @api.model
    def create(self, vals):
        vals['seq'] = self.env['ir.sequence'].sudo().next_by_code('reservation.reservation')
        return super(crystal_reservation, self).create(vals)
