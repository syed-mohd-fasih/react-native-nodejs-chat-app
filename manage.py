import subprocess
import os
import sys
import platform
import shutil

FRONTEND_DIR = "frontend"
BACKEND_DIR = "backend"

def install_all():
    system = platform.system()

    if system == "Windows":
        print("Installing frontend dependencies...")
        subprocess.Popen(
            f'start cmd /k "cd /d {FRONTEND_DIR} && npm install && echo. && echo Press any key to close... && pause >nul && exit"',
            shell=True
        )

        print("Installing backend dependencies...")
        subprocess.Popen(
            f'start cmd /k "cd /d {BACKEND_DIR} && npm install && echo. && echo Press any key to close... && pause >nul && exit"',
            shell=True
        )

    elif system == "Linux":
        terminal = shutil.which("gnome-terminal") or shutil.which("x-terminal-emulator")
        if not terminal:
            print("Error: No suitable terminal emulator found.")
            return

        subprocess.Popen([
            terminal,
            "--",
            "bash",
            "-c",
            f"cd '{FRONTEND_DIR}' && npm install; echo -e '\\nPress any key to close...'; read -n 1; exit"
        ])

        subprocess.Popen([
            terminal,
            "--",
            "bash",
            "-c",
            f"cd '{BACKEND_DIR}' && npm install; echo -e '\\nPress any key to close...'; read -n 1; exit"
        ])

    elif system == "Darwin":  # macOS
        subprocess.Popen([
            "osascript",
            "-e",
            f'tell application "Terminal" to do script "cd \\"{FRONTEND_DIR}\\"; npm install; echo \\"\\nPress any key to close...\\"; read -n 1; exit"'
        ])

        subprocess.Popen([
            "osascript",
            "-e",
            f'tell application "Terminal" to do script "cd \\"{BACKEND_DIR}\\"; npm install; echo \\"\\nPress any key to close...\\"; read -n 1; exit"'
        ])

    else:
        print("Unsupported platform...")

    print("Dependencies installation launched in separate terminals.")

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
