from odoo import api, fields, models


class CtsRoom(models.Model):
    _name = 'cts.room'
    _description = 'CtsRoom'

    name = fields.Char(required=True)
    line_ids = fields.One2many('cts.seat.line', 'room_id')


class SeatLine(models.Model):
    _name = 'cts.seat.line'
    _description = 'Cts Seat'

    name = fields.Char(required=True)
    type = fields.Many2one('cts.seat.type', required=True)
    amount = fields.Monetary('Amount',related='type.amount')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
    room_id = fields.Many2one('cts.room', required=False)


class CtsSeatType(models.Model):
    _name = 'cts.seat.type'
    _description = 'CTS'

    name = fields.Char()
    amount = fields.Monetary('Amount')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
