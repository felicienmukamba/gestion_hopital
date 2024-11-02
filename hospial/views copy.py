from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Patient, Traitement, Beneficier, Chambre, Consultation, Commande, Consommer, Depense, GradeMed, Interner, LigneCommande, Medicament, Plainte, PrescriptionLunette, PrescriptionMedicale, Produit, Soignant
from .forms import PatientForm, TraitementForm, ConsultationForm, DepenseForm, ChambreForm, ConsommerForm, BeneficierForm, CommandeForm, InternerForm, LigneCommandeForm, MedicamentForm, PlainteForm, PrescriptionLunetteForm, PrescriptionMedicaleForm, SoignantForm
from django.contrib.auth.mixins import LoginRequiredMixin
from fpdf import FPDF
import io
from django.http import FileResponse

class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'app/patient_list.html'
    context_object_name = 'patients'

class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'app/patient_detail.html'
    context_object_name = 'patient'

class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'app/patient_form.html'
    success_url = reverse_lazy('patient-list')

class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'app/patient_form.html'
    success_url = reverse_lazy('patient-list')

class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = 'app/patient_confirm_delete.html'
    success_url = reverse_lazy('patient-list')

class ConsultationListView(LoginRequiredMixin, ListView):
    model = Consultation
    template_name = 'app/consultation_list.html'
    context_object_name = 'consultations'

class ConsultationDetailView(LoginRequiredMixin, DetailView):
    model = Consultation
    template_name = 'app/consultation_detail.html'
    context_object_name = 'consultation'

class ConsultationCreateView(LoginRequiredMixin, CreateView):
    model = Consultation
    form_class = ConsultationForm
    template_name = 'app/consultation_form.html'
    success_url = reverse_lazy('consultation-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ConsultationUpdateView(LoginRequiredMixin, UpdateView):
    model = Consultation
    form_class = ConsultationForm
    template_name = 'app/consultation_form.html'
    success_url = reverse_lazy('consultation-list')

class ConsultationDeleteView(LoginRequiredMixin, DeleteView):
    model = Consultation
    template_name = 'app/consultation_confirm_delete.html'
    success_url = reverse_lazy('consultation-list')

class DepenseListView(LoginRequiredMixin, ListView):
    model = Depense
    template_name = 'app/depense_list.html'
    context_object_name = 'depenses'

class DepenseDetailView(LoginRequiredMixin, DetailView):
    model = Depense
    template_name = 'app/depense_detail.html'
    context_object_name = 'depense'

class DepenseCreateView(LoginRequiredMixin, CreateView):
    model = Depense
    form_class = DepenseForm
    template_name = 'app/depense_form.html'
    success_url = reverse_lazy('depense-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DepenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Depense
    form_class = DepenseForm
    template_name = 'app/depense_form.html'
    success_url = reverse_lazy('depense-list')

class DepenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Depense
    template_name = 'app/depense_confirm_delete.html'
    success_url = reverse_lazy('depense-list')

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        patients = Patient.objects.all()
        consultations = Consultation.objects.all()
        depenses = Depense.objects.all()
        context = {
            'patients': patients,
            'consultations': consultations,
            'depenses': depenses,
        }
        return render(request, 'app/dashboard.html', context)

# Traitement Views
class TraitementListView(LoginRequiredMixin, ListView):
    model = Traitement
    template_name = 'app/traitement_list.html'
    context_object_name = 'traitements'

class TraitementDetailView(LoginRequiredMixin, DetailView):
    model = Traitement
    template_name = 'app/traitement_detail.html'
    context_object_name = 'traitement'

class TraitementCreateView(LoginRequiredMixin, CreateView):
    model = Traitement
    form_class = TraitementForm
    template_name = 'app/traitement_form.html'
    success_url = reverse_lazy('traitement-list')

class TraitementUpdateView(LoginRequiredMixin, UpdateView):
    model = Traitement
    form_class = TraitementForm
    template_name = 'app/traitement_form.html'
    success_url = reverse_lazy('traitement-list')

class TraitementDeleteView(LoginRequiredMixin, DeleteView):
    model = Traitement
    template_name = 'app/traitement_confirm_delete.html'
    success_url = reverse_lazy('traitement-list')

# Chambre Views
class ChambreListView(LoginRequiredMixin, ListView):
    model = Chambre
    template_name = 'app/chambre_list.html'
    context_object_name = 'chambres'

class ChambreDetailView(LoginRequiredMixin, DetailView):
    model = Chambre
    template_name = 'app/chambre_detail.html'
    context_object_name = 'chambre'

class ChambreCreateView(LoginRequiredMixin, CreateView):
    model = Chambre
    form_class = ChambreForm
    template_name = 'app/chambre_form.html'
    success_url = reverse_lazy('chambre-list')

class ChambreUpdateView(LoginRequiredMixin, UpdateView):
    model = Chambre
    form_class = ChambreForm
    template_name = 'app/chambre_form.html'
    success_url = reverse_lazy('chambre-list')

class ChambreDeleteView(LoginRequiredMixin, DeleteView):
    model = Chambre
    template_name = 'app/chambre_confirm_delete.html'
    success_url = reverse_lazy('chambre-list')

# Interner Views
class InternerListView(LoginRequiredMixin, ListView):
    model = Interner
    template_name = 'app/interner_list.html'
    context_object_name = 'interners'

class InternerDetailView(LoginRequiredMixin, DetailView):
    model = Interner
    template_name = 'app/interner_detail.html'
    context_object_name = 'interner'

class InternerCreateView(LoginRequiredMixin, CreateView):
    model = Interner
    form_class = InternerForm
    template_name = 'app/interner_form.html'
    success_url = reverse_lazy('interner-list')

class InternerUpdateView(LoginRequiredMixin, UpdateView):
    model = Interner
    form_class = InternerForm
    template_name = 'app/interner_form.html'
    success_url = reverse_lazy('interner-list')

class InternerDeleteView(LoginRequiredMixin, DeleteView):
    model = Interner
    template_name = 'app/interner_confirm_delete.html'
    success_url = reverse_lazy('interner-list')

# LigneCommande Views
class LigneCommandeListView(LoginRequiredMixin, ListView):
    model = LigneCommande
    template_name = 'app/lignecommande_list.html'
    context_object_name = 'lignecommandes'

class LigneCommandeDetailView(LoginRequiredMixin, DetailView):
    model = LigneCommande
    template_name = 'app/lignecommande_detail.html'
    context_object_name = 'lignecommande'

class LigneCommandeCreateView(LoginRequiredMixin, CreateView):
    model = LigneCommande
    form_class = LigneCommandeForm
    template_name = 'app/lignecommande_form.html'
    success_url = reverse_lazy('lignecommande-list')

class LigneCommandeUpdateView(LoginRequiredMixin, UpdateView):
    model = LigneCommande
    form_class = LigneCommandeForm
    template_name = 'app/lignecommande_form.html'
    success_url = reverse_lazy('lignecommande-list')

class LigneCommandeDeleteView(LoginRequiredMixin, DeleteView):
    model = LigneCommande
    template_name = 'app/lignecommande_confirm_delete.html'
    success_url = reverse_lazy('lignecommande-list')

class InvoiceView(LoginRequiredMixin, View):
    def get(self, request, pk):
        consultation = get_object_or_404(Consultation, pk=pk)
        lignes_commandes = LigneCommande.objects.filter(commande__consultation=consultation)
        
        total = sum(item.quantite * item.produit.prix for item in lignes_commandes)
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Hospital Information
        hospital_name = "Your Hospital Name"
        hospital_address = "1234 Hospital St, City, Country"
        hospital_contact = "Phone: +1234567890"

        pdf.cell(200, 10, txt=hospital_name, ln=True, align='C')
        pdf.cell(200, 10, txt=hospital_address, ln=True, align='C')
        pdf.cell(200, 10, txt=hospital_contact, ln=True, align='C')
        
        pdf.ln(20)
        
        # Patient and Consultation Information
        pdf.cell(200, 10, txt=f"Patient: {consultation.patient.nom} {consultation.patient.postnom}", ln=True)
        pdf.cell(200, 10, txt=f"Consultation Date: {consultation.date}", ln=True)
        
        pdf.ln(10)

        # Items
        for item in lignes_commandes:
            pdf.cell(200, 10, txt=f"Product: {item.produit.libelle}, Price: {item.produit.prix} x {item.quantite} = {item.produit.prix * item.quantite}", ln=True)

        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Total: {total}", ln=True)

        pdf_output = io.BytesIO()
        pdf.output(pdf_output)

        pdf_output.seek(0)
        return FileResponse(pdf_output, as_attachment=True, filename='invoice.pdf')
