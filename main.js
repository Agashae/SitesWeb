//juste l'horloge de la taskbar, plus besoin du reste vu qu'il y a plus de fenetres a ouvrir/fermer

function majHeure() {
    const maintenant = new Date();

    //ajoute un 0 devant si c'est plus petit que 10
    let heures = maintenant.getHours();
    let minutes = maintenant.getMinutes();
    if (heures < 10) { heures = "0" + heures; }
    if (minutes < 10) { minutes = "0" + minutes; }

    document.getElementById("heure").textContent = heures + ":" + minutes;
}

//on lance direct une fois, sinon ca met 1 seconde a s'afficher
majHeure();
setInterval(majHeure, 1000);
