from pathlib import Path
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from core.settings import BASE_DIR
from .models import Consommer, Depense, GradeMed, Interner, Lunette, Medicament, Patient, Plainte, PrescriptionLunette, PrescriptionMedicale, Produit, Soignant, Traitement, Beneficier, Chambre, Consultation, Commande, LigneCommande
from .forms import BeneficierForm, ChambreForm, ConsommerForm, DepenseForm, FactureForm, GradeMedForm, InternerForm, LigneFactureForm, LunetteForm, MedicamentForm, PatientForm, PlainteForm, PrescriptionLunetteForm, PrescriptionMedicaleForm, ProduitForm, SoignantForm, TraitementForm, ConsultationForm, CommandeForm, LigneCommandeForm

class PatientListView(LoginRequiredMixin, View):
    def get(self, request):
        patients = Patient.objects.all()
        return render(request, 'patients/patient_list.html', {'patients': patients})

class PatientDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        return render(request, 'patients/patient_detail.html', {'patient': patient})

class PatientCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PatientForm()
        return render(request, 'patients/patient_form.html', {'form': form})

    def post(self, request):
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient-list')
        return render(request, 'patients/patient_form.html', {'form': form})

class PatientUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        form = PatientForm(instance=patient)
        return render(request, 'patients/patient_form.html', {'form': form})

    def post(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient-detail', pk=pk)
        return render(request, 'patients/patient_form.html', {'form': form})

class PatientDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        return render(request, 'patients/patient_confirm_delete.html', {'patient': patient})

    def post(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        patient.delete()
        return redirect('patient-list')




class MedicamentListView(LoginRequiredMixin, View):
    def get(self, request):
        medicaments = Medicament.objects.all()
        return render(request, 'medicaments/medicament_list.html', {'medicaments': medicaments})

class MedicamentDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        medicament = get_object_or_404(Medicament, pk=pk)
        return render(request, 'medicaments/medicament_detail.html', {'medicament': medicament})

class MedicamentCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = MedicamentForm()
        return render(request, 'medicaments/medicament_form.html', {'form': form})

    def post(self, request):
        form = MedicamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicament-list')
        return render(request, 'medicaments/medicament_form.html', {'form': form})

class MedicamentUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        medicament = get_object_or_404(Medicament, pk=pk)
        form = MedicamentForm(instance=medicament)
        return render(request, 'medicaments/medicament_form.html', {'form': form})

    def post(self, request, pk):
        medicament = get_object_or_404(Medicament, pk=pk)
        form = MedicamentForm(request.POST, instance=medicament)
        if form.is_valid():
            form.save()
            return redirect('medicament-detail', pk=pk)
        return render(request, 'medicaments/medicament_form.html', {'form': form})

class MedicamentDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        medicament = get_object_or_404(Medicament, pk=pk)
        return render(request, 'medicaments/medicament_confirm_delete.html', {'medicament': medicament})

    def post(self, request, pk):
        medicament = get_object_or_404(Medicament, pk=pk)
        medicament.delete()
        return redirect('medicament-list')




class ConsultationListView(LoginRequiredMixin, View):
    def get(self, request):
        consultations = Consultation.objects.all()
        return render(request, 'consultations/consultation_list.html', {'consultations': consultations})

class ConsultationDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        consultation = get_object_or_404(Consultation, pk=pk)
        return render(request, 'consultations/consultation_detail.html', {'consultation': consultation})

class ConsultationCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ConsultationForm()
        return render(request, 'consultations/consultation_form.html', {'form': form})

    def post(self, request):
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultation-list')
        return render(request, 'consultations/consultation_form.html', {'form': form})

class ConsultationUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        consultation = get_object_or_404(Consultation, pk=pk)
        form = ConsultationForm(instance=consultation)
        return render(request, 'consultations/consultation_form.html', {'form': form})

    def post(self, request, pk):
        consultation = get_object_or_404(Consultation, pk=pk)
        form = ConsultationForm(request.POST, instance=consultation)
        if form.is_valid():
            form.save()
            return redirect('consultation-detail', pk=pk)
        return render(request, 'consultations/consultation_form.html', {'form': form})

class ConsultationDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        consultation = get_object_or_404(Consultation, pk=pk)
        return render(request, 'consultations/consultation_confirm_delete.html', {'consultation': consultation})

    def post(self, request, pk):
        consultation = get_object_or_404(Consultation, pk=pk)
        consultation.delete()
        return redirect('consultation-list')


class TraitementListView(LoginRequiredMixin, View):
    def get(self, request):
        traitements = Traitement.objects.all()
        return render(request, 'traitements/traitement_list.html', {'traitements': traitements})

class TraitementDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        traitement = get_object_or_404(Traitement, pk=pk)
        return render(request, 'traitements/traitement_detail.html', {'traitement': traitement})

class TraitementCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = TraitementForm()
        return render(request, 'traitements/traitement_form.html', {'form': form})

    def post(self, request):
        form = TraitementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traitement-list')
        return render(request, 'traitements/traitement_form.html', {'form': form})

class TraitementUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        traitement = get_object_or_404(Traitement, pk=pk)
        form = TraitementForm(instance=traitement)
        return render(request, 'traitements/traitement_form.html', {'form': form})

    def post(self, request, pk):
        traitement = get_object_or_404(Traitement, pk=pk)
        form = TraitementForm(request.POST, instance=traitement)
        if form.is_valid():
            form.save()
            return redirect('traitement-detail', pk=pk)
        return render(request, 'traitements/traitement_form.html', {'form': form})

class TraitementDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        traitement = get_object_or_404(Traitement, pk=pk)
        return render(request, 'traitements/traitement_confirm_delete.html', {'traitement': traitement})

    def post(self, request, pk):
        traitement = get_object_or_404(Traitement, pk=pk)
        traitement.delete()
        return redirect('traitement-list')


class LigneCommandeListView(LoginRequiredMixin, View):
    def get(self, request):
        lignes_commandes = LigneCommande.objects.all()
        return render(request, 'lignes_commandes/ligne_commande_list.html', {'lignes_commandes': lignes_commandes})

class LigneCommandeDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        ligne_commande = get_object_or_404(LigneCommande, pk=pk)
        return render(request, 'lignes_commandes/ligne_commande_detail.html', {'ligne_commande': ligne_commande})

class LigneCommandeCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = LigneCommandeForm()
        return render(request, 'lignes_commandes/ligne_commande_form.html', {'form': form})

    def post(self, request):
        form = LigneCommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ligne_commande-list')
        return render(request, 'lignes_commandes/ligne_commande_form.html', {'form': form})

class LigneCommandeUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        ligne_commande = get_object_or_404(LigneCommande, pk=pk)
        form = LigneCommandeForm(instance=ligne_commande)
        return render(request, 'lignes_commandes/ligne_commande_form.html', {'form': form})

    def post(self, request, pk):
        ligne_commande = get_object_or_404(LigneCommande, pk=pk)
        form = LigneCommandeForm(request.POST, instance=ligne_commande)
        if form.is_valid():
            form.save()
            return redirect('ligne_commande-detail', pk=pk)
        return render(request, 'lignes_commandes/ligne_commande_form.html', {'form': form})

class LigneCommandeDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        ligne_commande = get_object_or_404(LigneCommande, pk=pk)
        return render(request, 'lignes_commandes/ligne_commande_confirm_delete.html', {'ligne_commande': ligne_commande})

    def post(self, request, pk):
        ligne_commande = get_object_or_404(LigneCommande, pk=pk)
        ligne_commande.delete()
        return redirect('ligne_commande-list')



class BeneficierListView(LoginRequiredMixin, View):
    def get(self, request):
        beneficiers = Beneficier.objects.all()
        return render(request, 'beneficiers/beneficier_list.html', {'beneficiers': beneficiers})

class BeneficierDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        beneficier = get_object_or_404(Beneficier, pk=pk)
        return render(request, 'beneficiers/beneficier_detail.html', {'beneficier': beneficier})

class BeneficierCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = BeneficierForm()
        return render(request, 'beneficiers/beneficier_form.html', {'form': form})

    def post(self, request):
        form = BeneficierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beneficier-list')
        return render(request, 'beneficiers/beneficier_form.html', {'form': form})

class BeneficierUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        beneficier = get_object_or_404(Beneficier, pk=pk)
        form = BeneficierForm(instance=beneficier)
        return render(request, 'beneficiers/beneficier_form.html', {'form': form})

    def post(self, request, pk):
        beneficier = get_object_or_404(Beneficier, pk=pk)
        form = BeneficierForm(request.POST, instance=beneficier)
        if form.is_valid():
            form.save()
            return redirect('beneficier-detail', pk=pk)
        return render(request, 'beneficiers/beneficier_form.html', {'form': form})

class BeneficierDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        beneficier = get_object_or_404(Beneficier, pk=pk)
        return render(request, 'beneficiers/beneficier_confirm_delete.html', {'beneficier': beneficier})

    def post(self, request, pk):
        beneficier = get_object_or_404(Beneficier, pk=pk)
        beneficier.delete()
        return redirect('beneficier-list')



class ChambreListView(LoginRequiredMixin, View):
    def get(self, request):
        chambres = Chambre.objects.all()
        return render(request, 'chambres/chambre_list.html', {'chambres': chambres})

class ChambreDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        chambre = get_object_or_404(Chambre, pk=pk)
        return render(request, 'chambres/chambre_detail.html', {'chambre': chambre})

class ChambreCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ChambreForm()
        return render(request, 'chambres/chambre_form.html', {'form': form})

    def post(self, request):
        form = ChambreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chambre-list')
        return render(request, 'chambres/chambre_form.html', {'form': form})

class ChambreUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        chambre = get_object_or_404(Chambre, pk=pk)
        form = ChambreForm(instance=chambre)
        return render(request, 'chambres/chambre_form.html', {'form': form})

    def post(self, request, pk):
        chambre = get_object_or_404(Chambre, pk=pk)
        form = ChambreForm(request.POST, instance=chambre)
        if form.is_valid():
            form.save()
            return redirect('chambre-detail', pk=pk)
        return render(request, 'chambres/chambre_form.html', {'form': form})

class ChambreDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        chambre = get_object_or_404(Chambre, pk=pk)
        return render(request, 'chambres/chambre_confirm_delete.html', {'chambre': chambre})

    def post(self, request, pk):
        chambre = get_object_or_404(Chambre, pk=pk)
        chambre.delete()
        return redirect('chambre-list')




class CommandeListView(LoginRequiredMixin, View):
    def get(self, request):
        commandes = Commande.objects.all()
        return render(request, 'commandes/commande_list.html', {'commandes': commandes})

class CommandeDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        commande = get_object_or_404(Commande, pk=pk)
        return render(request, 'commandes/commande_detail.html', {'commande': commande})

class CommandeCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = CommandeForm()
        return render(request, 'commandes/commande_form.html', {'form': form})

    def post(self, request):
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('commande-list')
        return render(request, 'commandes/commande_form.html', {'form': form})

class CommandeUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        commande = get_object_or_404(Commande, pk=pk)
        form = CommandeForm(instance=commande)
        return render(request, 'commandes/commande_form.html', {'form': form})

    def post(self, request, pk):
        commande = get_object_or_404(Commande, pk=pk)
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('commande-detail', pk=pk)
        return render(request, 'commandes/commande_form.html', {'form': form})

class CommandeDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        commande = get_object_or_404(Commande, pk=pk)
        return render(request, 'commandes/commande_confirm_delete.html', {'commande': commande})

    def post(self, request, pk):
        commande = get_object_or_404(Commande, pk=pk)
        commande.delete()
        return redirect('commande-list')




class PlainteListView(LoginRequiredMixin, View):
    def get(self, request):
        plaintes = Plainte.objects.all()
        return render(request, 'plaintes/plainte_list.html', {'plaintes': plaintes})

class PlainteDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        plainte = get_object_or_404(Plainte, pk=pk)
        return render(request, 'plaintes/plainte_detail.html', {'plainte': plainte})

class PlainteCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PlainteForm()
        return render(request, 'plaintes/plainte_form.html', {'form': form})

    def post(self, request):
        form = PlainteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plainte-list')
        return render(request, 'plaintes/plainte_form.html', {'form': form})

class PlainteUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        plainte = get_object_or_404(Plainte, pk=pk)
        form = PlainteForm(instance=plainte)
        return render(request, 'plaintes/plainte_form.html', {'form': form})

    def post(self, request, pk):
        plainte = get_object_or_404(Plainte, pk=pk)
        form = PlainteForm(request.POST, instance=plainte)
        if form.is_valid():
            form.save()
            return redirect('plainte-detail', pk=pk)
        return render(request, 'plaintes/plainte_form.html', {'form': form})

class PlainteDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        plainte = get_object_or_404(Plainte, pk=pk)
        return render(request, 'plaintes/plainte_confirm_delete.html', {'plainte': plainte})

    def post(self, request, pk):
        plainte = get_object_or_404(Plainte, pk=pk)
        plainte.delete()
        return redirect('plainte-list')




class LunetteListView(LoginRequiredMixin, View):
    def get(self, request):
        lunettes = Lunette.objects.all()
        return render(request, 'lunettes/lunette_list.html', {'lunettes': lunettes})

class LunetteDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        lunette = get_object_or_404(Lunette, pk=pk)
        return render(request, 'lunettes/lunette_detail.html', {'lunette': lunette})

class LunetteCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = LunetteForm()
        return render(request, 'lunettes/lunette_form.html', {'form': form})

    def post(self, request):
        form = LunetteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lunette-list')
        return render(request, 'lunettes/lunette_form.html', {'form': form})

class LunetteUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        lunette = get_object_or_404(Lunette, pk=pk)
        form = LunetteForm(instance=lunette)
        return render(request, 'lunettes/lunette_form.html', {'form': form})

    def post(self, request, pk):
        lunette = get_object_or_404(Lunette, pk=pk)
        form = LunetteForm(request.POST, instance=lunette)
        if form.is_valid():
            form.save()
            return redirect('lunette-detail', pk=pk)
        return render(request, 'lunettes/lunette_form.html', {'form': form})

class LunetteDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        lunette = get_object_or_404(Lunette, pk=pk)
        return render(request, 'lunettes/lunette_confirm_delete.html', {'lunette': lunette})

    def post(self, request, pk):
        lunette = get_object_or_404(Lunette, pk=pk)
        lunette.delete()
        return redirect('lunette-list')



class PrescriptionLunetteListView(LoginRequiredMixin, View):
    def get(self, request):
        prescriptions = PrescriptionLunette.objects.all()
        return render(request, 'prescriptions_lunettes/prescription_lunette_list.html', {'prescriptions': prescriptions})

class PrescriptionLunetteDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        prescription = get_object_or_404(PrescriptionLunette, pk=pk)
        return render(request, 'prescriptions_lunettes/prescription_lunette_detail.html', {'prescription': prescription})

class PrescriptionLunetteCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PrescriptionLunetteForm()
        return render(request, 'prescriptions_lunettes/prescription_lunette_form.html', {'form': form})

    def post(self, request):
        form = PrescriptionLunetteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prescription_lunette-list')
        return render(request, 'prescriptions_lunettes/prescription_lunette_form.html', {'form': form})

class PrescriptionLunetteUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        prescription = get_object_or_404(PrescriptionLunette, pk=pk)
        form = PrescriptionLunetteForm(instance=prescription)
        return render(request, 'prescriptions_lunettes/prescription_lunette_form.html', {'form': form})

    def post(self, request, pk):
        prescription = get_object_or_404(PrescriptionLunette, pk=pk)
        form = PrescriptionLunetteForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            return redirect('prescription_lunette-detail', pk=pk)
        return render(request, 'prescriptions_lunettes/prescription_lunette_form.html', {'form': form})

class PrescriptionLunetteDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        prescription = get_object_or_404(PrescriptionLunette, pk=pk)
        return render(request, 'prescriptions_lunettes/prescription_lunette_confirm_delete.html', {'prescription': prescription})

    def post(self, request, pk):
        prescription = get_object_or_404(PrescriptionLunette, pk=pk)
        prescription.delete()
        return redirect('prescription_lunette-list')


class ProduitListView(LoginRequiredMixin, View):
    def get(self, request):
        produits = Produit.objects.all()
        return render(request, 'produits/produit_list.html', {'produits': produits})

class ProduitDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        produit = get_object_or_404(Produit, pk=pk)
        return render(request, 'produits/produit_detail.html', {'produit': produit})

class ProduitCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProduitForm()
        return render(request, 'produits/produit_form.html', {'form': form})

    def post(self, request):
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produit-list')
        return render(request, 'produits/produit_form.html', {'form': form})

class ProduitUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        produit = get_object_or_404(Produit, pk=pk)
        form = ProduitForm(instance=produit)
        return render(request, 'produits/produit_form.html', {'form': form})

    def post(self, request, pk):
        produit = get_object_or_404(Produit, pk=pk)
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('produit-detail', pk=pk)
        return render(request, 'produits/produit_form.html', {'form': form})

class ProduitDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        produit = get_object_or_404(Produit, pk=pk)
        return render(request, 'produits/produit_confirm_delete.html', {'produit': produit})

    def post(self, request, pk):
        produit = get_object_or_404(Produit, pk=pk)
        produit.delete()
        return redirect('produit-list')



class GradeMedListView(LoginRequiredMixin, View):
    def get(self, request):
        grades_med = GradeMed.objects.all()
        return render(request, 'grades_med/grade_med_list.html', {'grades_med': grades_med})

class GradeMedDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        grade_med = get_object_or_404(GradeMed, pk=pk)
        return render(request, 'grades_med/grade_med_detail.html', {'grade_med': grade_med})

class GradeMedCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = GradeMedForm()
        return render(request, 'grades_med/grade_med_form.html', {'form': form})

    def post(self, request):
        form = GradeMedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_med-list')
        return render(request, 'grades_med/grade_med_form.html', {'form': form})

class GradeMedUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        grade_med = get_object_or_404(GradeMed, pk=pk)
        form = GradeMedForm(instance=grade_med)
        return render(request, 'grades_med/grade_med_form.html', {'form': form})

    def post(self, request, pk):
        grade_med = get_object_or_404(GradeMed, pk=pk)
        form = GradeMedForm(request.POST, instance=grade_med)
        if form.is_valid():
            form.save()
            return redirect('grade_med-detail', pk=pk)
        return render(request, 'grades_med/grade_med_form.html', {'form': form})

class GradeMedDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        grade_med = get_object_or_404(GradeMed, pk=pk)
        return render(request, 'grades_med/grade_med_confirm_delete.html', {'grade_med': grade_med})

    def post(self, request, pk):
        grade_med = get_object_or_404(GradeMed, pk=pk)
        grade_med.delete()
        return redirect('grade_med-list')



class SoignantListView(LoginRequiredMixin, View):
    def get(self, request):
        soignants = Soignant.objects.all()
        return render(request, 'soignants/soignant_list.html', {'soignants': soignants})

class SoignantDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        soignant = get_object_or_404(Soignant, pk=pk)
        return render(request, 'soignants/soignant_detail.html', {'soignant': soignant})

class SoignantCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = SoignantForm()
        return render(request, 'soignants/soignant_form.html', {'form': form})

    def post(self, request):
        form = SoignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('soignant-list')
        return render(request, 'soignants/soignant_form.html', {'form': form})

class SoignantUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        soignant = get_object_or_404(Soignant, pk=pk)
        form = SoignantForm(instance=soignant)
        return render(request, 'soignants/soignant_form.html', {'form': form})

    def post(self, request, pk):
        soignant = get_object_or_404(Soignant, pk=pk)
        form = SoignantForm(request.POST, instance=soignant)
        if form.is_valid():
            form.save()
            return redirect('soignant-detail', pk=pk)
        return render(request, 'soignants/soignant_form.html', {'form': form})

class SoignantDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        soignant = get_object_or_404(Soignant, pk=pk)
        return render(request, 'soignants/soignant_confirm_delete.html', {'soignant': soignant})

    def post(self, request, pk):
        soignant = get_object_or_404(Soignant, pk=pk)
        soignant.delete()
        return redirect('soignant-list')



class InternerListView(LoginRequiredMixin, View):
    def get(self, request):
        interners = Interner.objects.all()
        return render(request, 'interners/interner_list.html', {'interners': interners})

class InternerDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        interner = get_object_or_404(Interner, pk=pk)
        return render(request, 'interners/interner_detail.html', {'interner': interner})

class InternerCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = InternerForm()
        return render(request, 'interners/interner_form.html', {'form': form})

    def post(self, request):
        form = InternerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interner-list')
        return render(request, 'interners/interner_form.html', {'form': form})

class InternerUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        interner = get_object_or_404(Interner, pk=pk)
        form = InternerForm(instance=interner)
        return render(request, 'interners/interner_form.html', {'form': form})

    def post(self, request, pk):
        interner = get_object_or_404(Interner, pk=pk)
        form = InternerForm(request.POST, instance=interner)
        if form.is_valid():
            form.save()
            return redirect('interner-detail', pk=pk)
        return render(request, 'interners/interner_form.html', {'form': form})

class InternerDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        interner = get_object_or_404(Interner, pk=pk)
        return render(request, 'interners/interner_confirm_delete.html', {'interner': interner})

    def post(self, request, pk):
        interner = get_object_or_404(Interner, pk=pk)
        interner.delete()
        return redirect('interner-list')


class ConsommerListView(LoginRequiredMixin, View):
    def get(self, request):
        consommations = Consommer.objects.all()
        return render(request, 'consommers/consommer_list.html', {'consommations': consommations})

class ConsommerDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        consommer = get_object_or_404(Consommer, pk=pk)
        return render(request, 'consommers/consommer_detail.html', {'consommer': consommer})

class ConsommerCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ConsommerForm()
        return render(request, 'consommers/consommer_form.html', {'form': form})

    def post(self, request):
        form = ConsommerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consommer-list')
        return render(request, 'consommers/consommer_form.html', {'form': form})

class ConsommerUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        consommer = get_object_or_404(Consommer, pk=pk)
        form = ConsommerForm(instance=consommer)
        return render(request, 'consommers/consommer_form.html', {'form': form})

    def post(self, request, pk):
        consommer = get_object_or_404(Consommer, pk=pk)
        form = ConsommerForm(request.POST, instance=consommer)
        if form.is_valid():
            form.save()
            return redirect('consommer-detail', pk=pk)
        return render(request, 'consommers/consommer_form.html', {'form': form})

class ConsommerDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        consommer = get_object_or_404(Consommer, pk=pk)
        return render(request, 'consommers/consommer_confirm_delete.html', {'consommer': consommer})

    def post(self, request, pk):
        consommer = get_object_or_404(Consommer, pk=pk)
        consommer.delete()
        return redirect('consommer-list')


class DepenseListView(LoginRequiredMixin, View):
    def get(self, request):
        depenses = Depense.objects.all()
        return render(request, 'depenses/depense_list.html', {'depenses': depenses})

class DepenseDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        depense = get_object_or_404(Depense, pk=pk)
        return render(request, 'depenses/depense_detail.html', {'depense': depense})

class DepenseCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = DepenseForm()
        return render(request, 'depenses/depense_form.html', {'form': form})

    def post(self, request):
        form = DepenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('depense-list')
        return render(request, 'depenses/depense_form.html', {'form': form})

class DepenseUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        depense = get_object_or_404(Depense, pk=pk)
        form = DepenseForm(instance=depense)
        return render(request, 'depenses/depense_form.html', {'form': form})

    def post(self, request, pk):
        depense = get_object_or_404(Depense, pk=pk)
        form = DepenseForm(request.POST, instance=depense)
        if form.is_valid():
            form.save()
            return redirect('depense-detail', pk=pk)
        return render(request, 'depenses/depense_form.html', {'form': form})

class DepenseDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        depense = get_object_or_404(Depense, pk=pk)
        return render(request, 'depenses/depense_confirm_delete.html', {'depense': depense})

    def post(self, request, pk):
        depense = get_object_or_404(Depense, pk=pk)
        depense.delete()
        return redirect('depense-list')



class PrescriptionMedicaleListView(LoginRequiredMixin, View):
    def get(self, request):
        prescriptions = PrescriptionMedicale.objects.all()
        return render(request, 'prescriptions_medicales/prescription_medicale_list.html', {'prescriptions': prescriptions})

class PrescriptionMedicaleDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        prescription = get_object_or_404(PrescriptionMedicale, pk=pk)
        return render(request, 'prescriptions_medicales/prescription_medicale_detail.html', {'prescription': prescription})

class PrescriptionMedicaleCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PrescriptionMedicaleForm()
        return render(request, 'prescriptions_medicales/prescription_medicale_form.html', {'form': form})

    def post(self, request):
        form = PrescriptionMedicaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prescription_medicale-list')
        return render(request, 'prescriptions_medicales/prescription_medicale_form.html', {'form': form})

class PrescriptionMedicaleUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        prescription = get_object_or_404(PrescriptionMedicale, pk=pk)
        form = PrescriptionMedicaleForm(instance=prescription)
        return render(request, 'prescriptions_medicales/prescription_medicale_form.html', {'form': form})

    def post(self, request, pk):
        prescription = get_object_or_404(PrescriptionMedicale, pk=pk)
        form = PrescriptionMedicaleForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            return redirect('prescription_medicale-detail', pk=pk)
        return render(request, 'prescriptions_medicales/prescription_medicale_form.html', {'form': form})

class PrescriptionMedicaleDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        prescription = get_object_or_404(PrescriptionMedicale, pk=pk)
        return render(request, 'prescriptions_medicales/prescription_medicale_confirm_delete.html', {'prescription': prescription})

    def post(self, request, pk):
        prescription = get_object_or_404(PrescriptionMedicale, pk=pk)
        prescription.delete()
        return redirect('prescription_medicale-list')
















from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Patient, Facture, LigneFacture, Interner
from .forms import FactureForm, LigneFactureForm
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import io
from core.settings import BASE_DIR

from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


# Vue pour créer une facture pour un patient spécifique
def creer_facture(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    
    if request.method == 'POST':
        facture_form = FactureForm(request.POST)
        ligne_form = LigneFactureForm(request.POST)
        if facture_form.is_valid() and ligne_form.is_valid():
            facture = facture_form.save(commit=False)
            facture.patient = patient
            facture.user = request.user
            facture.total = 0  # Initialise le total à 0
            facture.save()
            
            ligne_facture = ligne_form.save(commit=False)
            ligne_facture.facture = facture
            ligne_facture.save()
            
            # Met à jour le total de la facture
            facture.total += ligne_facture.total_cost()
            facture.save()
            
            return redirect('facture_detail', facture_id=facture.id)
    else:
        facture_form = FactureForm(initial={'patient': patient})
        ligne_form = LigneFactureForm()
    
    return render(request, 'factures/creer_facture.html', {'facture_form': facture_form, 'ligne_form': ligne_form})

def facture_detail(request, facture_id):
    facture = get_object_or_404(Facture, pk=facture_id)
    lignes_facture = LigneFacture.objects.filter(facture=facture)
    consultations = Consultation.objects.filter(patient=facture.patient)
    internements = Interner.objects.filter(patient=facture.patient)
    consommations = Consommer.objects.filter(patient=facture.patient)

    # Calculer le coût total des consommations de médicaments
    for consommation in consommations:
        consommation.total_cost = consommation.quantite * consommation.medicament.prix

    context = {
        'facture': facture,
        'lignes_facture': lignes_facture,
        'consultations': consultations,
        'internements': internements,
        'consommations': consommations,
    }
    return render(request, 'factures/facture_detail.html', context)

def delete_facture(request, facture_id):
    facture = get_object_or_404(Facture, id=facture_id)
    facture.delete()
    return redirect('facture_list')

def delete_ligne_facture(request, ligne_facture_id):
    ligne_facture = get_object_or_404(LigneFacture, id=ligne_facture_id)
    facture_id = ligne_facture.facture.id
    ligne_facture.delete()
    return redirect('facture_detail', facture_id=facture_id)


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Facture, LigneFacture, Consultation, Interner, Consommer
import io
from pathlib import Path

def generate_invoice_pdf(request, invoice_id):
    invoice = get_object_or_404(Facture, pk=invoice_id)
    patient = invoice.patient
    # Create PDF using reportlab
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="invoice-{invoice.pk}-{patient.nom}-{patient.postnom}.pdf"'

    # Fonts
    APTO_FONT = Path(BASE_DIR) / "static/assets/fonts/Aptos.ttf"
    APTO_FONT_BOLD = Path(BASE_DIR) / "static/assets/fonts/Aptos-Bold.ttf"
    pdfmetrics.registerFont(TTFont('Aptos', str(APTO_FONT)))
    pdfmetrics.registerFont(TTFont('Aptos-Bold', str(APTO_FONT_BOLD)))

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.setTitle(f"Facture {invoice.pk}-{patient.nom}-{patient.postnom}")

    styles = getSampleStyleSheet()
    normal_style = styles['Normal']
    bold_style = styles['Heading3']

    # Entête avec logo et informations de l'entreprise et du patient
    logo_path = Path(BASE_DIR) / "static/assets/img/angular_gradient.png"
    p.drawImage(str(logo_path), 20 * mm, 260 * mm, width=30 * mm, height=30 * mm)

    p.setFont("Aptos", 12)
    p.drawString(60 * mm, 285 * mm, "Centre de santé".upper())
    p.setFont("Aptos-Bold", 12)
    p.drawString(60 * mm, 278 * mm, "MALIKIA WA AMANI".upper())
    p.setFont("Aptos", 10)
    p.drawString(60 * mm, 270 * mm, "N°43 Av. Maniema, IBANDA/BUKAVU")
    p.drawString(60 * mm, 265 * mm, "Téléphone : +243 993 722 532")
    p.drawString(60 * mm, 260 * mm, "Télephone : +243 852 896 185")

    p.setFont("Aptos-Bold", 12)
    p.drawString(120 * mm, 285 * mm, "Informations du Patient".upper())
    p.setFont("Aptos", 10)
    p.drawString(120 * mm, 270 * mm, f"Nom: {patient.nom} {patient.postnom} {patient.prenom}")
    p.drawString(120 * mm, 265 * mm, f"Date de Naissance: {patient.date_naissance.strftime('%Y-%m-%d')}")
    p.drawString(120 * mm, 260 * mm, f"Téléphone: {patient.telephone}")
    p.drawString(120 * mm, 255 * mm, f"Adresse: {patient.adresse_complete}")

    p.setFont("Aptos-Bold", 28)
    p.drawString(70 * mm, 240 * mm, f"FACTURE N°...{invoice_id}".upper())

    y_pos = 220 * mm  # Ajustement de la position initiale de y

    def draw_table(p, data, col_widths, y_pos):
        table = Table(data, colWidths=col_widths)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.darkblue),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Aptos-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        table_width, table_height = table.wrap(0, 0)
        x_pos = (A4[0] - table_width) / 2  # Centrage horizontal
        table.drawOn(p, x_pos, y_pos)
        return y_pos - table_height  # Retourne la nouvelle position y après avoir dessiné la table

    # Consommables
    consommables_data = [['Quantité', 'Désignation', 'PU', 'PT']]
    lignes_facture = LigneFacture.objects.filter(facture=invoice)
    for ligne in lignes_facture:
        consommables_data.append([str(ligne.quantite), ligne.produit.libelle, f"${ligne.produit.prix:.2f}", f"${ligne.total_cost():.2f}"])

    y_pos = draw_table(p, consommables_data, [40 * mm, 60 * mm, 50 * mm, 50 * mm], y_pos)
    y_pos -= 20  # Espace entre les sections

    # Consultations
    consultations_data = [['Consultation ID', 'Soignant', 'Coût Total']]
    consultations = Consultation.objects.filter(patient=patient)
    for consultation in consultations:
        consultations_data.append([consultation.pk, consultation.soignant.noms, f"${consultation.total_cost():.2f}"])

    y_pos = draw_table(p, consultations_data, [60 * mm, 80 * mm, 60 * mm], y_pos)
    y_pos -= 20  # Espace entre les sections

    # Internements
    internements_data = [['Chambre', 'Date d\'entrée', 'Coût Total']]
    internements = Interner.objects.filter(patient=patient)
    for internement in internements:
        internements_data.append([internement.chambre.designation, internement.date_entree.strftime('%Y-%m-%d'), f"${internement.total_cost():.2f}"])

    y_pos = draw_table(p, internements_data, [60 * mm, 80 * mm, 60 * mm], y_pos)
    y_pos -= 20  # Espace entre les sections

    # Consommations de médicaments
    consommations_data = [['Médicament', 'Quantité', 'Coût Total']]
    consommations = Consommer.objects.filter(patient=patient)
    for consommation in consommations:
        consommations_data.append([consommation.medicament.libelle, consommation.quantite, f"${consommation.quantite * consommation.medicament.prix:.2f}"])

    y_pos = draw_table(p, consommations_data, [60 * mm, 60 * mm, 80 * mm], y_pos)
    y_pos -= 20  # Espace entre les sections

    # Calcul du coût total général
    sous_total = invoice.total + sum(consultation.total_cost() for consultation in consultations) + sum(internement.total_cost() for internement in internements) + sum(consommation.quantite * consommation.medicament.prix for consommation in consommations)
    tva = sous_total * 0.16  # TVA à 18%
    total_general = sous_total + tva

    p.setFont("Aptos-Bold", 12)
    p.drawString(120 * mm, y_pos, "Sous-total :")
    p.drawString(160 * mm, y_pos, f"${sous_total:.2f}")
    y_pos -= 20

    p.drawString(120 * mm, y_pos, "TVA (16%) :")
    p.drawString(160 * mm, y_pos, f"${tva:.2f}")
    y_pos -= 20

    p.drawString(120 * mm, y_pos, "Total Général :")
    p.drawString(160 * mm, y_pos, f"${total_general:.2f}")

    # Pied de page avec informations légales
    p.setFont("Aptos", 8)
    p.drawString(20 * mm, 30 * mm, "Informations légales de l'entreprise")
    p.drawString(20 * mm, 20 * mm, "RCS : 123 456 789 | TVA : FR 12 345678901 | Adresse : 123 Rue Exemple, 75000 Paris")

    # Save PDF content
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

# Vue pour lister toutes les factures
def facture_list(request):
    factures = Facture.objects.all()
    return render(request, 'factures/facture_list.html', {'factures': factures})
