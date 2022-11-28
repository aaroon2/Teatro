from odoo import models, fields


class TeatroModelo(models.Model):
    _name = 'teatro.modelo'
    _description = 'Teatro Modelo'

    name = fields.Char(string="Nombre")
    fecha = fields.Date(string="Fecha")
    hora = fields.Float(string="Hora")
    precio = fields.Float(string="Precio")
    descripcion = fields.Text(string="Descripcion")
    duracion = fields.Float(string="Duracion")
    butacas = fields.Integer(string="Butacas")
    sala = fields.Char(string="Sala")
    actores = fields.Many2many('teatro.actor', string="Actores")
    director = fields.Many2one('teatro.director', string="Director")
    productor = fields.Many2one('teatro.productor', string="Productor")
    genero = fields.Many2one('teatro.genero', string="Genero")

class Salas(models.Model):
    _name = 'teatro.sala'
    _description = 'Teatro Sala'

    name = fields.Char(string="Nombre")
    id = fields.Integer(string="ID")
    butacas = fields.Integer(string="Butacas")

class Obras(models.Model):
    _name = 'teatro.obra'
    _description = 'Teatro Obra'

    id = fields.Integer(string="ID")
    titulo = fields.Char(string="Titulo")
    genero = fields.Many2one('teatro.genero', string="Genero")
    idioma = fields.Many2one('teatro.idioma', string="Idioma")
    duracion = fields.Float(string="Duracion")
    fecha_estreno = fields.Date(string="Fecha de estreno")
    resumen = fields.Text(string="Resumen")

class Personas(models.Model):
    _name = 'teatro.persona'
    _description = 'Teatro Persona'

    name = fields.Char(string="Nombre")
    nacionalidad = fields.Many2one('teatro.pais', string="Nacionalidad")
    
class Actores(models.Model):
    _name = 'teatro.actor'
    _description = 'Teatro Actor'

    fecha_comienzo = fields.Date(string="Fecha de comienzo")
    personaje_interpretar = fields.Char(string="Personaje a interpretar")

class Directores(models.Model):
    _name = 'teatro.director'
    _description = 'Teatro Director'

    experiencia = fields.Integer(string="Experiencia")
    conocimientos = fields.Char(string="Conocimientos")
    destrezas = fields.Char(string="Destrezas")

    
