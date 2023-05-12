const monIcone = document.getElementById('monIcone');
const fontAwesome = new FontAwesome();

// Ajouter la classe CSS pour l'icône
monIcone.classList.add('fa', 'fa-envelope');

// Colorer l'icône en rouge
fontAwesome.dom.i2svg({node: monIcone, color: 'red'});
