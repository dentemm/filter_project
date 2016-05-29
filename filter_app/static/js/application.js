$("#first-select").change(function() {

	console.log($(this).val())

	$.ajax({
		type: "GET",
	  	url: "/filters/formtest/",
	  	data: {
	  		tool: $(this).val()
	  	},
	  	success: success_handler 
	});

	function success_handler(data){

		//console.log(data)
		$(".form-container").html(data);

		//Need to call this, to re-evaluate application.js
		$.getScript("/static/js/application.js");

	}
});


/* Form submission for filter swap */
$("#form-submit").on('click', function(e){

	e.preventDefault(); //DO NOT PREVENT DEFAULT!

	console.log('submit form now');


	var form = $("#swap-add");


	form.submit(function(){

		console.log('going to submit');

		console.log($('#first-select').val());


		$.ajax({

			data: form.serialize(),
			type: form.attr('method'),
			url: form.attr('action'),
			success: success_handler,

			error: function(request, ajaxOptions, thrownError) {
				alert('error!');
				alert(request.responseText);
				console.log(request.responseText);
			}

		});
		//return false;

		console.log('ready to submit form b');
	});

	function success_handler(data, status, response){

		//var response_success;


		//console.log('success!')
		//console.log(response.getResponseHeader('temm'));


		/*if (response.getResponseHeader('temm') == 'fail') {

			response_success = true;
		}

		else {
			response_success = false
		}*/
		


		//console.log(response_success);
		
		//console.log('temm');
		//console.log(data);
	}
});


/* Links in Tool View to render detailed content */
$("a.detail").click(function(e){

	e.preventDefault();

	pk = $(this).data("pk");

	// console.log('application called');
	// console.log($(this).data('pk'));

	$.ajax({
		method: "GET",
		dataType: "html",
		url: "/filters/ajax/" + pk,
		success: success_handler,
		error: function(request, ajaxOptions, thrownError) {
			alert(request.responseText);
		}
	});

	function success_handler(data){
		
		//console.log(data);

		$("#tool-container").html(data);
		//$("body").html(data);
		$.getScript("/static/js/toolkit.min.js");
	}
});