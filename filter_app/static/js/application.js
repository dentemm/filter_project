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