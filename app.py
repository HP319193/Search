import chainlit as cl
from duckduckgo_search import DDGS

@cl.on_message
async def main(message: cl.Message):
    query = message.content
    msg = cl.Message(content="")
    await msg.send()

    results = DDGS().text(query, max_results=5)

    response = ""
    for result in results:
        response += f"{result['title']}\n{result['body']}\n{result['href']}\n\n"

    for character in response:
        await msg.stream_token(character)
        await cl.sleep(0.01)

    await msg.update()
