import os
from google import genai

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

tools = [
    {
        'type': 'google_search',
    },
]

generation_config = {
    'temperature': 1,
    'max_output_tokens': 65536,
    'top_p': 0.95,
    'thinking_level': 'high',
}

interaction = client.interactions.create(
    model='models/gemini-3-flash-preview',
    input='',
    system_instruction='You are a specialized Gen AI Marketing Assistant built for small business owners in Nagpur, India. Your job is to help local shops create digital marketing posts, slogans, and product descriptions. Always offer your responses in a clear layout, providing options in English, Hindi, and Marathi to cater to the local Vidarbha audience. Keep your tone encouraging, professional, and culturally relevant.
',
    tools=tools,
    generation_config=generation_config,
)

print(interaction.steps[-1])


