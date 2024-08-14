function clearNote () {
  noteTextField = document.getElementById('note-text')
  noteTextField.textContent = ''
}

const resetButton = document.getElementById('reset-button')

resetButton.addEventListener('click', clearNote)
