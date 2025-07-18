window.onload = () => {
    const resultBox = document.querySelector('.result-box');
    if (resultBox) {
        resultBox.style.opacity = 0;
        setTimeout(() => {
            resultBox.style.transition = "opacity 1s ease-in";
            resultBox.style.opacity = 1;
        }, 300);
    }
};
