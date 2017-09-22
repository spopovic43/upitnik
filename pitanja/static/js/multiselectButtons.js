$(document).ready(function() {
    $('.single_multiple').multiselect({
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onDropdownShow: function(event) {
            /*alert($(event.target).width());
            console.log(event);*/

            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }


    });

    //Vrsta Organizacije
    $('#id_form1-Vrsta_organizacije').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form1-Vrsta_organizacije option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Остало") {
                    $('#div_id_form1-Vrsta_organizacije_drugo').css('display', 'block');
                    $('#id_form1-Vrsta_organizacije_drugo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {
                    $('#div_id_form1-Vrsta_organizacije_drugo').css('display', 'none');
                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form1-Vrsta_organizacije_drugo').css('display', 'none');
            console.log(selected);
        },
        onDropdownShow: function(event) {
            /*alert($(event.target).width());
            console.log(event);*/

            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }
    });

    //Glavna strucna oblast organizacije
    $('#id_form1-Glavna_strucna_oblast_vase_organizacije').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form1-Glavna_strucna_oblast_vase_organizacije option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Остало") {
                    $('#div_id_form1-Glavna_strucna_oblast_vase_organizacije_ostalo').css('display', 'block');
                    $('#id_form1-Glavna_strucna_oblast_vase_organizacije_ostalo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {
                    $('#div_id_form1-Glavna_strucna_oblast_vase_organizacije_ostalo').css('display', 'none');
                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form1-Glavna_strucna_oblast_vase_organizacije_ostalo').css('display', 'none');
            console.log(selected);
        },

        onDropdownShow: function(event) {
            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }
    });

    /* Na_kom_teritorijalnom_nivu_vasa_organizacija_obavlja_delatnost polje */
    $('#id_form1-Na_kom_teritorijalnom_nivu_vasa_organizacija_obavlja_delatnost').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onDropdownShow: function(event) {
            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }
    });

    //Kako se vasa organizacija finansira 
    $('#id_form1-Kako_se_vasa_organizacija_finansira').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form1-Kako_se_vasa_organizacija_finansira option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Остало") {
                    $('#div_id_form1-Kako_se_vasa_organizacija_finansira_ostalo').css('display', 'block');
                    $('#id_form1-Kako_se_vasa_organizacija_finansira_ostalo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {
                    $('#div_id_form1-Kako_se_vasa_organizacija_finansira_ostalo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form1-Kako_se_vasa_organizacija_finansira_ostalo').css('display', 'none');
            console.log(selected);
        },

        onDropdownShow: function(event) {
            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    //Glavne prepreke za koriscenje geoinformacija 
    $('#id_form2-Glavne_prepreke_za_koriscenje_geoinformacija_5').on('click', function() {
        if ($(this).is(":checked")) {
            $('#div_id_form2-Glavne_prepreke_za_koriscenje_geoinformacija_ostalo').css('display', 'block');
        } else {
            $('#div_id_form2-Glavne_prepreke_za_koriscenje_geoinformacija_ostalo').css('display', 'none');
        }


    });

    //Serveri za prostorne podatke
    $('#id_form2-Serveri_za_prostorne_podatke_6').on('click', function() {
        if ($(this).is(":checked")) {
            $('#div_id_form2-Serveri_za_prostorne_podatke_ostalo').css('display', 'block');
        } else {
            $('#div_id_form2-Serveri_za_prostorne_podatke_ostalo').css('display', 'none');
        }

    });

    //11. У ком домену имате потребу за додатним образовањем у оквиру Ваше организације? 
    $('#id_form6-Dodatno_obrazovanje_u_okviru_organizacije').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form6-Dodatno_obrazovanje_u_okviru_organizacije option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Друго") {

                    $('#div_id_form6-Dodatno_obrazovanje_u_okviru_organizacije_drugo').css('display', 'block');
                    $('#id_form6-Dodatno_obrazovanje_u_okviru_organizacije_drugo')
                        .css({ 'border': '1px solid green', 'width': '540px' })
                        .parent()
                        .prev().css('color', 'green');
                } else {
                    //$('#div_id_form6-Dodatno_obrazovanje_u_okviru_organizacije_drugo').val("");

                    $('#div_id_form6-Dodatno_obrazovanje_u_okviru_organizacije_drugo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form6-Dodatno_obrazovanje_u_okviru_organizacije_drugo').css('display', 'none');
            console.log(selected);
        },

        onDropdownShow: function(event) {
            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });


    //15. Начин складиштења
    $('#id_form11-Nacin_skladistenja').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form11-Nacin_skladistenja  option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Остало") {

                    $('#div_id_form11-Nacin_skladistenja_ostalo').css('display', 'block');
                    $('#id_form11-Nacin_skladistenja_ostalo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {
                    $('#div_id_form11-Nacin_skladistenja_ostalo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form11-Nacin_skladistenja_ostalo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    //15. Формат дистрибуције
    $('#id_form11-Format_Distribucije').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form11-Format_Distribucije  option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Остало") {

                    $('#div_id_form11-Format_Distribucije_ostalo').css('display', 'block');
                    $('#id_form11-Format_Distribucije_ostalo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {
                    $('#div_id_form11-Format_Distribucije_ostalo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form11-Format_Distribucije_ostalo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    //15. Начин дистрибуције
    $('#id_form11-Nacin_Distribucije').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form11-Nacin_Distribucije  option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Остало") {

                    $('#div_id_form11-Nacin_Distribucije_ostalo').css('display', 'block');
                    $('#id_form11-Nacin_Distribucije_ostalo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {

                    $('#div_id_form11-Nacin_Distribucije_ostalo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form11-Nacin_Distribucije_ostalo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    //15. Координатни систем
    $('#id_form11-Koordinatni_Sistem').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form11-Koordinatni_Sistem  option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Остало") {

                    $('#div_id_form11-Koordinatni_Sistem_ostalo').css('display', 'block');
                    $('#id_form11-Koordinatni_Sistem_ostalo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {

                    $('#div_id_form11-Koordinatni_Sistem_ostalo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form11-Koordinatni_Sistem_ostalo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    //15. Период ажурирања
    $('#id_form11-Period_Azuriranja').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form11-Period_Azuriranja  option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Остало") {

                    $('#div_id_form11-Period_Azuriranja_ostalo').css('display', 'block');
                    $('#id_form11-Period_Azuriranja_ostalo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {

                    $('#div_id_form11-Period_Azuriranja_ostalo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form11-Period_Azuriranja_ostalo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });



    //19. На који начин обезбеђујете просторне податке за Ваше потребе?
    $('#id_form15-Na_koji_nacin_obezbedjujete_podatke_za_svoje_potrebe').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form15-Na_koji_nacin_obezbedjujete_podatke_za_svoje_potrebe  option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Друго") {
                    $('#div_id_form15-Na_koji_nacin_obezbedjujete_podatke_za_svoje_potrebe_drugo').css('display', 'block');
                    $('#id_form15-Na_koji_nacin_obezbedjujete_podatke_za_svoje_potrebe_drugo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {

                    $('#div_id_form15-Na_koji_nacin_obezbedjujete_podatke_za_svoje_potrebe_drugo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form15-Na_koji_nacin_obezbedjujete_podatke_za_svoje_potrebe_drugo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    // 20. На који начин сарађујете са другим организацијама при размени геоподатака?
    $('#id_form15-Na_koji_nacin_saradjujete_sa_drugim_organizacijama_pri_razmeni').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form15-Na_koji_nacin_saradjujete_sa_drugim_organizacijama_pri_razmeni  option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Друго") {
                    $('#div_id_form15-Na_koji_nacin_saradjujete_sa_drugim_organizacijama_pri_razmeni_drugo').css('display', 'block');
                    $('#id_form15-Na_koji_nacin_saradjujete_sa_drugim_organizacijama_pri_razmeni_drugo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {

                    $('#div_id_form15-Na_koji_nacin_saradjujete_sa_drugim_organizacijama_pri_razmeni_drugo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form15-Na_koji_nacin_saradjujete_sa_drugim_organizacijama_pri_razmeni_drugo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    // 21. Ко су корисници Ваших производа? 
    $('#id_form15-Ko_su_korisnici_vasih_proizvoda').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form15-Ko_su_korisnici_vasih_proizvoda  option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Друго") {
                    $('#div_id_form15-Ko_su_korisnici_vasih_proizvoda_drugo').css('display', 'block');
                    $('#id_form15-Ko_su_korisnici_vasih_proizvoda_drugo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {

                    $('#div_id_form15-Ko_su_korisnici_vasih_proizvoda_drugo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form15-Ko_su_korisnici_vasih_proizvoda_drugo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });
    /*
    //22. Која је ценовна политика за ваше геоподатке/услуге?
    $('#id_form15-Koja_je_cenovna_politika_za_geopodatke').multiselect({
        enableClickableOptGroups:true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups:true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
                    if (options.length === 0) {
                        return 'Ништа од понуђеног није селектовано';
                    }
                    else if (options.length == 1) {
                        return 'Селектовали сте ' + options.length + " одговор";
                    }
                    else if (options.length > 1) {
                        return 'Селектовали сте ' + options.length + " одговора";
                    }
                     
                },
        onChange: function(element, checked) {
            var brands = $('#id_form15-Koja_je_cenovna_politika_za_geopodatke  option:selected');
            
            var selected = [];
            $(brands).each(function(index, brand){
                if($(this).val() == "Друго"){
                    $('#div_id_form15-Koja_je_cenovna_politika_za_geopodatke_drugo').css('display', 'block');
                    $('#id_form15-Koja_je_cenovna_politika_za_geopodatke_drugo')
                                    .css('border', '1px solid green')
                                    .parent()
                                    .prev().css('color', 'green'); 
                }
                else {
                    
                    $('#div_id_form15-Koja_je_cenovna_politika_za_geopodatke_drugo').css('display', 'none');
                    
                }
               
                selected.push([$(this).val()]);
            });
            if(brands.length == 0)
                $('#div_id_form15-Koja_je_cenovna_politika_za_geopodatke_drugo').css('display', 'none');
    
            console.log(selected);
        },

        onDropdownShow: function(event) {
            alert("Djordje Dropdown Show");
            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));
            
            
        }
        
    });

   //25. Да ли подржавате размену података преко портала е-плаћања?
  $('#id_form15-Da_li_Podrzavate_razmenu_podataka_preko_portala_e_placanje').multiselect({
    enableClickableOptGroups:true,
    buttonClass: 'btn btn-default',
    enableClickableOptGroups:true,
    buttonWidth: '540px',
    buttonText: function(options, select) {
                if (options.length === 0) {
                    return 'Ништа од понуђеног није селектовано';
                }
                else if (options.length == 1) {
                    return 'Селектовали сте ' + options.length + " одговор";
                }
                else if (options.length > 1) {
                    return 'Селектовали сте ' + options.length + " одговора";
                }
                 
            },
    onChange: function(element, checked) {
        var brands = $('#id_form15-Da_li_Podrzavate_razmenu_podataka_preko_portala_e_placanje  option:selected');
        alert('Changed');
        var selected = [];
        $(brands).each(function(index, brand){
            if($(this).val() == "Друго"){
                $('#div_id_form15-Da_li_Podrzavate_razmenu_podataka_preko_portala_e_placanje_drugo').css('display', 'block');
                $('#id_form15-Da_li_Podrzavate_razmenu_podataka_preko_portala_e_placanje_drugo')
                                .css('border', '1px solid green')
                                .parent()
                                .prev().css('color', 'green'); 
            }
            else {
                
                $('#div_id_form15-Da_li_Podrzavate_razmenu_podataka_preko_portala_e_placanje_drugo').css('display', 'none');
                
            }
           
            selected.push([$(this).val()]);
        });
        if(brands.length == 0)
            $('#div_id_form15-Da_li_Podrzavate_razmenu_podataka_preko_portala_e_placanje_drugo').css('display', 'none');

        console.log(selected);
    },

    onDropdownShow: function(event) {
        alert($(event.target).width());
        console.log(event);

        var butParent = event.target.style.width;
        var childs = event.target.childNodes
        var child = childs[1];
        //alert($(child).width());
        $(child).width($(event.target).width());
        //alert('Client width');
        //alert($(child).width($(event.target).width()));
        
        
    }
    
});
*/


    //23. Који је модел одређивања цене просторних производа/услуга?
    $('#id_form15-Model_odredjivanja_cene').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form15-Model_odredjivanja_cene  option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Друго") {
                    $('#div_id_form15-Model_odredjivanja_cene_drugo').css('display', 'block');
                    $('#id_form15-Model_odredjivanja_cene_drugo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {

                    $('#div_id_form15-Model_odredjivanja_cene_drugo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form15-Model_odredjivanja_cene_drugo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    //24. Којем моделу финансирања НИГП-а треба тежити?
    $('#id_form15-Kojem_modelu_finansiranja_NGIPA_treba_teziti').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form15-Kojem_modelu_finansiranja_NGIPA_treba_teziti  option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Друго") {
                    $('#div_id_form15-Kojem_modelu_finansiranja_NGIPA_treba_teziti_drugo').css('display', 'block');
                    $('#id_form15-Kojem_modelu_finansiranja_NGIPA_treba_teziti_drugo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');

                } else {

                    $('#div_id_form15-Kojem_modelu_finansiranja_NGIPA_treba_teziti_drugo').css('display', 'none');


                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form15-Kojem_modelu_finansiranja_NGIPA_treba_teziti_drugo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            /*alert($(event.target).width());
            console.log(event);*/

            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    //27. Који су проблеми присутни приликом набавке геоподатака од других организација за Вашу организацију?
    $('#id_form15-Problemi_prilikom_nabavke_geopodataka').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form15-Problemi_prilikom_nabavke_geopodataka  option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Друго") {
                    $('#div_id_form15-Problemi_prilikom_nabavke_geopodataka_drugo').css('display', 'block');
                    $('#id_form15-Problemi_prilikom_nabavke_geopodataka_drugo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {

                    $('#div_id_form15-Problemi_prilikom_nabavke_geopodataka_drugo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form15-Problemi_prilikom_nabavke_geopodataka_drugo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            /*alert($(event.target).width());
            console.log(event);*/

            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    //29. Које од метода коришћења и заштите просторних података користите?
    $('#id_form17-Metode_koriscenja_i_zastite').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form17-Metode_koriscenja_i_zastite  option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Друго") {
                    $('#div_id_form17-Metode_koriscenja_i_zastite_drugo').css('display', 'block');
                    $('#id_form17-Metode_koriscenja_i_zastite_drugo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {

                    $('#div_id_form17-Metode_koriscenja_i_zastite_drugo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form17-Metode_koriscenja_i_zastite_drugo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            /*alert($(event.target).width());
            console.log(event);*/

            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    //30. Да ли подржавате прикупљање референтних скупова података према концепту отворених података?
    $('#id_form17-Da_li_podrzavate_prikupljanje_geopodataka_prema_konceptu_otvorenih_podataka').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form17-Da_li_podrzavate_prikupljanje_geopodataka_prema_konceptu_otvorenih_podataka  option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Друго") {
                    $('#div_id_form17-Da_li_podrzavate_prikupljanje_geopodataka_prema_konceptu_otvorenih_podataka_drugo').css('display', 'block');
                    $('#id_form17-Da_li_podrzavate_prikupljanje_geopodataka_prema_konceptu_otvorenih_podataka_drugo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {

                    $('#div_id_form17-Da_li_podrzavate_prikupljanje_geopodataka_prema_konceptu_otvorenih_podataka_drugo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form17-Da_li_podrzavate_prikupljanje_geopodataka_prema_konceptu_otvorenih_podataka_drugo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            /*alert($(event.target).width());
            console.log(event);*/

            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    //31. Да ли сте упознати са неким од постојећих портала за приступ отвореним подацима?
    $('#id_form17-Da_li_ste_upoznati_sa_nekim_od_postojecih_portala').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form17-Da_li_ste_upoznati_sa_nekim_od_postojecih_portala  option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Друго") {
                    $('#div_id_form17-Da_li_ste_upoznati_sa_nekim_od_postojecih_portala_drugo').css('display', 'block');
                    $('#id_form17-Da_li_ste_upoznati_sa_nekim_od_postojecih_portala_drugo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {

                    $('#div_id_form17-Da_li_ste_upoznati_sa_nekim_od_postojecih_portala_drugo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form17-Da_li_ste_upoznati_sa_nekim_od_postojecih_portala_drugo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            /*alert($(event.target).width());
            console.log(event);*/

            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    //32. Да ли сте користили неки сет података који је јавно доступан према концепту отворених података? 
    $('#id_form17-Da_li_ste_koristili_besplatne_setove_podataka').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form17-Da_li_ste_koristili_besplatne_setove_podataka  option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Друго") {
                    $('#div_id_form17-Da_li_ste_koristili_besplatne_setove_podataka_drugo').css('display', 'block');
                    $('#id_form17-Da_li_ste_koristili_besplatne_setove_podataka_drugo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {

                    $('#div_id_form17-Da_li_ste_koristili_besplatne_setove_podataka_drugo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form17-Da_li_ste_koristili_besplatne_setove_podataka_drugo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            /*alert($(event.target).width());
            console.log(event);*/

            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    //33. За које послове сте користили преузете податке?
    $('#id_form17-Za_koje_poslove_ste_koristili_podatke').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form17-Za_koje_poslove_ste_koristili_podatke  option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Друго") {
                    $('#div_id_form17-Za_koje_poslove_ste_koristili_podatke_drugo').css('display', 'block');
                    $('#id_form17-Za_koje_poslove_ste_koristili_podatke_drugo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {

                    $('#div_id_form17-Za_koje_poslove_ste_koristili_podatke_drugo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form17-Za_koje_poslove_ste_koristili_podatke_drugo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            /*alert($(event.target).width());
            console.log(event);*/

            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    //34. У ком формату су били преузети подаци?
    $('#id_form17-Format_podataka').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form17-Format_podataka option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Друго") {
                    $('#div_id_form17-Format_podataka_drugo').css('display', 'block');
                    $('#id_form17-Format_podataka_drugo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {

                    $('#div_id_form17-Format_podataka_drugo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form17-Format_podataka_drugo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            /*alert($(event.target).width());
            console.log(event);*/

            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    //35. Коју врсту података сте користили?
    $('#id_form17-Koju_vrstu_podataka_ste_koristili').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form17-Koju_vrstu_podataka_ste_koristili option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Друго") {
                    $('#div_id_form17-Koju_vrstu_podataka_ste_koristili_drugo').css('display', 'block');
                    $('#id_form17-Koju_vrstu_podataka_ste_koristili_drugo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {

                    $('#div_id_form17-Koju_vrstu_podataka_ste_koristili_drugo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form17-Koju_vrstu_podataka_ste_koristili_drugo').css('display', 'none');

            console.log(selected);
        },

        onDropdownShow: function(event) {
            /*alert($(event.target).width());
            console.log(event);*/

            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });

    //37. Ако се у пракси не примени ‘Open Data’ концепт, да ли сте заинтересовани да заједно са другим институцијама учествујете у суфинансирању референтних података?
    $('#id_form17-Sufinansiranje_podataka').multiselect({
        enableClickableOptGroups: true,
        buttonClass: 'btn btn-default',
        enableClickableOptGroups: true,
        buttonWidth: '540px',
        buttonText: function(options, select) {
            if (options.length === 0) {
                return 'Ништа од понуђеног није селектовано';
            } else if (options.length == 1) {
                return 'Селектовали сте ' + options.length + " одговор";
            } else if (options.length > 1) {
                return 'Селектовали сте ' + options.length + " одговора";
            }

        },
        onChange: function(element, checked) {
            var brands = $('#id_form17-Sufinansiranje_podataka option:selected');

            var selected = [];
            $(brands).each(function(index, brand) {
                if ($(this).val() == "Друго") {
                    $('#div_id_form17-Sufinansiranje_podataka_drugo').css('display', 'block');
                    $('#id_form17-Sufinansiranje_podataka_drugo')
                        .css('border', '1px solid green')
                        .parent()
                        .prev().css('color', 'green');
                } else {

                    $('#div_id_form17-Sufinansiranje_podataka_drugo').css('display', 'none');

                }

                selected.push([$(this).val()]);
            });
            if (brands.length == 0)
                $('#div_id_form17-Sufinansiranje_podataka_drugo').css('display', 'none');

            console.log(selected);
        },
        onDropdownShow: function(event) {
            /*alert($(event.target).width());
            console.log(event);*/

            var butParent = event.target.style.width;
            var childs = event.target.childNodes
            var child = childs[1];
            //alert($(child).width());
            $(child).width($(event.target).width());
            //alert('Client width');
            //alert($(child).width($(event.target).width()));


        }

    });




    var but = $('.multiselect,.dropdown-toggle');
    but.on('click', function() {
        $(this).css('background-color', 'white');
    });

    var elem = $('#id_form20-Da_ne_2').next();


    //40. Prikaz input polja za ovo pitanje
    $('#div_id_form20-Da_ne > div > div:nth-child(1) > label').on('click', function() {

        $('#div_id_form20-Naziv_akta').css('display', 'block');

    });
    $('#id_form20-Da_ne_3').parent().on('click', function() {

        $('#div_id_form20-Naziv_akta').css('display', 'none');

    });


    //$('.modal-body input[type="checkbox"]').wrap("<label></label>");
    $('tr td input').wrap("<label></label>");
    $('.modal-body #id_form11-Digitalni_Format, #id_form11-Metapodaci, #id_form11-Naknada').wrap("<label></label>");


    //Unwrap label of formsets
    $('#formset25 input').unwrap();
    $('#formset26 input').unwrap();
    $('#formset28 input').unwrap();
    $('#formset33 input').unwrap();
    $('#formset35 input').unwrap();

    $('#formset52 input').unwrap();

    $('input').after("<span></span>");

    /* $('.modal-body input[type="checkbox"]').on('click', function(){
         	    alert("Djole Subiotic");

     });*/

    /*********************************************************************************Ostalo pitanje za modal*************************************************/

    //Nacin Skladistenja
    $('.modal-body #id_form11-Nacin_skladistenja_modal').on('change', function() {
        var sviCekirani = $('.modal-body #id_form11-Nacin_skladistenja_modal option:selected');
        if (sviCekirani.length == 0) {
            $('#div_id_form11-Nacin_skladistenja_ostalo_modal').css('display', 'none');

        }
        sviCekirani.each(function(index, element) {

            if ($(element).val() == "Остало") {

                $('.modal-body  #div_id_form11-Nacin_skladistenja_ostalo_modal').css('display', 'block');
                $('.modal-body  #id_form11-Nacin_skladistenja_ostalo_modal')
                    .css('border', '1px solid green')
                    .parent()
                    .prev().css('color', 'green');
            } else {

                $('#div_id_form11-Nacin_skladistenja_ostalo_modal').css('display', 'none');

            }
        })
    });


    //Format Distribucije
    $('.modal-body #id_form11-Format_Distribucije_modal').on('change', function() {
        var sviCekirani = $('.modal-body #id_form11-Format_Distribucije_modal option:selected');
        if (sviCekirani.length == 0) {
            $('#div_id_form11-Format_Distribucije_ostalo_modal').css('display', 'none');

        }
        sviCekirani.each(function(index, element) {

            if ($(element).val() == "Остало") {

                $('.modal-body  #div_id_form11-Format_Distribucije_ostalo_modal').css('display', 'block');
                $('.modal-body  #id_form11-Format_Distribucije_ostalo_modal')
                    .css('border', '1px solid green')
                    .parent()
                    .prev().css('color', 'green');
            } else {

                $('#div_id_form11-Format_Distribucije_ostalo_modal').css('display', 'none');

            }
        })
    });

    //Nacin Distribucije
    $('.modal-body #id_form11-Nacin_Distribucije_modal').on('change', function() {
        var sviCekirani = $('.modal-body #id_form11-Nacin_Distribucije_modal option:selected');
        if (sviCekirani.length == 0) {
            $('#div_id_form11-Nacin_Distribucije_ostalo_modal').css('display', 'none');
        }
        sviCekirani.each(function(index, element) {

            if ($(element).val() == "Остало") {

                $('.modal-body  #div_id_form11-Nacin_Distribucije_ostalo_modal').css('display', 'block');
                $('.modal-body  #id_form11-Nacin_Distribucije_ostalo_modal')
                    .css('border', '1px solid green')
                    .parent()
                    .prev().css('color', 'green');
            } else {

                $('#div_id_form11-Nacin_Distribucije_ostalo_modal').css('display', 'none');

            }
        })
    });

    //Koordinatni Sistem
    $('.modal-body #div_id_form11-Koordinatni_Sistem_modal').on('change', function() {
        var sviCekirani = $('.modal-body #div_id_form11-Koordinatni_Sistem_modal option:selected');
        if (sviCekirani.length == 0) {
            $('#div_id_form11-Koordinatni_Sistem_ostalo_modal').css('display', 'none');
        }
        sviCekirani.each(function(index, element) {

            if ($(element).val() == "Остало") {

                $('.modal-body  #div_id_form11-Koordinatni_Sistem_ostalo_modal').css('display', 'block');
                $('.modal-body  #id_form11-Koordinatni_Sistem_ostalo_modal')
                    .css('border', '1px solid green')
                    .parent()
                    .prev().css('color', 'green');
            } else {

                $('#div_id_form11-Koordinatni_Sistem_ostalo_modal').css('display', 'none');

            }
        })
    });

    //Period Azuriranja
    $('.modal-body #div_id_form11-Period_Azuriranja_modal').on('change', function() {
        var sviCekirani = $('.modal-body #div_id_form11-Period_Azuriranja_modal option:selected');
        sviCekirani.each(function(index, element) {
            if ($(element).val() == "Остало") {

                $('.modal-body  #div_id_form11-Period_Azuriranja_ostalo_modal').css('display', 'block');
                $('.modal-body  #id_form11-Period_Azuriranja_ostalo_modal')
                    .css('border', '1px solid green')
                    .parent()
                    .prev().css('color', 'green');
            } else {

                $('#div_id_form11-Period_Azuriranja_ostalo_modal').css('display', 'none');

            }
        })
    });



    /*$('.modal-body #id_form11-Nacin_skladistenja_modal option:selected').each(function(index, elem){
        alert($(value).val());
    });*/




});