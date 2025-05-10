# type: ignore
# Usando subprocess para executar e comandos externos
import subprocess
import sys

# sys.platform = linux, linux2, darwin, win32

# Define command based on operating system
cmd = ['ls', '-lah', '/']  # Changed to list format for better security
encoding = 'utf_8'
system = sys.platform

if system == "win32":
    cmd = ['ping', '127.0.0.1']
    encoding = 'cp850'

# Execute the command
proc = subprocess.run(
    cmd,
    capture_output=True,
    text=True,
    encoding=encoding,
    shell=False  # Changed to False for better security
)

print()

# Print command output
print(proc.stdout)