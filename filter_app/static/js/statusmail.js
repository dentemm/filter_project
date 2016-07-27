/* Form submission for filter swap */
$("#statusmail").on('click', function(e){

	e.preventDefault(); //DO NOT PREVENT DEFAULT!

	$.ajax({

		type: 'GET',
		url: 'http://statusmail.imec.be/json/module/list.json',
		dataType: 'json',
		crossDomain: true,
		success: function (response) {
			var resp = JSON.parse(response);
			alert(resp.status);
		},
		
		error: function(request, ajaxOptions, thrownError) {
			//alert('error!');
			alert('Data is enkel beschikbaar via het imec netwerk');
			console.log(request);
			console.log(ajaxOptions);
			console.log(thrownError);
			console.log(request.responseText);
		}

	});

});

function success_handler(data, status, response){

	console.log(data);

}



