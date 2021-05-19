FROM python:3.7-alpine
WORKDIR /League-Champs-Basestats
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY . /League-Champs-Basestats
CMD ["python", "best_champ_stat.py"]