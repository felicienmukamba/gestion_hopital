from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Consommer, Depense, GradeMed, Interner, Lunette, Medicament, Patient, Plainte, PrescriptionLunette, PrescriptionMedicale, Produit, Soignant, Traitement, Beneficier, Chambre, Consultation, Commande, LigneCommande
from .forms import BeneficierForm, ChambreForm, ConsommerForm, DepenseForm, GradeMedForm, InternerForm, LunetteForm, MedicamentForm, PatientForm, PlainteForm, PrescriptionLunetteForm, PrescriptionMedicaleForm, ProduitForm, SoignantForm, TraitementForm, ConsultationForm, CommandeForm, LigneCommandeForm

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
