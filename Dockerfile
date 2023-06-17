FROM python:3.9
RUN wget -O main.py https://raw.githubusercontent.com/RubenShaw1/discord-bot/main/bot.py
RUN /bin/sh -c pip install discord discord.ext
CMD [“python”, “./main.py”] 
