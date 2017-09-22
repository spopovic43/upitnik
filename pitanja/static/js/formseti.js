$(document).ready(function(){

    /*Java Script for adding, updating and deleting forms from formset*/

    function updateElementIndex(el, prefix, ndx) {
        var id_regex = new RegExp('(' + prefix + '-\d+)');
        var replacement = prefix + '-' + ndx;
        if ($(el).attr("for"))
            $(el).attr("for", $(el).attr("for").replace($(el).attr("for"), replacement));
            
        if (el.id) {
        prefix_for_new_rows = prefix + '-' + $('#id_' + prefix + '-TOTAL_FORMS').val()
            d = 'id_' + prefix_for_new_rows + el.id.substring(22, el.id.length)
            el.id = d;
        }

        if (el.name) {
            prefix_for_new_rows = prefix + '-' + $('#id_' + prefix + '-TOTAL_FORMS').val()
            d = prefix_for_new_rows + el.name.substring(19, el.name.length)
            el.name = d
        }
        
    };

    function addForm(btn, prefix, cname) {
        var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
        var row = $('.' + cname + ':first').clone(false).get(0);
        
        $(row).removeAttr('id').insertAfter($('.' + cname + ':last')).children('.hidden').removeClass('hidden');
        
        $(row).children().not(':last').children().each(function(index,element) {
            
            updateElementIndex(this, prefix, formCount);
            
           
        });
       
        var a = $(row).children().children();
        console.log(a);
        $(row).children().children().each(function(){
            if($(this).hasClass('jedinstveni')){
               // alert("has class Jedinstveni");
                prefix_for_new_rows = prefix + '-' + $('#id_' + prefix + '-TOTAL_FORMS').val()
                id = 'id_' + prefix_for_new_rows + '-Jedinstveni';
                name = prefix_for_new_rows + '-Jedinstveni';
                this.id = id 
                this.name = name

            }
        });
        $(row).find('.delete-row').click(function() {
            deleteForm(this, prefix, cname);
        });
        $('#id_' + prefix + '-TOTAL_FORMS').val(formCount + 1);
        return false;
    };

    function deleteForm(btn, prefix, cname) {
        $(btn).parents('.' + cname).remove();
        var forms = $('.' + cname);
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i = 0, formCount = forms.length; i < formCount; i++) {
            $(forms.get(i)).children().not(':last').children().each(function() {
                updateElementIndex(this, prefix, i);
            });
        }
        return false;
    }

    /***********************************************************************************************************/

    //Pitanje2_8Formset form5 
    $('.add-row_pitanje2_8').click(function() {
        return addForm(this, 'pitanje2_8formset', 'dynamic-form-pitanje2_8');
    });
    $('.delete-row_pitanje2_8').click(function() {
        return deleteForm(this, 'pitanje2_8formset', 'dynamic-form-pitanje2_8');
    })

    //Pitanje2_6Formset form4 
    $('.add-row_pitanje2_6').click(function() {
        return addForm(this, 'pitanje2_6formset', 'dynamic-form-pitanje2_6');
    });
    $('.delete-row_pitanje2_6').click(function() {
        return deleteForm(this, 'pitanje2_6formset', 'dynamic-form-pitanje2_6');
    })

    //Pitanje2_5Formset form3 
    $('.add-row_pitanje2_5').click(function() {
        return addForm(this, 'pitanje2_5formset', 'dynamic-form-pitanje2_5');
    });
    $('.delete-row_pitanje2_5').click(function() {
        return deleteForm(this, 'pitanje2_5formset', 'dynamic-form-pitanje2_5');
    })

    //Pitanje3_3Formset form12 
    $('.add-row_pitanje3_3').click(function() {
        return addForm(this, 'pitanje3_3formset', 'dynamic-form-pitanje3_3');
    });
    $('.delete-row_pitanje3_3').click(function() {
        return deleteForm(this, 'pitanje3_3formset', 'dynamic-form-pitanje3_3');
    })

    //Pitanje3_3Formset form14
    $('.add-row_pitanje3_5').click(function() {
        return addForm(this, 'pitanje3_5formset', 'dynamic-form-pitanje3_5');
    });
    $('.delete-row_pitanje3_5').click(function() {
        return deleteForm(this, 'pitanje3_5formset', 'dynamic-form-pitanje3_5');
    })

    //Pitanje5_2Formset form19
    $('.add-row_pitanje5_2').click(function() {
        return addForm(this, 'pitanje5_2formset', 'dynamic-form-pitanje5_2');
    });
    $('.delete-row_pitanje5_2').click(function() {
        return deleteForm(this, 'pitanje5_2formset', 'dynamic-form-pitanje5_2');
    })

    $(".selectpicker").selectpicker({
        style : "btn-default"

    });

    $('#btnPosalji').on('click',function(e){
       
        e.preventDefault()
        var jedinstveni = $('#id_form1-Naziv_organizacije').val(); 
        $('.jedinstveni').val(jedinstveni); 
       $('#formUpitnik').submit();
       
    });

    /*popover za Aneks pitanja*/ 
    $('[data-toggle="popover"]').popover();
    
    

});
