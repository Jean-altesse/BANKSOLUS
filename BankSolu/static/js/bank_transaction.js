// Récupérer le montant actuel du compte
var balanceAmount = parseFloat(document.getElementById('balance-amount').textContent);

// Gérer la soumission du formulaire de transaction
document.getElementById('transaction-form').addEventListener('submit', function(event) {
  event.preventDefault();

  var amount = parseFloat(document.getElementById('amount').value);
  var type = document.getElementById('type').value;

  // Effectuer la transaction
  if (type === 'deposit') {
    balanceAmount += amount;
  } else if (type === 'withdraw') {
    if (amount <= balanceAmount) {
      balanceAmount -= amount;
    } else {
      alert("Fonds insuffisants !");
      return;
    }
  }

  // Mettre à jour le montant du compte affiché
  document.getElementById('balance-amount').textContent = balanceAmount.toFixed(2);

  // Réinitialiser le formulaire
  document.getElementById('transaction-form').reset();
});