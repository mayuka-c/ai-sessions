import subprocess
import sys

MODEL = "granite3.3:8b"

print(f"Pulling {MODEL} model using Ollama...")
try:
    result = subprocess.run(
        ["ollama", "pull", MODEL],
        check=True,
        capture_output=True,
        text=True
    )
    print(result.stdout)
    print(f"Model {MODEL} downloaded successfully!")
except subprocess.CalledProcessError as e:
    print(f"Error downloading model: {e.stderr}")
    sys.exit(1)
except FileNotFoundError:
    print("Error: Ollama is not installed or not in PATH.")
    print("Please install Ollama from https://ollama.ai")
    sys.exit(1)
