var b = 1;
jQuery(document).on('click', '.add-new-row', function (e) {
    e.preventDefault();
    b++;
    let inner_row = jQuery('#order_number_inner_row');
    inner_row.append('<br/><div class="row"><div class="col-6"><input type="text" name="order_number[' + b + ']" class="form-control" placeholder="شماره سفارش" id="id_order_number"></div> <div class="col-6"><input type="text" name="document_defects[' + b + ']" class="form-control" placeholder="نقص مدارک" id="id_document_defects"></div></div></div>');
})

jalaliDatepicker.startWatch();


function show_stores() {
    search_btn = document.getElementById('myDropdown');

    if (search_btn.style.display == 'none') {
        document.getElementById('myDropdown').style.display = 'block';
    } else {
        document.getElementById('myDropdown').style.display = 'none';
    }

}

function filterFunction() {
    var input, filter, ul, li, a, i;

    input = document.getElementById("myInput");

    filter = input.value.toUpperCase();

    div = document.getElementById("myDropdown");

    a = div.getElementsByTagName("a");

    for (i = 0; i < a.length; i++) {
        txtValue = a[i].textContent || a[i].innerText;

        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}

function add_to_input(store_name, store_id) {
    console.log(store_name)
    document.getElementById('store_id_input').value = store_id;
    document.getElementById('fake_store_id_input').value = store_name;

    document.getElementById('myDropdown').style.display = 'none';

    document.getElementById('sub-btn').style.display = 'inline-block';
    document.getElementById('unactive-sub-btn').style.display = 'none';
}

function remove_from_input() {
    document.getElementById('store_id_input').value = '';
    document.getElementById('fake_store_id_input').value = '';

    document.getElementById('unactive-sub-btn').style.display = 'inline-block';
    document.getElementById('sub-btn').style.display = 'none';
}


