// Event listener for form submission
document.getElementById('imageForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const textInput = document.getElementById('textInput').value;
    
    if (textInput.trim() !== "") {
        // Show the spinner and disable the form while waiting for the image
        document.getElementById('spinner').style.display = 'block';
        document.querySelector('button').disabled = true;
        document.getElementById('resetButton').disabled = true;

        // Send the description to Python
        if (window.pywebview) {
            window.pywebview.api.receive_url(textInput);
        }
    } else {
        alert("Please enter some text to generate an image URL!");
    }
});

// Reset button behavior to stop spinner and enable buttons
document.getElementById('resetButton').addEventListener('click', function() {
    document.getElementById('spinner').style.display = 'none';
    document.querySelector('button').disabled = false;
    document.getElementById('resetButton').disabled = false;
    document.getElementById('textInput').value = '';
    document.getElementById('generatedImage').style.display = 'none';
});

// Show success message and update image
function showSuccessMessage(imagePath) {
    document.getElementById('spinner').style.display = 'none';
    document.querySelector('button').disabled = false;
    document.getElementById('resetButton').disabled = false;
    document.getElementById('successMessage').style.display = 'block';
    document.getElementById('generatedImage').src = imagePath;
    document.getElementById('generatedImage').style.display = 'block';

    // Hide success message after 5 seconds
    setTimeout(function() {
        document.getElementById('successMessage').style.display = 'none';
    }, 5000);
}
