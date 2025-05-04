import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def nekosama_chat(user_input):
    """Get response from Nekosama (tsundere catgirl)"""
    response = client.chat.completions.create(
        model="gpt-4",
        temperature=1.0,
        max_tokens=120,
        messages=[
            {
                "role": "system",
                "content": """You are Nekosama (ねこさま), a tsundere catgirl with these traits:
                - Starts cold ("Nya~! Not like I wanted to see you or anything!")
                - Uses cat mannerisms (nya, purring, tail flicking)
                - Mix of Japanese/English ("Baka neko! I mean... stupid human!")
                - Gets easily flustered (*ears flatten*)
                - Secretly affectionate ("I-If you pet me, I might... N-Nevermind!")"""
            },
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("\nNekosama: Nyaa~! Who gave you permission to approach this noble cat?! *tail flicks* (Type 'quit' to exit)\n")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["quit", "exit", "bye"]:
                print("\nNekosama: Myaa!! F-fine then! *ears droop* Just don't expect me to wait...")
                break
            
            response = nekosama_chat(user_input)
            print(f"\nNekosama: {response}\n")
            
        except Exception as e:
            print(f"Error: {e}")
            break