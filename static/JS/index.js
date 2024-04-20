document.addEventListener('DOMContentLoaded', () => {
  const inputForm = document.getElementById('inputForm');

  const outputText = document.getElementById('outputText');

  inputForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    const inputText = this.querySelector('textarea').value;

    try {
      const response = await axios.post('/process', { text: inputText });
      outputText.innerHTML = response.data.html; 
    } catch (error) {
      console.error('Error:', error);
    }
  });
});
