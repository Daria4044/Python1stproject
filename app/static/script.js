window.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById("welcome-btn");
    const message = document.getElementById("welcome-msg");
  
    if (button && message) {
      button.addEventListener("click", () => {
        message.textContent = "Welcome to KeepFresh!";
      });
    }
  
    // ✅ Count grocery list rows
    const tableRows = document.querySelectorAll("tbody tr");
    const countSpan = document.getElementById("item-count");
  
    if (countSpan) {
      countSpan.textContent = tableRows.length;
    }
  });
  // Count and update number of grocery items
document.addEventListener("DOMContentLoaded", function () {
  const rows = document.querySelectorAll("tbody tr");
  document.getElementById("item-count").textContent = rows.length;
});
