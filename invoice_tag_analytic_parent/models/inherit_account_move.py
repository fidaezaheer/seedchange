from odoo import api, fields, models, _
from odoo.exceptions import UserError


class accountMoveInherit(models.Model):
    _inherit = "account.move"

