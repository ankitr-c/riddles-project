// // Function to display a random riddle from the API
// async function displayRandomRiddle() {
//     const riddleContainer = document.getElementById("riddle-container");
  
//     try {
//       // Make an API call to get a random riddle
//       const response = await fetch("http://192.168.0.7:5000/get_riddle");
//       const riddleData = await response.json();
  
//       // Display the retrieved riddle
//       riddleContainer.innerHTML = `<p>${riddleData.riddle}</p>`;
//     } catch (error) {
//       console.error("Error fetching riddle:", error);
//     }
//   }
  
//   // Event listener for the "New Riddle" button
//   document.getElementById("new-riddle-btn").addEventListener("click", displayRandomRiddle);
  
//   // Event listener for the "Get Answer" button
//   document.getElementById("get-answer-btn").addEventListener("click", () => {
//     const answerPopup = document.getElementById("answer-popup");
//     const riddleAnswer = document.getElementById("riddle-answer");
  
//     // Display the answer popup
//     answerPopup.style.display = "block";
  
//     // Get the current riddle
//     const currentRiddle = document.getElementById("riddle-container").innerText;
  
//     // Find the answer corresponding to the current riddle (from the local data)
//     const currentAnswer = data.find(item => item.riddle === currentRiddle)?.ans;
  
//     // Display the answer
//     riddleAnswer.innerText = currentAnswer || "Answer not found";
//   });
  
//   // Event listener for the close button in the answer popup
//   document.getElementById("close-popup").addEventListener("click", () => {
//     const answerPopup = document.getElementById("answer-popup");
  
//     // Close the answer popup
//     answerPopup.style.display = "none";
//   });
  

// Sample riddle and answer data
const data = [
    { riddle: "Riddle 1", ans: "Answer 1" },
    { riddle: "Riddle 2", ans: "Answer 2" },
    { riddle: "Riddle 3", ans: "Answer 3" }
  ];
  
  // Function to display a random riddle from the API
  async function displayRandomRiddle() {
    const riddleContainer = document.getElementById("riddle-container");
  
    try {
      // Make an API call to get a random riddle
      const response = await fetch("http://localhost:8000/get_riddle");
      const riddleData = await response.json();
  
      // Display the retrieved riddle
      riddleContainer.innerHTML = `<p>${riddleData.riddle}</p>`;
  
      // Store the current riddle and answer for later use
      currentRiddle = riddleData.riddle;
      currentAnswer = riddleData.ans;
    } catch (error) {
      console.error("Error fetching riddle:", error);
    }
  }
  
  // Event listener for the "New Riddle" button
  document.getElementById("new-riddle-btn").addEventListener("click", displayRandomRiddle);
  
  // Variables to store the current riddle and answer
  let currentRiddle = "";
  let currentAnswer = "";
  
  // Event listener for the "Get Answer" button
  document.getElementById("get-answer-btn").addEventListener("click", () => {
    const answerPopup = document.getElementById("answer-popup");
    const riddleAnswer = document.getElementById("riddle-answer");
  
    // Display the answer popup
    answerPopup.style.display = "block";
  
    // Display the stored answer corresponding to the current riddle
    riddleAnswer.innerText = currentAnswer || "Answer not found";
  });
  
  // Event listener for the close button in the answer popup
  document.getElementById("close-popup").addEventListener("click", () => {
    const answerPopup = document.getElementById("answer-popup");
  
    // Close the answer popup
    answerPopup.style.display = "none";
  });
  