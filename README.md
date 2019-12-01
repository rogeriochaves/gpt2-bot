# gpt-2 bot

A bot that uses gpt-2 model

## Installation

Download the model data
```
sh download_model.sh 117M
```

Install python packages:
```
pip3 install -r requirements.txt
```

Start an interactive chat:
```
python3 bot/chat.py
```

Start the chatbot server:
```
python3 bot
```

You can call POST localhost:8888 with the chat history as the POST body, and the bot will complete it for you