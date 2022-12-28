$("#id_city").change(function () {
    const url = $("#UserForm").attr("data-cities-url");  // get the url of the `load_cities` view
    const cityId = $(this).val();  // get the selected country ID from the HTML input

    $.ajax({ // initialize an AJAX request
        url: url, // set the url of the request (= /members/ajax/load-cities/ )
        data: {
            'city_id': cityId  // GET parameters
        },
        success: function (data) {
            $("#id_district").html(data);
        }
    });

});