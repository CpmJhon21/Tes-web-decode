document.addEventListener("DOMContentLoaded", () => {
    gsap.from(".container", { duration: 1.5, opacity: 0, scale: 0.8 });
});

async function generateHash(algo) {
    const text = document.getElementById("inputText").value;
    const response = await fetch(`/hash/${algo}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data: text })
    });
    const result = await response.json();
    document.getElementById("result").innerText = result.result;
    animateText();
}

async function generateBase64(action) {
    const text = document.getElementById("inputText").value;
    const response = await fetch(`/base64_${action}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data: text })
    });
    const result = await response.json();
    document.getElementById("result").innerText = result.result;
    animateText();
}

function copyToClipboard() {
    const resultText = document.getElementById("result").innerText;
    navigator.clipboard.writeText(resultText).then(() => {
        alert("Copied to clipboard!");
    });
}

function animateText() {
    anime({
        targets: "#result",
        scale: [1, 1.2, 1],
        duration: 500,
        easing: "easeInOutQuad"
    });
}
