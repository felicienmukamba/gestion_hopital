from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.db.models import Avg, Count

from hospial.models import (
    Patient, Traitement, Beneficier, Chambre, Consultation, Commande, LigneCommande,
    Medicament, Plainte, Lunette, PrescriptionLunette, PrescriptionMedicale, Produit,
    GradeMed, Soignant, Interner, Consommer, Depense
)
# Home View


class HomeView(View):
    def get(self, request):
        return render(request, "core/home.html")


# Dashboard View
class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'patients': {
                'count': Patient.objects.count(),
                'objects': Patient.objects.all()
            },
            'traitements': {
                'count': Traitement.objects.count(),
                'price_mean': Traitement.objects.aggregate(Avg('prix'))['prix__avg'],
                'objects': Traitement.objects.all()
            },
            'beneficiers': Beneficier.objects.all(),
            'chambres': Chambre.objects.all(),
            'consultations': Consultation.objects.all(),
            'commandes': Commande.objects.all(),
            'lignes_commandes': LigneCommande.objects.all(),
            'medicaments': Medicament.objects.all(),
            'plaintes': Plainte.objects.all(),
            'lunettes': Lunette.objects.all(),
            'prescriptions_lunettes': PrescriptionLunette.objects.all(),
            'prescriptions_medicales': PrescriptionMedicale.objects.all(),
            'produits': Produit.objects.all(),
            'grades_med': GradeMed.objects.all(),
            'soignants': Soignant.objects.all(),
            'interners': Interner.objects.all(),
            'consommers': Consommer.objects.all(),
            'depenses': Depense.objects.all(),
        }
        return render(request, 'core/dashboard.html',  context)
