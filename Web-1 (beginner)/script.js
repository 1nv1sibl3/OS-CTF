function checkFlag() {
    const flagInput = document.getElementById('flagInput').value;
    const result = document.getElementById('result');
    const flag = "OSCTF{y0U_f0unD_M3_bY_1n5p3C7t1nG!}";

    if (flagInput === flag) {
        result.textContent = "Congratulations! You found the flag!";
        result.style.color = "green";
    } else {
        result.textContent = "Incorrect flag. Try again.";
        result.style.color = "red";
    }
}
