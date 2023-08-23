# Define your CSS styles in a separate variable
css = '''
<style>
    body {
        font-family: 'Open Sans', sans-serif;
        background-color: #f2f2f2;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.15);
        border-radius: 1rem;
    }
    .chat-message:hover {
        transform: scale(1.05);
    }
    .chat-message.user {
        background-color: #2b313e;
    }
    .chat-message.bot {
        background-color: #475063
    }
    .chat-message .avatar {
        width: 20%;
    }
    .chat-message .avatar img {
        max-width: 78px;
        max-height: 78px;
        border-radius: 50%;
        object-fit: cover;
    }
    .chat-message .message {
        width: 80%;
        padding: 0 1.5rem;
        color: #fff;
    }
    @keyframes slideIn {
        0% {
            transform: translateX(-50px);
            opacity: 0;
        }
        100% {
            transform: translateX(0);
            opacity: 1;
        }
    }
    .chat-message {
        animation: slideIn 0.5s ease-out;
    }
</style>
'''

# Define templates for bot and user messages
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.postimg.cc/P5phFqqh/bot.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.postimg.cc/MHMdJgfc/human.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;" alt="User Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

button_css = '''
<style>
div[class="row-widget stButton"] > button {
    width: 20%;
    height: 60px;
    border-radius: 5px;
    font-size: 20px;
} 
</style>
'''

