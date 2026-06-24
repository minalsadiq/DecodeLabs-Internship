
#   DecodeLabs Industrial Training Kit | Batch 2026
#   Project 1: Rule-Based AI Chatbot
#   Name  : Minal Sadiq
#   Concept : Control Flow + Logic (No ML required)


knowledge_base = {
    # Greetings
    "hello"         : "Hello! Welcome to DecodeLabs Assistant. How can I help you today?",
    "hi"            : "Hi there! I'm your DecodeLabs AI Bot. What do you need?",
    "hey"           : "Hey! Great to see you. Ask me anything!",

    # About DecodeLabs
    "what is decodelabs?" : "DecodeLabs is a tech training company that provides hands-on industrial AI projects for interns.",
    "who made you?"       : "I was built by a DecodeLabs intern Minal Sadiq using Python  pure rule-based logic, no ML yet!",
    "about decodelabs"   : "DecodeLabs is based in Greater Lucknow, Pakistan. They train future AI engineers through real projects.",

    # Time & Date
    "what time is it?" : "I don't have a clock, but Python's datetime module can help with that in future projects!",
    "what is today?"   : "I don't track dates yet that's a feature for Project 2!",

    # Help
    "can you please help me?" : "Sure! You can ask me: greetings, about DecodeLabs, Python basics, AI concepts, or just say 'joke'.",
    "what can you do?": "I can answer questions about DecodeLabs, Python, AI, and tell jokes! Try asking me something.",

    # Python
    "what is python?"  : "Python is a beginner friendly programming language widely used in AI, data science, and automation.",
    "why python?"      : "Python has simple syntax, powerful libraries like NumPy & TensorFlow, and a huge community!",
    "what is a loop?"  : "A loop repeats a block of code. I myself run inside a 'while True' loop that's my heartbeat!",
    "what is a dictionary" : "A dictionary in Python stores key-value pairs. My entire brain IS a dictionary!",

    # AI Concepts
    "what is ai?"      : "AI stands for Artificial Intelligence making machines simulate human-like decision-making.",
    "what is ml?"      : "ML (Machine Learning) teaches machines using data. I use rules instead I'm rule-based AI!",
    "difference between ai and ml?" : "AI is the broad concept of smart machines. ML is a subset where machines learn from data automatically.",
    "what is rule based ai" : "Rule-based AI uses explicit if-else logic defined by humans. It's transparent, safe, and 100% predictable!",

    # Fun / Personality
    "joke"           : "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "are you smart"  : "I know everything I was taught and nothing more. That's the beauty and limit of rule-based AI!",
    "how are you"    : "I'm running at 100% efficiency! No bugs detected. How are YOU doing?",
    "what is your name?" : "I'm DecoBot  your Project 1 AI assistant built at DecodeLabs!",

    # Farewell
    "bye"            : "Goodbye! Keep building amazing things. See you soon! 👋",
    "goodbye"        : "Take care! Remember: every great AI engineer started with their first rule. You just wrote yours!",
    "thanks"         : "You're welcome! It's what I'm programmed for 😊",
    "thank you"      : "Happy to help! That's my purpose.",
}


# STARTUP MESSAGE
def show_welcome():
    print("=" * 55)
    print("   🤖  DecoBot — Rule-Based AI Chatbot")
    print("   DecodeLabs Industrial Training | Project 1")
    print("=" * 55)
    print("   Type 'help' to see what I can do.")
    print("   Type 'quit' to exit the chatbot.")
    print("=" * 55)
    print()

# ====================================================== #
# SANITIZATION FUNCTION
# Cleans raw user input so matching works reliably.
# "Hello " → "hello"
# "HELLO"  → "hello"
# " HeLLo" → "hello"
def sanitize(raw_input):
    clean = raw_input.lower().strip()  # lowercase + remove extra spaces
    return clean

# ====================================================== #
# CORE: GET RESPONSE FUNCTION
# Uses dictionary .get() method THE PROFESSIONAL APPROACH
# If the key exists → returns the response
# If not           → returns the fallback message
# This is O(1) speed instant, no matter how big the dictionary!


def get_response(user_input):
    # COMPONENT 4: FALLBACK default reply for unknown inputs
    fallback = "🤔 I don't understand that yet. Type 'help' to see what I can answer!"
    
    response = knowledge_base.get(user_input, fallback)
    return response

# ====================================================== #
# COMPONENT 1: MAIN LOOP (The Heartbeat)
# The chatbot stays alive inside 'while True'
# It only stops when the user types 'quit' → break


def run_chatbot():
    show_welcome()

    while True:  # Infinite loop chatbot keeps running

        # Step 1: Get raw input from user
        raw_input = input("You: ")

        # Step 2: Sanitize it
        user_input = sanitize(raw_input)

        # COMPONENT 5: EXIT STRATEGY clean break command
        if user_input in ["quit", "exit", "stop", "q"]:
            print("\nDecoBot: Shutting down... Goodbye, future AI Engineer! 🚀")
            print("=" * 55)
            break  # Exit the while loop cleanly

        # Step 3: Skip empty inputs (user just pressed Enter)
        if user_input == "":
            print("DecoBot: Please type something! I'm listening...\n")
            continue

        # Step 4: Get response from knowledge base
        reply = get_response(user_input)

        # Step 5: Print the response
        print(f"DecoBot: {reply}\n")


# ====================================================== #
# PROGRAM ENTRY POINT
# This line ensures the chatbot only runs when
# you execute THIS file directly (not when imported)


if __name__ == "__main__":
    run_chatbot()