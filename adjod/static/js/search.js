/*
 * Advance Search - Brands autoload 
 */
// $(window).load(function (){	
// 	    var url = window.location.href;
        
//         if(url.indexOf('/search')>=0)
//         {
//             if($("#typeandbrandtxt").val().length>15)
//             {
//                 valKey = jQuery.trim($("#typeandbrandtxt").val()).substring(0, 15).trim(this) + "...";
//             }
//             else
//             {
//                 valKey = $("#typeandbrandtxt").val();  
//             }            
//             $( "#typeandbrandtxt" ).val(valKey);               
//         }
// }); 
/*
 * Autocomplete_keyword
 */

$(window).load(function(){
    $('.product_images1 img').each(function () {
        $(this).center();
    });
});

$('.search_btn').click(function() {
    validateSearch();
});

$(function() {
// alert("document ready");
    $("#typeandbrandtxt").autocomplete({
        source : "/autocomplete_brandlist",
        select : function(event, ui) {
            $("#typeandbrand").val(ui.item.value);
        },

        close : function(event, ui) {
            valKey = $("#typeandbrandtxt").val();
            $("#typeandbrand").val(valKey);
            if ($("#typeandbrandtxt").val().length > 15) {
                valKey = jQuery.trim(valKey).substring(0, 15).trim(this) + "...";
            } else {
                valKey = $("#typeandbrandtxt").val();
            }
            $("#typeandbrandtxt").val(valKey);                               
        }
    });    
    
});  	

function perform_search(){
            // alert("perform_search");
   
            // $.cookie('keywords', $('input[name=keywords]').val(),{ path: "/" });
            // $.cookie('location', $('input[name=locations]').val(),{ path: "/" });
            // left_dyanmic_height();  
            // $(".infield").inFieldLabels();
            // $(".infield_p").inFieldLabels();
            // show_searching(true);
            // $('[name=rating_start]').val('')
            // $('[name=rating_end]').val('')                                              
            // q = q.replace(/filtersearch/g,'q'); 
            var q = $('#form_search_filter').serialize();
            // alert(q);
    

            //q=decodeURIComponent(q);
            var pageurl = window.location.href;
            //alert(pageurl);
            // var url=pageurl.split('/')[3] + '/' + pageurl.split('/')[4]
            // alert(url);
            // q = q.replace(/filtersearch/g,'q'); 

            var qsort = $("#sorteddata").val();
            q = q +'&sorteddata='+$.trim(qsort);
            // alert(q);
            // var qlang = $("#currentlanguage").val();
            if ($('[name=newsearch]').val() == "new")
            {
                    // alert('top');
                    $.get('v2/search/?'+ q, function(data){                                                           
                        show_searching(false);
                        $('#search_result').html(data);
                       
                        // leadfound= $('.founded_no').text().trim();
                        // if (leadfound == '')
                        //     $('[name=search_founded_no]').val ('0 ' + gettext("Leads found"));
                        // else
                        //      $('[name=search_founded_no]').val($('.founded_no').text().trim());
                        //      $.get('/search/?'+ q, function(data){
                        //       // show_searching(false);
                        //       $('#search_result').html(data);
                        //       attach_pagination_events();
                        //       // if($('[name=keywords]').val() == '')
                        //       //     $('#keyword_highlight').hide();                                     
                        //       // if($('[name=locations]').val() == '')
                        //       //     $('#location_highlight').hide();
                        // });
                        // $.get(url+'/?'+ q, function(data){   
                        //     // alert("enter url")
                        //     // alert(data);
                        //     $('#search_result').html(data);
                        attach_pagination_events();
                        }); 
                        $('.product_images1 img').each(function( index ) {
                                    alert("before call");
                                    $(this).center1();
                        });
                        //  $.get(url+'/?'+ q, function(data){
                        //  alert("enter url")
                        //  alert(data);
                        //  $('#search_result').html(data);                                         
                        // }); 
                        // $('#search_result').html(data); 
                        // attach_pagination_events();
                                  
            }else{
                    $.get('/search/?'+ q, function(data){                                                                                             
                    $('#search_result').html(data);
                    attach_pagination_events();
                    

                    // show_searching(false);             
                    // leadfound= $('.founded_no').text().trim();
                    // if (leadfound == '')
                    //     $('[name=search_founded_no]').val ('0 ' + gettext("Leads found"));
                    //  else
                    //      $('[name=search_founded_no]').val($('.founded_no').text().trim());
                    // attach_pagination_events();
                   
                    // if($('[name=keywords]').val() == '')
                    //     $('#keyword_highlight').hide();
                    
                    // if($('[name=locations]').val() == '')
                    //     $('#location_highlight').hide();
                    // left_dyanmic_height();
                            
                });
            }

            // $(".product_images1 img").one("load", function() {
            //         alert("before");
            //         var height = $(this).height();
            //         alert(height);
            //         var width = $(this).width();
            //         alert(width);
            //         $(this).css({'margin-top': -height / 2 + "px", 'margin-left': -width / 2 + "px"});  
            // }).each(function() {
            //   if(this.complete) $(this).load();
            // });
            
            // $('.product_images1').each(function () {
            //     var height = $(this).height();
            //     alert("height"+height);
            //     var width = $(this).width();
            //     alert("width"+width);
            //     $(this).css({'margin-top': -height / 2 + "px", 'margin-left': -width / 2 + "px"});   
            // });

            // $('.product_images1 img').load(function(){
            //     $(this).center1();
            // });

            $(document).ajaxComplete(function(){
               $('.product_images1 img').each(function () {
                    $(this).center();
                });
            });
}

function attach_pagination_events(){
    // pagination_filter_align();
            $('[data-ajaxlink=true]').click(function(ele){
            $("html, body").animate({ scrollTop: 0 }, "slow");
                        $('[name=page]').val($(ele.currentTarget).attr('data-ajaxpage'));
            // var url = window.location.href;
            // alert(url);

            // // var pageURL = $(location).attr("href");
            // url1=url.split('/')[3]
            // alert(url1);
            // url2=url.split('/')[4]
            // alert(url2);
            // alert(url1+'/'+url2);
            perform_search();
            return false;
            });
            
}
$(document).ready(function() {
            $("li.brand_folder > ul").hide();
            attach_pagination_events();

            var url = window.location.href;
            // var pageURL = $(location).attr("href");
            url1=url.split('/')[3];            
            url2=url.split('/')[4];            
            
            // Toggle for Categories and SubCategories in Advance Menu 
            $('.list_folder').on('click',function(e){
                e.stopImmediatePropagation();               
                $(this).find('.hide_list:first').slideToggle();
                perform_search();
            });
            $('.get').on('click',function(e){
                var text = $(this).text();
                $('.all').hide();
                $('.list_display').html(text + " <i class='fa fa-angle-right right'></i>");
                
            });
             $('.get1').on('click',function(e){
                var text = $(this).text();
                $('.all').hide();
                $('.list_display_subcat').html(text + " <i class='fa fa-angle-right right'></i>");
                
            });

            
            // $(document).on("click", '.brand_folder', function () {
            // // e.stopImmediatePropagation();               
            //     $(this).find('#brand_toggle').slideToggle();
            // });
            
            // $('.brand_folder').on('click',function(e){
            //     // e.stopImmediatePropagation();               
            //     $(this).find('#brand_toggle').slideToggle();
            // });
    //category choose

    // $('.categoryclick > li a.categoryselected').click(function () {
            
    //       var catid = $(this).next('.ajax_categoryid').text();
    //       alert("catid"+catid);
    //       var ajax_catid = $('input[type="hidden"]#categoryid').val(catid);
    //       $('#categoryid').val(ajax_catid);
    //         // alert(JSON.stringify($('#categoryid').val(ajax_catid)));
    //        perform_search();
    //          // var category_choose = $(this).next('.ajax_categoryid').val($(this).val());
    //        // var ajax_catid = $('input[type="hidden"]#categoryid').val(category_choose);
    //        //  $('#categoryid').val(ajax_catid);  
         
    //        //  perform_search();
    //         // var category_choose = $(this).parent().next('.ajax_categoryid').text;
    //         //  var trim_catid = $.trim(category_choose);
    //         //   var ajax_catid = $('input[type="hidden"]#categoryselected').val(trim_catid);
    //         //     $('[name=categoryselected]').text(trim_catid);  
    //         // alert("trim_catid"+trim_catid);
    //         // perform_search();
    //       });

    //subcategory list choose
    $('.subclick > li .subcategory_choose').click(function () {
            

        $('.subclick > li .subcategory_choose').each(function( index ) {
            $(this).removeClass('orange_text');
        });
            
        $(this).addClass('orange_text');
       
        var subid =  $(this).next('.ajax_subid').text();
        // alert(subid);
        var trim_subid = $.trim(subid);
        var ajax_subid = $('input[type="hidden"]#subcategoryid').val(trim_subid);
        $('[name=subcategoryid]').text(trim_subid);  
         var trim_subid = $.trim(subid);
         // alert($.trim(subid));
            fill_brands(trim_subid);
        $.trim($.cookie('subcatcookie',JSON.stringify(trim_subid)));
        perform_search(); 
    });
            


              
        //brand type

        $(document).on("change", 'input.brandtype', function () {
            if ($(this).prop('checked') == true){
                // alert($(this).val());
                // alert("true");
                var check = $(this).parent().parent().next('#brandsubcategoryid').val($(this).val());
                // alert("check"+JSON.stringify(check));
                perform_search(); 
            }
            else{
                // alert("false");
                $('#brandsubcategoryid').val('');
                perform_search(); 
            }
        });
		
		// city based search
		 $(document).on("change", '.city', function () {
		    // $( ".city" ).change(function () {          
    		var selected_option = $( ".city option:selected" ).val();  
    		$('p#cityselected').html($( ".city option:selected" ).text());            
    		var city = $('input[type="hidden"]#city').val($(this).val());  		          
    		perform_search();		      
		});
		
		//sort by dropdown
		// $(document).on('change',".prov_custom_sort_value_act", function(){
		        
		// var selected_option = $( ".prov_custom_sort_value_act option:selected" ).val();
		         
		// $('#prov_custom_sort_value_act').html($( ".prov_custom_sort_value_act option:selected" ).text()); 
		         
		// $('input[type="hidden"]#sorteddata').val($(this).val());
		          
		// perform_search();
		    
		// });

        $(".prov_custom_sort_value_act").on('change', function(){         
            var selected_option = $( ".prov_custom_sort_value_act option:selected" ).text();
            $('#prov_custom_sort_value_act').html(selected_option);               
            $('input[type="hidden"]#sorteddata').val($(this).val());                  
            perform_search();           
        });


    

//price range selection
    $('input.pricerange').on('change', function(){     
            if ($(this).prop('checked') == true){
                    var splitprice = [];
                    var splitprice = $(this).val().split("#");  
                    // alert(splitprice);                  
                    $('#price_start').val(splitprice[0]); 
                    $('#price_end').val(splitprice[1]);
                    perform_search();    
            }

          if ($(this).prop('checked') == false){
                $('[name=price_start]').val('');
                $('[name=price_end]').val('');
                $.cookie("subcatcookie")
                // alert($.cookie("subcatcookie"));
                perform_search();                         
            }    
            
    });

    // //sort by dropdown  
    //  $("select.prov_custom_sort_value_act option:selected").each(function () {
    //      fill_brands();
    //     perform_search();
        // var selected_option = $( ".prov_custom_sort_value_act option:selected" ).text();
        // $('#prov_custom_sort_value_act').html(selected_option); 


    //sort by dropdown
    // $( ".prov_custom_sort_value_act" ).on('change', function () {
              
    //   var selected_option = $( ".prov_custom_sort_value_act option:selected" ).text();
    //   $('#prov_custom_sort_value_act').html(selected_option); 
       
    //   $('input[type="hidden"]#sorteddata').val(selected_option);
    //   alert($('input[type="hidden"]#sorteddata').val(selected_option)); 
    //   perform_search();
    // });
    

            //current_city based search
        // $('select.city_select').click(function () {
        //     var current_city = $("select").val($("#currentid :selected").val());
        //     alert("current_city"+$("select").val($("#currentid :selected").val()));
        // });
 

            
// $("#cityid").change(function(){
//         $.getJSON("/home/", {city: city},
//                         function(ret, textStatus) {

//             $(this).parent().parent().next('input[type="hidden"]#currentid').val($(this).val());
//             alert("city_selected"+ $(this).parent().parent().next('input[type="hidden"]#currentid').val($(this).val()));
//             perform_search();
//         });
// });

    


function show_searching(show) {

    if(show){

        $('.loding_icon').show();
        $('.founded_no').hide();

    }else{

        $('.loding_icon').hide();
        $('.founded_no').show();

    }

}


// function left_dyanmic_height() {

//             var profile_sidebar = $('.right_content_holder, .v2_dashboard_wrapper, .right_content_wrapper, .dashboard_content_wrapper, .filter_result_wrapper').height();

//             profile_sidebar_height = profile_sidebar + 180;
//             profile_sidebar_height_2 = profile_sidebar;
            
//             $('.profile_sidebar').height(profile_sidebar_height);
            
//             var shouldShow = $.cookie('show_desc') == 'yep';
// 				if( shouldShow ) {
// 					if(profile_sidebar_height_2 > 700){
// 						$('.filter_wrapper').height(profile_sidebar_height_2 + 120);
// 					}
// 					else{
// 						$('.filter_wrapper').height(profile_sidebar_height_2 + 830);
// 					} 
					 
// 				}
// 				else {
// 					$('.filter_wrapper').height(profile_sidebar_height_2 + 120); 
// 				}
            
           

// }

function validateSearch() {
   left_dyanmic_height();
   // code by Karthikesh on 30/10/2013, for search ajax issue
   var is_search_page = window.location.href.indexOf('/search');
   if(is_search_page > 1)
   {
    
   		$('[name=q]').val($('#q').val());
		perform_search();
   }
   else
   {
    
       	if($('#q').val() == ''){

	         $('#q').val('');
    	}	
    	$("#f_search").submit();
   }
    //return true;
}
});
