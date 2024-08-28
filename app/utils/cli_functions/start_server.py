import subprocess

def start_server():
    """Start the FastAPI server using Uvicorn"""
    subprocess.run(["uvicorn", "app.main:app", "--reload"])