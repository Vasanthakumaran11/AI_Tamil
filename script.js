async function sendMessage() {
    const input = document.getElementById("user-input");
    const text = input.value.trim();
    if (!text) return;
    
    addMessage(text, "user");
    input.value = "";

    try {
        const res = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: text })
        });
        const data = await res.json();
        addMessage(data.reply, "bot");
    } catch (err) {
        addMessage("Error connecting to server.", "bot");
    }
}

function addMessage(text, sender) {
    const box = document.getElementById("chat-box");
    const div = document.createElement("div");
    div.className = `message ${sender}`;
    div.textContent = text;
    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
}
