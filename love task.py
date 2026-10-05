<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>For You ❤️</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    height: 100vh;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #ff758c, #ff7eb3);
    color: white;
    text-align: center;
}

.container {
    padding: 30px;
    animation: fadeIn 2s ease;
}

.heart {
    font-size: 100px;
    animation: heartbeat 1s infinite;
}

h1 {
    font-size: 48px;
    margin: 20px 0;
    text-shadow: 0 0 15px rgba(255,255,255,0.8);
}

p {
    font-size: 22px;
    margin-bottom: 25px;
}

button {
    border: none;
    padding: 14px 30px;
    border-radius: 30px;
    background: white;
    color: #ff4f81;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
}

button:hover {
    transform: scale(1.08);
}

#message {
    display: none;
    margin-top: 25px;
    font-size: 24px;
    animation: fadeIn 1s ease;
}

.floating-heart {
    position: absolute;
    bottom: -30px;
    font-size: 25px;
    animation: float 6s linear infinite;
}

@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.25); }
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes float {
    from {
        transform: translateY(0);
        opacity: 1;
    }
    to {
        transform: translateY(-110vh);
        opacity: 0;
    }
}
</style>
</head>

<body>

<div class="container">

    <div class="heart">❤️</div>

    <h1>I Love You</h1>

    <p>You are very special to me 🥰</p>

    <button onclick="showMessage()">Click Me ❤️</button>

    <div id="message">
        💕 I Love You Forever 💕<br>
        You make my world beautiful! 🌎❤️
    </div>

</div>

<script>
function showMessage() {
    document.getElementById("message").style.display = "block";
}

function createHeart() {
    const heart = document.createElement("div");
    heart.className = "floating-heart";
    heart.innerHTML = "❤️";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.animationDuration = (4 + Math.random() * 4) + "s";

    document.body.appendChild(heart);

    setTimeout(() => {
        heart.remove();
    }, 8000);
}

setInterval(createHeart, 500);
</script>

</body>
</html>