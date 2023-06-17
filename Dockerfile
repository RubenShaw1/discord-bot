FROM python:3.9
RUN wget -O main.py https://raw.githubusercontent.com/RubenShaw1/discord-bot/main/bot.py
RUN pip install discord discord.ext
CMD ["/bin/bash", "-c", "python ./main.py"]
