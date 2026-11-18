# What exactly is a "trust boundary" in your drawn data-flow diagram?
- Trust boundary is in my data diagram flow is application layer

# Why is it necessary to bind the Ollama daemon specifically to 127.0.0.1 instead of 0.0.0.0?
- because on 0.0.0.0 anyone from internet can access my port and might leak my credentials

# How does your operating system enforce that local socket binding to drop external traffic?
- By binding ollama endpoint to my system sepecific using , sudo ss -ltnp | grep ':11434'

# What happens if OLLAMA_HOST is misconfigured and your laptop connects to a public Wi-Fi network?
- Then i might loose credentials to internet and hackers will steal data

# Why not just let the Ollama daemon handle user authentication directly instead of putting an application API in front of it?
- because ollama generakky don't do authentication and it is safe practice to have authentication in application layer

# How does the output from your ss or lsof command definitively prove the port is isolated?
- i tested from my app and got the response on same endpoint

# Where could this network isolation fail when you eventually move this setup into a Docker container?
- especially in network binding host

# Can you verbally trace the exact path of a request from the user, through your application, to the model, and back?
- Yes, just strated so not much have toay 