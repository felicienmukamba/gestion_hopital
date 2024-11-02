from django.contrib import admin
from .models import (
    Patient, Traitement, Beneficier, Chambre, Consultation, Commande, LigneCommande, 
    Medicament, Plainte, Lunette, PrescriptionLunette, PrescriptionMedicale, Produit, 
    GradeMed, Soignant, Interner, Consommer, Depense
)


# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'postnom', 'prenom', 'sexe', 'date_naissance', 'telephone')
    search_fields = ('nom', 'postnom', 'prenom', 'telephone')
    list_filter = ('sexe', 'date_naissance')

class TraitementAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'prix')
    search_fields = ('libelle',)

class BeneficierAdmin(admin.ModelAdmin):
    list_display = ('date', 'patient', 'traitement', 'user')
    search_fields = ('patient__nom', 'traitement__libelle', 'user__username')
    list_filter = ('date',)

class ChambreAdmin(admin.ModelAdmin):
    list_display = ('designation', 'prix')
    search_fields = ('designation',)

class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('date', 'patient', 'soignant', 'user')
    search_fields = ('patient__nom', 'soignant__noms', 'user__username')
    list_filter = ('date',)

class CommandeAdmin(admin.ModelAdmin):
    list_display = ('date', 'consultation', 'user')
    search_fields = ('consultation__patient__nom', 'user__username')
    list_filter = ('date',)

class LigneCommandeAdmin(admin.ModelAdmin):
    list_display = ('quantite', 'produit', 'commande', 'user')
    search_fields = ('produit__libelle', 'commande__consultation__patient__nom', 'user__username')
    list_filter = ('produit',)

class MedicamentAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'emballage', 'unite', 'nbre_par_emballage', 'capacite')
    search_fields = ('libelle',)

class PlainteAdmin(admin.ModelAdmin):
    list_display = ('contenu', 'consultation', 'user')
    search_fields = ('consultation__patient__nom', 'user__username')

class LunetteAdmin(admin.ModelAdmin):
    list_display = ('modele',)
    search_fields = ('modele',)

class PrescriptionLunetteAdmin(admin.ModelAdmin):
    list_display = ('vision', 'SPH', 'SYL', 'axe', 'oeil', 'consultation', 'user')
    search_fields = ('consultation__patient__nom', 'user__username')
    list_filter = ('vision', 'oeil')

class PrescriptionMedicaleAdmin(admin.ModelAdmin):
    list_display = ('mode_emploi', 'medicament', 'consultation', 'user')
    search_fields = ('medicament__libelle', 'consultation__patient__nom', 'user__username')

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('prix',)
    search_fields = ('prix',)

class GradeMedAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'prix_consult')
    search_fields = ('libelle',)

class SoignantAdmin(admin.ModelAdmin):
    list_display = ('noms', 'sexe', 'grade_med')
    search_fields = ('noms', 'grade_med__libelle')
    list_filter = ('sexe',)

class InternerAdmin(admin.ModelAdmin):
    list_display = ('patient', 'chambre', 'maladie', 'date_entree', 'date_sortie', 'diagnostic_sorti', 'caution', 'user')
    search_fields = ('patient__nom', 'chambre__designation', 'user__username')
    list_filter = ('date_entree', 'date_sortie')

class ConsommerAdmin(admin.ModelAdmin):
    list_display = ('quantite', 'date', 'patient', 'medicament', 'user')
    search_fields = ('patient__nom', 'medicament__libelle', 'user__username')
    list_filter = ('date',)

class DepenseAdmin(admin.ModelAdmin):
    list_display = ('motif', 'montant', 'date', 'user')
    search_fields = ('motif', 'user__username')
    list_filter = ('date',)



admin.site.register(Patient, PatientAdmin)
admin.site.register(Traitement, TraitementAdmin)
admin.site.register(Beneficier, BeneficierAdmin)
admin.site.register(Chambre, ChambreAdmin)
admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(Commande, CommandeAdmin)
admin.site.register(LigneCommande, LigneCommandeAdmin)
admin.site.register(Medicament, MedicamentAdmin)
admin.site.register(Plainte, PlainteAdmin)
admin.site.register(Lunette, LunetteAdmin)
admin.site.register(PrescriptionLunette, PrescriptionLunetteAdmin)
admin.site.register(PrescriptionMedicale, PrescriptionMedicaleAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(GradeMed, GradeMedAdmin)
admin.site.register(Soignant, SoignantAdmin)
admin.site.register(Interner, InternerAdmin)
admin.site.register(Consommer, ConsommerAdmin)
admin.site.register(Depense, DepenseAdmin)
