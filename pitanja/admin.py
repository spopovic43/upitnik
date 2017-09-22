from django.contrib import admin
from .models import (
	
	OrganizacijaOsnovniPodaci, KadroviInfrastruktura, Pitanje2_8, Pitanje2_6, 
	Pitanje2_5, ProstorniPodaci,Pitanje3_5, Pitanje3_4, Pitanje3_3, Pitanje3_2,  Pitanje3_1,
	SaradnjaIzmedjuSubjekata, Pitanje4_7, StandardizacijaOtvorenihPodataka, Pitanje5_14,
	Pitanje5_13, Pitanje5_12, Pitanje5_4, Pitanje5_2, Pitanje5_1, SveobuhvatniModel,

	 			
)

data = [
	OrganizacijaOsnovniPodaci, KadroviInfrastruktura,Pitanje2_5, Pitanje2_6, Pitanje2_8,ProstorniPodaci, Pitanje3_5,
	Pitanje3_4, Pitanje3_3,Pitanje3_2,  Pitanje3_1, SaradnjaIzmedjuSubjekata, Pitanje4_7,
	StandardizacijaOtvorenihPodataka, Pitanje5_14, Pitanje5_13, Pitanje5_12, Pitanje5_4, Pitanje5_2, Pitanje5_1,
	SveobuhvatniModel
]

# Register your models here.
for i in data:
	admin.site.register(i)




'''Aneks1,Aneks2, Aneks3, Block, Building, Profile, FamilyMember, '''	