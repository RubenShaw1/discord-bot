FROM python:3.9
ADD main.py
RUN pip install discord discord.ext
CMD [“python”, “./main.py”] 