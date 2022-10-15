#Getting the base image
FROM python:3.9-slim-buster

#Setup the directory and app structure
WORKDIR /app

#Upgrade PIP
RUN python3 -m pip install --upgrade pip 

#Copy requirements file
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#Copy all app files from local to container
COPY . .

#Run the application
CMD streamlit run app.py
 

