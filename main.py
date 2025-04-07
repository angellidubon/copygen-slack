import os
import openai
from flask import Flask, request, jsonify
import langdetect

app = Flask(__name__)

openai.api_key = os.environ["OPENAI_API_KEY"]

def detect_language(text):
    return langdetect.detect(text)

def count_emoji_chars(text):
    return sum(2 if ord(c) > 10000 else 1 for c in text)

def format_prompt(brief, lang):
    if lang == "pt":
        return f"Crie 3 opções de mensagem de WhatsApp com emojis, abaixo de 1024 caracteres cada (emojis contam como 2), para o seguinte briefing: \"{brief}\". Adapte ao local e à estação do ano mencionada ou detectada. Seja claro e persuasivo."
    else:
        return f"Crea 3 opciones de mensaje de WhatsApp con emojis, cada una debajo de 1024 caracteres (los emojis cuentan como 2), para el siguiente briefing: \"{brief}\". Adapta al lugar y estación del año mencionada o detectada. Sé claro y persuasivo."

@app.route("/slack", methods=["POST"])
def slack_command():
    text = request.form.get("text", "")
    lang = detect_language(text)

    prompt = format_prompt(text, lang)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um especialista em marketing de WhatsApp."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    output = response["choices"][0]["message"]["content"]

    return jsonify({
        "response_type": "in_channel",
        "text": output
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)