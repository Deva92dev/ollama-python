
import httpx

message = []

url = "http://127.0.0.1:11434/api/chat"

with httpx.Client(
    timeout=50,
) as client:
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input: break
            temp = message + [{"role":"user", "content": user_input}]
            payload = {
            "model": "gemma4:e2b",
            "messages": temp,
            "stream":False
            }

            response = client.post(url, json = payload)
            response.raise_for_status()
            res = response.json()
            reply = res["message"]["content"]

            print(f"Assistant: {reply}")
            message.append({"role": "user", "content":user_input})
            message.append({"role": "assistant", "content": reply})

        except httpx.HTTPStatusError as e:
            # handles 4xx and 5xx errors
            print(f"HTTP Error {e.response.status_code}: {e.request.url}")
        except httpx.RequestError as e:
            # Handles network issues (timeouts, DNS, etc.)
            print(f"Request Error: {e.request.url}")
        except ValueError as e:
            # Handles invalid data types or arguments, e.g., invalid JSON parsing
            print(f"Value Error: {e}")
        except KeyError as e:
            # Handles missing keys in response data
            print(f"Missing data key: {e}")
        except (KeyboardInterrupt, EOFError):
            # Clean exit on user interrupt or end of input
            print("\nOperation cancelled by user.")
            break



