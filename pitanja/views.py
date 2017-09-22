from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.forms import formset_factory, modelformset_factory, inlineformset_factory

from . forms import (	Pitanje2_5Formset , Pitanje2_6Formset , Pitanje2_8Formset,
						Pitanje3_3Formset, Pitanje3_5Formset,
						Pitanje5_2Formset,  
						OrganizacijaOsnovniPodaciForma,	KadroviInfrastrukturaForma,Pitanje2_5Forma, Pitanje2_6Forma, Pitanje2_8Forma,
						ProstorniPodaciForma, Aneks1Forma, Aneks2Forma, Aneks3Forma, Pitanje3_1Forma, Pitanje3_2Forma, Pitanje3_3Forma,
						Pitanje3_4Forma, Pitanje3_5Forma, SaradnjaIzmedjuSubjekataForma,
						Pitanje4_7Forma, StandardizacijaOtvorenihPodatakaForma, Pitanje5_1Forma, Pitanje5_2Forma, Pitanje5_4Forma,
						Pitanje5_12Forma, Pitanje5_13Forma, Pitanje5_14Forma, SveobuhvatniModelForma
						
						)
from .models import (
						OrganizacijaOsnovniPodaci,	KadroviInfrastruktura,Pitanje2_5, Pitanje2_6, Pitanje2_8,
						ProstorniPodaci, Aneks1, Aneks2, Aneks3, Pitanje3_2, Pitanje3_3,
						Pitanje3_4, Pitanje3_5, ProstorniPodaci, SaradnjaIzmedjuSubjekata,
						Pitanje4_7, StandardizacijaOtvorenihPodataka, Pitanje5_1, Pitanje5_2, Pitanje5_4,
						Pitanje5_12, Pitanje5_13, Pitanje5_14, SveobuhvatniModel
				)
# Create your views here.
def home_page(request):
	return render(request, 'pitanja/home_page.html') 
	
def upitnik1(request):
	if request.method == "POST":
		form1 = OrganizacijaOsnovniPodaciForma(request.POST, prefix="form1")
		
		form2 = KadroviInfrastrukturaForma(request.POST, prefix="form2")
		form3 = Pitanje2_5Formset (request.POST, prefix = "pitanje2_5formset")
		form4 = Pitanje2_6Formset (request.POST, prefix = "pitanje2_6formset")
		form5 = Pitanje2_8Formset (request.POST, prefix = "pitanje2_8formset")
		
		form6 = ProstorniPodaciForma(request.POST, prefix="form6")
		form7 = Pitanje3_1Forma(request.POST, prefix="form7")
		form11 = Pitanje3_2Forma(request.POST, prefix="form11")
		form12 = Pitanje3_3Formset (request.POST, prefix = "pitanje3_3formset")
		form13 = Pitanje3_4Forma(request.POST, prefix="form13")
		form14 = Pitanje3_5Formset (request.POST, prefix = "pitanje3_5formset")
		
		form15 = SaradnjaIzmedjuSubjekataForma(request.POST, prefix="form15")
		form16 = Pitanje4_7Forma(request.POST, prefix="form15")
		
		form17 = StandardizacijaOtvorenihPodatakaForma(request.POST, prefix="form17")
		form18 = Pitanje5_1Forma(request.POST, prefix="form18")
		form19 = Pitanje5_2Formset (request.POST, prefix = "pitanje5_2formset")
		form20 = Pitanje5_4Forma(request.POST, prefix="form20")
		form21 = Pitanje5_12Forma(request.POST, prefix="form21")
		form22 = Pitanje5_13Forma(request.POST, prefix="form22")
		form23 = Pitanje5_14Forma(request.POST, prefix="form23")
		
		
		if (form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and
			form5.is_valid() and form6.is_valid() and form7.is_valid() and form11.is_valid() and form12.is_valid() and
			form13.is_valid() and form14.is_valid() and form15.is_valid() and form16.is_valid() and
			form7.is_valid() and form18.is_valid() and form19.is_valid() and form20.is_valid() and
			form21.is_valid() and form22.is_valid() and form23.is_valid()):
			
			#OrganizacijaOsnovniPodaci
			organizacija = form1.save(commit = False)
			organizacija.save()
			
			#KadrovInfrastruktura
			kadrovi_infrastruktura = form2.save(commit=False)
			for form in form3:
				kadrovi_infrastruktura.Koje_aplikacije_su_u_upotrebi_za_obradu = form.save()
			for form in form4:
				kadrovi_infrastruktura.Koji_sistemi_za_upravljanje_bazama_imate = form.save()
			for form in form5:
				kadrovi_infrastruktura.Mobilne_gis_aplikacije = form.save()
			kadrovi_infrastruktura.save()
			
			#ProstorniPodaci
			prostorni_podaci = form6.save(commit=False)
			prostorni_podaci.Za_koje_od_navedenih_INSPIRE_tema_proizvodite_podatke = form7.save()
			prostorni_podaci.Uneti_podatke_o_podacima_koje_vasa_organizacija_proizvodi  = form11.save()
			for form in form12:
				prostorni_podaci.Koje_prostorne_podatke_nabavljate_od_drugih = form.save()
			prostorni_podaci.Odrediti_vazne_podatke_od_drugih_organizacija_za_redovne_aktivnosti  = form13.save() 
			for form in form14:
				prostorni_podaci.Za_kojim_prostornim_podacima_imate_potrebu_a_koji_nisu_dostupni = form.save()
			prostorni_podaci.save() 

			#SaradnjaIzmedjuSubjekata 
			saradnja_subjekata =form15.save(commit=False)
			saradnja_subjekata.Uloga_nacionalnog_geoportala = form16.save()
			saradnja_subjekata.save() 

			#StandardizacijaOtvorenihPodataka
			standardizacija_podataka = form17.save(commit=False) 
			standardizacija_podataka.Status_standarda = form18.save()
			for form in form19:
				standardizacija_podataka.Standardi_iz_oblasti_geoinformacija  = form.save()
			standardizacija_podataka.Propis_prava_koriscenja  = form20.save()
			standardizacija_podataka.Prepreke_za_uspostavljanje_koncepta_gopodataka = form21.save()
			standardizacija_podataka.Vaznost_Prepreka = form22.save()
			standardizacija_podataka.Koliko_se_slazete_sa_tvrdnjama = form23.save()
			standardizacija_podataka.save()

			#SveobuhvatniModel 
			sveobuhvatni = SveobuhvatniModel(
					Prva_sekcija =  organizacija,
					Druga_sekcija = kadrovi_infrastruktura, 
					Treca_sekcija = prostorni_podaci,
					Cetvrta_sekcija = saradnja_subjekata, 
					Peta_sekcija = standardizacija_podataka
				
				)
			sveobuhvatni.save()
			return HttpResponse("All Forms are valid")
		else:
			return render(request, 'pitanja/upitnik1_forma.html', { 
											'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4,'form5': form5,
											'form6': form6,'form7': form7, 
											'form11': form11,'form12': form12, 'form13': form13, 'form14': form14,
											'form15': form15, 'form16': form16,
											'form17': form17, 'form18': form18, 'form19': form19, 'form20': form20,'form21': form21,
											'form22': form22,'form23': form23
											}) 
	else:
		#******************************************Prva Sekcija Osnovni Podaci*************************************************************#
		form1 = OrganizacijaOsnovniPodaciForma(prefix="form1")
		#******************************************Druga Sekcija KadroviInfrastruktura*************************************************************#
		form2 = KadroviInfrastrukturaForma(prefix="form2")
		form3=  Pitanje2_5Formset (prefix = "pitanje2_5formset", queryset=Pitanje2_5.objects.none())
		form4 = Pitanje2_6Formset (prefix = "pitanje2_6formset", queryset=Pitanje2_6.objects.none())
		form5 = Pitanje2_8Formset (prefix = "pitanje2_8formset", queryset=Pitanje2_8.objects.none())
		
		#***************************************************Prostorni Podaci****************************************************************#
		form6 = ProstorniPodaciForma(prefix="form6")
		form7 = Pitanje3_1Forma(prefix="form7")
		form11 = Pitanje3_2Forma(prefix="form11")
		form12 = Pitanje3_3Formset (prefix = "pitanje3_3formset", queryset=Pitanje3_3.objects.none())
		form13 = Pitanje3_4Forma(prefix="form13")
		form14 = Pitanje3_5Formset (prefix = "pitanje3_5formset", queryset=Pitanje3_5.objects.none())
		
		#***************************************************Saradnja Izmedju Subjekata NIGIP-a****************************************************************#
		form15 = SaradnjaIzmedjuSubjekataForma(prefix="form15")
		form16 = Pitanje4_7Forma(prefix="form16")
		
		#***************************************************Standardizacija i koncept otvorenih podataka****************************************************************#
		form17 = StandardizacijaOtvorenihPodatakaForma(prefix="form17")
		form18 = Pitanje5_1Forma(prefix="form18")
		
		form19 = Pitanje5_2Formset (prefix = "pitanje5_2formset", queryset=Pitanje5_2.objects.none())
		form20 = Pitanje5_4Forma(prefix="form20")
		form21 = Pitanje5_12Forma(prefix="form21")
		form22 = Pitanje5_13Forma(prefix="form22")
		form23 = Pitanje5_14Forma(prefix="form23")
		
		form24 = SveobuhvatniModelForma(prefix="form24")

		return render(request, 'pitanja/upitnik1_forma.html', {
											'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4,'form5': form5,
											'form6': form6,'form7': form7, 
											'form11': form11,'form12': form12, 'form13': form13, 'form14': form14,
											'form15': form15, 'form16': form16,
											'form17': form17, 'form18': form18, 'form19': form19, 'form20': form20,'form21': form21,
											'form22': form22,'form23': form23, 'form24': form24
											}) 

def manual_forma(request):
	if request.method == "POST":
		form1 = OrganizacijaOsnovniPodaciForma(request.POST, prefix="form1")
		
		form2 = KadroviInfrastrukturaForma(request.POST, prefix="form2")
		form3 = Pitanje2_5Forma(request.POST, prefix="form3")
		form4 = Pitanje2_6Forma(request.POST, prefix="form4")
		form5 = Pitanje2_8Forma(request.POST, prefix="form5")
		
		form6 = ProstorniPodaciForma(request.POST, prefix="form6")
		form7 = Pitanje3_1Forma(request.POST, prefix="form7")
		
		form11 = Pitanje3_2Forma(request.POST, prefix="form11")
		form12 = Pitanje3_3Forma(request.POST, prefix="form12")
		form13 = Pitanje3_4Forma(request.POST, prefix="form13")
		form14 = Pitanje3_5Forma(request.POST, prefix="form14")
		
		form15 = SaradnjaIzmedjuSubjekataForma(request.POST, prefix="form15")
		form16 = Pitanje4_7Forma(request.POST, prefix="form15")
		
		form17 = StandardizacijaOtvorenihPodatakaForma(request.POST, prefix="form17")
		form18 = Pitanje5_1Forma(request.POST, prefix="form18")
		form19 = Pitanje5_2Forma(request.POST, prefix="form19")
		form20 = Pitanje5_4Forma(request.POST, prefix="form20")
		form21 = Pitanje5_12Forma(request.POST, prefix="form21")
		form22 = Pitanje5_13Forma(request.POST, prefix="form22")
		form23 = Pitanje5_14Forma(request.POST, prefix="form23")
		form24 = SveobuhvatniModelForma(request.POST)
		
		if (form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and
			form5.is_valid() and form6.is_valid() and form7.is_valid() and form11.is_valid() and form12.is_valid() and
			form13.is_valid() and form14.is_valid() and form15.is_valid() and form16.is_valid() and
			form7.is_valid() and form18.is_valid() and form19.is_valid() and form20.is_valid() and
			form21.is_valid() and form22.is_valid() and form23.is_valid()):
			
			#form1.save()
			
			kadrovi_infrastruktura = form2.save(commit=False)
			kadrovi_infrastruktura.Koje_aplikacije_su_u_upotrebi_za_obradu = form3.save()
			kadrovi_infrastruktura.Koji_sistemi_za_upravljanje_bazama_imate = form4.save()
			kadrovi_infrastruktura.Mobilne_gis_aplikacije = form5.save()
			#kadrovi_infrastruktura.save()
			
			prostorni_podaci = form6.save(commit=False)
			prostorni_podaci.Za_koje_od_navedenih_INSPIRE_tema_proizvodite_podatke = form7.save()
			prostorni_podaci.Uneti_podatke_o_podacima_koje_vasa_organizacija_proizvodi  = form11.save()
			prostorni_podaci.Koje_prostorne_podatke_nabavljate_od_drugih = form12.save()
			prostorni_podaci.Odrediti_vazne_podatke_od_drugih_organizacija_za_redovne_aktivnosti  = form13.save() 
			prostorni_podaci.Za_kojim_prostornim_podacima_imate_potrebu_a_koji_nisu_dostupni = form14.save()
			#prostorni_podaci.save() 
			
			saradnja_subjekata =form15.save(commit=False)
			saradnja_subjekata.Uloga_nacionalnog_geoportala = form16.save()
			#saradnja_subjekata.save() 
			
			standardizacija_podataka = form17.save(commit=False) 
			standardizacija_podataka.Status_standarda = form18.save()
			standardizacija_podataka.Standardi_iz_oblasti_geoinformacija  = form19.save()
			standardizacija_podataka.Propis_prava_koriscenja  = form20.save()
			standardizacija_podataka.Prepreke_za_uspostavljanje_koncepta_gopodataka = form21.save()
			standardizacija_podataka.Vaznost_Prepreka = form22.save()
			standardizacija_podataka.Koliko_se_slazete_sa_tvrdnjama = form23.save()
			#standardizacija_podataka.save()

			sveobuhvatni = form24.save(commit = False)
			sveobuhvatni.Prva_sekcija = form1.save()
			sveobuhvatni.Druga_sekcija = kadrovi_infrastruktura.save()
			sveobuhvatni.Treca_sekcija = prostorni_podaci.save()
			sveobuhvatni.Cetvrta_sekcija = saradnja_subjekata.save() 
			sveobuhvatni.Peta_sekcija = standardizacija_podataka.save()
			sveobuhvatni.save()
			
			return HttpResponse("Uspesno ste snimili formu")
		else:
			return render(request, 'pitanja/upitnik1_forma.html', {
											'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4,'form5': form5,
											'form6': form6,'form7': form7, 
											'form11': form11,'form12': form12, 'form13': form13, 'form14': form14,
											'form15': form15, 'form16': form16,
											'form17': form17, 'form18': form18, 'form19': form19, 'form20': form20,'form21': form21,
											'form22': form22,'form23': form23, 'form24': form24
											}) 
		
	else:
	#******************************************Prva Sekcija Osnovni Podaci*************************************************************#
		#******************************************Prva Sekcija Osnovni Podaci*************************************************************#
		form1 = OrganizacijaOsnovniPodaciForma(prefix="form1")
		#******************************************Druga Sekcija KadroviInfrastruktura*************************************************************#
		form2 = KadroviInfrastrukturaForma(prefix="form2")
		'''form3 = Pitanje2_5Forma(prefix="form3") #Pitanje2_5
		form4 = Pitanje2_6Forma(prefix="form4") #Pitanje2_6
		form5 = Pitanje2_8Forma(prefix="form5") #Pitanje2_8'''
		pitanje2_5formset = Pitanje2_5Formset (prefix = "pitanje2_5formset", data = {'pitanje2_5formset-TOTAL_FORMS': 1,'pitanje2_5formset-INITIAL_FORMS': '0','pitanje2_5formset-MAX_NUM_FORMS': '10'})
		pitanje2_6formset = Pitanje2_6Formset (prefix = "pitanje2_6formset", data = {'pitanje2_6formset-TOTAL_FORMS': 1,'pitanje2_6formset-INITIAL_FORMS': '0','pitanje2_6formset-MAX_NUM_FORMS': '10'})
		pitanje2_8formset = Pitanje2_8Formset (prefix = "pitanje2_8formset", data = {'pitanje2_8formset-TOTAL_FORMS': 1,'pitanje2_8formset-INITIAL_FORMS': '0','pitanje2_8formset-MAX_NUM_FORMS': '10'})
		#***************************************************Prostorni Podaci****************************************************************#
		form6 = ProstorniPodaciForma(prefix="form6")
		form7 = Pitanje3_1Forma(prefix="form7") #Pitanje3_1
		
		form11 = Pitanje3_2Forma(prefix="form11")
		form12 = Pitanje3_3Forma(prefix="form12")
		form13 = Pitanje3_4Forma(prefix="form13")
		form14 = Pitanje3_5Forma(prefix="form14")
		
		#***************************************************Saradnja Izmedju Subjekata NIGIP-a****************************************************************#
		form15 = SaradnjaIzmedjuSubjekataForma(prefix="form15")
		form16 = Pitanje4_7Forma(prefix="form16")
		
		#***************************************************Standardizacija i koncept otvorenih podataka****************************************************************#
		form17 = StandardizacijaOtvorenihPodatakaForma(prefix="form17")
		form18 = Pitanje5_1Forma(prefix="form18")
		form19 = Pitanje5_2Forma(prefix="form19")
		form20 = Pitanje5_4Forma(prefix="form20")
		form21 = Pitanje5_12Forma(prefix="form21")
		form22 = Pitanje5_13Forma(prefix="form22")
		form23 = Pitanje5_14Forma(prefix="form23")
		
		form24 = SveobuhvatniModelForma()
		return render(request, 'pitanja/upitnik1_forma.html', {
											'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4,'form5': form5,
											'form6': form6,'form7': form7, 
											'form11': form11,'form12': form12, 'form13': form13, 'form14': form14,
											'form15': form15, 'form16': form16,
											'form17': form17, 'form18': form18, 'form19': form19, 'form20': form20,'form21': form21,
											'form22': form22,'form23': form23, 'form24': form24
											}) 


































		





#********************************************** Family formset View *****************************************#
def family(request):
	if request.POST:
		kadrovi_forma = KadroviInfrastrukturaForma(request.POST, prefix = "kadrovi_forma")
		pitanje2_5formset = Pitanje2_5Formset (request.POST, prefix = "pitanje2_5formset")
		pitanje2_6formset = Pitanje2_6Formset (request.POST, prefix = "pitanje2_6formset")
		pitanje2_8formset = Pitanje2_8Formset (request.POST, prefix = "pitanje2_8formset")

		pitanje3_3formset = Pitanje3_3Formset (request.POST, prefix = "pitanje3_3formset")
		pitanje3_5formset = Pitanje3_5Formset (request.POST, prefix = "pitanje3_5formset")
		pitanje5_2formset = Pitanje5_2Formset (request.POST, prefix = "pitanje5_2formset")
		
		
		
		if (
			pitanje2_5formset.is_valid() and pitanje2_6formset.is_valid() and pitanje2_8formset.is_valid() and
			kadrovi_forma.is_valid() and 
			pitanje3_3formset.is_valid() and pitanje3_5formset.is_valid() and pitanje5_2formset.is_valid()
			
		):	
			'''data = request.POST

			return HttpResponse(data.items())'''
			kadrovi = kadrovi_forma.save(commit=False)
			
			for form in pitanje2_5formset:
				print("Data from form2_5\t",form.cleaned_data)
				kadrovi.Koje_aplikacije_su_u_upotrebi_za_obradu = form.save()
			for form in pitanje2_6formset:
				kadrovi.Koji_sistemi_za_upravljanje_bazama_imate = form.save()
				print("Data from form2_6\t",form.cleaned_data)
			for form in pitanje2_8formset:
				kadrovi.Mobilne_gis_aplikacije = form.save()
				print("Data from form2_8\t",form.cleaned_data)
					
			kadrovi.save()
			
			
			
			return HttpResponse("Its Valid")
		
		else:
			
			context = {

				'kadrovi_forma': kadrovi_forma,
				'pitanje2_5formset': pitanje2_5formset,
				'pitanje2_6formset' : pitanje2_6formset,
				'pitanje2_8formset' : pitanje2_8formset,
				
				'pitanje3_3formset' : pitanje3_3formset,
				'pitanje3_5formset' : pitanje3_5formset,
				'pitanje5_2formset' : pitanje5_2formset,
				
			}
			return render(request, 'pitanja/formset_family.html', context)

	else:
		kadrovi_forma = KadroviInfrastrukturaForma(prefix = "kadrovi_forma")
		pitanje2_5formset = Pitanje2_5Formset (prefix = "pitanje2_5formset", queryset=Pitanje2_5.objects.none())
		pitanje2_6formset = Pitanje2_6Formset (prefix = "pitanje2_6formset", queryset=Pitanje2_6.objects.none())
		pitanje2_8formset = Pitanje2_8Formset (prefix = "pitanje2_8formset", queryset=Pitanje2_8.objects.none())

		pitanje3_3formset = Pitanje3_3Formset (prefix = "pitanje3_3formset", queryset=Pitanje3_3.objects.none())
		pitanje3_5formset = Pitanje3_5Formset (prefix = "pitanje3_5formset", queryset=Pitanje3_5.objects.none())
		pitanje5_2formset = Pitanje5_2Formset (prefix = "pitanje5_2formset", queryset=Pitanje5_2.objects.none())
		
		context = {
				'kadrovi_forma': kadrovi_forma,
				'pitanje2_5formset': pitanje2_5formset,
				'pitanje2_6formset' : pitanje2_6formset,
				'pitanje2_8formset' : pitanje2_8formset,

				'pitanje3_3formset' : pitanje3_3formset,
				'pitanje3_5formset' : pitanje3_5formset,
				'pitanje5_2formset' : pitanje5_2formset,
				
		}

		return render(request, 'pitanja/formset_family.html', context)




################################################################## Raw Upitnik ############################################################################################################################################
def raw_upitnik(request):	
	if request.POST:
    	#OrganizacijaOsnovniPodaci	
		form1 = OrganizacijaOsnovniPodaciForma(request.POST, prefix="form1")
		
		#KadrovInfrastruktura
		form2 = KadroviInfrastrukturaForma(request.POST, prefix="form2")
		form3 = Pitanje2_5Formset (request.POST, prefix = "pitanje2_5formset")
		form4 = Pitanje2_6Formset (request.POST, prefix = "pitanje2_6formset")
		form5 = Pitanje2_8Formset (request.POST, prefix = "pitanje2_8formset")
		#ProstorniPodaci
		form6 = ProstorniPodaciForma(request.POST, prefix="form6")
		form7 = Pitanje3_1Forma(request.POST, prefix="form7") 
		form11 = Pitanje3_2Forma(request.POST, prefix="form11")
		form12 = Pitanje3_3Formset (request.POST, prefix = "pitanje3_3formset")
		form13 = Pitanje3_4Forma(request.POST, prefix="form13")
		form14 = Pitanje3_5Formset (request.POST, prefix = "pitanje3_5formset")

		#SaradnjaIzmedjuSubjekata
		form15 = SaradnjaIzmedjuSubjekataForma(request.POST, prefix="form15")
		form16 = Pitanje4_7Forma(request.POST, prefix="form16")

		#StandardizacijaOtvorenihPodataka
		form17 = StandardizacijaOtvorenihPodatakaForma(request.POST, prefix="form17")
		form18 = Pitanje5_1Forma(request.POST, prefix="form18")
		form19 = Pitanje5_2Formset (request.POST, prefix = "pitanje5_2formset")
		form20 = Pitanje5_4Forma(request.POST, prefix="form20")
		form21 = Pitanje5_12Forma(request.POST, prefix="form21")
		form22 = Pitanje5_13Forma(request.POST, prefix="form22")
		form23 = Pitanje5_14Forma(request.POST, prefix="form23")

		
		
		if(
			form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and 
			form6.is_valid() and form7.is_valid() and form11.is_valid() and form12.is_valid() and form13.is_valid() and 
			form14.is_valid() and form15.is_valid() and form16.is_valid() and 
			form17.is_valid() and form18.is_valid() and form19.is_valid() and 
			form20.is_valid() and form21.is_valid() and form22.is_valid() and form23.is_valid()

		):
			
			try:
				print(request.POST)
			except UnicodeEncodeError as e:
				print("Greska u nucodu je ", e)
			print("Validacija prosla")
			
			#OrganizacijaOsnovniPodaci
			organizacija = form1.save(commit = False)
			organizacija.save()
			
			#KadrovInfrastruktura
			kadrovi_infrastruktura = form2.save(commit=False)
			for form in form3:
				kadrovi_infrastruktura.Koje_aplikacije_su_u_upotrebi_za_obradu = form.save()
			for form in form4:
				kadrovi_infrastruktura.Koji_sistemi_za_upravljanje_bazama_imate = form.save()
			for form in form5:
				kadrovi_infrastruktura.Mobilne_gis_aplikacije = form.save()
			kadrovi_infrastruktura.save()
			
			#ProstorniPodaci
			prostorni_podaci = form6.save(commit=False)
			prostorni_podaci.Za_koje_od_navedenih_INSPIRE_tema_proizvodite_podatke = form7.save()
			prostorni_podaci.Uneti_podatke_o_podacima_koje_vasa_organizacija_proizvodi  = form11.save()
			for form in form12:
				prostorni_podaci.Koje_prostorne_podatke_nabavljate_od_drugih = form.save()
			prostorni_podaci.Odrediti_vazne_podatke_od_drugih_organizacija_za_redovne_aktivnosti  = form13.save() 
			for form in form14:
				prostorni_podaci.Za_kojim_prostornim_podacima_imate_potrebu_a_koji_nisu_dostupni = form.save()
			prostorni_podaci.save() 

			#SaradnjaIzmedjuSubjekata 
			saradnja_subjekata =form15.save(commit=False)
			saradnja_subjekata.Uloga_nacionalnog_geoportala = form16.save()
			saradnja_subjekata.save() 

			#StandardizacijaOtvorenihPodataka
			standardizacija_podataka = form17.save(commit=False) 
			standardizacija_podataka.Status_standarda = form18.save()
			for form in form19:
				standardizacija_podataka.Standardi_iz_oblasti_geoinformacija  = form.save()
			standardizacija_podataka.Propis_prava_koriscenja  = form20.save()
			standardizacija_podataka.Prepreke_za_uspostavljanje_koncepta_gopodataka = form21.save()
			standardizacija_podataka.Vaznost_Prepreka = form22.save()
			standardizacija_podataka.Koliko_se_slazete_sa_tvrdnjama = form23.save()
			standardizacija_podataka.save()

			#SveobuhvatniModel 
			sveobuhvatni = SveobuhvatniModel(
					Prva_sekcija =  organizacija,
					Druga_sekcija = kadrovi_infrastruktura, 
					Treca_sekcija = prostorni_podaci,
					Cetvrta_sekcija = saradnja_subjekata, 
					Peta_sekcija = standardizacija_podataka
				
				)
			sveobuhvatni.save()
			return HttpResponseRedirect("http://nigp.usg-grf.rs/Zavrsna/Zavrsna.html")
		else:			
			print("Validacija formi nije prosla")
			print( "Validacija 1", form1.is_valid() )
			print( "Validacija 2", form2.is_valid() )
			print( "Validacija 3", form3.is_valid() )
			print( "Validacija 4", form4.is_valid() )
			print( "Validacija 5", form5.is_valid() )
			print( "Validacija 6", form6.is_valid() )
			print( "Validacija 7", form7.is_valid() )
			print( "Validacija 11", form11.is_valid() )
			print( "Validacija 12", form12.is_valid() )
			print( "Validacija 13", form13.is_valid() )

			print( "Validacija 14", form14.is_valid() )
			print( "Validacija 15", form15.is_valid() )
			print( "Validacija 16", form16.is_valid() )
			print( "Validacija 17", form17.is_valid() )
			print( "Validacija 18", form18.is_valid() )
			print( "Validacija 19", form19.is_valid() )
			print( "Validacija 20", form20.is_valid() )
			print( "Validacija 21", form21.is_valid() )
			print( "Validacija 22", form22.is_valid() )
			print( "Validacija 23", form23.is_valid() )
			
			return render(request, 'pitanja/upitnik1_forma_raw.html', {
											'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4,'form5': form5,
											'form6': form6,'form7': form7, 
											'form11': form11,'form12': form12, 'form13': form13, 'form14': form14,
											'form15': form15, 'form16': form16,
											'form17': form17, 'form18': form18, 'form19': form19, 'form20': form20,'form21': form21,
											'form22': form22,'form23': form23
											}) 

	else:
    	#******************************************Prva Sekcija Osnovni Podaci*************************************************************#
		form1 = OrganizacijaOsnovniPodaciForma(prefix="form1")

		#******************************************Druga Sekcija KadroviInfrastruktura*************************************************************#
		form2 = KadroviInfrastrukturaForma(prefix="form2")
		
		#form3 = Pitanje2_5Forma(prefix="form3") #Pitanje2_5
		#form4 = Pitanje2_6Forma(prefix="form4") #Pitanje2_6
		#form5 = Pitanje2_8Forma(prefix="form5") #Pitanje2_8'''
		form3 = Pitanje2_5Formset (prefix = "pitanje2_5formset", queryset=Pitanje2_5.objects.none())
		form4 = Pitanje2_6Formset (prefix = "pitanje2_6formset", queryset=Pitanje2_6.objects.none())
		form5 = Pitanje2_8Formset (prefix = "pitanje2_8formset", queryset=Pitanje2_8.objects.none())
		
		#***************************************************Prostorni Podaci****************************************************************#
		form6 = ProstorniPodaciForma(prefix="form6")
		form7 = Pitanje3_1Forma(prefix="form7") #Pitanje3_1
		
		form11 = Pitanje3_2Forma(prefix="form11")
		#form12 = Pitanje3_3Forma(prefix="form12")
		form12 =  Pitanje3_3Formset (prefix = "pitanje3_3formset", queryset=Pitanje3_3.objects.none())
		form13 = Pitanje3_4Forma(prefix="form13")
		#form14 = Pitanje3_5Forma(prefix="form14")
		form14 =  Pitanje3_5Formset (prefix = "pitanje3_5formset", queryset=Pitanje3_5.objects.none())
		
		#***************************************************Saradnja Izmedju Subjekata NIGIP-a****************************************************************#
		form15 = SaradnjaIzmedjuSubjekataForma(prefix="form15")
		form16 = Pitanje4_7Forma(prefix="form16")
		
		#***************************************************Standardizacija i koncept otvorenih podataka****************************************************************#
		form17 = StandardizacijaOtvorenihPodatakaForma(prefix="form17")
		form18 = Pitanje5_1Forma(prefix="form18")
		#form19 = Pitanje5_2Forma(prefix="form19")
		form19 =  Pitanje5_2Formset (prefix = "pitanje5_2formset", queryset=Pitanje5_2.objects.none())

		form20 = Pitanje5_4Forma(prefix="form20")
		form21 = Pitanje5_12Forma(prefix="form21")
		form22 = Pitanje5_13Forma(prefix="form22")
		form23 = Pitanje5_14Forma(prefix="form23")
		
		form24 = SveobuhvatniModelForma(prefix="form24")
		
		return render(request, 'pitanja/upitnik1_forma_raw.html', {
											'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4,'form5': form5,
											'form6': form6,'form7': form7, 
											'form11': form11,'form12': form12, 'form13': form13, 'form14': form14,
											'form15': form15, 'form16': form16,
											'form17': form17, 'form18': form18, 'form19': form19, 'form20': form20,'form21': form21,
											'form22': form22,'form23': form23
											}) 


#*********************************************** Pojedinacne Forme View-s *********************************# 

#******************************************Prva Sekcija Osnovni Podaci*************************************************************#
#Forma1 OrganizacijaOsnovniPodaciForma
def proces_form1_OrganizacijaOsnovniPodaciForma(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form1 = OrganizacijaOsnovniPodaciForma(prefix="form1") 
		context = {'form1': form1}
		return render(request, 'pitanja/pojedinacne_forme/form1_OrganizacijaOsnovniPodaciForma.html',context)

#******************************************Druga Sekcija KadroviInfrastruktura*************************************************************#
#Forma2 form2_KadroviInfrastrukturaForma
def proces_form2_KadroviInfrastrukturaForma(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form2 = KadroviInfrastrukturaForma(prefix="form2")
		context = {'form2': form2}
		return render(request, 'pitanja/pojedinacne_forme/form2_KadroviInfrastrukturaForma.html',context)

#Forma3 form3_pitanje2_5Forma
def proces_form3_Pitanje2_5Formset(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form3 = Pitanje2_5Formset (prefix = "pitanje2_5formset", queryset=Pitanje2_5.objects.none())
		context = {'form3': form3}
		return render(request, 'pitanja/pojedinacne_forme/form3_Pitanje2_5Formset.html',context) 

#Forma4 form4_Pitanje2_6Formset
def proces_form4_Pitanje2_6Formset(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form4 = Pitanje2_6Formset (prefix = "pitanje2_6formset", queryset=Pitanje2_6.objects.none())
		context = {'form4': form4}
		return render(request, 'pitanja/pojedinacne_forme/form4_Pitanje2_6Formset.html',context) 

#Forma5 form5_Pitanje2_8Formset
def proces_form5_Pitanje2_8Formset(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form5 = Pitanje2_8Formset (prefix = "pitanje2_8formset", queryset=Pitanje2_8.objects.none())
		context = {'form5': form5}
		return render(request, 'pitanja/pojedinacne_forme/form5_Pitanje2_8Formset.html',context)  

#***************************************************Prostorni Podaci****************************************************************#
#Forma6 form6_ProstorniPodaciForma
def proces_form6_ProstorniPodaciForma(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form6 = ProstorniPodaciForma(prefix="form6")
		context = {'form6': form6}
		return render(request, 'pitanja/pojedinacne_forme/form6_ProstorniPodaciForma.html',context)

#Forma7 form7_Pitanje3_1Forma
def proces_form7_Pitanje3_1Forma(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form7 = Pitanje3_1Forma(prefix="form7")
		context = {'form7': form7}
		return render(request, 'pitanja/pojedinacne_forme/form7_Pitanje3_1Forma.html',context)

#Forma11 form11_Pitanje3_2Forma
def proces_form11_Pitanje3_2Forma(request):
	if request.POST:
		print("Processing Form 3_2 Pitanje")
		d = {};
		for i in request.POST:
    			d[i] = request.POST[i]
		form11 = Pitanje3_2Forma(request.POST, prefix="form11")
		if form11.is_valid():
			form11.save()
			print("Forma je snimljena")
			return HttpResponse([(i,d[i]) for i in d])
			#return HttpResponseRedirect(reverse('pitanja:Pitanje3_2Forma'))
		else:
    			return HttpResponse("Error, Forms Is not valid")
	else:
		form11 = Pitanje3_2Forma(prefix="form11")
		context = {'form11': form11}
		return render(request, 'pitanja/pojedinacne_forme/form11_Pitanje3_2Forma.html',context)    
    
#Forma12 form12_Pitanje3_3Formset
def proces_form12_Pitanje3_3Formset(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form12 =  Pitanje3_3Formset (prefix = "pitanje3_3formset", queryset=Pitanje3_3.objects.none())
		context = {'form12': form12}
		return render(request, 'pitanja/pojedinacne_forme/form12_Pitanje3_3Formset.html',context)    

#Forma13 form13_Pitanje3_4Forma
def proces_form13_Pitanje3_4Forma(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form13 = Pitanje3_4Forma(prefix="form13")
		context = {'form13': form13}
		return render(request, 'pitanja/pojedinacne_forme/form13_Pitanje3_4Forma.html',context)  

#Forma14 form14 _Pitanje3_5Formset
def proces_form14_Pitanje3_5Formset(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form14 =  Pitanje3_5Formset (prefix = "pitanje3_5formset", queryset=Pitanje3_5.objects.none())
		context = {'form14': form14}
		return render(request, 'pitanja/pojedinacne_forme/form14_Pitanje3_5Formset.html',context)   


#***************************************************Saradnja Izmedju Subjekata NIGIP-a****************************************************************#
#Forma15 form15_SaradnjaIzmedjuSubjekataForma
def proces_form15_SaradnjaIzmedjuSubjekataForma(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form15 = SaradnjaIzmedjuSubjekataForma(prefix="form15")
		context = {'form15': form15}
		return render(request, 'pitanja/pojedinacne_forme/form15_SaradnjaIzmedjuSubjekataForma.html',context)    

#Forma16 form16_Pitanje4_7Forma
def proces_form16_Pitanje4_7Forma(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form16 = Pitanje4_7Forma(prefix="form16")
		context = {'form16': form16}
		return render(request, 'pitanja/pojedinacne_forme/form16_Pitanje4_7Forma.html',context)   
		
		
#***************************************************Standardizacija i koncept otvorenih podataka****************************************************************#
#Forma17 form17_StandardizacijaOtvorenihPodatakaForma
def proces_form17_StandardizacijaOtvorenihPodatakaForma(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form17 = StandardizacijaOtvorenihPodatakaForma(prefix="form17")
		context = {'form17': form17}
		return render(request, 'pitanja/pojedinacne_forme/form17_StandardizacijaOtvorenihPodatakaForma.html',context)    

#Forma18 form18_Pitanje5_1Forma
def proces_form18_Pitanje5_1Forma(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form18 = Pitanje5_1Forma(prefix="form18")
		context = {'form18': form18}
		return render(request, 'pitanja/pojedinacne_forme/form18_Pitanje5_1Forma.html',context) 

#Forma19 form19_Pitanje5_2Formset
def proces_form19_Pitanje5_2Formset(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form19 =  Pitanje5_2Formset (prefix = "pitanje5_2formset", queryset=Pitanje5_2.objects.none())
		context = {'form19': form19}
		return render(request, 'pitanja/pojedinacne_forme/form19_Pitanje5_2Formset.html',context)      

#Forma20 form20_Pitanje5_4Forma
def proces_form20_Pitanje5_4Forma(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form20 = Pitanje5_4Forma(prefix="form20")
		context = {'form20': form20}
		return render(request, 'pitanja/pojedinacne_forme/form20_Pitanje5_4Forma.html',context)  

#Forma21 form20_Pitanje5_4Forma
def proces_form21_Pitanje5_12Forma(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form21 = Pitanje5_12Forma(prefix="form21")
		context = {'form21': form21}
		return render(request, 'pitanja/pojedinacne_forme/form21_Pitanje5_12Forma.html',context) 

#Forma22 form22_Pitanje5_13Forma
def proces_form22_Pitanje5_13Forma(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form22 = Pitanje5_13Forma(prefix="form22")
		context = {'form22': form22}
		return render(request, 'pitanja/pojedinacne_forme/form22_Pitanje5_13Forma.html',context)   

#Forma23 form23_Pitanje5_14Forma
def proces_form23_Pitanje5_14Forma(request):
	if request.POST:
		return HttpResponse(request.POST)
	else:
		form22 = Pitanje5_13Forma(prefix="form22")
		context = {'form22': form22}
		return render(request, 'pitanja/pojedinacne_forme/form23_Pitanje5_14Forma.html',context)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

def zaAjax(request):
	return render(request, 'pitanja/zaAjax.html') 


def test(request):
	all = SveobuhvatniModel.objects.all()
	return render(request, 'pitanja/moje.html', {'all':all})   