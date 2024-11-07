from flask import Flask, request, jsonify
import wikipediaapi

app = Flask(__name__)
wiki_wiki = wikipediaapi.Wikipedia('en')

# Function to fetch response from Wikipedia
def get_wikipedia_summary(topic):
    page = wiki_wiki.page(topic)
    if page.exists():
        return page.summary[:500]  # Limit response length to 500 characters
    else:
        return "I'm sorry, I couldn't find information on that topic in Wikipedia."

# Main function for Jarvis commands
def jarvis_response(command):
    if "play song" in command:
        song_name = command.split("play song ")[1]
        return f"Playing song: {song_name} (feature not fully implemented)"
    elif "who is your creator" in command:
        return "Pranshul Jain"
    elif "mujhe" in command and "ke baare me batao" in command:
        topic = command.split("mujhe ")[1].split(" ke baare me batao")[0]
        return get_wikipedia_summary(topic)
    elif command in ["hi", "hello", "hey", "hey jarvis", "hi jarvis", "how are you"]:
        return "Hi sir, nice to meet you!"
    else:
        # If command is unknown, attempt Wikipedia search
        return get_wikipedia_summary(command)

# API endpoint to receive commands
@app.route("/api/command", methods=["POST"])
def api_command():
    data = request.get_json()
    command = data.get("command", "")
    response = jarvis_response(command)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
