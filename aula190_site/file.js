// Get elements from DOM
const title = document.getElementById('title');
const button = document.getElementById('changeButton');

// Add click event listener
button.addEventListener('click', () => {
    // Change the title text
    if (title.textContent === 'Click the button!') {
        title.textContent = 'Text changed!';
    } else {
        title.textContent = 'Click the button!';
    }
    
    // Change button color randomly
    const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
    button.style.backgroundColor = randomColor;
});