from django.db import models
from django.db.models import Sum
from django.contrib.auth import get_user_model


class Patient(models.Model):
    nom = models.CharField(max_length=50)
    postnom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50, null=True, blank=True)
    sexe = models.CharField(max_length=1, choices=[
                            ('M', 'Male'), ('F', 'Female')])
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=13)
    adresse_complete = models.CharField(max_length=100)
    employeur = models.CharField(max_length=50, null=True, blank=True)
    profession = models.CharField(max_length=50, null=True, blank=True)
    carte = models.CharField(max_length=50, null=True, blank=True)
    numero_carte = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.postnom} {self.prenom}"

    def age(self):
        from datetime import date
        age = date.today().year - self.date_naissance.year
        if date.today().month < self.date_naissance.month or (date.today().month == self.date_naissance.month and date.today().day < self.date_naissance.day):
            age -= 1
        return age

    def total_spent(self):
        return self.depense_set.aggregate(total=Sum('montant'))['total'] or 0


class Traitement(models.Model):
    libelle = models.CharField(max_length=50)
    prix = models.FloatField()

    def __str__(self):
        return self.libelle


class Beneficier(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    traitement = models.ForeignKey(Traitement, on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.patient} - {self.traitement}"


class Chambre(models.Model):
    designation = models.CharField(max_length=50)
    prix = models.FloatField()

    def __str__(self):
        return self.designation

class Consultation(models.Model):
    date = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    soignant = models.ForeignKey('Soignant', on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Consultation - {self.date} - {self.patient}"

    def total_cost(self):
        lignes_commandes = self.commande_set.all()

        return sum(item.quantite * item.produit.prix for item in lignes_commandes)


class Commande(models.Model):
    date = models.DateField()
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Commande - {self.consultation} - {self.date}"


class LigneCommande(models.Model):
    quantite = models.IntegerField()
    produit = models.ForeignKey('Produit', on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Ligne Commande - {self.produit} - {self.quantite}"

    def total_cost(self):
        return self.quantite * self.produit.prix


class Medicament(models.Model):
    libelle = models.CharField(max_length=50)
    emballage = models.CharField(max_length=50)
    unite = models.CharField(max_length=50)
    nbre_par_emballage = models.IntegerField()
    capacite = models.IntegerField()

    def __str__(self):
        return self.libelle


class Plainte(models.Model):
    contenu = models.CharField(max_length=255)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.contenu


class Lunette(models.Model):
    modele = models.CharField(max_length=50)

    def __str__(self):
        return self.modele


class PrescriptionLunette(models.Model):
    vision = models.CharField(max_length=4, choices=[
                              ('Loin', 'Loin'), ('Près', 'Près')])
    SPH = models.CharField(max_length=50)
    SYL = models.CharField(max_length=50)
    axe = models.CharField(max_length=50)
    oeil = models.CharField(max_length=6, choices=[
                            ('Gauche', 'Gauche'), ('Droit', 'Droit')])
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Prescription Lunette - {self.vision} - {self.oeil}"


class PrescriptionMedicale(models.Model):
    mode_emploi = models.CharField(max_length=50)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.mode_emploi


class Produit(models.Model):
    libelle = models.CharField(max_length=50)
    prix = models.FloatField()

    def __str__(self):
        return self.libelle


class GradeMed(models.Model):
    libelle = models.CharField(max_length=50)
    prix_consult = models.FloatField()

    def __str__(self):
        return self.libelle


class Soignant(models.Model):
    noms = models.CharField(max_length=100)
    sexe = models.CharField(max_length=1, choices=[
                            ('M', 'Male'), ('F', 'Female')])
    grade_med = models.ForeignKey('GradeMed', on_delete=models.CASCADE)

    def __str__(self):
        return self.noms


class Interner(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    maladie = models.CharField(max_length=200)
    date_entree = models.DateField(auto_now_add=True)
    date_sortie = models.DateField(null=True, blank=True)
    diagnostic_sorti = models.CharField(max_length=255, null=True, blank=True)
    caution = models.FloatField(default=0)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Internement - {self.patient} - {self.maladie}"

    def total_cost(self):
        from datetime import date
        if self.date_sortie:
            days_in_hospital = (self.date_sortie - self.date_entree).days
        else:
            days_in_hospital = (date.today() - self.date_entree).days
        return days_in_hospital * self.chambre.prix


class Consommer(models.Model):
    quantite = models.IntegerField()
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicament = models.ForeignKey('Medicament', on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.patient} - {self.medicament}"


class Depense(models.Model):
    motif = models.CharField(max_length=100)
    montant = models.FloatField()
    date = models.DateField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.motif} - {self.montant}"


class Facture(models.Model):
    date = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    total = models.FloatField()
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Facture {self.id} - {self.patient}"


class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    def __str__(self):
        return f"Ligne Facture {self.id} - {self.produit}"

    def total_cost(self):
        return self.quantite * self.produit.prix
