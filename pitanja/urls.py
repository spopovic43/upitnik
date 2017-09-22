"""Upitnik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name = "home_page"),
	url(r'^pitanja/up1/$', views.upitnik1, name = "upitnik1_forma"), # stara glavna forma
    url(r'^formset/family$', views.family, name = "family"),#Deo forme savisestrukim unosom istog pitanja
    url(r'^raw/$', views.raw_upitnik, name = "raw_upitnik"), # Glavna forma bez visetrukog unosa istog pitanja
    #url(r'^raw/pitanje2_5/$', views.proces_formset2_5, name = "proces_formset2_5"),

    #******************************************Prva Sekcija Osnovni Podaci*************************************************************#
    url(r'^pojedinacne/form1$',  views.proces_form1_OrganizacijaOsnovniPodaciForma, name = "OrganizacijaOsnovniPodaciForma"),
    
    #******************************************Druga Sekcija KadroviInfrastruktura*************************************************************#
    url(r'^pojedinacne/form2$',  views.proces_form2_KadroviInfrastrukturaForma,  name = "KadroviInfrastrukturaForma"),
    url(r'^pojedinacne/form3$',  views.proces_form3_Pitanje2_5Formset,  name = "Pitanje2_5Formset"),
    url(r'^pojedinacne/form4$',  views.proces_form4_Pitanje2_6Formset,  name = "Pitanje2_6Formset"),
    url(r'^pojedinacne/form5$',  views.proces_form5_Pitanje2_8Formset,  name = "Pitanje2_8Formset"),
    
    #*************************************************** Treca Sekcija Prostorni Podaci****************************************************************#
    url(r'^pojedinacne/form6$',  views.proces_form6_ProstorniPodaciForma,  name = "ProstorniPodaciForma"),
    url(r'^pojedinacne/form7$',  views.proces_form7_Pitanje3_1Forma,  name = "Pitanje3_1Forma"),
    url(r'^pojedinacne/form11$', views.proces_form11_Pitanje3_2Forma, name = "Pitanje3_2Forma"),
    url(r'^pojedinacne/form12$', views.proces_form12_Pitanje3_3Formset, name = "Pitanje3_3Formset"),
    url(r'^pojedinacne/form13$', views.proces_form13_Pitanje3_4Forma, name = "form13_Pitanje3_4Forma"),
    url(r'^pojedinacne/form14$', views.proces_form14_Pitanje3_5Formset, name = "Pitanje3_5Formset"),
    
    #***************************************************Cetvrta Sekcija Saradnja Izmedju Subjekata NIGIP-a****************************************************************#
    url(r'^pojedinacne/form15$', views.proces_form15_SaradnjaIzmedjuSubjekataForma, name = "SaradnjaIzmedjuSubjekataForma"),
    url(r'^pojedinacne/form16$', views.proces_form16_Pitanje4_7Forma, name = "Pitanje4_7Forma"),
    
    #***************************************************Peta Sekcija Standardizacija i koncept otvorenih podataka****************************************************************#
    url(r'^pojedinacne/form17$', views.proces_form17_StandardizacijaOtvorenihPodatakaForma, name = "StandardizacijaOtvorenihPodatakaForma"),
    url(r'^pojedinacne/form18$', views.proces_form18_Pitanje5_1Forma, name = "Pitanje5_1Forma"),
    url(r'^pojedinacne/form19$', views.proces_form19_Pitanje5_2Formset, name = "Pitanje5_2Formset"),
    url(r'^pojedinacne/form20$', views.proces_form20_Pitanje5_4Forma, name = "Pitanje5_4Forma"),
    url(r'^pojedinacne/form21$', views.proces_form21_Pitanje5_12Forma, name = "Pitanje5_12Forma"),
    url(r'^pojedinacne/form22$', views.proces_form22_Pitanje5_13Forma, name = "Pitanje5_13Forma"),
    url(r'^pojedinacne/form23$', views.proces_form23_Pitanje5_14Forma, name = "Pitanje5_14Forma"),
    
    url(r'^pojedinacne/ajax$', views.zaAjax, name = "zaAjax"),
    url(r'^test$', views.test, name = "test"),
    
]
