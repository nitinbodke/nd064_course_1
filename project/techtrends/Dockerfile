#Use a Python base image in version 2.7
# trying to use latest!
FROM python:3.7.3
WORKDIR /usr/src/app

#Expose the application port 3111
EXPOSE 3111/tcp

#Install packages defined in the requirements.txt file
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy source files
COPY . .

#Ensure that the database is initialized with the pre-defined posts in the init_db.py file
#COPY init_db.py ./
RUN python init_db.py

#The application should execute at the container start
CMD [ "python", "app.py" ]
