import subprocess
import sys
import os

# Simple server runner that might bypass firewall issues
if __name__ == "__main__":
    print("Starting FastAPI server...")
    print("Server will be available at: http://127.0.0.1:3001")
    
    # Change to the directory containing main.py
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Run uvicorn directly
    subprocess.run([
        sys.executable, "-m", "uvicorn", 
        "main:app", 
        "--host", "127.0.0.1", 
        "--port", "3001",
        "--reload"
    ])
