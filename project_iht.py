from odoo import models, fields

class ProjectIHT(models.Model):
    _inherit = 'project.project'

    lokasi_proyek = fields.Text(string="Lokasi Proyek")
    source_aplikasi_pendukung = fields.Char(string="Source Aplikasi Pendukung", help="URL aplikasi pendukung proyek")
    daftar_perkerja_remote = fields.Json(string="Daftar Pekerja Remote", help="List pekerja remote dalam format JSON")
