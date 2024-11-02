from django import forms
from .models import (
    Patient, Traitement, Beneficier, Chambre, Consultation, Commande, LigneCommande,
    Medicament, Plainte, Lunette, PrescriptionLunette, PrescriptionMedicale, Produit,
    GradeMed, Soignant, Interner, Consommer, Depense
)

class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class PatientForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'nom', 'postnom', 'prenom', 'sexe', 'date_naissance', 'telephone',
            'adresse_complete', 'employeur', 'profession', 'carte', 'numero_carte'
        ]
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
        }

class TraitementForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Traitement
        fields = ['libelle', 'prix']

class BeneficierForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Beneficier
        fields = ['date', 'patient', 'traitement', 'user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ChambreForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Chambre
        fields = ['designation', 'prix']

class ConsultationForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['patient', 'soignant', 'user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class CommandeForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['date', 'consultation', 'user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class LigneCommandeForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = LigneCommande
        fields = ['quantite', 'produit', 'commande', 'user']

class MedicamentForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Medicament
        fields = ['libelle', 'emballage', 'unite', 'nbre_par_emballage', 'capacite']

class PlainteForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Plainte
        fields = ['contenu', 'consultation', 'user']

class LunetteForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Lunette
        fields = ['modele']

class PrescriptionLunetteForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = PrescriptionLunette
        fields = ['vision', 'SPH', 'SYL', 'axe', 'oeil', 'consultation', 'user']

class PrescriptionMedicaleForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = PrescriptionMedicale
        fields = ['mode_emploi', 'medicament', 'consultation', 'user']

class ProduitForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['prix']

class GradeMedForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = GradeMed
        fields = ['libelle', 'prix_consult']

class SoignantForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Soignant
        fields = ['noms', 'sexe', 'grade_med']

class InternerForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Interner
        fields = [
            'patient', 'chambre', 'maladie', 'date_sortie', 'diagnostic_sorti', 'caution', 'user'
        ]
        widgets = {
            'date_entree': forms.DateInput(attrs={'type': 'date'}),
            'date_sortie': forms.DateInput(attrs={'type': 'date'}),
        }

class ConsommerForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Consommer
        fields = ['quantite', 'date', 'patient', 'medicament', 'user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class DepenseForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Depense
        fields = ['motif', 'montant', 'date', 'user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
