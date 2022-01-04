# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime,timedelta


class crystal_reservation(models.Model):
    _name = 'reservation.reservation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'seq'

    seq = fields.Char("Reservation Number", default="New", tracking=True)
    first_name = fields.Char("First Name", tracking=True)
    lastname = fields.Char("Last Name", tracking=True)
    calendar = fields.Datetime("Calendar")
    reservation_date = fields.Date("Date", tracking=True)
    start_date = fields.Datetime("Start Date",compute='_compute_start_date',store=True)
    end_date = fields.Datetime("End Date",compute='_compute_start_date',store=True)
    full_name = fields.Char("Name",compute='_compute_full_name',store=True)
    email = fields.Char("Email", tracking=True)
    phone = fields.Char("Phone", tracking=True)
    no_guest = fields.Char("Number Of Guests")
    no_children = fields.Char("Number Of Children")
    dome = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], tracking=True)
    no_guest_sel = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),('7', '7'), ('8', '8')],string="Number Of Guests", tracking=True)
    no_children_sel = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')],string="Number Of Children", tracking=True)
    time_slot = fields.Selection([('11:45', '11:45'),('14:00', '14:00'),('16:30', '16:30'),('18:45', '18:45'),('21:00', '21:00')],string="Time Slot", tracking=True)

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

    # Function For Send Mail For Proposal Submit
    def action_send_email(self):
        '''
        This function opens a window to compose an email, with the emai template message loaded by default
        '''
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('crystal_reservation', 'mail_template_reservation')[
                1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        ctx = {
            'default_model': 'reservation.reservation',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_document_sent': True,
        }
        return {
            'name': _('Confirmation Email'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }
