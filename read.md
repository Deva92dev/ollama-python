installed python3 -m venv ollama-venv then started it using source ollama-venv/bin/active

# How to know if venv is active
- import sys
  print(sys.prefix != sys.base_prefix)   
  if it is true means that is active

# requirement files
  - To install from this file in the future: ''' pip install -r requirements.txt '''

# which model is running
- ollama ps and how much storage it is using



# ollama bindings

sudo systemctl edit ollama.service
[Service]
Environment="OLLAMA_HOST=127.0.0.1:11434"

Save the override, reload the manager, restart the service and inspect the listener again. These commands can interrupt requests that are currently running. On a shared system, schedule that interruption and tell users first.

sudo systemctl daemon-reload
sudo systemctl restart ollama.service
systemctl is-active ollama.service
sudo ss -ltnp | grep ':11434'