import os
import subprocess

# Get all Python files in the current folder
files = [f for f in os.listdir('.') if f.endswith('.py') and f != 'run_all.py']

for file in files:
    print(f"\n--- Running {file} ---")
    subprocess.run(['python', file])