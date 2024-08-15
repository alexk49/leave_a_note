function clearNote () {
  noteText.textContent = ''
}

function textCounter () {
  // count note-text in textarea
  // and update number in counter div
  const maxLength = noteText.getAttribute('maxlength')
  const currentLength = noteText.value.length
  const counter = document.getElementById('counter')

  counter.innerHTML = `${currentLength}/${maxLength}`
}

const noteText = document.getElementById('note-text')
noteText.addEventListener('input', textCounter)

const resetButton = document.getElementById('reset-button')
resetButton.addEventListener('click', clearNote)
