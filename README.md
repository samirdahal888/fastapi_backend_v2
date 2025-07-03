# what is the project is about 
# 🎓 Student Management System (FastAPI)

## 📝 What is the project about?

This is a simple yet secure **Student Management System** built using **FastAPI** — a modern, fast (high-performance) web framework for building APIs with Python.

### ✨ Key Features:

- Only **authorized Admins** can perform **CRUD operations** (Create, Read, Update, Delete) on student data.
- Authentication is handled using **JWT (JSON Web Tokens)**.
- Unauthorized users attempting to access protected endpoints will receive a `401 Unauthorized` response.
- Uses **Docker** for easy deployment.
- Interactive API documentation available at `/docs`.

---

## 🚀 How to quickly start the project

This guide helps you set up and run the project **within minutes** using Docker.

### ✅ Step-by-step instructions:

### 1. 📥 Clone the repository

Open your terminal and run:

```bash
# This command downloads the code to your local machine.
git clone https://github.com/username/repo.git
cd your-repo

```
### 2. ⚙️ Setup environment variables

Before running the app, you need a .env file that stores sensitive settings like the secret key.

- Copy the example env_example file to .env:
```bash
cp env_example .env
```
- Generate a secure secret key using:
```bash
openssl rand -hex 32
```

-  Paste the key into your .env file:

SECRET_KEY="your_generated_key_here"
This key is used to sign and verify JWT tokens, which are required to authenticate requests.

### 3. 🐳 Run the app using Docker
- Make sure you have Docker and Docker Compose installed.

Start the application with:
 ```bash 
 docker compose up -d
```

4. 🌐 Open the API documentation
Visit the API docs in your browser:

```bash 
http://localhost:8000/docs
```
- Here, you can interact with all the available endpoints using a simple web interface (Swagger UI).




## 👨‍💻 For Development

If you're a developer or contributor who wants to work on this project locally, follow the steps below to set up your development environment.

### 1. Clone the repository

```bash
git clone https://github.com/username/repo.git
cd your-repo

```
### 2. Create and activate a virtual environment
This helps keep dependencies isolated.

```bash
python -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate
```

### 3. Install project dependencies
```bash 
pip install -r requirements.txt
```

### 4. Set up your .env file
- Copy the example env_example to .env and update the values (especially SECRET_KEY).

```bash 
cp env_example .env
```

- Generate a secure secret key:

```bash
openssl rand -hex 32
```
- Paste it into your .env file like this:

    - SECRET_KEY="your_generated_key"

### 5. Run the development server
```bash
uvicorn main:app --reload
```

- The --reload flag automatically restarts the server when you make changes to the code — great for development.

### Once started, visit:
```bash
 http://localhost:8000/docs
 ```

 ### 📌 Notes for contributors
-  Make sure to write clean, well-documented code.

- Follow existing folder and module structures (e.g., use routers/, schemas/, models/ properly).

- Before submitting a pull request:

- Test your changes

- Keep commit messages clear

- Avoid committing .env, .venv, or __pycache__ folders

- You’re welcome to open issues, suggest features, or improve documentation.


