# AttendIQ

AttendIQ is an AI-powered attendance management app built with Streamlit. It helps teachers take attendance using facial recognition and voice-based verification, while students can enroll in subjects, log in using face recognition, and track their attendance status.

## Overview

This project is designed for classroom attendance workflows where:

- a teacher creates and manages subjects
- students enroll in a class using a subject code
- students log in with face recognition
- teachers upload classroom photos or use voice attendance
- the app identifies students and records attendance in a database

## Features

- Teacher and student portal flows
- Face-based student login and registration
- Subject creation and sharing with course codes
- AI attendance analysis from uploaded classroom photos
- Optional voice attendance mode
- Attendance records and subject overview dashboards
- Supabase-powered storage and retrieval

## Tech Stack

- Python
- Streamlit
- Supabase
- NumPy, Pandas
- Pillow
- scikit-learn
- dlib / face_recognition pipeline
- librosa / resemblyzer

## Project Structure

```text
AttendIQ-app/
├── app.py                     # Main entry point for Streamlit
├── requirements.txt           # Python dependencies
├── assets/                    # Static UI assets like logos and images
├── src/
│   ├── components/            # UI dialogs, cards, header/footer widgets
│   ├── database/              # Supabase client and database logic
│   ├── pipelines/             # Face recognition and voice analysis pipelines
│   ├── screens/               # Teacher/student/home screens
│   ├── ui/                    # Styles and layout helpers
│   └── utils/                 # Utility functions
├── .streamlit/                # Local secrets for Streamlit (created by you)
├── .venv/                     # Virtual environment (created locally)
└── README.md
```

## Prerequisites

Before starting, make sure you have:

- Python 3.10 or later
- pip installed
- Git installed (optional but recommended)
- A Supabase project created in the Supabase dashboard
- Access to your project URL and API key

## Step-by-Step Setup

### 1. Open a terminal in the project folder

Go to the project root:

```bash
cd AttendIQ-app
```

If you are in the correct folder, you should see files such as `app.py`, `requirements.txt`, and `src/`.

### 2. Create a virtual environment

Create an isolated Python environment for this app:

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activation, your terminal prompt usually changes and shows the virtual environment name.

### 3. Upgrade pip

It is a good idea to ensure pip is updated before installing dependencies:

```bash
python -m pip install --upgrade pip
```

### 4. Install project dependencies

Install all packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

This may take several minutes because the project includes ML-related packages like `dlib-bin`, `face_recognition`, and audio processing libraries.

> If installation fails on Windows, you may need Visual C++ build tools or additional OS-level support for face recognition libraries.

### 5. Create the Streamlit secrets file

The app reads database credentials from `.streamlit/secrets.toml`.

Create a folder named `.streamlit` in the project root if it does not already exist:

```bash
mkdir .streamlit
```

Then create a file named `secrets.toml` inside it:

```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-anon-or-service-role-key"
```

Replace the example values with your own Supabase URL and key.

### 6. Verify the secret file is in the right place

Your folder should look like this:

```text
AttendIQ-app/
├── .streamlit/
│   └── secrets.toml
├── app.py
├── requirements.txt
├── src/
```

The app uses:

```python
st.secrets["SUPABASE_URL"]
st.secrets["SUPABASE_KEY"]
```

so the file must be exactly named `secrets.toml` and inside `.streamlit/`.

### 7. Run the app

Start Streamlit from the project root:

```bash
streamlit run app.py
```

After a short while, Streamlit will print a local URL such as:

```text
Local URL: http://localhost:8501
```

Open that URL in your browser.

## How the App Works

### Teacher Flow

1. Select the Teacher portal on the home screen.
2. Log in or register a teacher account.
3. Create one or more subjects.
4. Share the subject code with students.
5. Upload photos for attendance or use voice attendance.
6. Run the AI attendance analysis.
7. View attendance results and summaries.

### Student Flow

1. Select the Student portal.
2. Use the camera to log in with face recognition.
3. Register a new profile if the face is not recognized.
4. Enroll in available subjects using a join code.
5. View attendance information for enrolled courses.

## Database Requirements

This app expects the backend to have tables and records compatible with the SQL queries in the project. In particular, the app uses Supabase tables related to:

- teacher records
- student records
- subjects
- subject enrollments
- attendance logs

You need to make sure your database matches the app’s expected schema or the app will fail when loading data.

## Common Issues and Fixes

### 1. `ModuleNotFoundError`

If you see missing package errors, reinstall dependencies:

```bash
pip install -r requirements.txt
```

### 2. Face recognition install errors

If `dlib` or `face_recognition` fails to install:

- upgrade pip
- install Visual Studio Build Tools on Windows
- ensure you are using a supported Python version
- retry the install inside the activated virtual environment

### 3. Supabase connection errors

If the app cannot connect to Supabase:

- confirm the values in `.streamlit/secrets.toml`
- check that the URL is correct
- check that the API key is valid
- verify the database is reachable

### 4. Streamlit does not start

Run:

```bash
streamlit --version
```

If that works, the Streamlit installation is valid. Then run:

```bash
streamlit run app.py
```

## Recommended Development Flow

1. Create the virtual environment.
2. Install dependencies.
3. Add the Supabase secrets file.
4. Start the app.
5. Test teacher login and subject creation.
6. Test student registration and face login.
7. Validate photo attendance processing.
8. Check attendance records in the database.

## Notes

- This project depends on ML and audio libraries, so setup time may be longer than a simple Python web app.
- Some features are environment-sensitive and may require system dependencies depending on your OS.
- The app is intended as a prototype or educational project and may need schema adjustments for production use.

## License

This project is provided as a local application prototype for educational and attendance-use scenarios. Add your preferred license if you intend to distribute it.
