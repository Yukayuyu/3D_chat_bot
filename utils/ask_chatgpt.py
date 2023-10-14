import openai
from utils import config_loader, chatgpt_context

openai.api_key = config_loader.api_key


def ask(id, req):
    his = chatgpt_context.getConext(id)
    his.append({"role": "user", "content": req})

    response = openai.ChatCompletion.create(
        model=config_loader.model,
        messages=his,
        temperature=float(config_loader.temperature),
        max_tokens=int(config_loader.max_tokens),
        top_p=float(config_loader.top_p),
        frequency_penalty=float(config_loader.frequency_penalty),
        presence_penalty=float(config_loader.presence_penalty)
    )

    response_message = response.choices[0].message.content
    print(response_message)

    chatgpt_context.updateConext(id, req, response_message)

    return response_message


def getResponseLetters(id):
    return chatgpt_context.getLastLetter(id)
