const body = document.querySelector("body"),
    sidebar = body.querySelector(".sidebar"),
    toggle = body.querySelector(".toggle"),
    searchBtn = body.querySelector(".search-box"),
    modeSwtich = body.querySelector(".toggle-switch"),
    modeText = body.querySelector(".mode-text");

    toggle.addEventListener("click", () =>{
        sidebar.classList.toggle("close");
    });
    searchBtn.addEventListener("click", () =>{
        sidebar.classList.remove("close");
    });


    modeSwtich.addEventListener("click", () =>{
        body.classList.toggle("dark");

        if (body.classList.contains("dark")){
            modeText.innerText = "Light Mode"
        }else{
            modeText.innerText = "Dark mode"
        }
    });







    function previewFile() {
        var preview = document.querySelector('img');
        var file    = document.querySelector('input[type=file]').files[0];
        var reader  = new FileReader();
      
        reader.addEventListener("load", function () {
          preview.src = reader.result;
        }, false);
      
        if (file) {
          reader.readAsDataURL(file);
        }
      }
                            $(function() {
                  $('#profile-image1').on('click', function() {
                      $('#profile-image-upload').click();
                  });
              });






function afficherFormulaire1() {
    var formulaireDepot = document.getElementById('formulaire-depot');
    formulaireDepot.classList.add('show');
}

function afficherFormulaire2() {
    var formulaireDepot = document.getElementById('formulaire-retrait');
    formulaireDepot.classList.add('show');
}


// code pour gerer les depots et les retraits



function afficherFormulaire(idFormulaire) {
    var formulaire = document.getElementById(idFormulaire);
    formulaire.classList.add('show');
}

function effectuerDepot(event) {
    event.preventDefault();

    var montantDepot = parseFloat(document.getElementById('montant-depot').value);
    var solde = parseFloat(document.getElementById('solde').innerText.replace(',', ''));

    if (isNaN(montantDepot) || montantDepot <= 0) {
        afficherMessage('Veuillez entrer un montant valide pour le dépôt', 'erreur');
        resetForm('formulaire-depot');
        return;
    }

    solde += montantDepot;
    document.getElementById('solde').innerText = solde.toFixed(2);

    afficherMessage('Dépôt effectué avec succès', 'succes');
    resetForm('formulaire-depot');
}

function effectuerRetrait(event) {
    event.preventDefault();

    var montantRetrait = parseFloat(document.getElementById('montant-retrait').value);
    var solde = parseFloat(document.getElementById('solde').innerText.replace(',', ''));

    if (isNaN(montantRetrait) || montantRetrait <= 0) {
        afficherMessage('Veuillez entrer un montant valide pour le retrait', 'erreur');
        resetForm('formulaire-retrait');
        return;
    }

    if (montantRetrait > solde) {
        afficherMessage('Solde insuffisant pour le retrait', 'erreur');
        resetForm('formulaire-retrait');
        return;
    }

    solde -= montantRetrait;
    document.getElementById('solde').innerText = solde.toFixed(2);

    afficherMessage('Retrait effectué avec succès', 'succes');
    resetForm('formulaire-retrait');
}

function resetForm(idFormulaire) {
    document.getElementById(idFormulaire).classList.remove('show');
    document.getElementById(idFormulaire).querySelector('form').reset();
}

function afficherMessage(message, type) {
    var messageDiv = document.createElement('div');
    messageDiv.classList.add('message', type);
    messageDiv.innerText = message;
    document.body.appendChild(messageDiv);

    setTimeout(function() {
        messageDiv.remove();
    }, 3000);
}





// Ajout des événements pour les boutons de dépôt et de retrait
document.getElementById('formulaire-depot').addEventListener('submit', effectuerDepot);
document.getElementById('formulaire-retrait').addEventListener('submit', effectuerRetrait);