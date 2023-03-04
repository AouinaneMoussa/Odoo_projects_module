from odoo import fields, models, api

class Projet(models.Model):
    _name = "aouinane.projet"
    _description = "Projet"
    
    name = fields.Char(string="Projet", required=True)
    description = fields.Char(string="Description")
    date_debut = fields.Date(string="Date")

class Etudiant(models.Model):
    _name = "aouinane.etudiant"
    _description = "Etudiant"
    
    matricule = fields.Integer(string="Matricule",required=True)
    name = fields.Char(string="Nom_etudiant", required=True)
    projet_id = fields.Many2one('aouinane.projet',ondelete='cascade', string="Projet")

class Evaluation(models.Model):
    _name = "aouinane.evaluation"
    _description = " Evaluation"
    
    name = fields.Char(string="Evaluation", required=True)
    evaluateurs= fields.Many2many('aouinane.evaluateur',ondelete='cascade', string="Evaluateur")
    appreciation= fields.Selection([('1','A'),('2','B'),('3','C'),('4','D')], string='Appreciation')
    recommandation = fields.Char(string="Recommandation")
    projet_id = fields.Many2one('aouinane.projet',ondelete='cascade', string="Projet")

class Evaluateur(models.Model):
    _name = "aouinane.evaluateur"
    _description = "Evaluateur"
    
    name = fields.Char(string="Nom_evaluateur", required=True)
    prenom = fields.Char(string="Prenom_evaluateur", required=True)
    entreprise = fields.Char(string='Entreprise')
    evaluations= fields.Many2many('aouinane.evaluation',ondelete='cascade', string="Evaluation")



    