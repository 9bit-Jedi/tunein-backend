# TuneIn Backend Repository

## Tech Stack

- **Framework**: Django (Python)
- **Database**: Sqlite3
- **Socket Connection**: Node, WebSocket
- **API Layer**: Django REST Framework (DRF)
- **Virtual Environment**: `venv` (Python built-in)
- **Frontend**: React + MUI

---

## Getting Started

### Clone the Repository

To get started, first clone the repository:

```bash
git clone https://github.com/9bit-Jedi/tunein-backend.git
```

### Change to Project Directory

Navigate into the project directory:

```bash
cd tunein-backend
```

### Setup Virtual Environment

Create and activate a virtual environment to manage dependencies:

1. Create the virtual environment:

   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:

   - On **Windows**:
   
     ```bash
     .\.venv\Scripts\activate
     ```

   - On **Mac/Linux**:
   
     ```bash
     source .venv/bin/activate
     ```

### Install Dependencies

With the virtual environment activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Development Server

Before running the server, ensure your environment is properly set up.

1. If running for the **first time**, ensure the database is migrated:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. You may need to create a **superuser** to access Django's admin interface:

    ```bash
    python manage.py createsuperuser
    ```

3. Start the development server:

    ```bash
    python manage.py runserver
    ```

By default, the server will be running on `http://127.0.0.1:8000/`.

---

## Setting Up the WebSocket Server

### Install Node.js Dependencies

1. Navigate to the WebSocket server folder:

   ```bash
   cd websocket-server
   ```

2. Initialize the project:

   ```bash
   npm install
   ```

### Run the WebSocket Server

```bash
node server.js
```

The WebSocket server will run at `ws://localhost:8080/`.

---

## Git Workflow

To sync the repository with the latest code from the `main` branch, use the following commands:

1. **Pull the latest changes**:

    ```bash
    git pull origin main
    ```

2. **Switch branches** (if needed):

    ```bash
    git checkout <branch_name>
    ```

3. **Install/update dependencies** (after pulling new changes):

    ```bash
    pip install -r requirements.txt
    ```

