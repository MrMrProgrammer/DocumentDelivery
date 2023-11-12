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
    document.getElementById('sub-btn-again').style.display = 'inline-block';

    document.getElementById('unactive-sub-btn').style.display = 'none';
    document.getElementById('unactive-sub-btn-again').style.display = 'none';
}

function remove_from_input() {
    document.getElementById('store_id_input').value = '';
    document.getElementById('fake_store_id_input').value = '';

    document.getElementById('unactive-sub-btn').style.display = 'inline-block';
    document.getElementById('unactive-sub-btn-again').style.display = 'inline-block';

    document.getElementById('sub-btn').style.display = 'none';
    document.getElementById('sub-btn-again').style.display = 'none';
}

//==============================================================

// function dropfunc() {
//     document.getElementById("myDropdown").classList.toggle("show");
// }
//
// let myDropdown = document.getElementById("myDropdown");
// let myDropdownBtn = document.getElementById("myDropdownBtn");
// document.addEventListener('click', function (e) {
//
//     if (!myDropdown.contains(e.target) && !myDropdownBtn.contains(e.target)) {
//         if (myDropdown.classList.contains('show')) {
//             e.preventDefault();
//             myDropdown.classList.remove('show');
//         }
//     }
// });

//==============================================================
