function toggleMenu() {
    var navList = document.getElementById('navList');
    var menuIcon = document.getElementById('menuIcon');
    navList.classList.toggle('show');
    if (navList.classList.contains('show')) {
        // Set Display to 'flex' to show the menu
        navList.style.display = 'flex';
        menuIcon.innerHTML = '&times;';  // Change to 'X' when the menu is open
    } else {
        // Set Display to 'none' to hide the menu
        navList.style.display = 'none';
        menuIcon.innerHTML = '&#9776;';  // Change back to '☰' when the menu is closed
    }
}