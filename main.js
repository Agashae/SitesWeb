// Code JavaScript simple pour gérer les fenêtres (Ouvrir, Fermer, Déplacer)

// 1. Horloge et Date de la barre des tâches
function updateClockAndDate() {
    const clockElement = document.getElementById('clock');
    const dateElement = document.getElementById('date');
    const now = new Date();
    
    // Ajoute un "0" devant si les minutes ou heures sont plus petites que 10
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    clockElement.textContent = `${hours}:${minutes}`;

    // Gestion de la date (Jour/Mois/Année)
    const day = String(now.getDate()).padStart(2, '0');
    const month = String(now.getMonth() + 1).padStart(2, '0'); // +1 car les mois commencent à 0
    const year = now.getFullYear();
    dateElement.textContent = `${day}/${month}/${year}`;
}
// Met à jour l'horloge et la date toutes les secondes
setInterval(updateClockAndDate, 1000);
updateClockAndDate();

// 2. Ouvrir une fenêtre
function openWindow(windowId) {
    const win = document.getElementById(windowId);
    if (win) {
        win.classList.remove('hidden');
        bringToFront(win);
    }
}

// 3. Fermer une fenêtre
function closeWindow(windowId) {
    const win = document.getElementById(windowId);
    if (win) {
        win.classList.add('hidden');
    }
}

// Variable pour gérer quelle fenêtre est au dessus des autres
let highestZIndex = 100;

function bringToFront(windowElement) {
    highestZIndex += 1;
    windowElement.style.zIndex = highestZIndex;
}

// 4. Déplacer les fenêtres avec la souris (Drag & Drop simple)
document.addEventListener('DOMContentLoaded', () => {
    const windows = document.querySelectorAll('.window');

    windows.forEach(win => {
        const header = win.querySelector('.window-header');
        
        let isDragging = false;
        let offsetX = 0;
        let offsetY = 0;

        header.addEventListener('mousedown', (e) => {
            if (e.target.closest('.control-btn')) return;

            isDragging = true;
            bringToFront(win);

            offsetX = e.clientX - win.offsetLeft;
            offsetY = e.clientY - win.offsetTop;
            win.style.transition = 'none'; 
        });

        document.addEventListener('mousemove', (e) => {
            if (!isDragging) return;

            let newX = e.clientX - offsetX;
            let newY = e.clientY - offsetY;

            if (newY < 0) newY = 0;

            win.style.left = newX + 'px';
            win.style.top = newY + 'px';
        });

        document.addEventListener('mouseup', () => {
            if (isDragging) {
                isDragging = false;
                win.style.transition = 'transform 0.2s, opacity 0.2s';
            }
        });
        
        win.addEventListener('mousedown', () => {
            bringToFront(win);
        });
    });
});
