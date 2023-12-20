document.addEventListener("DOMContentLoaded", function () {
    // Event listener for the "Add Riddle" button
    document.getElementById("add-riddle-btn").addEventListener("click", function () {
        // Get the values from the input fields
        const riddleInput = document.getElementById("riddle-input").value;
        const answerInput = document.getElementById("answer-input").value;

        // Check if both inputs are filled
        if (riddleInput.trim() === "" || answerInput.trim() === "") {
            alert("Please enter both the riddle and its answer.");
            return;
        }

        // Create an object with the new riddle data
        const newRiddle = { "riddle": riddleInput, "ans": answerInput };

        // Send a POST request to add the new riddle
        fetch("http://localhost:8000/add_riddle", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(newRiddle),
        })
        .then(response => response.json())
        .then(data => {
            // Display a success message
            alert(data.message);

            // Clear the input fields
            document.getElementById("riddle-input").value = "";
            document.getElementById("answer-input").value = "";
        })
        .catch(error => {
            console.error("Error adding riddle:", error);
            // Display an error message
            alert("Error adding riddle. Please try again.");
        });
    });
});
