$( document ).ready(function() {

  $("#search_btn").click("click", function (e) {
    let queries = {}
    let from_date = $("#from_data_picker").val()
    let to_date = $("#to_data_picker").val()
    queries['from_date'] = from_date
    queries['to_date'] = to_date
    document.location.href="?"+$.param(queries);
    
  })
})