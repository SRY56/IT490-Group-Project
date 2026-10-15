import subprocess
result = subprocess.run(["pgrep", "-f", "python3 backend_server.py"], capture_output=True, text=True)
if result.stdout.strip():
    print("ACTIVE")
else:
    print("INACTIVE")
