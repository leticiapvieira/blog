// Fecha os alerts após 10 segundos
// para aumentar ou diminuir o tempo x1000 e altera na ultima parte da linha 
document.querySelectorAll('.alert').forEach(alert => {
    setTimeout(() => { bootstrap.Alert.getOrCreateInstance(alert).close(); }, 10000);
});