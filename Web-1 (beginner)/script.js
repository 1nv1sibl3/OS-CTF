function checkFlag() {
    const flagInput = document.getElementById('flagInput').value;
    const result = document.getElementById('result');
    const flag = "OSCTF{Cr4zY_In5P3c71On}";

    if (flagInput === flag) {
        result.textContent = "Congratulations! You found the flag!";
        result.style.color = "green";
    } else {
        result.textContent = "Incorrect flag. Try again.";
        result.style.color = "red";
    }
}
