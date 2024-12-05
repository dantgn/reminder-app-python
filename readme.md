## Introduction

This is a Python FastAPI project that implements the Backend part of a Reminder Tasks application.

The API provides the ability to create, get and delete Todo Tasks.

It is deployed with Vercel and API documentation can be checked at [API Docs](https://reminder-app-python.vercel.app/docs)

### Frontend Part of the project
The Frontend App which uses this API is implemented with Vite + React, and is also deployed with Vercel at [Remminder APP](https://reminder-tasks-frontend.vercel.app/)

 The Github repository is also public and can be found at https://github.com/dantgn/reminder-tasks-frontend


## Run Locally

### Install dependencies
`pip3 install -r requirements.txt`

### Start the server locally
`fastapi dev app/main.py --host 0.0.0.0 --port 3000`

### Check swagger documentation
Open API docs at http://localhost:3000/docs