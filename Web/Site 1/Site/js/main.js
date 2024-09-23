const changeTextButton = document.getElementById('changeTextButton');
const displayText = document.getElementById('displayText');

changeTextButton.addEventListener('click', () => {
    displayText.textContent = 'Texto alterado pelo JavaScript!';
});
