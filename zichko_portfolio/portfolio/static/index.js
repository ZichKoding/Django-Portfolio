function toggleMenu() {
    var navList = document.getElementById('navList');
    var menuIcon = document.getElementById('menuIcon');
    navList.classList.toggle('show');
    if (navList.classList.contains('show')) {
        menuIcon.innerHTML = '&times;';  // Change to 'X' when the menu is open
    } else {
        menuIcon.innerHTML = '&#9776;';  // Change back to '☰' when the menu is closed
    }
}