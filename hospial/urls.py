from django.urls import path
from .views import creer_facture, delete_facture, delete_ligne_facture, facture_detail, facture_list, generate_invoice_pdf
from .views import (
    MedicamentCreateView, MedicamentDeleteView, MedicamentDetailView, MedicamentListView, MedicamentUpdateView, PatientListView, PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView,
    ConsultationListView, ConsultationDetailView, ConsultationCreateView, ConsultationUpdateView, ConsultationDeleteView,
    TraitementListView, TraitementDetailView, TraitementCreateView, TraitementUpdateView, TraitementDeleteView,
    LigneCommandeListView, LigneCommandeDetailView, LigneCommandeCreateView, LigneCommandeUpdateView, LigneCommandeDeleteView,
    BeneficierListView, BeneficierDetailView, BeneficierCreateView, BeneficierUpdateView, BeneficierDeleteView,
    ChambreListView, ChambreDetailView, ChambreCreateView, ChambreUpdateView, ChambreDeleteView,
    CommandeListView, CommandeDetailView, CommandeCreateView, CommandeUpdateView, CommandeDeleteView,
    PlainteListView, PlainteDetailView, PlainteCreateView, PlainteUpdateView, PlainteDeleteView,
    LunetteListView, LunetteDetailView, LunetteCreateView, LunetteUpdateView, LunetteDeleteView,
    PrescriptionLunetteListView, PrescriptionLunetteDetailView, PrescriptionLunetteCreateView, PrescriptionLunetteUpdateView, PrescriptionLunetteDeleteView,
    PrescriptionMedicaleListView, PrescriptionMedicaleDetailView, PrescriptionMedicaleCreateView, PrescriptionMedicaleUpdateView, PrescriptionMedicaleDeleteView,
    ProduitListView, ProduitDetailView, ProduitCreateView, ProduitUpdateView, ProduitDeleteView,
    GradeMedListView, GradeMedDetailView, GradeMedCreateView, GradeMedUpdateView, GradeMedDeleteView,
    SoignantListView, SoignantDetailView, SoignantCreateView, SoignantUpdateView, SoignantDeleteView,
    InternerListView, InternerDetailView, InternerCreateView, InternerUpdateView, InternerDeleteView,
    ConsommerListView, ConsommerDetailView, ConsommerCreateView, ConsommerUpdateView, ConsommerDeleteView,
    DepenseListView, DepenseDetailView, DepenseCreateView, DepenseUpdateView, DepenseDeleteView
)


urlpatterns = [
    path('patients/', PatientListView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('patients/add/', PatientCreateView.as_view(), name='patient-add'),
    path('patients/<int:pk>/edit/', PatientUpdateView.as_view(), name='patient-edit'),
    path('patients/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient-delete'),

    path('medicaments/', MedicamentListView.as_view(), name='medicament-list'),
    path('medicaments/<int:pk>/', MedicamentDetailView.as_view(), name='medicament-detail'),
    path('medicaments/add/', MedicamentCreateView.as_view(), name='medicament-add'),
    path('medicaments/<int:pk>/edit/', MedicamentUpdateView.as_view(), name='medicament-edit'),
    path('medicaments/<int:pk>/delete/', MedicamentDeleteView.as_view(), name='medicament-delete'),

    path('consultations/', ConsultationListView.as_view(), name='consultation-list'),
    path('consultations/<int:pk>/', ConsultationDetailView.as_view(), name='consultation-detail'),
    path('consultations/add/', ConsultationCreateView.as_view(), name='consultation-add'),
    path('consultations/<int:pk>/edit/', ConsultationUpdateView.as_view(), name='consultation-edit'),
    path('consultations/<int:pk>/delete/', ConsultationDeleteView.as_view(), name='consultation-delete'),

    path('traitements/', TraitementListView.as_view(), name='traitement-list'),
    path('traitements/<int:pk>/', TraitementDetailView.as_view(), name='traitement-detail'),
    path('traitements/add/', TraitementCreateView.as_view(), name='traitement-add'),
    path('traitements/<int:pk>/edit/', TraitementUpdateView.as_view(), name='traitement-edit'),
    path('traitements/<int:pk>/delete/', TraitementDeleteView.as_view(), name='traitement-delete'),

    path('lignes_commandes/', LigneCommandeListView.as_view(), name='ligne_commande-list'),
    path('lignes_commandes/<int:pk>/', LigneCommandeDetailView.as_view(), name='ligne_commande-detail'),
    path('lignes_commandes/add/', LigneCommandeCreateView.as_view(), name='ligne_commande-add'),
    path('lignes_commandes/<int:pk>/edit/', LigneCommandeUpdateView.as_view(), name='ligne_commande-edit'),
    path('lignes_commandes/<int:pk>/delete/', LigneCommandeDeleteView.as_view(), name='ligne_commande-delete'),


    path('beneficiers/', BeneficierListView.as_view(), name='beneficier-list'),
    path('beneficiers/<int:pk>/', BeneficierDetailView.as_view(), name='beneficier-detail'),
    path('beneficiers/add/', BeneficierCreateView.as_view(), name='beneficier-add'),
    path('beneficiers/<int:pk>/edit/', BeneficierUpdateView.as_view(), name='beneficier-edit'),
    path('beneficiers/<int:pk>/delete/', BeneficierDeleteView.as_view(), name='beneficier-delete'),

    path('chambres/', ChambreListView.as_view(), name='chambre-list'),
    path('chambres/<int:pk>/', ChambreDetailView.as_view(), name='chambre-detail'),
    path('chambres/add/', ChambreCreateView.as_view(), name='chambre-add'),
    path('chambres/<int:pk>/edit/', ChambreUpdateView.as_view(), name='chambre-edit'),
    path('chambres/<int:pk>/delete/', ChambreDeleteView.as_view(), name='chambre-delete'),

    path('commandes/', CommandeListView.as_view(), name='commande-list'),
    path('commandes/<int:pk>/', CommandeDetailView.as_view(), name='commande-detail'),
    path('commandes/add/', CommandeCreateView.as_view(), name='commande-add'),
    path('commandes/<int:pk>/edit/', CommandeUpdateView.as_view(), name='commande-edit'),
    path('commandes/<int:pk>/delete/', CommandeDeleteView.as_view(), name='commande-delete'),


    path('plaintes/', PlainteListView.as_view(), name='plainte-list'),
    path('plaintes/<int:pk>/', PlainteDetailView.as_view(), name='plainte-detail'),
    path('plaintes/add/', PlainteCreateView.as_view(), name='plainte-add'),
    path('plaintes/<int:pk>/edit/', PlainteUpdateView.as_view(), name='plainte-edit'),
    path('plaintes/<int:pk>/delete/', PlainteDeleteView.as_view(), name='plainte-delete'),

    path('lunettes/', LunetteListView.as_view(), name='lunette-list'),
    path('lunettes/<int:pk>/', LunetteDetailView.as_view(), name='lunette-detail'),
    path('lunettes/add/', LunetteCreateView.as_view(), name='lunette-add'),
    path('lunettes/<int:pk>/edit/', LunetteUpdateView.as_view(), name='lunette-edit'),
    path('lunettes/<int:pk>/delete/', LunetteDeleteView.as_view(), name='lunette-delete'),


    path('prescriptions_lunettes/', PrescriptionLunetteListView.as_view(), name='prescription_lunette-list'),
    path('prescriptions_lunettes/<int:pk>/', PrescriptionLunetteDetailView.as_view(), name='prescription_lunette-detail'),
    path('prescriptions_lunettes/add/', PrescriptionLunetteCreateView.as_view(), name='prescription_lunette-add'),
    path('prescriptions_lunettes/<int:pk>/edit/', PrescriptionLunetteUpdateView.as_view(), name='prescription_lunette-edit'),
    path('prescriptions_lunettes/<int:pk>/delete/', PrescriptionLunetteDeleteView.as_view(), name='prescription_lunette-delete'),

    path('produits/', ProduitListView.as_view(), name='produit-list'),
    path('produits/<int:pk>/', ProduitDetailView.as_view(), name='produit-detail'),
    path('produits/add/', ProduitCreateView.as_view(), name='produit-add'),
    path('produits/<int:pk>/edit/', ProduitUpdateView.as_view(), name='produit-edit'),
    path('produits/<int:pk>/delete/', ProduitDeleteView.as_view(), name='produit-delete'),

    path('grades_med/', GradeMedListView.as_view(), name='grade_med-list'),
    path('grades_med/<int:pk>/', GradeMedDetailView.as_view(), name='grade_med-detail'),
    path('grades_med/add/', GradeMedCreateView.as_view(), name='grade_med-add'),
    path('grades_med/<int:pk>/edit/', GradeMedUpdateView.as_view(), name='grade_med-edit'),
    path('grades_med/<int:pk>/delete/', GradeMedDeleteView.as_view(), name='grade_med-delete'),

    path('soignants/', SoignantListView.as_view(), name='soignant-list'),
    path('soignants/<int:pk>/', SoignantDetailView.as_view(), name='soignant-detail'),
    path('soignants/add/', SoignantCreateView.as_view(), name='soignant-add'),
    path('soignants/<int:pk>/edit/', SoignantUpdateView.as_view(), name='soignant-edit'),
    path('soignants/<int:pk>/delete/', SoignantDeleteView.as_view(), name='soignant-delete'),

    path('interners/', InternerListView.as_view(), name='interner-list'),
    path('interners/<int:pk>/', InternerDetailView.as_view(), name='interner-detail'),
    path('interners/add/', InternerCreateView.as_view(), name='interner-add'),
    path('interners/<int:pk>/edit/', InternerUpdateView.as_view(), name='interner-edit'),
    path('interners/<int:pk>/delete/', InternerDeleteView.as_view(), name='interner-delete'),


    path('consommations/', ConsommerListView.as_view(), name='consommer-list'),
    path('consommations/<int:pk>/', ConsommerDetailView.as_view(), name='consommer-detail'),
    path('consommations/add/', ConsommerCreateView.as_view(), name='consommer-add'),
    path('consommations/<int:pk>/edit/', ConsommerUpdateView.as_view(), name='consommer-edit'),
    path('consommations/<int:pk>/delete/', ConsommerDeleteView.as_view(), name='consommer-delete'),

    path('depenses/', DepenseListView.as_view(), name='depense-list'),
    path('depenses/<int:pk>/', DepenseDetailView.as_view(), name='depense-detail'),
    path('depenses/add/', DepenseCreateView.as_view(), name='depense-add'),
    path('depenses/<int:pk>/edit/', DepenseUpdateView.as_view(), name='depense-edit'),
    path('depenses/<int:pk>/delete/', DepenseDeleteView.as_view(), name='depense-delete'),

    path('prescriptions_medicales/', PrescriptionMedicaleListView.as_view(), name='prescription_medicale-list'),
    path('prescriptions_medicales/<int:pk>/', PrescriptionMedicaleDetailView.as_view(), name='prescription_medicale-detail'),
    path('prescriptions_medicales/add/', PrescriptionMedicaleCreateView.as_view(), name='prescription_medicale-add'),
    path('prescriptions_medicales/<int:pk>/edit/', PrescriptionMedicaleUpdateView.as_view(), name='prescription_medicale-edit'),
    path('prescriptions_medicales/<int:pk>/delete/', PrescriptionMedicaleDeleteView.as_view(), name='prescription_medicale-delete'),



    path('factures/creer/<int:patient_id>/', creer_facture, name='creer_facture'),
    path('facture/<int:facture_id>/', facture_detail, name='facture_detail'),
    path('facture-à-imprimer/<int:invoice_id>/pdf/', generate_invoice_pdf, name='generate_invoice_pdf'),
    path('factures/', facture_list, name='facture_list'),
    path('facture/supprimer/<int:facture_id>/', delete_facture, name='delete_facture'),
    path('ligne_facture/supprimer/<int:ligne_facture_id>/', delete_ligne_facture, name='delete_ligne_facture')

]
