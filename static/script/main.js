document.addEventListener('DOMContentLoaded', function() {
    const next_btn = document.getElementById('nextBtn');
    const prev_btn = document.getElementById('prevBtn');
    const first_menu = document.getElementById('step-1');
    const second_menu = document.getElementById('step-2');
    const third_menu = document.getElementById('step-3');
    const register_btn = document.getElementById('registerBtn');
    let current_stp = 1;

    next_btn.addEventListener('click', function() {
        if (current_stp == 1){
            current_stp = 2;
            prev_btn.style.display = 'block';
            first_menu.style.display = 'none';
            second_menu.style.display = 'block';
            return 0;
        };
        if (current_stp == 2){
            current_stp = 3;
            next_btn.style.display = 'none';
            register_btn.style.display = 'block';
            second_menu.style.display = 'none';
            third_menu.style.display = 'block';
            return 0;
        };
    });

    prev_btn.addEventListener('click', function() {
        if (current_stp == 3){
            current_stp = 2;
            next_btn.style.display = 'block';
            register_btn.style.display = 'none';
            second_menu.style.display = 'block';
            third_menu.style.display = 'none';
            return 0;
        };
        if (current_stp == 2){
            current_stp = 1;
            prev_btn.style.display = 'none';
            first_menu.style.display = 'block';
            second_menu.style.display = 'none';
            return 0;
        };
    });
    

    document.getElementById('mainpbtn').addEventListener('click', function() {
        window.location.href = "/";
    });
});