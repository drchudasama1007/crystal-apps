# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime,timedelta


class crystal_reservation(models.Model):
    _name = 'reservation.reservation'
    _rec_name = 'seq'

    seq = fields.Char("Reservation Number", default="New")
    first_name = fields.Char("First Name")
    lastname = fields.Char("Last Name")
    calendar = fields.Datetime("Calendar")
    reservation_date = fields.Date("Date")
    start_date = fields.Datetime("Start Date",compute='_compute_start_date',store=True)
    end_date = fields.Datetime("End Date",compute='_compute_start_date',store=True)
    full_name = fields.Char("Name",compute='_compute_full_name',store=True)
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

    @api.depends('reservation_date','time_slot')
    def _compute_start_date(self):
        for rec in self:
            if rec.reservation_date and rec.time_slot:
                start_time_object = datetime.strptime(rec.time_slot, '%H:%M').time()
                rec.start_date  = datetime.combine(rec.reservation_date, start_time_object) + timedelta(hours=-5, minutes=-30)
                rec.end_date = datetime.combine(rec.reservation_date, start_time_object) + timedelta(hours=-3,minutes=-30)
            else:
                rec.start_date = False
                rec.end_date = False

    @api.depends('first_name', 'lastname')
    def _compute_full_name(self):
        for rec in self:
            if rec.first_name and rec.lastname:
                rec.full_name = rec.first_name + " " + rec.lastname
            elif rec.first_name and not rec.lastname:
                rec.full_name = rec.first_name
            elif not rec.first_name and rec.lastname:
                rec.full_name = rec.lastname
            else:
                rec.full_name = ''