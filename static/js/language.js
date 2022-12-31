$("#id_languages").change(function () {
    const url = $("#lang_id").val();  // get the url of the `load_cities` view
    const lang_id = $(this).val();  // get the selected country ID from the HTML input
    $.ajax({ // initialize an AJAX request
        url: url, // set the url of the request (= /members/ajax/load-cities/ )
        type: "POST",
        data: {
            'lang_id': lang_id  // GET parameters
        },
        success: function (data) {
            $("#lang_levels_id").html(data);
        },
        error: function (error){
            console.log(error)
        }
    });
});
