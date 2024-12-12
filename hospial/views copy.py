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





# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.units import mm
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfbase import pdfmetrics
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# from .models import Facture, Consultation
# import io
# from pathlib import Path

# def generate_invoice_pdf(request, invoice_id):
#     invoice = get_object_or_404(Facture, pk=invoice_id)
#     patient = invoice.patient
#     # Create PDF using reportlab
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'inline; filename="invoice-{invoice.pk}-{patient.nom}-{patient.postnom}.pdf"'

#     # Fonts
#     APTO_FONT = Path(BASE_DIR) / "static/assets/fonts/Aptos.ttf"
#     APTO_FONT_BOLD = Path(BASE_DIR) / "static/assets/fonts/Aptos-Bold.ttf"
#     pdfmetrics.registerFont(TTFont('Aptos', str(APTO_FONT)))
#     pdfmetrics.registerFont(TTFont('Aptos-Bold', str(APTO_FONT_BOLD)))

#     buffer = io.BytesIO()
#     p = canvas.Canvas(buffer, pagesize=A4)
#     p.setTitle(f"Facture #{invoice.pk}")

#     # Invoice header information
#     p.setFont("Aptos-Bold", 22)
#     p.drawString(20 * mm, 260 * mm, "Facture")
#     p.setFont("Aptos", 12)
#     p.drawString(20 * mm, 250 * mm, f"Facture ID: {invoice.pk}")
#     p.drawString(20 * mm, 240 * mm, f"Date: {invoice.date}")

#     # Add margin below Facture title
#     p.line(20 * mm, 238 * mm, 195 * mm, 238 * mm)

#     # Patient information
#     p.setFont("Aptos-Bold", 16)
#     p.drawString(20 * mm, 220 * mm, "Patient Information")
#     p.setFont("Aptos", 10)
#     p.drawString(20 * mm, 210 * mm, f"Name: {patient.nom} {patient.postnom} {patient.prenom}")
#     p.drawString(20 * mm, 200 * mm, f"Date of Birth: {patient.date_naissance.strftime('%Y-%m-%d')}")
#     p.drawString(20 * mm, 190 * mm, f"Phone Number: {patient.telephone}")

#     # Add margin below Patient Information title
#     p.line(20 * mm, 188 * mm, 195 * mm, 188 * mm)

#     # Space after phone number
#     p.drawString(20 * mm, 180 * mm, "")

#     # Service details
#     p.setFont("Aptos-Bold", 16)
#     p.drawString(20 * mm, 160 * mm, "Service Details")
#     p.setFont("Aptos", 10)
#     y_pos = 150 * mm

#     consultations = Consultation.objects.filter(patient=patient.pk)
#     for consultation in consultations:
#         p.drawString(20 * mm, y_pos, f"- Consultation (ID: {consultation.pk}) : {consultation.soignant.noms}")
#         y_pos -= 10 * mm

#     # Add margin below Service Details title
#     p.line(20 * mm, 138 * mm, 195 * mm, 138 * mm)

#     # Invoice summary
#     p.setFont("Aptos-Bold", 16)
#     p.drawString(20 * mm, 80 * mm, "Facture Summary")
#     p.setFont("Aptos", 10)
#     p.drawString(20 * mm, 70 * mm, f"Total Cost: ${invoice.total:.2f}")

#     # Add margin below Facture Summary title
#     p.line(20 * mm, 68 * mm, 195 * mm, 68 * mm)

#     # Space after total cost
#     p.drawString(20 * mm, 60 * mm, "")

#     # Draw lines
#     p.setStrokeColorRGB(0, 0, 0)  # Set line color to black
#     p.line(20 * mm, 190 * mm, 195 * mm, 190 * mm)  # Line under Patient Information
#     p.line(20 * mm, 150 * mm, 195 * mm, 150 * mm)  # Line under Service Details

#     # Save PDF content
#     p.showPage()
#     p.save()

#     # Get the value of the BytesIO buffer and write it to the response.
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     return response

# # Vue pour lister toutes les factures
# def facture_list(request):
#     factures = Facture.objects.all()
#     return render(request, 'factures/facture_list.html', {'factures': factures})






# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.units import mm
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfbase import pdfmetrics
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# from .models import Facture, Consultation
# import io
# from pathlib import Path

# def generate_invoice_pdf(request, invoice_id):
#     invoice = get_object_or_404(Facture, pk=invoice_id)
#     patient = invoice.patient
#     # Create PDF using reportlab
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'inline; filename="invoice-{invoice.pk}-{patient.nom}-{patient.postnom}.pdf"'

#     # Fonts
#     APTO_FONT = Path(BASE_DIR) / "static/assets/fonts/Aptos.ttf"
#     APTO_FONT_BOLD = Path(BASE_DIR) / "static/assets/fonts/Aptos-Bold.ttf"
#     pdfmetrics.registerFont(TTFont('Aptos', str(APTO_FONT)))
#     pdfmetrics.registerFont(TTFont('Aptos-Bold', str(APTO_FONT_BOLD)))

#     buffer = io.BytesIO()
#     p = canvas.Canvas(buffer, pagesize=A4)
#     p.setTitle(f"Facture #{invoice.pk}")

#     # Entête avec logo et informations de l'entreprise et du patient
#     logo_path = Path(BASE_DIR) / "static/assets/img/angular_gradient.png"
#     p.drawImage(str(logo_path), 20 * mm, 260 * mm, width=30 * mm, height=30 * mm)

#     p.setFont("Aptos-Bold", 12)
#     p.drawString(60 * mm, 280 * mm, "Nom de l'entreprise")
#     p.setFont("Aptos", 10)
#     p.drawString(60 * mm, 270 * mm, "Adresse de l'entreprise")
#     p.drawString(60 * mm, 260 * mm, "Téléphone : 01 23 45 67 89")
#     p.drawString(60 * mm, 250 * mm, "Email : contact@entreprise.com")

#     p.setFont("Aptos-Bold", 12)
#     p.drawString(120 * mm, 280 * mm, "Informations du Patient")
#     p.setFont("Aptos", 10)
#     p.drawString(120 * mm, 270 * mm, f"Nom: {patient.nom} {patient.postnom} {patient.prenom}")
#     p.drawString(120 * mm, 260 * mm, f"Date de Naissance: {patient.date_naissance.strftime('%Y-%m-%d')}")
#     p.drawString(120 * mm, 250 * mm, f"Téléphone: {patient.telephone}")

#     # Corps de la facture
#     p.setFont("Aptos-Bold", 16)
#     p.drawString(20 * mm, 220 * mm, "Détails des Consommables")
#     p.setFont("Aptos", 10)

#     y_pos = 210 * mm
#     p.drawString(20 * mm, y_pos, "Quantité")
#     p.drawString(60 * mm, y_pos, "Désignation")
#     p.drawString(120 * mm, y_pos, "PU")
#     p.drawString(160 * mm, y_pos, "PT")
#     y_pos -= 10 * mm

#     # Exemple de consommables (à remplacer par les données réelles)
#     consommables = [
#         {"quantité": 2, "désignation": "Produit A", "pu": 50, "pt": 100},
#         {"quantité": 1, "désignation": "Produit B", "pu": 80, "pt": 80},
#         {"quantité": 3, "désignation": "Produit C", "pu": 20, "pt": 60}
#     ]

#     for item in consommables:
#         p.drawString(20 * mm, y_pos, str(item["quantité"]))
#         p.drawString(60 * mm, y_pos, item["désignation"])
#         p.drawString(120 * mm, y_pos, f"${item['pu']:.2f}")
#         p.drawString(160 * mm, y_pos, f"${item['pt']:.2f}")
#         y_pos -= 10 * mm

#     total_general = sum(item["pt"] for item in consommables)
#     p.drawString(20 * mm, y_pos, "")
#     p.setFont("Aptos-Bold", 12)
#     p.drawString(120 * mm, y_pos, "Total Général :")
#     p.drawString(160 * mm, y_pos, f"${total_general:.2f}")

#     # Pied de page avec informations légales
#     p.setFont("Aptos", 8)
#     p.drawString(20 * mm, 30 * mm, "Informations légales de l'entreprise")
#     p.drawString(20 * mm, 20 * mm, "RCS : 123 456 789 | TVA : FR 12 345678901 | Adresse : 123 Rue Exemple, 75000 Paris")

#     # Save PDF content
#     p.showPage()
#     p.save()

#     # Get the value of the BytesIO buffer and write it to the response.
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     return response

# # Vue pour lister toutes les factures
# def facture_list(request):
#     factures = Facture.objects.all()
#     return render(request, 'factures/facture_list.html', {'factures': factures})






# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.units import mm
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfbase import pdfmetrics
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# from .models import Facture, LigneFacture
# import io
# from pathlib import Path

# def generate_invoice_pdf(request, invoice_id):
#     invoice = get_object_or_404(Facture, pk=invoice_id)
#     patient = invoice.patient
#     # Create PDF using reportlab
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'inline; filename="invoice-{invoice.pk}-{patient.nom}-{patient.postnom}.pdf"'

#     # Fonts
#     APTO_FONT = Path(BASE_DIR) / "static/assets/fonts/Aptos.ttf"
#     APTO_FONT_BOLD = Path(BASE_DIR) / "static/assets/fonts/Aptos-Bold.ttf"
#     pdfmetrics.registerFont(TTFont('Aptos', str(APTO_FONT)))
#     pdfmetrics.registerFont(TTFont('Aptos-Bold', str(APTO_FONT_BOLD)))

#     buffer = io.BytesIO()
#     p = canvas.Canvas(buffer, pagesize=A4)
#     p.setTitle(f"Facture #{invoice.pk}")

#     # Entête avec logo et informations de l'entreprise et du patient
#     logo_path = Path(BASE_DIR) / "static/assets/img/angular_gradient.png"
#     p.drawImage(str(logo_path), 20 * mm, 260 * mm, width=30 * mm, height=30 * mm)

#     p.setFont("Aptos-Bold", 12)
#     p.drawString(60 * mm, 280 * mm, "Nom de l'entreprise")
#     p.setFont("Aptos", 10)
#     p.drawString(60 * mm, 270 * mm, "Adresse de l'entreprise")
#     p.drawString(60 * mm, 260 * mm, "Téléphone : 01 23 45 67 89")
#     p.drawString(60 * mm, 250 * mm, "Email : contact@entreprise.com")

#     p.setFont("Aptos-Bold", 12)
#     p.drawString(120 * mm, 280 * mm, "Informations du Patient")
#     p.setFont("Aptos", 10)
#     p.drawString(120 * mm, 270 * mm, f"Nom: {patient.nom} {patient.postnom} {patient.prenom}")
#     p.drawString(120 * mm, 260 * mm, f"Date de Naissance: {patient.date_naissance.strftime('%Y-%m-%d')}")
#     p.drawString(120 * mm, 250 * mm, f"Téléphone: {patient.telephone}")
#     p.drawString(120 * mm, 240 * mm, f"Adresse: {patient.adresse_complete}")

#     # Corps de la facture
#     p.setFont("Aptos-Bold", 16)
#     p.drawString(20 * mm, 220 * mm, "Détails des Consommables")
#     p.setFont("Aptos", 10)

#     y_pos = 210 * mm
#     p.drawString(20 * mm, y_pos, "Quantité")
#     p.drawString(60 * mm, y_pos, "Désignation")
#     p.drawString(120 * mm, y_pos, "PU")
#     p.drawString(160 * mm, y_pos, "PT")
#     y_pos -= 10 * mm

#     # Récupérer les lignes de facture réelles
#     lignes_facture = LigneFacture.objects.filter(facture=invoice)
#     for ligne in lignes_facture:
#         p.drawString(20 * mm, y_pos, str(ligne.quantite))
#         # p.drawString(60 * mm, y_pos, ligne.produit.libelle)
#         p.drawString(120 * mm, y_pos, f"${ligne.produit.prix:.2f}")
#         p.drawString(160 * mm, y_pos, f"${ligne.total_cost():.2f}")
#         y_pos -= 10 * mm

#     p.drawString(20 * mm, y_pos, "")
#     p.setFont("Aptos-Bold", 12)
#     p.drawString(120 * mm, y_pos, "Total Général :")
#     p.drawString(160 * mm, y_pos, f"${invoice.total:.2f}")

#     # Pied de page avec informations légales
#     p.setFont("Aptos", 8)
#     p.drawString(20 * mm, 30 * mm, "Informations légales de l'entreprise")
#     p.drawString(20 * mm, 20 * mm, "RCS : 123 456 789 | TVA : FR 12 345678901 | Adresse : 123 Rue Exemple, 75000 Paris")

#     # Save PDF content
#     p.showPage()
#     p.save()

#     # Get the value of the BytesIO buffer and write it to the response.
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     return response

# # Vue pour lister toutes les factures
# def facture_list(request):
#     factures = Facture.objects.all()
#     return render(request, 'factures/facture_list.html', {'factures': factures})




# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.units import mm
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfbase import pdfmetrics
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# from .models import Facture, LigneFacture, Consultation, Interner, Consommer
# import io
# from pathlib import Path

# def generate_invoice_pdf(request, invoice_id):
#     invoice = get_object_or_404(Facture, pk=invoice_id)
#     patient = invoice.patient
#     # Create PDF using reportlab
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'inline; filename="invoice-{invoice.pk}-{patient.nom}-{patient.postnom}.pdf"'

#     # Fonts
#     APTO_FONT = Path(BASE_DIR) / "static/assets/fonts/Aptos.ttf"
#     APTO_FONT_BOLD = Path(BASE_DIR) / "static/assets/fonts/Aptos-Bold.ttf"
#     pdfmetrics.registerFont(TTFont('Aptos', str(APTO_FONT)))
#     pdfmetrics.registerFont(TTFont('Aptos-Bold', str(APTO_FONT_BOLD)))

#     buffer = io.BytesIO()
#     p = canvas.Canvas(buffer, pagesize=A4)
#     p.setTitle(f"Facture #{invoice.pk}")

#     # Entête avec logo et informations de l'entreprise et du patient
#     logo_path = Path(BASE_DIR) / "static/assets/img/angular_gradient.png"
#     p.drawImage(str(logo_path), 20 * mm, 260 * mm, width=30 * mm, height=30 * mm)

#     p.setFont("Aptos-Bold", 12)
#     p.drawString(60 * mm, 280 * mm, "Nom de l'entreprise")
#     p.setFont("Aptos", 10)
#     p.drawString(60 * mm, 270 * mm, "Adresse de l'entreprise")
#     p.drawString(60 * mm, 260 * mm, "Téléphone : 01 23 45 67 89")
#     p.drawString(60 * mm, 250 * mm, "Email : contact@entreprise.com")

#     p.setFont("Aptos-Bold", 12)
#     p.drawString(120 * mm, 280 * mm, "Informations du Patient")
#     p.setFont("Aptos", 10)
#     p.drawString(120 * mm, 270 * mm, f"Nom: {patient.nom} {patient.postnom} {patient.prenom}")
#     p.drawString(120 * mm, 260 * mm, f"Date de Naissance: {patient.date_naissance.strftime('%Y-%m-%d')}")
#     p.drawString(120 * mm, 250 * mm, f"Téléphone: {patient.telephone}")
#     p.drawString(120 * mm, 240 * mm, f"Adresse: {patient.adresse_complete}")

#     # Corps de la facture
#     y_pos = 220 * mm

#     # Consommables
#     p.setFont("Aptos-Bold", 16)
#     p.drawString(20 * mm, y_pos, "Détails des Consommables")
#     p.setFont("Aptos", 10)
#     y_pos -= 10 * mm

#     p.drawString(20 * mm, y_pos, "Quantité")
#     p.drawString(60 * mm, y_pos, "Désignation")
#     p.drawString(120 * mm, y_pos, "PU")
#     p.drawString(160 * mm, y_pos, "PT")
#     y_pos -= 10 * mm

#     lignes_facture = LigneFacture.objects.filter(facture=invoice)
#     for ligne in lignes_facture:
#         p.drawString(20 * mm, y_pos, str(ligne.quantite))
#         p.drawString(60 * mm, y_pos, ligne.produit.libelle)
#         p.drawString(120 * mm, y_pos, f"${ligne.produit.prix:.2f}")
#         p.drawString(160 * mm, y_pos, f"${ligne.total_cost():.2f}")
#         y_pos -= 10 * mm

#     # Consultations
#     p.setFont("Aptos-Bold", 16)
#     p.drawString(20 * mm, y_pos, "Consultations")
#     p.setFont("Aptos", 10)
#     y_pos -= 10 * mm

#     consultations = Consultation.objects.filter(patient=patient)
#     for consultation in consultations:
#         p.drawString(20 * mm, y_pos, f"Consultation ID: {consultation.pk}")
#         p.drawString(60 * mm, y_pos, f"Soignant: {consultation.soignant.noms}")
#         p.drawString(120 * mm, y_pos, f"Coût Total: ${consultation.total_cost():.2f}")
#         y_pos -= 10 * mm

#     # Internements
#     p.setFont("Aptos-Bold", 16)
#     p.drawString(20 * mm, y_pos, "Internements")
#     p.setFont("Aptos", 10)
#     y_pos -= 10 * mm

#     internements = Interner.objects.filter(patient=patient)
#     for internement in internements:
#         p.drawString(20 * mm, y_pos, f"Chambre: {internement.chambre.designation}")
#         p.drawString(60 * mm, y_pos, f"Date d'entrée: {internement.date_entree.strftime('%Y-%m-%d')}")
#         p.drawString(120 * mm, y_pos, f"Coût Total: ${internement.total_cost():.2f}")
#         y_pos -= 10 * mm

#     # Consommations de médicaments
#     p.setFont("Aptos-Bold", 16)
#     p.drawString(20 * mm, y_pos, "Consommations de Médicaments")
#     p.setFont("Aptos", 10)
#     y_pos -= 10 * mm

#     consommations = Consommer.objects.filter(patient=patient)
#     for consommation in consommations:
#         p.drawString(20 * mm, y_pos, f"Médicament: {consommation.medicament.libelle}")
#         p.drawString(60 * mm, y_pos, f"Quantité: {consommation.quantite}")
#         p.drawString(120 * mm, y_pos, f"Coût Total: ${consommation.quantite * consommation.medicament.prix:.2f}")
#         y_pos -= 10 * mm

#     # Calcul du coût total général
#     total_general = invoice.total + sum(consultation.total_cost() for consultation in consultations) + sum(internement.total_cost() for internement in internements) + sum(consommation.quantite * consommation.medicament.prix for consommation in consommations)
#     p.setFont("Aptos-Bold", 12)
#     p.drawString(120 * mm, y_pos, "Total Général :")
#     p.drawString(160 * mm, y_pos, f"${total_general:.2f}")

#     # Pied de page avec informations légales
#     p.setFont("Aptos", 8)
#     p.drawString(20 * mm, 30 * mm, "Informations légales de l'entreprise")
#     p.drawString(20 * mm, 20 * mm, "RCS : 123 456 789 | TVA : FR 12 345678901 | Adresse : 123 Rue Exemple, 75000 Paris")

#     # Save PDF content
#     p.showPage()
#     p.save()

#     # Get the value of the BytesIO buffer and write it to the response.
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     return response

# # Vue pour lister toutes les factures
# def facture_list(request):
#     factures = Facture.objects.all()
#     return render(request, 'factures/facture_list.html', {'factures': factures})




# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.units import mm
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfbase import pdfmetrics
# from reportlab.platypus import Table, TableStyle, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib import colors
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# from .models import Facture, LigneFacture, Consultation, Interner, Consommer
# import io
# from pathlib import Path

# def generate_invoice_pdf(request, invoice_id):
#     invoice = get_object_or_404(Facture, pk=invoice_id)
#     patient = invoice.patient
#     # Create PDF using reportlab
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'inline; filename="invoice-{invoice.pk}-{patient.nom}-{patient.postnom}.pdf"'

#     # Fonts
#     APTO_FONT = Path(BASE_DIR) / "static/assets/fonts/Aptos.ttf"
#     APTO_FONT_BOLD = Path(BASE_DIR) / "static/assets/fonts/Aptos-Bold.ttf"
#     pdfmetrics.registerFont(TTFont('Aptos', str(APTO_FONT)))
#     pdfmetrics.registerFont(TTFont('Aptos-Bold', str(APTO_FONT_BOLD)))

#     buffer = io.BytesIO()
#     p = canvas.Canvas(buffer, pagesize=A4)
#     p.setTitle(f"Facture #{invoice.pk}")

#     styles = getSampleStyleSheet()
#     normal_style = styles['Normal']
#     bold_style = styles['Heading3']

#     # Entête avec logo et informations de l'entreprise et du patient
#     logo_path = Path(BASE_DIR) / "static/assets/img/angular_gradient.png"
#     p.drawImage(str(logo_path), 20 * mm, 270 * mm, width=30 * mm, height=30 * mm)

#     p.setFont("Aptos-Bold", 12)
#     p.drawString(60 * mm, 270 * mm, "Nom de l'entreprise")
#     p.setFont("Aptos", 10)
#     p.drawString(60 * mm, 260 * mm, "Adresse de l'entreprise")
#     p.drawString(60 * mm, 250 * mm, "Téléphone : 01 23 45 67 89")
#     p.drawString(60 * mm, 240 * mm, "Email : contact@entreprise.com")

#     p.setFont("Aptos-Bold", 12)
#     p.drawString(120 * mm, 270 * mm, "Informations du Patient")
#     p.setFont("Aptos", 10)
#     p.drawString(120 * mm, 260 * mm, f"Nom: {patient.nom} {patient.postnom} {patient.prenom}")
#     p.drawString(120 * mm, 250 * mm, f"Date de Naissance: {patient.date_naissance.strftime('%Y-%m-%d')}")
#     p.drawString(120 * mm, 240 * mm, f"Téléphone: {patient.telephone}")
#     p.drawString(120 * mm, 230 * mm, f"Adresse: {patient.adresse_complete}")

#     y_pos = 200 * mm  # Ajustement de la position initiale de y

#     def draw_table(p, data, col_widths, y_pos):
#         table = Table(data, colWidths=col_widths)
#         table.setStyle(TableStyle([
#             ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#             ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#             ('FONTNAME', (0, 0), (-1, 0), 'Aptos-Bold'),
#             ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#             ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#             ('GRID', (0, 0), (-1, -1), 1, colors.black)
#         ]))
#         table.wrapOn(p, 30 * mm, y_pos)
#         table.drawOn(p, 30 * mm, y_pos)
#         return y_pos - table._height  # Retourne la nouvelle position y après avoir dessiné la table

#     # Consommables
#     consommables_data = [['Quantité', 'Désignation', 'PU', 'PT']]
#     lignes_facture = LigneFacture.objects.filter(facture=invoice)
#     for ligne in lignes_facture:
#         consommables_data.append([str(ligne.quantite), ligne.produit.libelle, f"${ligne.produit.prix:.2f}", f"${ligne.total_cost():.2f}"])

#     y_pos = draw_table(p, consommables_data, [40 * mm, 80 * mm, 50 * mm, 50 * mm], y_pos)
#     y_pos -= 20  # Espace entre les sections

#     # Consultations
#     consultations_data = [['Consultation ID', 'Soignant', 'Coût Total']]
#     consultations = Consultation.objects.filter(patient=patient)
#     for consultation in consultations:
#         consultations_data.append([consultation.pk, consultation.soignant.noms, f"${consultation.total_cost():.2f}"])

#     y_pos = draw_table(p, consultations_data, [60 * mm, 80 * mm, 60 * mm], y_pos)
#     y_pos -= 20  # Espace entre les sections

#     # Internements
#     internements_data = [['Chambre', 'Date d\'entrée', 'Coût Total']]
#     internements = Interner.objects.filter(patient=patient)
#     for internement in internements:
#         internements_data.append([internement.chambre.designation, internement.date_entree.strftime('%Y-%m-%d'), f"${internement.total_cost():.2f}"])

#     y_pos = draw_table(p, internements_data, [60 * mm, 80 * mm, 60 * mm], y_pos)
#     y_pos -= 20  # Espace entre les sections

#     # Consommations de médicaments
#     consommations_data = [['Médicament', 'Quantité', 'Coût Total']]
#     consommations = Consommer.objects.filter(patient=patient)
#     for consommation in consommations:
#         consommations_data.append([consommation.medicament.libelle, consommation.quantite, f"${consommation.quantite * consommation.medicament.prix:.2f}"])

#     y_pos = draw_table(p, consommations_data, [60 * mm, 60 * mm, 80 * mm], y_pos)
#     y_pos -= 20  # Espace entre les sections

#     # Calcul du coût total général
#     sous_total = invoice.total + sum(consultation.total_cost() for consultation in consultations) + sum(internement.total_cost() for internement in internements) + sum(consommation.quantite * consommation.medicament.prix for consommation in consommations)
#     tva = sous_total * 0.18  # TVA à 18%
#     total_general = sous_total + tva

#     p.setFont("Aptos-Bold", 12)
#     p.drawString(120 * mm, y_pos, "Sous-total :")
#     p.drawString(160 * mm, y_pos, f"${sous_total:.2f}")
#     y_pos -= 20

#     p.drawString(120 * mm, y_pos, "TVA (18%) :")
#     p.drawString(160 * mm, y_pos, f"${tva:.2f}")
#     y_pos -= 20

#     p.drawString(120 * mm, y_pos, "Total Général :")
#     p.drawString(160 * mm, y_pos, f"${total_general:.2f}")

#     # Pied de page avec informations légales
#     p.setFont("Aptos", 8)
#     p.drawString(20 * mm, 30 * mm, "Informations légales de l'entreprise")
#     p.drawString(20 * mm, 20 * mm, "RCS : 123 456 789 | TVA : FR 12 345678901 | Adresse : 123 Rue Exemple, 75000 Paris")

#     # Save PDF content
#     p.showPage()
#     p.save()

#     # Get the value of the BytesIO buffer and write it to the response.
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     return response

# # Vue pour lister toutes les factures
# def facture_list(request):
#     factures = Facture.objects.all()
#     return render(request, 'factures/facture_list.html', {'factures': factures})


