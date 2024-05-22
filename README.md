# Task Management API

This is a simple task management API built using Flask. It allows users to perform basic CRUD operations on tasks, which include attributes like id, title, description, and status.

Submitted by: Renze Meinard Mortiga, BSIT 3A

## Table of Contents

- [Overview](#overview)
- [Setup Instructions](#setup-instructions)
- [Running the API](#running-the-api)

## Overview

The Task Management API provides a simple way to manage tasks. Each task has an ID, title, description, and status. The API supports the following operations:

- Create a new task
- Retrieve all tasks
- Retrieve a specific task by ID
- Update a specific task by ID
- Delete a specific task by ID

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Project Structure

Ensure you have the following project structure:

flask_project/
├── app/
│ ├── init.py
│ ├── routes.py
├── venv/
├── app.py
├── requirements.txt
└── README.md

### Steps to Set Up the Project

1. **Navigate to the Project Directory:**

    Open a terminal or command prompt and navigate to the project directory:

    ```sh
    cd C:\Users\renze\OneDrive\Desktop\flask_project
    ```

2. **Create and Activate a Virtual Environment:**

    - Create a virtual environment:

      ```sh
      python -m venv venv
      ```

    - Activate the virtual environment:
      - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
      - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

3. **Install Dependencies:**

    Install the required packages listed in `requirements.txt`:

    ```sh
    pip install -r requirements.txt
    ```

## Running the API

To start the Flask application, run:

```sh
python app.py
