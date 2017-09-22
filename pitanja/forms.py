from django import forms
from django.forms import Textarea, RadioSelect,MultipleChoiceField, SelectMultiple, CheckboxSelectMultiple,SelectMultiple, formset_factory, modelformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab 
from crispy_forms.layout import Submit, Layout, Div, Fieldset, HTML, Column

from .models import (
						 
						SveobuhvatniModel, Pitanje2_5, Pitanje2_6, KadroviInfrastruktura,
						OrganizacijaOsnovniPodaci,
						KadroviInfrastruktura, Pitanje2_8, ProstorniPodaci,
						Pitanje3_1, Aneks1, Aneks2, Aneks3, Pitanje3_2, Pitanje3_3, Pitanje3_4, 
						Pitanje3_5, SaradnjaIzmedjuSubjekata, Pitanje4_7, 
						StandardizacijaOtvorenihPodataka, Pitanje5_1, Pitanje5_2, Pitanje5_4,
						Pitanje5_12, Pitanje5_13, Pitanje5_14,
						
						Sekcija2_5_Program_Choices, Sekcija2_5_Namena_Choices, Sekcija2_5_Ucestalost_koriscenja_Choices,
						Sekcija2_6_Program_Choices, Sekcija2_6_Namena_Choices, Sekcija2_8_Program_Choices, Sekcija2_8_Namena_Choices,
						Sekcija2_3_Znacaj_Upotrebe_Choices, Sekcija2_4_Prepreke_Koriscenja_Geoinformacija_Choices, Sekcija2_7_Serveri_Choices,
						Sekcija3_1_Aneks1_Choices, Sekcija3_1_Aneks2_Choices, Sekcija3_1_Aneks3_Choices,
						Sekcija3_3_Proizvod_Choices, Sekcija3_3_Proizvodjac_Choices, Sekcija3_3_Prostorni_Obuhvat_Choices,
						Sekcija3_5_Proizvod_Choices, Sekcija3_5_Proizvodjac_Choices, Sekcija3_5_Prostorni_Obuhvat_Choices,Sekcija3_5_Razlog_Nedostupnosti_Choices, 
						Sekcija3_4_Univerzalni_Za_Sve_Choices, 
						Selekcija5_1_Univerzalno,Selekcija5_13_Vaznost_Prepreke_Univerzalno_Choices, Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices
						)

						
from django.forms import inlineformset_factory, formset_factory, modelformset_factory
from django.forms.models import BaseInlineFormSet

#*********************************************** Prva kategorija Pitanja ********************************************************#		
class OrganizacijaOsnovniPodaciForma(forms.ModelForm):
	
	def __init__(self, *args, **kwargs):
		super(OrganizacijaOsnovniPodaciForma, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-6'
		self.helper.field_class = 'col-md-6'
		self.helper.form_tag = False
		self.disable_csrf = False
		
	
	
	class Meta:
		model = OrganizacijaOsnovniPodaci
		fields = "__all__" 

		widgets = {

			'Kako_se_vasa_organizacija_finansira': forms.SelectMultiple(),
			'Glavna_strucna_oblast_vase_organizacije': forms.SelectMultiple()
			
		}
#********************************************** Druga kategorija pitanja sa pomocnim klasama *************************************#
class Pitanje2_5Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Pitanje2_5Forma, self).__init__(*args, **kwargs)
		#self.fields['Jedinstveni'] = forms.CharField()
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		#self.fields['Jedinstveni'].widget = forms.HiddenInput()
		self.fields['Namena'] = forms.MultipleChoiceField(choices = Sekcija2_5_Namena_Choices)
		self.helper = FormHelper()
		#self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		#self.helper.label_class = 'col-md-6'
		self.helper.form_show_labels = False
		self.helper.field_class = 'col-md-6'
		self.helper.form_tag = False
		self.disable_csrf = False
		
		'''self.helper.layout = Layout(
			TabHolder(
						Tab('Program5', 'Program'),
						Tab('Namena5', 'Namena'),
						Tab('Ucestalost Koriscenja5', 'Ucestalost_Koriscenja')
					),
				
			
		)'''
		self.helper.layout = Div(
			
						Column('Program', css_class='col-md-3'),
						Column('Namena', css_class='col-md-3'),
						Column('Ucestalost_Koriscenja', css_class='col-md-4'),
						
						css_class='row-fluid'
		)
		
	class Meta:
		model = Pitanje2_5
		fields = "__all__"
		#exclude = ('Koje_aplikacije_su_u_upotrebi_za_obradu','Koji_sistemi_za_upravljanje_bazama_imate','Mobilne_gis_aplikacije')
		widgets = {
			
			#'Program':SelectMultiple(choices = Sekcija2_5_Program_Choices),
			#'Namena':MultipleChoiceField(),
			#'Ucestalost_Koriscenja':SelectMultiple(choices = Sekcija2_5_Ucestalost_koriscenja_Choices)
		}
		
class Pitanje2_6Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Pitanje2_6Forma, self).__init__(*args, **kwargs)
		#self.fields['jedinstveni'] =forms.CharField()
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.fields['Namena'] = forms.MultipleChoiceField(choices = Sekcija2_6_Namena_Choices)
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-12'
		self.helper.form_show_labels = False
		self.helper.field_class = 'col-md-6'
		self.helper.form_tag = False
		self.disable_csrf = False

		'''self.helper.layout = Layout(
			TabHolder(
						Tab('Program6', 'Program'),
						Tab('Namena6', 'Namena')
						
					)'''
		self.helper.layout = Div(
			
						Column('Program', css_class='col-md-6'),
						Column('Namena', css_class='col-md-6'),
						
						css_class='row-fluid'
		)
	class Meta:
		model = Pitanje2_6
		fields = "__all__"
		#exclude = ('Koje_aplikacije_su_u_upotrebi_za_obradu','Koji_sistemi_za_upravljanje_bazama_imate','Mobilne_gis_aplikacije')
		'''widgets = {
			'Program':RadioSelect(choices = Sekcija2_6_Program_Choices),
			'Namena':RadioSelect(choices = Sekcija2_6_Namena_Choices),
			
		}'''
		
		
class Pitanje2_8Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Pitanje2_8Forma, self).__init__(*args, **kwargs)
		#self.fields['jedinstveni'] =forms.CharField()
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.fields['Namena'] = forms.MultipleChoiceField(choices = Sekcija2_8_Namena_Choices)
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		#self.helper.label_class = 'col-md-6'
		self.helper.form_show_labels = False
		self.helper.field_class = 'col-md-12'
		self.helper.form_tag = False
		self.disable_csrf = False
		'''self.helper.layout = Layout(
			TabHolder(
						Tab('Program8', 'Program'),
						Tab('Namena8', 'Namena')
						
					)'''
		self.helper.layout = Div(
			
						Column('Program', css_class='col-md-6'),
						Column('Namena', css_class='col-md-6'),
						
						css_class='row-fluid'
		)
		
	class Meta:
		model = Pitanje2_8
		fields = "__all__"
		'''widgets = {
			'Program':RadioSelect(choices = Sekcija2_8_Program_Choices),
			'Namena':RadioSelect(choices = Sekcija2_8_Namena_Choices),
			
		}'''
		
class KadroviInfrastrukturaForma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(KadroviInfrastrukturaForma, self).__init__(*args, **kwargs)
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-12'
		self.helper.field_class = 'col-md-4'
		self.helper.form_tag = False
		self.disable_csrf = False

		
		'''for field_name in self.fields:
			field = self.fields.get(field_name)
			if field and isinstance(field , forms.RadioSelect) or isinstance(field , forms.CheckboxSelectMultiple):
				field.choices = field.choices[1:]'''
		
	class Meta:
		model = KadroviInfrastruktura
		#fields = "__all__"
		exclude = ('Koje_aplikacije_su_u_upotrebi_za_obradu','Koji_sistemi_za_upravljanje_bazama_imate','Mobilne_gis_aplikacije') 
		widgets = {
			'Procenite_znacaj_upotrebe_geoinformacija':RadioSelect(choices = Sekcija2_3_Znacaj_Upotrebe_Choices),
			
			#'Serveri_za_prostorne_podatke':RadioSelect(choices = Sekcija2_7_Serveri_Choices),
			
		}
		
		
		
		
#********************************************** Treca kategorija pitanja sa pomocnim klasama *************************************#	


class Pitanje3_1Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Pitanje3_1Forma, self).__init__(*args, **kwargs)
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		#self.helper.label_class = 'col-md-6'
		self.helper.form_show_labels = False
		self.helper.field_class = 'col-md-6'
		self.helper.form_tag = False
		self.disable_csrf = False
		self.helper.layout = Layout(
			TabHolder(
						Tab('Aneks1', 'Aneks1_polje'),
						Tab('Aneks2', 'Aneks2_polje'),
						Tab('Aneks3', 'Aneks3_polje')
						
					)
		)
		'''for i in self.fields:
			field = self.fields[i] 
			if field == 'Jedinstveni':
				field.widget = forms.TextInput()'''
	
	class Meta:
		model = Pitanje3_1
		fields = "__all__"
		widgets = {
			'Jedinstveni':forms.TextInput(),
			#'Aneks2_polje':SelectMultiple(choices = Sekcija3_1_Aneks2_Choices),
			#'Aneks3_polje':SelectMultiple(choices = Sekcija3_1_Aneks3_Choices),
			
		}
		
class Aneks1Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Aneks1Forma, self).__init__(*args, **kwargs)
		#self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		#self.helper.label_class = 'col-md-6'
		self.helper.field_class = 'col-md-12'
		self.helper.form_tag = False
		self.disable_csrf = False

	class Meta:
		model = Aneks1
		fields = "__all__"

class Aneks2Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Aneks2Forma, self).__init__(*args, **kwargs)
		#self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		#self.helper.label_class = 'col-md-6'
		self.helper.field_class = 'col-md-12'
		self.helper.form_tag = False
		self.disable_csrf = False

	class Meta:
		model = Aneks2
		fields = "__all__"

class Aneks3Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Aneks3Forma, self).__init__(*args, **kwargs)
		#self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		#self.helper.label_class = 'col-md-6'
		self.helper.field_class = 'col-md-12'
		self.helper.form_tag = False
		self.disable_csrf = False

	class Meta:
		model = Aneks3	
		fields = "__all__"		
		
		
class Pitanje3_2Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Pitanje3_2Forma, self).__init__(*args, **kwargs)
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-4'
		self.helper.field_class = 'col-md-8'
		self.helper.form_tag = False
		self.disable_csrf = False

	class Meta:
		model = Pitanje3_2	
		fields = "__all__"	

		widgets = {
			'Nacin_skladistenja': forms.SelectMultiple(),
			'Format_Distribucije': forms.SelectMultiple(),
			'Nacin_Distribucije': forms.SelectMultiple(),
			'Koordinatni_Sistem': forms.SelectMultiple(),
			#'Dostupnost': forms.SelectMultiple(),
			#'Web_Servis': forms.SelectMultiple(),
			#'Prava_Pristupa': forms.SelectMultiple(),
			
			
		}

class Pitanje3_3Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Pitanje3_3Forma, self).__init__(*args, **kwargs)
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		#self.helper.label_class = 'col-md-6'
		self.disable_csrf = False
		self.helper.form_tag = False
		self.helper.field_class = 'col-md-12'
		self.helper.form_show_labels = False
		self.helper.layout = Div(
			
						Column('Proizvod', css_class='col-md-3'),
						Column('Proizvodjac', css_class='col-md-3'),
						Column('Prostorni_Obuhvat', css_class='col-md-3'),
						HTML("<span class='glyphicon glyphicon-plus'></span>"),
						css_class='row-fluid'
						
					
		)
		
		
	class Meta:
		model = Pitanje3_3	
		fields = "__all__"
		'''widgets = {
			'Proizvod':CheckboxSelectMultiple(choices = Sekcija3_3_Proizvod_Choices),
			'Proizvodjac':CheckboxSelectMultiple(choices = Sekcija3_3_Proizvodjac_Choices),
			'Prostorni_Obuhvat':CheckboxSelectMultiple(choices = Sekcija3_3_Prostorni_Obuhvat_Choices),
			
		}'''

		
class Pitanje3_4Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Pitanje3_4Forma, self).__init__(*args, **kwargs)
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		#self.helper.label_class = 'col-md-6'
		#self.helper.field_class = 'col-md-12'
		self.helper.form_tag = False
		#self.helper.form_show_labels = False
		self.disable_csrf = False

		'''for i in self.fields:
			field = self.fields[i]
			
			if field != "Jedinstveni":
				field.widget = RadioSelect(choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
			
			self.helper.layout = Layout(
				InlineRadios(field)
			)	
		
		self.helper.layout = Layout(
			InlineRadios('Koordinatni_referentni_sistemi')

		)
    	'''
		
		
	class Meta:
		model = Pitanje3_4	
		fields = "__all__"	
		widgets = {
			'Jedinstveni':forms.TextInput(),
			
			
		}
class Pitanje3_5Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Pitanje3_5Forma, self).__init__(*args, **kwargs)
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-4'
		self.helper.field_class = 'col-md-8'
		self.helper.form_tag = False
		self.disable_csrf = False
		self.helper.layout = Div(
			
						Column('Proizvod', css_class='col-md-3'),
						Column('Proizvodjac', css_class='col-md-3'),
						Column('Prostorni_obuhvat', css_class='col-md-2'),
						Column('Razlog_nedostupnosti', css_class='col-md-2'),
						
						css_class='row-fluid'
		)
	class Meta:
		model = Pitanje3_5	
		fields = "__all__"	
		widgets = {
			'Jedinstveni':forms.TextInput(),
		}	
	
class ProstorniPodaciForma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProstorniPodaciForma, self).__init__(*args, **kwargs)
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-12'
		self.helper.field_class = 'col-md-4'
		self.helper.form_tag = False
		self.disable_csrf = False

	class Meta:
		model = ProstorniPodaci
		
		exclude = (
					'Za_koje_od_navedenih_INSPIRE_tema_proizvodite_podatke', 
					'Uneti_podatke_o_podacima_koje_vasa_organizacija_proizvodi',
					'Koje_prostorne_podatke_nabavljate_od_drugih',
					'Odrediti_vazne_podatke_od_drugih_organizacija_za_redovne_aktivnosti',
					'Za_kojim_prostornim_podacima_imate_potrebu_a_koji_nisu_dostupni',
				)
		widgets = {
			'Jedinstveni':forms.TextInput(),
			'Dodatno_obrazovanje_u_okviru_organizacije': forms.SelectMultiple(),
			'Nacin_razmene_podataka_sa_drugima': forms.SelectMultiple(),
		}	
	
#************************************************* Saradnja Izmedju Subjekata NIGIP-a *************************************************************#		

class Pitanje4_7Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Pitanje4_7Forma, self).__init__(*args, **kwargs)
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-2'
		self.helper.field_class = 'col-md-10'
		self.helper.form_tag = False
		self.disable_csrf = False

		'''for i in self.fields:
			field = self.fields[i]
			if field != 'Jedinstveni': 
				field.widget = RadioSelect(choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)'''

	class Meta:
		model = Pitanje4_7	
		fields = "__all__"	
		widgets = {
			'Jedinstveni': forms.TextInput()
		}
		
class SaradnjaIzmedjuSubjekataForma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(SaradnjaIzmedjuSubjekataForma, self).__init__(*args, **kwargs)
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-12'
		self.helper.field_class = 'col-md-6'
		self.helper.form_tag = False
		self.disable_csrf = False

	class Meta:
		model = SaradnjaIzmedjuSubjekata
		exclude = ('Uloga_nacionalnog_geoportala',)

		widgets = {
			
			'Na_koji_nacin_obezbedjujete_podatke_za_svoje_potrebe': forms.SelectMultiple(),
			'Na_koji_nacin_saradjujete_sa_drugim_organizacijama_pri_razmeni': forms.SelectMultiple(),
			'Ko_su_korisnici_vasih_proizvoda': forms.SelectMultiple(),
			'Koja_je_cenovna_politika_za_geopodatke': forms.SelectMultiple(),
			'Model_odredjivanja_cene': forms.SelectMultiple(),
			'Kojem_modelu_finansiranja_NGIPA_treba_teziti': forms.SelectMultiple(),
			'Problemi_prilikom_nabavke_geopodataka': forms.SelectMultiple()
		}
		
		
		
#************************************************* Standardizacija Otvorenih Podataka *************************************************************#		
	

class Pitanje5_1Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Pitanje5_1Forma, self).__init__(*args, **kwargs)
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-2'
		self.helper.field_class = 'col-md-10'
		self.helper.form_tag = False
		self.disable_csrf = False

		'''for i in self.fields:
			field = self.fields[i] 
			field.widget = RadioSelect(choices = Selekcija5_1_Univerzalno)'''

	class Meta:
		model = Pitanje5_1	
		fields = "__all__"	
		widgets = {
			'Jedinstveni':forms.TextInput()
		}

class Pitanje5_2Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Pitanje5_2Forma, self).__init__(*args, **kwargs)
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'

		
		
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-2'
		self.helper.field_class = 'col-md-10'
		self.helper.form_tag = False
		self.disable_csrf = False

	class Meta:
		model = Pitanje5_2	
		fields = "__all__"
		widgets = {
			'Jedinstveni':forms.TextInput()
		}

class Pitanje5_4Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Pitanje5_4Forma, self).__init__(*args, **kwargs)
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-4'
		self.helper.field_class = 'col-md-6'
		self.helper.form_tag = False
		self.disable_csrf = False

	class Meta:
		model = Pitanje5_4	
		fields = "__all__"
		'''widgets = {
			Naziv_akta: RadioSelect(choices = (('Da', 'Da'),('Ne', 'Ne')))

		}'''

		widgets = {
			'Jedinstveni':forms.TextInput(), 
			'Da_ne': RadioSelect(choices = (('Da', 'Да'),('Ne', 'Не')))
		}


class Pitanje5_12Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Pitanje5_12Forma, self).__init__(*args, **kwargs)
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-4'
		self.helper.field_class = 'col-md-6'
		self.helper.form_tag = False
		self.disable_csrf = False
		self.helper.layout = Div(
			
						Column('Prepreka1', css_class='col-md-4'),
						Column('Prepreka2', css_class='col-md-4'),
						Column('Prepreka3', css_class='col-md-4'),
						
						
						css_class='row-fluid'
		)
	class Meta:
		model = Pitanje5_12	
		fields = "__all__"
		widgets = {
			'Jedinstveni':forms.TextInput()
		}

class Pitanje5_13Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Pitanje5_13Forma, self).__init__(*args, **kwargs)
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		#self.helper.label_class = 'col-md-2'
		#self.helper.field_class = 'col-md-10'
		self.helper.form_tag = False
		self.disable_csrf = False

		'''for i in self.fields:
			field = self.fields[i]
			if field != 'Jedinstveni':
				field.widget = RadioSelect(choices = Selekcija5_13_Vaznost_Prepreke_Univerzalno_Choices)
				'''
	class Meta:
		model = Pitanje5_13	
		fields = "__all__"
		widgets = {
			'Jedinstveni':forms.TextInput()
		}
	
class Pitanje5_14Forma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(Pitanje5_14Forma, self).__init__(*args, **kwargs)
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-6'
		self.helper.field_class = 'col-md-6'
		self.helper.form_tag = False
		self.disable_csrf = False

		'''for i in self.fields:
			field = self.fields[i]
			if field != 'Jedinstveni':
				field.widget = RadioSelect(choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices)
				'''
	class Meta:
		model = Pitanje5_14	
		fields = "__all__"
		widgets = {
			'Jedinstveni':forms.TextInput()
		}

class StandardizacijaOtvorenihPodatakaForma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(StandardizacijaOtvorenihPodatakaForma, self).__init__(*args, **kwargs)
		self.fields['Jedinstveni'].widget.attrs['class'] = 'jedinstveni'
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-12'
		self.helper.field_class = 'col-md-6'
		self.helper.form_tag = False
		self.disable_csrf = False

	class Meta:
		model = StandardizacijaOtvorenihPodataka
		#fields = "__all__"
		exclude = (
					'Status_standarda', 
					'Standardi_iz_oblasti_geoinformacija',
					'Propis_prava_koriscenja',
					'Prepreke_za_uspostavljanje_koncepta_gopodataka',
					'Vaznost_Prepreka',
					'Koliko_se_slazete_sa_tvrdnjama'
				)		
		
		widgets = {
			'Jedinstveni':forms.TextInput(),
			'Metode_koriscenja_i_zastite': forms.SelectMultiple(),
			'Da_li_ste_upoznati_sa_nekim_od_postojecih_portala': forms.SelectMultiple(),
			'Format_podataka': forms.SelectMultiple(),
			'Koju_vrstu_podataka_ste_koristili': forms.SelectMultiple(),
			'Za_koje_poslove_ste_koristili_podatke': forms.SelectMultiple(),
			'Da_li_ste_koristili_besplatne_setove_podataka': forms.SelectMultiple(),
		}

class SveobuhvatniModelForma(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(SveobuhvatniModelForma, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class="col-md-12"
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-md-12'
		self.helper.field_class = 'col-md-6'
		self.disable_csrf = False
		self.helper.form_tag = False
		self.helper.add_input(Submit('submit', 'Posalji'))
		
	class Meta:
		model = SveobuhvatniModel
		#fields = "__all__"
		exclude = (
					'Prva_sekcija', 
					'Druga_sekcija',
					'Treca_sekcija',
					'Cetvrta_sekcija',
					'Peta_sekcija',
					
				)		
		
#******************************************** Testing On Section 2 ******************************************# 
Pitanje2_5Formset = modelformset_factory(Pitanje2_5, Pitanje2_5Forma)
Pitanje2_6Formset = modelformset_factory(Pitanje2_6, Pitanje2_6Forma)
Pitanje2_8Formset = modelformset_factory(Pitanje2_8, Pitanje2_8Forma)

Pitanje3_3Formset = modelformset_factory(Pitanje3_3, Pitanje3_3Forma)
Pitanje3_5Formset = modelformset_factory(Pitanje3_5, Pitanje3_5Forma)

Pitanje5_2Formset = modelformset_factory(Pitanje5_2, Pitanje5_2Forma)
		
		
		
		
		
		
		
		
		
		
		
		
