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
	}
});

$("a.detail").click(function(e){

	e.preventDefault();

	pk = $(this).data('pk');

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