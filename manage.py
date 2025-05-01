import subprocess
import os
import sys
import platform

FRONTEND_DIR = "frontend"
BACKEND_DIR = "backend"

def install_all():
    print("Installing frontend dependencies...")
    subprocess.run(["npm", "install"], cwd=FRONTEND_DIR, shell=True)

    print("Installing backend dependencies...")
    subprocess.run(["npm", "install"], cwd=BACKEND_DIR, shell=True)

def run_all():
    if platform.system() == "Windows":
        frontend_path = os.path.abspath(FRONTEND_DIR)
        backend_path = os.path.abspath(BACKEND_DIR)

        # Open frontend dev server in a new terminal
        subprocess.Popen([
            "start", "cmd", "/k", f"cd /d {frontend_path} && npm run dev"
        ], shell=True)

        # Open backend dev server in another terminal
        subprocess.Popen([
            "start", "cmd", "/k", f"cd /d {backend_path} && npm run dev"
        ], shell=True)

    else:
        # Non-Windows systems (macOS/Linux)
        subprocess.Popen(["npm", "run", "dev"], cwd=FRONTEND_DIR)
        subprocess.Popen(["npm", "run", "dev"], cwd=BACKEND_DIR)

def print_help():
    print("Usage:")
    print("  python manage.py install   # Install dependencies in both frontend and backend")
    print("  python manage.py dev       # Run both frontend and backend dev servers")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1]

    if command == "install":
        install_all()
    elif command == "dev":
        run_all()
    else:
        print_help()
