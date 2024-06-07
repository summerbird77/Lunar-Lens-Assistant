import os
import google.generativeai as genai
import telebot
from dotenv import load_dotenv

load_dotenv()

# Replace `os.getenv("TELEGRAM_TOKEN")` with your own token
bot = telebot.TeleBot(os.getenv("7480253592:AAFFwrQ_IPLj1jbBoVssE2jnE9POUenrSNA"), parse_mode=None)

# Replace `os.getenv("GENAI_API_KEY")` with your own API key
genai.configure(api_key=os.getenv("AIzaSyD7rqwU-R7CjcHcJ8x_ihdh8q3aReUjskg"))

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config = generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(
    history=[
{
      "role": "user",
      "parts": [
        "halo",
      ],
    },
        {
      "role": "model",
      "parts": [
        "Halo! Aku Lunar Lens, asisten pribadimu, siap membantu apa pun yang kamu butuhkan.  Bagaimana kabarnya hari ini?  Boleh aku tahu apa yang kamu rencanakan? \n",
      ],
    },
        {
      "role": "user",
      "parts": [
        "aku ingin ke planet mars, bagaimana keadaannya disana ?",
      ],
    },
        {
      "role": "model",
      "parts": [
        "Wah, ambisius! Mars memang planet yang menarik. Tapi sebelum kita membahasnya, bagaimana kabarnya hari ini?  Ceritakan tentang harimu. \n\nOke, tentang Mars...  Mars adalah planet yang dingin dan berdebu, dengan atmosfer tipis yang membuatnya tidak layak huni bagi manusia. Tapi, di bawah permukaannya tersimpan rahasia yang menarik.  Ada bukti kuat bahwa dulunya Mars memiliki air cair, mungkin bahkan lautan, dan mungkin bisa dihuni. \n\nApa yang ingin kamu ketahui tentang Mars secara spesifik? Apa yang membuatmu tertarik ke sana? \n",
      ],
    },
    ]
)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    convo.send_message(message.text)
    response = convo.last.text
    bot.reply_to(message, response)


bot.infinity_polling()