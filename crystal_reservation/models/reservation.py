# -*- coding: utf-8 -*-

from odoo import models, fields, api


class crystal_reservation(models.Model):
    _name = 'reservation.reservation'
    _rec_name = 'seq'

    seq = fields.Char("Reservation Number", default="New")
    first_name = fields.Char("First Name")
    lastname = fields.Char("Last Name")
    calendar = fields.Datetime("Calendar")
    reservation_date = fields.Date("Date")
    email = fields.Char("Email")
    phone = fields.Char("Phone")
    no_guest = fields.Char("Number Of Guests")
    no_children = fields.Char("Number Of Children")
    dome = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])
    no_guest_sel = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')],string="Number Of Guests")
    no_children_sel = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')],string="Number Of Children")
    time_slot = fields.Selection([('11:45', '11:45'),('14:00', '14:00'),('16:30', '16:30'),('18:45', '18:45'),('21:00', '21:00')],string="Time Slot")

    @api.model
    def create(self, vals):
        vals['seq'] = self.env['ir.sequence'].sudo().next_by_code('reservation.reservation')
        return super(crystal_reservation, self).create(vals)
