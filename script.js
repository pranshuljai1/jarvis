async function sendCommand() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    const chatLog = document.getElementById("chat-log");
    chatLog.innerHTML += `<div><strong>You:</strong> ${userInput}</div>`;
    document.getElementById("user-input").value = "";

    try {
        const response = await fetch('https://<your-backend-url>/api/command', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ command: userInput }),
        });

        const data = await response.json();
        chatLog.innerHTML += `<div><strong>Jarvis:</strong> ${data.response}</div>`;
    } catch (error) {
        chatLog.innerHTML += `<div><strong>Jarvis:</strong> Error: Unable to connect to backend.</div>`;
    }

    chatLog.scrollTop = chatLog.scrollHeight;
}
