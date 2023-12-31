# information-extraction-from-legal-texts

To successfuly run the project follow the steps listed below

## Prerequisites

1. Python
2. pip
3. NodeJs

## Set up the backend

1. change directory into the backend folder by running `cd backend`

2. install the python virtual env package by running

   For linux systems

   ```
       sudo apt install python3-venv
   ```

   For Windows systems

   ```
       pip install virtualenv
   ```

3. create a virtual environment by running the following

   For linux systems

   ```
       python3 -m venv venv
   ```

   For windows systems

   ```
       python -m virtualenv venv
   ```

4. activate the virtual env by running

   For linux systems

   ```
       source venv/bin/activate
   ```

   For windows systems

   ```
       .\venv\Scripts\activate
   ```

5. install the required packages by running

   ```
       pip install -r requirements.txt
   ```

6. start the applicatipn server by running the following command `python3 server.py` for linux systems and `python server.py` for windows systems

## Set up the frontend

1. In a brand new terminal, change directory to the frontend directory by running `cd frontend`

2. Install the required packages by running `npm i`

3. Start the fronend server by running `npm run dev`

4. Visit http://localhost:3000 to access the frontend and get started.
