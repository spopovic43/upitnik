from django.db import models
from multiselectfield import MultiSelectField
# Create your models here. 

#**************************************** Osnovni podaci o organizaciji *********************************************************************************#
#********************************************************************************************************************************************#

#Definisanje "Vrsta Organizacije" Chice polja za pitanje 1_5
Sekcija1_5_Format_Vrsta_Organizacije_Choices = (
    
	('Орган државне управе (министарство, посебна организација)', 'Орган државне управе (министарство, посебна организација)'),
    ('Орган територијалне аутономије', 'Орган територијалне аутономије'),
    ('Орган локалне самоуправе (аутоматски попуњава следећа два питања са истим одговором)', 'Орган локалне самоуправе (аутоматски попуњава следећа два питања са истим одговором)'),
    ('Јавна агенција', 'Јавна агенција'),
    ('Јавно предузеће', 'Јавно предузеће'),
    ('Научно-образовна установа', 'Научно-образовна установа'),
    ('Пројектантскo-урбанистичка организација', 'Пројектантскo-урбанистичка организација'),
    ('Приватна организација', 'Приватна организација'),
    ('Остало', 'Остало'),
)

#Definisanje "Glavna Strucna Oblast Organizacije" Chice polja za pitanje 1_6
Sekcija1_6_Strucna_Oblast_Organizacije_Choices = (

    ('Орган локалне самоуправе', 'Орган локалне самоуправе'),
    ('Управљање земљиштем/непокретностима (катастар непокретности, опорезивање непокретности)', 'Управљање земљиштем/непокретностима (катастар непокретности, опорезивање непокретности)'),
    ('Заштита животне средине', 'Заштита животне средине'),
    ('Климатске промене', 'Климатске промене'),
    ('Метеорологија', 'Метеорологија'),
    ('Заштита од елементарних непогода', 'Заштита од елементарних непогода'),
    ('Пољопривреда', 'Пољопривреда'),
    ('Енергетика', 'Енергетика'),
    ('Шумарство', 'Шумарство'),
    ('Управљање водним ресурсима', 'Управљање водним ресурсима'),
    ('Одбрана и национална безбедност', 'Одбрана и национална безбедност'),
    ('Сеизмологија', 'Сеизмологија'),
    ('Геологија', 'Геологија'),
    ('Транспорт', 'Транспорт'),
    ('Просторно/урбанистичко планирање', 'Просторно/урбанистичко планирање'),
    ('Водови (комунална инфраструктура, комуникационе мреже, енергетска мрежа и др. )','Водови (комунална инфраструктура, комуникационе мреже, енергетска мрежа и др. )'),
    ('Туризам', 'Туризам'),
    ('Културна баштина', 'Културна баштина'),
    ('Остало', 'Остало'),
)

#Definisanje "Teritorijalni nivo" Choice polja za pitanje 1_7
Sekcija1_6_Teritorijalni_Nivo_Organizacije_Choices = (
    
	('Локалном', 'Локалном'),
    ('Националном', 'Националном'),
    ('Регионалном', 'Регионалном'),
    ('Међународном', 'Међународном'),
)
#Definisanje "Finansiranje Organizacije" Choice polja za pitanje 1_8
Sekcija1_6_Finansiranje_Organizacije_Choices = (
    
	('Државни буџет', 'Државни буџет'),
    ('Буџет аутономне покрајине/локалне самоуправе', 'Буџет аутономне покрајине/локалне самоуправе'),
    ('Сопствени приходи', 'Сопствени приходи'),
    ('Делимично буџет и делимично сопствени приходи', 'Делимично буџет и делимично сопствени приходи'),
    ('Остало', 'Остало'),
)


# Definisanje klase OrganizacijaOsnovniPodaci
class OrganizacijaOsnovniPodaci(models.Model):
	Naziv_organizacije = models.CharField(max_length=40, verbose_name='Назив организације')
	Adresa = models.CharField(max_length=50, verbose_name='Адреса', help_text="Место, Улица и број")
	Internet_sajt = models.URLField(verbose_name='Интернет сајт', help_text="Линк ка сајту")
	E_mail = models.EmailField(verbose_name='Е-адреса')
	Telefon = models.CharField(max_length=13, verbose_name='Телефон', help_text="У формату: 011/98-76-543")
	Vrsta_organizacije = models.CharField(max_length=90, choices=Sekcija1_5_Format_Vrsta_Organizacije_Choices, verbose_name='Врста организације')
	Vrsta_organizacije_drugo = models.CharField(max_length = 100, verbose_name="Врста организације друго",null=True, blank=True)

	Glavna_strucna_oblast_vase_organizacije = MultiSelectField(max_length=200, choices=Sekcija1_6_Strucna_Oblast_Organizacije_Choices , verbose_name='Главна стручна област Ваше организације')
	Glavna_strucna_oblast_vase_organizacije_ostalo = models.CharField(max_length = 100, verbose_name="Главна стручна област ваше организације друго",null=True, blank=True)
	Na_kom_teritorijalnom_nivu_vasa_organizacija_obavlja_delatnost = models.CharField(max_length=15, choices=Sekcija1_6_Teritorijalni_Nivo_Organizacije_Choices, verbose_name='На ком територијалном нивоу Ваша организација обавља делатност')
	Kako_se_vasa_organizacija_finansira = MultiSelectField(max_length=200, choices=Sekcija1_6_Finansiranje_Organizacije_Choices, verbose_name='Како се ваша организација финансира')
	Kako_se_vasa_organizacija_finansira_ostalo = models.CharField(max_length = 100, verbose_name="Како се ваша организација финансира остало",null=True, blank=True)
	Kontakt_osoba = models.CharField(max_length=40, verbose_name='Контакт особа', help_text="Име и презиме")
	Telefon_kontakt_osobe = models.CharField(max_length=13, verbose_name='Телефон контакт особе', help_text="У формату: 064/12-34-230")
	E_mail_kontakt_osobe = models.EmailField(verbose_name='Е-адреса')

	def __str__(self):
		return self.Naziv_organizacije
		
#********************************************************************************************************************************************#

#**************************************** Kadrovi i infrastruktura *********************************************************************************#
#*****************************************************************************************************************************#

#Definisanje "Znacaj Upotrebe Geoinformacija" Choice polja za pitanje 2_3
Sekcija2_3_Znacaj_Upotrebe_Choices  = (
    
	('Суштински', 'Суштински'),
	('Веома Користан', 'Веома Користан'),
	('Користан', 'Користан'),
	('Користан у мањој мери', 'Користан у мањој мери'),
   
)
#Definisanje "Prepreke Za Veci Stepen Koriscenja Geoinformacija" Choice polja za pitanje 2_4
Sekcija2_4_Prepreke_Koriscenja_Geoinformacija_Choices  = (
	
	('Недостатак квалификованог особља', 'Недостатак квалификованог особља'),
	('Недостатак ИТ капацитета', 'Недостатак ИТ капацитета(софтвер, опрема)'),
	('Недостатак података', 'Недостатак података(недоступни подаци, скушпо финансирање)'),
	('Остало', 'Остало')
)

#*********************************************** Definisanje Choice polja za klasu Pitanje2_5*********************************************#
#Definisanje "Program" Choice polja za pitanje 2_5
Sekcija2_5_Program_Choices = (
	
	('ArcGIS Desktop (ESRI)','ArcGIS Desktop (ESRI)'),
	('Q GIS','Q GIS'),
	('MapInfo','MapInfo'),
	('GeoMedia','GeoMedia'),
	('MapSoft','MapSoft'),
	('AutoCAD','AutoCAD'),
	('Bently MicroStation','Bently MicroStation'),
	('ERDAS IMAGINE','ERDAS IMAGINE'),
	('Leica Photogrametry Suite','Leica Photogrametry Suite'),
	('eCognition Trimble','eCognition Trimble'),
	('Интерно креиране апликације','Интерно креиране апликације'),
	('Остало','Остало')
) 
#Definisanje "Namena" Choice polja za pitanje 2_5
Sekcija2_5_Namena_Choices = (
	
	('Израда планова и карата','Израда планова и карата'),
	('Пројектовање','Пројектовање'),
	('Извештавање','Извештавање'),
	('Управљање и планирање коришћења земљишта','Управљање и планирање коришћења земљишта'),
	('Урбанизам и грађевински послови','Урбанизам и грађевински послови'),
	('Праћење промена и просторне анализе','Праћење промена и просторне анализе'),
	('Креирање и анализа ДМТ','Креирање и анализа ДМТ'),
	('Геореференцирање и обрада растерских података','Геореференцирање и обрада растерских података'),
	('Даљинска детекција','Даљинска детекција'),
	('Обрада података добијених ласерским скенирањем','Обрада података добијених ласерским скенирањем'),
	('Остало','Остало')
)
#Definisanje "Ucestalost Koriscenja" Choice polja za pitanje 2_5
Sekcija2_5_Ucestalost_koriscenja_Choices = (
	
	('Свакодневно','Свакодневно'),
	('Често за обимније анализе','Често за обимније анализе'),
	('Понекад за посебне анализе и извештаје','Понекад за посебне анализе и извештаје')
)

class Sekcija2_5_Namena_ChoicesClass(models.Model):
    namena_choices = models.CharField(max_length = 100, choices = Sekcija2_5_Namena_Choices)


#Definisanje klase Pitanje2_5, kao pomocne klase za pitanje 2_5
class Pitanje2_5(models.Model):
	Program = models.CharField(max_length = 100, choices = Sekcija2_5_Program_Choices)
	#Namena = models.CharField(max_length = 100, choices = Sekcija2_5_Namena_Choices, null=True)
	Namena = MultiSelectField(max_length = 1000, choices = Sekcija2_5_Namena_Choices, null= True, blank=True)
	Ucestalost_Koriscenja = models.CharField(max_length = 100, choices = Sekcija2_5_Ucestalost_koriscenja_Choices)
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)

#*********************************************** Definisanje Choice polja za klasu Pitanje2_6*********************************************#

#Definisanje "Program" Choice polja za pitanje 2_6
Sekcija2_6_Program_Choices = (
	
	('MS Access','MS Access'),
	('Oracle ','Oracle '),
	('PostgreSQL','PostgreSQL'),
	('MicrosoftSQL','MicrosoftSQL'),
	('Остало','Остало'),
) 


#Definisanje "Namena" Choice polja za pitanje 2_6
Sekcija2_6_Namena_Choices = (
	('Складиштење просторних података','Складиштење просторних података'),
	('Складиштење алфанумеричких података','Складиштење алфанумеричких података'),
	('Остало','Остало'),
)  
#Definisanje klase Pitanje2_6, kao pomocne klase za pitanje 2_6
class Pitanje2_6(models.Model):
	Program = models.CharField(max_length = 100, choices = Sekcija2_6_Program_Choices)
	Namena = MultiSelectField(max_length = 1000,choices = Sekcija2_6_Namena_Choices, null=True, blank = True)
	#Namena = models.CharField(max_length = 100, choices = Sekcija2_6_Namena_Choices, null=True)
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)

#Definisanje "Serveri" Choice polja za pitanje 2_7
Sekcija2_7_Serveri_Choices = (

	('ArcGIS Server (ESRI)','ArcGIS Server (ESRI)'),
	('Autodesk Infrastructure Map Server','Autodesk Infrastructure Map Server'),
	('GeoServer','GeoServer'),
	('MapServer','MapServer'),
	('ERDAS APOLLO','ERDAS APOLLO'),
	('Ostalo','Ostalo'),
) 
#*********************************************** Definisanje Choice polja za klasu Pitanje2_8*********************************************#
#Definisanje "Program" Choice polja za pitanje 2_8
Sekcija2_8_Program_Choices = (
	
	('ArcPAD','ArcPAD'),
	('Leica Zeno','Leica Zeno'),
	('Интерно креиране апликације','Интерно креиране апликације'),
	('Остало','Остало')
) 

#Definisanje "namena" Choice polja za pitanje 2_8
Sekcija2_8_Namena_Choices = (
	
	('Прикупљање података са терена','Прикупљање података са терена'),
	('Праћење возила','Праћење возила'),
	('Остало','Остало')
) 
							
#Definisanje klase Pitanje2_8, kao pomocne klase za pitanje 2_8
class Pitanje2_8(models.Model):
	Program = models.CharField(max_length = 100, choices = Sekcija2_8_Program_Choices)
	Namena = MultiSelectField(max_length = 1000, choices = Sekcija2_8_Namena_Choices, null=True)
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)
	
#Definisanje Klase osnovni KadroviIInfrastruktura
class KadroviInfrastruktura(models.Model):
	Broj_zaposlenih = models.IntegerField(blank=False, verbose_name="Наведите број запослених који раде на прикупљању, обради или коришћењу просторних података.", help_text='Унети приближан број запослених')
	Navesti_organizacionu_jedinicu = models.CharField(max_length=100, verbose_name="Навести организациону јединицу у чијој су надлежности послови у вези са просторним подацима уколико постоји", help_text='нпр.Одељење за ГИС')
	Procenite_znacaj_upotrebe_geoinformacija = models.CharField(max_length=100, choices = Sekcija2_3_Znacaj_Upotrebe_Choices, verbose_name="Процените значај геоинформација за пословање ваше организације?")
	Glavne_prepreke_za_koriscenje_geoinformacija = MultiSelectField(max_length = 1000, choices = Sekcija2_4_Prepreke_Koriscenja_Geoinformacija_Choices)
	Glavne_prepreke_za_koriscenje_geoinformacija_ostalo = models.CharField(max_length=100, verbose_name="Главне препреке за коришћенје геоинформација остало", null=True, blank=True)

	Koje_aplikacije_su_u_upotrebi_za_obradu =models.ForeignKey('Pitanje2_5', blank = True) 
	Koji_sistemi_za_upravljanje_bazama_imate = models.ForeignKey('Pitanje2_6',  blank = True) 
	Serveri_za_prostorne_podatke = MultiSelectField(max_length = 1000, choices = Sekcija2_7_Serveri_Choices) 
	Serveri_za_prostorne_podatke_ostalo = models.CharField(max_length=100, verbose_name="Сервери за просторне податке остало", null=True, blank=True)
	Mobilne_gis_aplikacije = models.ForeignKey('Pitanje2_8',  blank = True) 
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)

#********************************************************************************************************************************************#

#**************************************** Prostorni podaci *********************************************************************************#
#*****************************************************************************************************************************#

###########################################################################################Pitanje3_1#############################################################################################3
#Definisanje "Aneks1" Choice polja za pitanje 3_1
Sekcija3_1_Aneks1_Choices = (
	
	('Координатни референтни системи','Координатни референтни системи(Системи за јединствено одређивање просторних информација у простору као скупа координата (x, y, z) и/или географске ширине и географске дужине и висине, на основу геодетског хоризонталног и вертикалног датума.)'),
	('Коришћење земљишта','Коришћење земљишта(Територија описана у складу с постојећом и будућом планираном функционалном димензијом или друштвено-економском намена (нпр. стамбена, индустријска. комерцијална, пољопривредна, шумска, рекреативна).)'),
	('Географски мрежни системи','Географски мрежни системи(Хармонизована мрежа вишеструке резолуције са заједничком почетном тачком и стандардизованом локацијом и величином мрежних ћелија.)'),
	('Здравље људи и безбедност','Здравље људи и безбедност(Информације о географској дистрибуцији доминантних патологија (алергије, канцери, болести дисајних органа итд.), које указују на утицај на здравље (биомаркери, смањење плодности, епидемије) или добробит људи (замор, стрес итд.) у директној (загађивање ваздуха, хемикалије, смањење озонског омотача, бука итд.) или индиректној вези (храна, генетски модификовани организми итд.) с квалитетом животне средине.)'),
	('Географска имена','Географска имена(Имена подручја, региона, локалитета, градова, предграђа, градова или насеља, или било који географски или топографски објекат од јавног или историјског интереса.)'),
	('Водови и јавни сервиси','Водови и јавни сервиси(Подразумева водове као што су канализација, управљање отпадом, снабдевање енергијом и водом, административне и државне социјалне службе као што су државна администрација, локације цивилне заштите, школе и болнице.)'),
	('Административне јединице','Административне јединице(Административне јединице, које раздвајају подручја на којима државе чланице имају и/или остварују права у вези са надлежношћу, за локалну, регионалну и националну управу, и која су одвојена административним границама.)'),
	('Системи за праћење квалитета животне средине','Системи за праћење квалитета животне средине(Локација и функцијасистема за праћење животне средине укључујући посматрање и мерење емисије загађујућих материја, стања животне средине и других параметара екосистема (биодиверзитета, еколошких услова вегетације итд.) од стране или у име органа јавне власти.)'),
	('Адресе','Адресе(Локација непокретности на основу адресних идентификатора, обично имена улице, кућног броја, поштанског броја.)'),
	('Производни и индустријски системи','Производни и индустријски системи(Локације индустријске производње, укључујући инсталације за спречавање и контролу загађења, црпна постројења за воду, руднике, складишта и сл.)'),
	('Катастарске парцеле','Катастарске парцеле(Подручја одређена катастарским регистрима или њиховим еквивалентима.)'),
	('Системи за пољопривреду и аквакултуру','Системи за пољопривреду и аквакултуру(Пољопривредна опрема и објекти за производњу (укључујући системе за наводњавање, стакленици и штале).)'),
	('Транспортне мреже','Транспортне мреже(Друмске, железничке, ваздушне и водне транспортне мреже и припадајућа '),
	('Распрострањеност становништва – демографија','Распрострањеност становништва – демографија(Географска распрострањеност људи, укључујући '),
	('Хидрографија','Хидрографија(Хидрографски елементи, укључујући морска подручја и сва друга водена тела и припадајуће делове, укључујући речне сливове и подсливове.)'),
	('Област управљања','Област управљања/ограничења/зоне регулисања и јединице за извештавање (депоније, ограничена подручја око извора воде, зоне ограничења буке)(Области којима се управља, које се регулишу или користе за извештавање на међународном, европском, националном, регионалном и локалном нивоу. Укључује депоније, рестриктивне зоне око изворишта пијаће воде, зоне осетљиве на нитрате, уређене пловне путеве на мору или великим унутрашњим водама, области за одлагање отпада, зоне где се ограничава ниво буке, области за које је потребна дозвола за истраживање или рударство, области речних сливова, релевантне јединице извештавања и област управљања обалском зоном.)'),
	('Заштићена подручја','Заштићена подручја(Област која је одређена или којом се управља у оквиру међународног законодавства, законодавства Заједнице и држава чланица, са циљем постизања посебних циљева очувања.)'),
	('Зоне природног ризика','Зоне природног ризика(Осетљива подручја која се описују према природним хазардима (све атмосферске, хидролошке, сеизмичке, вулканске појаве и пожари, а који, због своје локације, озбиљности и учесталости имају потенцијал да озбиљно угрозе друштво), нпр. поплаве, одрони и улегнућа, лавине, шумски пожари, земљотреси, вулканске ерупције.)'),
)

#Definisanje "Aneks2" Choice polja za pitanje 3_1
Sekcija3_1_Aneks2_Choices = (
	('Атмосферски услови','Атмосферски услови(Укључују просторне податке засноване на мерењима, моделима или њиховој комбинацији и укључују локације за мерење.)'),
	('Висине','Висине(Дигитални  модели висина за површину копна, леда и океана. Укључује висину терена, батиметрију и линију обале.)'),
	('Метеоролошко-географске карактеристике','Метеоролошко-географске карактеристике(Временски услови и њихове мерења; падавине, температура, испаравање, брзина и смер ветра.)'),
	('Земљишни покривач','Земљишни покривач(Физичка и биолошка покривеност земљине површине укључујући вештачке површине, пољопривредне области, шуме, (полу)природне области, влажна земљишта, водна тела.)'),
	('Биогеографски региони','Биогеографски региони(Области релативно хомогених еколошких услова са заједничким карактеристикама.)'),
	('Ортофото','Ортофото(Геореференцирани снимци Земљине површине, прикупљени сателитским или аеро сензорима.)'),
	('Станишта и биотопи','Станишта и биотопи(Географске области које карактеришу специфични еколошки услови, процеси, структура и функције (за одржавање живота) које физички омогућавају организмима да ту живе. Укључује копнене и водене површине које се разликују својим географским, абиотским и биотским карактеристикама, потпуно природним или полуприродним.)'),
	('Геологија','Геологија(Геологија описана према саставу и структури. Укључује стеновито тло, водоносне слојеве и геоморфологију.)'),
								
)						
#Definisanje "Aneks3" Choice polja za pitanje 3_1
Sekcija3_1_Aneks3_Choices = (
	
	('Распрострањеност врста','Распрострањеност врста(Географска распрострањеност животињских и биљних врста, разврстаних по мрежи, региону, административној јединици или другој аналитичкој јединици.)'),
	('Статистичке јединице','Статистичке јединице(Јединице за дистрибуцију или коришћење статистичких података.)'),
	('Енергетски ресурси','Енергетски ресурси(Енергетски ресурси укључујући угљоводонике, енергију воде, биоенергију, соларну енергију, енергију ветра итд. а по потреби и информације о дубини/висини које се односе на величину ресурса.)'),
	('Зграде','Зграде(Географска локација зграда.)'),
	('Минерални ресурси','Минерални ресурси(Минерални ресурси укључују руде метала, индустријске минерале итд. а по потреби и информације о дубини/висини  које се односе на величину ресурса.)'),
	('Тло','Тло(Тло и слојеви тла испод површине описани према дубини, текстури, структури и садржају честица и органског материјала, каменитости, ерозији, а по потреби просечног нагиба и предвиђени капацитет за чување воде.)'),	
)

#Definisanje Klasa Aneks1, Aneks2, Aneks3 Za Potrebe Klase Pitanj3_1
class Aneks1(models.Model):
	Aneks1_polje= models.CharField(max_length = 100, choices = Sekcija3_1_Aneks1_Choices)

class Aneks2(models.Model):
	Aneks2_polje= models.CharField(max_length = 100, choices = Sekcija3_1_Aneks2_Choices)

class Aneks3(models.Model):
	Aneks3_polje= models.CharField(max_length = 100, choices = Sekcija3_1_Aneks3_Choices)


#Definisanje Klase Pitanje3_1 za Potrebe Prvog Pitanja u Klasi ProstorniPodaci
class Pitanje3_1(models.Model):
	'''Aneks1 = models.ForeignKey('Aneks1')
	Aneks2 = models.ForeignKey('Aneks2')
	Aneks3 = models.ForeignKey('Aneks3') '''
	Aneks1_polje= MultiSelectField(choices = Sekcija3_1_Aneks1_Choices, null=True, blank=True)
	Aneks2_polje= MultiSelectField(choices = Sekcija3_1_Aneks2_Choices, null=True, blank=True)
	Aneks3_polje= MultiSelectField(choices = Sekcija3_1_Aneks3_Choices, null=True, blank=True)
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)
#####################################################################################################################################################################3
###########################################################################################Pitanje3_2#############################################################################################3

#Definisanje "Nacin Skladistenja " CHOICE polja u pitanju 3_2
Sekcija3_2_Nacin_Skladistenja_Choices = (
	
	('gdb','ESRI file geodatabase (*.gdb)'),
	('mdb','ESRI personal geodatabase (*.mdb)'),
	('MS Access','MS Access'),
	('Oracle ','Oracle '),
	('PostgreSQL','PostgreSQL'),
	('MicrosoftSQL','MicrosoftSQL'),
	('Фолдерска структура на серверима','Фолдерска структура на серверима'),
	('Остало','Остало')
)
									
#Definisanje "Format Distribucije " CHOICE polja u pitanju 3_2
Sekcija3_2_Format_Distribucije_Choices = (
	
	('Adobe PDF', 'Adobe PDF (*.pdf)'),
	('ASCII gridded', 'ASCII gridded data format (*.xyz)'),
	('GeoTIFF', 'GeoTIFF (*.tif)'),
	('TIFF', 'TIFF (*.tif)'),
	('CorelDraw', 'CorelDraw file format (*.cdr)'),
	('TIFF', 'TIFF (*.tif), TFW (*.tfw)'),
	('ECW', 'ECW Image file format (*.ecw)'),
	('MrSID', 'MrSID file format (*.sid)'),
	('ESRI', 'ESRI shapefile (*.shp)'),
	('MapInfo ', 'MapInfo TAB format (*.tab)'),
	('KML', 'KML file format (*.kml, *.kmz)'),
	('IMG ', 'IMG file format (*.img)'),
	('NTF', 'NTF Image file format (*.ntf)'),
	('AutoCAD DXF', 'AutoCAD DXF (*.dxf)'),
	('ESRI file', 'ESRI file geodatabase (*.gdb)'),
	('ESRI personal', 'ESRI personal geodatabase (*.mdb)'),
	('JPG', 'JPG file format (*.jpg)'),
	('Microsoft Excel', 'Microsoft Excel file format (*.xls)'),
	('Остало', 'Остало')
)	
#Definisanje "Nacin Distribucije " CHOICE polja u pitanju 3_2
Sekcija3_2_Nacin_Distribucije_Choices = (
	
	('Поштом','Поштом'),
	('Преко имејла','Преко имејла'),
	('Директно преузимање ','Директно преузимање (дигитални медиј, папир)'),
	('Преузимање преко интернета','Преузимање преко интернета (download: HTTP и FTP )'),
	('Web сервиси','Web сервиси'),
	('Остало', 'Остало')
)
										
#Definisanje "Koordinatni Sistem " CHOICE polja u pitanju 3_2
Sekcija3_2_Koordinatni_Sistem_Choices = (
	
	('Гаус-Кригер','Гаус-Кригер'),
	('ETRS89/UTM','ETRS89/UTM'),
	('Географски координатни систем','Географски координатни систем'),
	('Подаци нису просторно одређени','Подаци нису просторно одређени - геореференцирани'),
	('Остало', 'Остало')
)

#Definisanje "Period Azuriranja" CHOICE polja u pitanju 3_2
Sekcija3_2_Period_Azuriranja_Choices = (
	
	('У континуитету','У континуитету'),
	('По потреби','По потреби'),
	('Периодично','Периодично – на сваких XXX дана'),
	('Према прописима','Према прописима'),
	('Преиспитивање плана','Преиспитивање плана'),
	('Остало','Остало'),
)

#Definisanje "Dostupnost Web Servis i Prava Pristupa" CHOICE polja u pitanju 3_2
Sekcija3_2_Dop_Web_Prava = (('интерно','интерно'),('доступно свима','доступно свима'))

#Definisanje Klase Pitanje3_2 za Potrebe Drugog Pitanja u Klasi ProstorniPodaci
class Pitanje3_2(models.Model):
	Naziv_Proizvoda = models.CharField(max_length = 100)
	Opis_Proizvoda = models.CharField(max_length = 100) 
	Digitalni_Format = models.BooleanField(max_length = 100)#Proveriti ChiceField ili nesto drugo 
	Nacin_skladistenja = MultiSelectField(max_length = 1000, choices = Sekcija3_2_Nacin_Skladistenja_Choices)
	Nacin_skladistenja_ostalo = models.CharField(max_length=100, verbose_name="Начин складиштења остало", null=True, blank=True)

	Format_Distribucije = MultiSelectField(max_length = 1000, choices = Sekcija3_2_Format_Distribucije_Choices) 
	Format_Distribucije_ostalo = models.CharField(max_length=100, verbose_name="Формат Дистрибуције остало", null=True, blank=True)

	Nacin_Distribucije = MultiSelectField(max_length = 1000, choices = Sekcija3_2_Nacin_Distribucije_Choices) 
	Nacin_Distribucije_ostalo = models.CharField(max_length=100, verbose_name="Начин Дистрибуције остало", null=True, blank=True)

	Tacnost = models.CharField(max_length = 100) #Sta je obvo polje

	Koordinatni_Sistem = MultiSelectField(max_length = 1000, choices = Sekcija3_2_Koordinatni_Sistem_Choices)
	Koordinatni_Sistem_ostalo = models.CharField(max_length=100, verbose_name="Координатни систем остало", null=True, blank=True)
	
	Obuhvaceno_Podrucje = models.CharField(max_length = 100)
	#Godina_azuriranja =  
	Period_Azuriranja = models.CharField(max_length = 100, choices = Sekcija3_2_Period_Azuriranja_Choices)
	Period_Azuriranja_ostalo = models.CharField(max_length=100, verbose_name="Период ажурирања остало", null=True, blank=True)

	Metapodaci = models.BooleanField() 
	Dostupnost = models.CharField(max_length = 1000, choices = Sekcija3_2_Dop_Web_Prava ) 
	Web_Servis = models.CharField(max_length = 1000, choices = Sekcija3_2_Dop_Web_Prava ) 
	Prava_Pristupa = models.CharField(max_length = 1000, choices = Sekcija3_2_Dop_Web_Prava ) 
	Naknada = models.BooleanField()
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)
#####################################################################################################################################################################3
###########################################################################################Pitanje3_3#############################################################################################3

#Definisanje "Proizvod" CHOICE polja u pitanju 3_3
Sekcija3_3_Proizvod_Choices = (
								('Катастарске парцеле и објекти','Катастарске парцеле и објекти'),
								('Подаци катастра непокретности','Подаци катастра непокретности'),
								('Ортофото','Ортофото'),
								('Адресе','Адресе'),
								('Топографске карте','Топографске карте (1:20 000 и ситније размере)'),
								('Основна државна карта','Основна државна карта (1:5000; 1:10 000)'),
								('Просторни планови','Просторни планови'),
								('Друго','Друго'),
							)
							
#Definisanje "Proizvodjac" CHOICE polja u pitanju 3_3
Sekcija3_3_Proizvodjac_Choices = (
	
	('РГЗ','Републички геодетски завод'),
	('ВГИ','Војногеографски институт'),
	('Завод за заштиту природе Србије','Завод за заштиту природе Србије'),
	('Републички завод за статистику','Републички завод за статистику'),
	('Републичка дирекција за воде','Републичка дирекција за воде'),
	('Републички хидрометролошки завод','Републички хидрометролошки завод'),
	('Завод за заштиту споменика културе','Завод за заштиту споменика културе'),
	('ЈП Пошта Србије','ЈП Пошта Србије'),
	('ЈП Путеви Србије','ЈП Путеви Србије'),
	('European Environment Agency','European Environment Agency (EEA)'),
	('Друго','Друго')
)

#Definisanje "Prostorni Obuhvat" CHOICE polja u pitanju 3_3
Sekcija3_3_Prostorni_Obuhvat_Choices = (
	
	('Територија Републике Србије','Територија Републике Србије'),
	('Територија административне надлежности организације','Територија административне надлежности организације'),
	('Друго','Друго')
)

#Definisanje Klase Pitanje3_3 za Potrebe Treceg Pitanja u Klasi ProstorniPodaci
class Pitanje3_3(models.Model):
	Proizvod = models.CharField(max_length = 100, choices = Sekcija3_3_Proizvod_Choices)
	Proizvodjac = models.CharField(max_length = 100, choices = Sekcija3_3_Proizvodjac_Choices)
	Prostorni_Obuhvat = models.CharField(max_length = 100, choices = Sekcija3_3_Prostorni_Obuhvat_Choices)
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)
#####################################################################################################################################################################3
###########################################################################################Pitanje3_4#############################################################################################3

#Definisanje "Univerzalnog Izbora za Klasu Pitanje3_4" CHOICE polja u pitanju 3_4
Sekcija3_4_Univerzalni_Za_Sve_Choices = (
	
	('Није од значаја','Није од значаја'),
	('Делимично значајно','Делимично значајно'),
	('Значајно','Значајно'),
	('Од великог значаја','Од великог значаја'),
	('Изузетно значајно','Изузетно значајно'),
)
#Definisanje Klase Pitanje3_4 Za Potrebe Cetvrtog Pitanja u Klasi ProstorniPodaci
class Pitanje3_4(models.Model):
	Koordinatni_referentni_sistemi = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Geografski_mrezni_sistemi = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Geografska_imena = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Administrativne_jedinice = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Adrese = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Katastarske_parcele = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Transportne_mreze = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Hidrografija = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Zasticena_podrucja = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Visine = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Zemljisni_pokrivac = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Ortofoto = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Geologija = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Statisticke_jedinice = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Zgrade = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Tlo = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Koriscenje_zemljista = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Zdravlje_ljudi_I_bezbednost = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Vodovi_i_javni_servisi = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Sistemi_za_pracenje_kvaliteta_zivotne_sredine = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Proizvodni_i_industrijski_sistemi = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Sistemi_za_poljoprivredu_i_akvakulturu = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Rasprostranjenost_stanovnistva_demografija = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Oblast_upravljanja = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Zone_prirodnog_rizika = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Atmosferski_uslovi = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Meteorolosko_geografske_karakteristike = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Biogeografski_Regioni = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Stanista_i_biotopi = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Rasprostranjenost_vrsta = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Energetski_resursi = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Mineralni_resursi = models.CharField(max_length = 100,choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)	
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)
#####################################################################################################################################################################3
########################################################################################### Pitanje3_5 #############################################################################################3
#Definisanje "Proizvod" CHOICE polja u pitanju 3_5	
Sekcija3_5_Proizvod_Choices = (
	('Катастарске парцеле и објекти','Катастарске парцеле и објекти'),
	('Подаци катастра непокретности','Подаци катастра непокретности'),
	('Ортофото','Ортофото'),
	('Адресе','Адресе'),
	('Топографске карте ','Топографске карте (1:20 000 и ситније размере)'),
	('Основна државна карта','Основна државна карта (1:5000; 1:10 000)'),
	('Просторни планови','Просторни планови'),
	('Друго','Друго')
)
							
#Definisanje "Proizvodjac" CHOICE polja u pitanju 3_5	
Sekcija3_5_Proizvodjac_Choices = (
	('РГЗ','Републички геодетски завод'),
	('ВГИ','Војногеографски институт'),
	('Завод за заштиту природе Србије','Завод за заштиту природе Србије'),
	('Републички завод за статистику','Републички завод за статистику'),
	('Републичка дирекција за воде','Републичка дирекција за воде'),
	('Републички хидрометролошки завод','Републички хидрометролошки завод'),
	('Завод за заштиту споменика културе','Завод за заштиту споменика културе'),
	('ЈП Пошта Србије','ЈП Пошта Србије'),
	('ЈП Путеви Србије','ЈП Путеви Србије'),
	('European Environment Agency','European Environment Agency (EEA)'),
	('Друго','Друго')
) 
	
#Definisanje "Razlog NEdostupnosti" CHOICE polja u pitanju 3_5
Sekcija3_5_Razlog_Nedostupnosti_Choices = (
	
	('Цена','Цена'),
	('Непостојање','Непостојање'),
	('Неажурност','Неажурност'),
	('Недоступност на интернету','Недоступност на интернету'),
	('Начин преузимања','Начин преузимања'),
	('Непокривеност','Непокривеност'),
	('Непостојање дигиталне форме','Непостојање дигиталне форме'),
	('Лоша садрадња са надлежном организацијом','Лоша садрадња са надлежном организацијом'),
	('Тајност података','Тајност података'),
	('Друго','Друго')
)

#Definisanje "Razlog NEdostupnosti" CHOICE polja u pitanju 3_5
Sekcija3_5_Prostorni_Obuhvat_Choices = (
	
	('Територија Републике Србије', 'Територија Републике Србије'),
	('Територија административне надлежности организације', 'Територија административне надлежности организације'),
	('Друго', 'Друго')
)		

										
#Definisanje Klase Pitanje3_5 Za Potrebe Petog Pitanja u Klasi ProstorniPodaci	
class Pitanje3_5(models.Model):
	Proizvod = models.CharField(max_length = 100,choices = Sekcija3_5_Proizvod_Choices)
	Proizvodjac = models.CharField(max_length = 100,choices = Sekcija3_5_Proizvodjac_Choices)
	Prostorni_obuhvat = models.CharField(max_length = 100,choices = Sekcija3_5_Prostorni_Obuhvat_Choices)
	Razlog_nedostupnosti = models.CharField(max_length = 100,choices = Sekcija3_5_Razlog_Nedostupnosti_Choices)	
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)

#Definisanje "Razmena Podataka" CHOICE polja u pitanju 3_6	
Sekcija3_6_Razmena_Podataka_Choices = (
	
	('Немамо искуства и потребе','Немамо искуства и потребе'),
	('Немамо искуства, имамо потребе','Немамо искуства, имамо потребе'),
	('Имамо искуства и потребе','Имамо искуства и потребе'),
)

#Definisanje "Izrada Servisa" CHOICE polja u pitanju 3_7	
Sekcija3_7_Izrada_servisa_Choices = (
	
	('Немамо капацитета, није у плану изградња капацитета','Немамо капацитета, није у плану изградња капацитета'),
	('Немамо капацитета, у плану је изградња капацитета','Немамо капацитета, у плану је изградња капацитета'),
	('Имамо капацитета, још увек не постоје креирани сервиси','Имамо капацитета, још увек не постоје креирани сервиси'),
	('Имамо капацитета, постоје креирани сервиси','Имамо капацитета, постоје креирани сервиси'),
)

#Definisanje "Obrazovanje" CHOICE polja u pitanju 3_8	
Sekcija3_8_Obrazovanje = (
	
	('Стандардизација геопроизвода и сервиса', 'Стандардизација геопроизвода и сервиса'),
	('Дефинисање техничке спецификације за геоподатке', 'Дефинисање техничке спецификације за геоподатке'),
	('Метаподаци', 'Метаподаци (креирање, стандардизације, израда каталога и сервиса)'),
	('Израда web сервиса за геоподатке', 'Израда web сервиса за геоподатке'),
	('Развој техничке инфраструктуре', 'Развој техничке инфраструктуре'),
	('Креирања тематских речника', 'Креирања тематских речника'),
	('Дефинисање политике размене, приступа и безбедности података', 'Дефинисање политике размене, приступа и безбедности података'),
	('Друго', 'Друго'),
)

#Definisanje "Razmena podataka" CHOICE polja u pitanju 3_9	
Selekcija3_9_Razmena_podataka_Choices = (
	
	('Директно преузимање', 'Директно преузимање (дигитални медиј, папир)'),
	('Преузимање преко интернета', 'Преузимање преко интернета (download: HTTP и FTP )'),
	('Web сервиси', 'Web сервиси'),
)
	

#Definisanje Klase ProstorniPodaci
class ProstorniPodaci(models.Model):
	Za_koje_od_navedenih_INSPIRE_tema_proizvodite_podatke = models.ForeignKey('Pitanje3_1') 
	Uneti_podatke_o_podacima_koje_vasa_organizacija_proizvodi = models.ForeignKey('Pitanje3_2') 
	Koje_prostorne_podatke_nabavljate_od_drugih = models.ForeignKey('Pitanje3_3')
	Odrediti_vazne_podatke_od_drugih_organizacija_za_redovne_aktivnosti = models.ForeignKey('Pitanje3_4')
	Za_kojim_prostornim_podacima_imate_potrebu_a_koji_nisu_dostupni = models.ForeignKey('Pitanje3_5')
	Da_li_imate_potrebu_za_razmenm_prostornih_podataka = models.CharField(max_length = 100, choices = Sekcija3_6_Razmena_Podataka_Choices)
	Da_li_imate_kapaciteta_za_izradu_servisa = models.CharField(max_length = 100, choices = Sekcija3_7_Izrada_servisa_Choices)
	Dodatno_obrazovanje_u_okviru_organizacije = MultiSelectField(max_length = 1000, choices = Sekcija3_8_Obrazovanje)
	Dodatno_obrazovanje_u_okviru_organizacije_drugo = models.CharField(max_length=100, verbose_name="Додатно образовање друго", null=True, blank=True)
	
	Nacin_razmene_podataka_sa_drugima = MultiSelectField(max_length = 1000, choices = Selekcija3_9_Razmena_podataka_Choices)
	Stav_o_razmeni_podataka = models.TextField()
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)

#**************************************** Saradnja Izmedju Subjekata NIGIP-a *********************************************************************************#
#*****************************************************************************************************************************# 

#Definisanje "Obezbedjivanje podataka" CHOICE polja u pitanju 4_1
Selekcija4_1_Obezbedjivanje_Podataka_Choices = (
	('Сопствена производња података', 'Сопствена производња података'),
	('Набавка кроз пројекте', 'Набавка кроз пројекте'),
	('Преузимањем од других државних органа без накнаде', 'Преузимањем од других државних органа без накнаде'),
	('Куповина', 'Куповина'),
	('Друго', 'Друго')
)

#Definisanje "Saradnja Razmena" CHOICE polja u pitanju 4_2
Selekcija4_2_saradnja_Razmena_Choices = (
	
	('По захтеву', 'По захтеву'),
	('На основу уговора/споразума', 'На основу уговора/споразума'),
	('На основу закона', 'На основу закона'),
	('Друго', 'Друго'),
)


#Definisanje "Korisnici Proizvoda" CHOICE polja u pitanju 4_4
Selekcija4_3_Korisnici_Proizvoda_Choices = (
	('Сопствене потребе', 'Сопствене потребе'),
	('Органи државне управе', 'Органи државне управе'),
	('Органи територијалне аутономије', 'Органи територијалне аутономије'),
	('Органи локалне самоуправе', 'Органи локалне самоуправе'),
	('Јавне агенције', 'Јавне агенције'),
	('Јавна предузећа', 'Јавна предузећа'),
	('Научно-образовне установе', 'Научно-образовне установе'),
	('Пројектантскo-урбанистичке организације', 'Пројектантскo-урбанистичке организације'),
	('Приватне организације', 'Приватне организације'),
	('Европске и друге међународне институције', 'Европске и друге међународне институције'),
	('Грађани', 'Грађани'),
	('Друго', 'Друго'),
)

#Definisanje "Cene Geopodaci" CHOICE polja u pitanju 4_4
Selekcija4_4_Cene_Geopodaci_Choices = (
	
	('Цена се одређује подзаконским актима или сопственим одлукама', 'Цена се одређује подзаконским актима или сопственим одлукама'),
	('Подаци/услуге су бесплатни ', 'Подаци/услуге су бесплатни '),
	('Комбиновани модел ', 'Комбиновани модел ')
)

#Definisanje "Model Finansiranja" CHOICE polja u pitanju 4_5
Selekcija4_5_Cene_Podataka = (
	('Покривање трошкова производње','Покривање трошкова производње'),
	('Тржишна цена','Тржишна цена'),
	('Друго','Друго')
)

#Definisanje "Model Finansiranja" CHOICE polja u pitanju 4_6	
Selekcija4_6_Model_Finansiranja = (
	
	('Покривање трошкова производње из буџета', 'Покривање трошкова производње из буџета за кључне геоподатке, уз размену без накнаде између субјеката НИГП-а'),
	('Накнада за коришћење геоподатака према договореним условима', 'Накнада за коришћење геоподатака према договореним условима'),
	('Тржишни услови', 'Тржишни услови'),
	('Друго', 'Друго')
)

#Definisanje Klase Pitanje4_7 Za Potrebe Sedmog Pitanja u Klasi SaradnjaIzmedjuSubjekata
class Pitanje4_7(models.Model):
	Postojanje_nacionalnog_geoportala = models.CharField(max_length = 100, choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Razvoj_nacionalnog_geoportala = models.CharField(max_length = 100, choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Razmena_podataka_preko_nacionalnog_geoportala = models.CharField(max_length = 100, choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Usaglasavanje_podataka = models.CharField(max_length = 100, choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Interoperabilnost_podataka = models.CharField(max_length = 100, choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Javni_uvid_i_javna_dostupnost = models.CharField(max_length = 100, choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Servis_Za_Pronalazenje = models.CharField(max_length = 100, choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Servis_Za_Pregled = models.CharField(max_length = 100, choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Servis_Za_Preuzimanje = models.CharField(max_length = 100, choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Servis_Za_Transformaciju = models.CharField(max_length = 100, choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Servis_za_povezivanje_mreznih_servisa = models.CharField(max_length = 100, choices = Sekcija3_4_Univerzalni_Za_Sve_Choices)
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)

#Definisanje "Problemi Nabavka" CHOICE polja u pitanju 4_10
Selekcija4_10_Problemi_Nabavka_Choices = (
	
	('Непостојање геоподатака у дигиталној форми ', 'Непостојање геоподатака у дигиталној форми '),
	('Слабо доступне информације о надлежној организацији за одређене геоподатке', 'Слабо доступне информације о надлежној организацији за одређене геоподатке'),
	('Стари/неажурни подаци', 'Стари/неажурни подаци'),
	('Некомплетни подаци', 'Некомплетни подаци (просторни обухват и атрибути)'),
	('Неодговарајући квалитет података', 'Неодговарајући квалитет података'),
	('Високе цене', 'Високе цене'),
	('Некомпатибилни формати података', 'Некомпатибилни формати података'),
	('Сложене и нејасне процедуре', 'Сложене и нејасне процедуре'),
	('Кашњење у испоруци', 'Кашњење у испоруци'),
	('Неодговарајућа корисничка подршка', 'Неодговарајућа корисничка подршка'),
	('Ограничена права приступа ', 'Ограничена права приступа '),
	('Друго', 'Друго')
)
										
#Definisanje Klase Saradnja Izmedju Subjekata 
class SaradnjaIzmedjuSubjekata(models.Model):
	Na_koji_nacin_obezbedjujete_podatke_za_svoje_potrebe = MultiSelectField(max_length = 200, choices = Selekcija4_1_Obezbedjivanje_Podataka_Choices)
	Na_koji_nacin_obezbedjujete_podatke_za_svoje_potrebe_drugo = models.CharField(max_length=100, verbose_name="На који начин обезбеђујете податке за своје потребе друго", null=True, blank=True)

	Na_koji_nacin_saradjujete_sa_drugim_organizacijama_pri_razmeni = MultiSelectField(max_length = 200, choices = Selekcija4_2_saradnja_Razmena_Choices)
	Na_koji_nacin_saradjujete_sa_drugim_organizacijama_pri_razmeni_drugo = models.CharField(max_length=100, verbose_name="На који начин сарађујете са другим организацијама при размени података друго", null=True, blank=True)

	Ko_su_korisnici_vasih_proizvoda = MultiSelectField(max_length = 200, choices = Selekcija4_3_Korisnici_Proizvoda_Choices)
	Ko_su_korisnici_vasih_proizvoda_drugo = models.CharField(max_length=100, verbose_name="Ко су корисници Ваших производа друго", null=True, blank=True)
	
	Koja_je_cenovna_politika_za_geopodatke = MultiSelectField(max_length = 1000, choices = Selekcija4_4_Cene_Geopodaci_Choices)
	
	Model_odredjivanja_cene = MultiSelectField(max_length = 200, choices = Selekcija4_5_Cene_Podataka)
	Model_odredjivanja_cene_drugo = models.CharField(max_length=100, verbose_name="Модел одређивања цене друго", null=True, blank=True)
	
	Kojem_modelu_finansiranja_NGIPA_treba_teziti = MultiSelectField(max_length = 200, choices = Selekcija4_6_Model_Finansiranja) 
	Kojem_modelu_finansiranja_NGIPA_treba_teziti_drugo = models.CharField(max_length=100, verbose_name="Којем моделу финансирања НИГП-а треба тежити друго", null=True, blank=True)
	
	Uloga_nacionalnog_geoportala = models.ForeignKey('Pitanje4_7') 
	Da_li_Podrzavate_razmenu_podataka_preko_portala_e_placanje = models.CharField(max_length = 100, choices = (('Da', 'Да, подржавамо'),('Ne', 'Не, не подржавамо')), null=True, blank=True)
	Da_li_postoji_prepreka_razmeni_preko_portala_e_placanje = models.TextField()
	
	Problemi_prilikom_nabavke_geopodataka = MultiSelectField(max_length = 200, choices = Selekcija4_10_Problemi_Nabavka_Choices) 
	Problemi_prilikom_nabavke_geopodataka_drugo = models.CharField(max_length=100, verbose_name="Проблеми приликом набавке геоподатака друго", null=True, blank=True)

	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)

#**************************************** Standardizacija i koncept otvorenih podataka *********************************************************************************#
#*****************************************************************************************************************************# 
#Definisanje "Univerzalno" CHOICE polja u pitanju 5_1
Selekcija5_1_Univerzalno = (
	
	('Користи се', 'Користи се'),
	('Делимично', 'Делимично'),
	('Потребно', 'Потребно'),
	('Не користи се', 'Не користи се'),
	('Нисмо упознати са стандардом', 'Нисмо упознати са стандардом'),
)

#Definisanje Klase Pitanje5_1 Za Potrebe Prvog Pitanja u Klasi Standardizacija Otvorenih Podataka
class Pitanje5_1(models.Model):
	Inspire = models.CharField(max_length = 100, choices = Selekcija5_1_Univerzalno)
	Iso_i_Cen = models.CharField(max_length = 100, choices = Selekcija5_1_Univerzalno)
	OGC = models.CharField(max_length = 100, choices = Selekcija5_1_Univerzalno)
	W3C = models.CharField(max_length = 100, choices = Selekcija5_1_Univerzalno)
	Standardi_proizvodjaca_gis_softvera = models.CharField(max_length = 100, choices = Selekcija5_1_Univerzalno)
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)

#Definisanje Klase Pitanje5_2 Za Potrebe Drugog Pitanja u Klasi Standardizacija Otvorenih Podataka
class Pitanje5_2(models.Model):
	Standard = models.CharField(max_length = 100, null=True, blank=True)
	Upotreba = models.TextField(null=True, blank=True)
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)

#Definisanje "Koriscenje Zastita" CHOICE polja u pitanju 5_3
Selekcija5_3_Koriscenje_Zastita = (
	
	('copyright', 'copyright'),
	('ауторизација приступа', 'ауторизација приступа'),
	('бекап', 'бекап'),
	('ограничена права приступа ', 'ограничена права приступа '),
	('GеоDRM', 'GеоDRM – Digital Right Management'),
	('Друго', 'Друго'),
)	

#Definisanje Klase Pitanje5_4 Za Potrebe Cetvrtog Pitanja u Klasi Standardizacija Otvorenih Podataka
class Pitanje5_4(models.Model):
    	
	Da_ne = models.CharField(max_length = 100, choices = (('Da', 'Да'),('Ne', 'Не')))
	Naziv_akta = models.CharField(max_length = 100, null=True, blank=True)
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)

#Definisanje "Prikupljanje Podataka" CHOICE polja u pitanju 5_5
Selekcija5_5_Prikupljanje_Podataka_Choices = (
	
	('Да ', 'Да '),
	('Не', 'Не'),
	('Друго', 'Друго'),
)	

#Definisanje "Postojeci Portali" CHOICE polja u pitanju 5_6
Selekcija5_6_Postojeci_Portali_Choices = (
	
	('data.gov.rs', 'Национални OpenData портал (data.gov.rs) '),
	('data.poverenik.rs', 'Портал отворених података Повереника за информације од јавног значаја и заштиту података о личности (data.poverenik.rs)'),
	('SHARE', 'Платформа SHARE фондације'),
	('Друго', 'Друго'),
)

#Definisanje "Korisceni podaci" CHOICE polja u pitanju 5_7
Selekcija5_7_Korisceni_Podaci_Choices = (
	
	('OpenData ', 'Користили смо, преузимањем са националног OpenData портала '),
	('Преуѕимање са других портала', 'Користили смо, преузимањем са других постојећих портала'),
	('Стандардни начин', 'Користили смо, преузимањем на стандардан начин (дигитални медиј, папир, поштом, преко имејла, и сл.)'),
	('Нисмо користили', 'Нисмо користили, планирамо интензивније коришћење отворених података у будућности'),
	('Друго', 'Друго'),
)

#Definisanje "Format Podataka" CHOICE polja u pitanju 5_8
Selekcija5_8_Koriscenje_Podataka_Choices = (
	
	('Креирање web сајта или мобилне апликације ', 'Креирање web сајта или мобилне апликације '),
	('Креирање web сервиса', 'Креирање web сервиса'),
	('Извештаји, радови или презентације', 'Извештаји, радови или презентације'),
	('Интеграција са већ постојећим web сајтовима или мобилним апликацијама', 'Интеграција са већ постојећим web сајтовима или мобилним апликацијама'),
	('Креирање тематских карата или сличних визуелизација отворених података', 'Креирање тематских карата или сличних визуелизација отворених података'),
	('Статистичке анализе', 'Статистичке анализе'),
	('Друго', 'Друго'),
)



#Definisanje "Format Podataka" CHOICE polja u pitanju 5_9
Selekcija5_9_Format_Podataka_Choices = (
	
	('CSV', 'Comma Separated Values file format (*.csv) '),
	('XLS', 'Microsoft Excel file format (*.xls)'),
	('PDF', 'Adobe PDF (*.pdf)'),
	('TIFF', 'Tagged Image File Format (*.tif)'),
	('CDR', 'CorelDraw file format (*.cdr)'),
	('SHP', 'ESRI shapefile (*.shp)'),
	('XML', 'Extensible Markup Language (*.xml)'),
	('KML', 'Keyhole Markup Language (*.kml, *.kmz)'),
	('DXF', 'AutoCAD file format (*.dxf)'),
	('JSON', 'JavaScript Object Notation (*.json)'),
	('Друго', 'Друго'),
)	

#Definisanje "Vrsta podataka" CHOICE polja u pitanju 5_10
Selekcija5_10_Vrsta_Podataka_Choices = (
	
	('Геоподаци ', 'Геоподаци '),
	('Финансијски подаци', 'Финансијски подаци'),
	('Статистички подаци', 'Статистички подаци'),
	('Научни подаци', 'Научни подаци'),
	('Подаци о времену', 'Подаци о времену'),
	('Подаци о култури', 'Подаци о култури'),
	('Подаци о животној средини', 'Подаци о животној средини'),
	('Подаци јавног сектора', 'Подаци јавног сектора'),
	('Друго', 'Друго')
)

#Definisanje Klase Pitanje5_12 Za Potrebe Dvanaestog Pitanja u Klasi Standardizacija Otvorenih Podataka
class Pitanje5_12(models.Model):
	Prepreka1 = models.TextField()
	Prepreka2 = models.TextField(blank=True, null=True)
	Prepreka3 = models.TextField(blank=True, null=True)
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)

#Definisanje "Vaznost prepreke Univerzalno" CHOICE polja u pitanju 5_13
Selekcija5_13_Vaznost_Prepreke_Univerzalno_Choices = (
	
	('Није од значаја', 'Није од значаја'),
	('Делимично значајно', 'Делимично значајно'),
	('Значајно', 'Значајно'),
	('Од великог значаја', 'Од великог значаја'),
	('Изузетно значајно', 'Изузетно значајно')
)

#Definisanje Klase Pitanje5_13 Za Potrebe Trinaestog Pitanja u Klasi Standardizacija Otvorenih Podataka
class Pitanje5_13(models.Model):
	Prepreka1 = models.CharField(max_length = 100, choices = Selekcija5_13_Vaznost_Prepreke_Univerzalno_Choices )
	Prepreka2 = models.CharField(max_length = 100, choices = Selekcija5_13_Vaznost_Prepreke_Univerzalno_Choices )
	Prepreka3 = models.CharField(max_length = 100, choices = Selekcija5_13_Vaznost_Prepreke_Univerzalno_Choices )
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)

#Definisanje "Slaganje Sa Tvrdnjom" CHOICE polja u pitanju 5_14
Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices = (
	('Уопште се не слажем', 'Уопште се не слажем'),
	('Не слажем се', 'Не слажем се'),
	('Неодлучан', 'Неодлучан'),
	('Слажем се', 'Слажем се'),
	('Потпуно се слажем', 'Потпуно се слажем'),
)

#Definisanje Klase Pitanje5_14 Za Potrebe Cetrnaestog Pitanja u Klasi Standardizacija Otvorenih Podataka
class Pitanje5_14(models.Model):
	Otvoreni_podaci_ce_dobrineti_boljem_razumevanju_drzavne_uprave = models.CharField(max_length = 100, choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices, verbose_name="Отворени подаци ће допринети бољем разумевању државне управе" )
	Otvoreni_podaci_ce_dobrineti_razvoju_lokalnih_samouprave = models.CharField(max_length = 100, choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices, verbose_name="Отворени подаци ће допринети развоју локалних самоуправа" )
	Otvoreni_podaci_ce_omoguciti_efikasniju_drzavnu_administraciju = models.CharField(max_length = 100, choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices, verbose_name="Отворени подаци ће омогућити ефикаснију државну админстрацију" )
	Otvoreni_podaci_ce_dobrineti_razvoju_koriscenja_podataka = models.CharField(max_length = 100, choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices, verbose_name="Отворени подаци ће допринети развоју коришћења просторних и других података" )
	
	Otvoreni_podaci_mogu_da_se_koriste_u_druge_svrhe = models.CharField(max_length = 100, choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices, verbose_name="Отворени подаци могу да се користе у комерцијалне сврхе" )
	Korisnici_koji_nisu_u_boljem_razumevanju_drzavne_uprave = models.CharField(max_length = 100, choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices, verbose_name="Корисници који нису у систему државне управе могу боље да искористе податке него органи државне управе"  )
	Svi_podaci_u_konceptu_open_data = models.CharField(max_length = 100, choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices,  verbose_name="Сви просторни подаци које производе органи државне управе треба да буду у концепту опен дата"  )
	Postoji_puno_razloga_da_podaci_ne_budu_opendata = models.CharField(max_length = 100, choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices, verbose_name="Постоји пуно разлога због чега не треба сви просторни подаци да буду у концепту опен дата" )
	Efikiasnija_i_brza_razmena_podataka = models.CharField(max_length = 100, choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices, verbose_name="Отворени подаци ће допринети ефикаснијој и бржој размени података" )
	Efikasnija_i_povoljinja_administracija = models.CharField(max_length = 100, choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices, verbose_name="Отворени подаци ће допринети ефикаснијој и повољнијој администрацији у оквиру државне управе" )
	Kvalitetnije_izvestavanje_ka_evropskim_institucijama = models.CharField(max_length = 100, choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices, verbose_name="Отворени подаци ће допринети квалитетнијим извештавањем према државним и Европским институцијама"  )
	Koristan_za_celokupnu_zajednicu = models.CharField(max_length = 100, choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices, verbose_name="Концепт отворених података је вишеструко користан за целокупну друштвену заједницу" )
	Manja_redudantnost_podataka = models.CharField(max_length = 100, choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices, verbose_name="Концепт отворених података би допринео мањој редудантности података у државном сектору" )
	Dostupni_u_pogodnom_obliku = models.CharField(max_length = 100, choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices, verbose_name="Подаци морају бити доступни у погодном облику који је могуће мењати" )
	Koriscenje_izvan_podrucja_namene = models.CharField(max_length = 100, choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices, verbose_name="Подаци морају имати дозволу за коришћење изван изворног подручја намене и редистрибуцију укључујући укрштање с другим скуповима података"  )
	Kreirati_servis_za_pronalazenje_podataka = models.CharField(max_length = 100, choices = Selekcija5_14_Slaganje_Sa_Tvrdnjom_Choices, verbose_name="Потребно је креирати сервис за проналажење доступних података који би омогућио боље коришћење отворених података" )
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)



#Definisanje "Sufinansiranje podataka" CHOICE polja u pitanju 5_15	
Selekcija5_15_Sufinansiranje_Podataka_Choices = (
	
	('Да', 'Да, заинтересовани смо да учествујемо у суфинансирању'),
	('Не', 'Не, нисмо заинтересовани да учествујемо у суфинансирању'),
	('Друго', 'Друго'),
)
	
#Definisanje Klase Standardizacija Otvorenih Podataka 	
class StandardizacijaOtvorenihPodataka(models.Model):
	Status_standarda = models.ForeignKey('Pitanje5_1') 
	Standardi_iz_oblasti_geoinformacija = models.ForeignKey("Pitanje5_2")
	
	Metode_koriscenja_i_zastite = MultiSelectField(max_length = 1000, choices = Selekcija5_3_Koriscenje_Zastita)
	Metode_koriscenja_i_zastite_drugo = models.CharField(max_length=100, verbose_name="Методе коришћења и заштите друго", null=True, blank=True)
	
	Propis_prava_koriscenja = models.ForeignKey("Pitanje5_4")
	
	Da_li_podrzavate_prikupljanje_geopodataka_prema_konceptu_otvorenih_podataka = models.CharField(max_length = 100, choices = Selekcija5_5_Prikupljanje_Podataka_Choices)
	Da_li_podrzavate_prikupljanje_geopodataka_prema_konceptu_otvorenih_podataka_drugo = models.CharField(max_length=100, verbose_name="Прикупљање према концепту отворениох података друго", null=True, blank=True)

	
	Da_li_ste_upoznati_sa_nekim_od_postojecih_portala = MultiSelectField(max_length = 1000, choices = Selekcija5_6_Postojeci_Portali_Choices)
	Da_li_ste_upoznati_sa_nekim_od_postojecih_portala_drugo = models.CharField(max_length=100, verbose_name="Да листе упознати са неким од постојећих портала друго", null=True, blank=True)

	
	Da_li_ste_koristili_besplatne_setove_podataka = MultiSelectField(max_length = 1000, choices = Selekcija5_7_Korisceni_Podaci_Choices )
	Da_li_ste_koristili_besplatne_setove_podataka_drugo = models.CharField(max_length=100, verbose_name="Да ли сте користили бесплатне сетове података друго", null=True, blank=True)

	
	Za_koje_poslove_ste_koristili_podatke = MultiSelectField(max_length = 1000, choices = Selekcija5_8_Koriscenje_Podataka_Choices)
	Za_koje_poslove_ste_koristili_podatke_drugo = models.CharField(max_length=100, verbose_name="За које послове сте користили податке друго", null=True, blank=True)

	Format_podataka = MultiSelectField(max_length = 1000, choices = Selekcija5_9_Format_Podataka_Choices)
	Format_podataka_drugo = models.CharField(max_length=100, verbose_name="У ком формату су били преузети подаци друго", null=True, blank=True)

	
	Koju_vrstu_podataka_ste_koristili = MultiSelectField(max_length = 1000, choices = Selekcija5_10_Vrsta_Podataka_Choices)
	Koju_vrstu_podataka_ste_koristili_drugo = models.CharField(max_length=100, verbose_name="Коју врсту података сте користили друго", null=True, blank=True)

	
	Opis_projekta_sa_prostornim_podacima = models.TextField() 
	Prepreke_za_uspostavljanje_koncepta_gopodataka = models.ForeignKey("Pitanje5_12")
	Vaznost_Prepreka = models.ForeignKey("Pitanje5_13")
	Koliko_se_slazete_sa_tvrdnjama = models.ForeignKey("Pitanje5_14") 
	
	Sufinansiranje_podataka = models.CharField(max_length = 1000, choices = Selekcija5_15_Sufinansiranje_Podataka_Choices)
	Sufinansiranje_podataka_drugo = models.CharField(max_length=100, verbose_name="Суфинансирање података друго", null=True, blank=True)

	
	Ostalo = models.TextField(verbose_name = "44. Простор за додатни коментар на питања која нису обухваћена овим упитником",
							help_text="Ваше мишљење о стању у геосектору, сарадњи између организација које производе и/или користе\
									  просторне податке, расподели надлежности над сетовима података, ценовној политици и сл.",blank=True, null=True)
	Jedinstveni = models.CharField(max_length = 100, null=True, blank=True)

class SveobuhvatniModel(models.Model):
	Prva_sekcija = models.ForeignKey('OrganizacijaOsnovniPodaci', unique = True)
	Druga_sekcija = models.ForeignKey('KadroviInfrastruktura', unique = True)
	Treca_sekcija = models.ForeignKey('ProstorniPodaci', unique = True)
	Cetvrta_sekcija = models.ForeignKey('SaradnjaIzmedjuSubjekata', unique = True)
	Peta_sekcija = models.ForeignKey('StandardizacijaOtvorenihPodataka', unique = True) 
	
	def __str__(self):
		return "%s %s"%(self.__class__.__name__,self.Prva_sekcija.Naziv_organizacije )
	
	













