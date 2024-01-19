from typing import List
import os
import base64
from openai import OpenAI, Stream
from openai.types.chat import ChatCompletion, ChatCompletionChunk

def llm_chat(messages: List) -> ChatCompletion | Stream[ChatCompletionChunk]:

    client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=messages,
        max_tokens=4096,
        temperature=0,
    )
    return response

def llm_messages(
    system_prompt: str, user_prompt: str, image_url_list: List
) -> List:
    # Initialize the messages list
    messages = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": system_prompt,
                }
            ],
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_prompt,
                },
            ],
        },
    ]

    # Iterate over image URLs and add them to the "user" message content
    for url in image_url_list:
        user_message = {
            "type": "image_url",
            "image_url": {"url": url},
        }
        messages[1]["content"].append(user_message)

    return messages

def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def read_image(system_prompt : str, user_prompt : str, image_urls: List[str]) -> str:
    encoded_images = []
    for image_url in image_urls:
        encoded_images.append(
            f"data:image/jpeg;base64,{encode_image(image_url)}"
        )

    response = llm_chat(
        messages=llm_messages(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            image_url_list=encoded_images,
        )
    )
    result = response.choices[0].message.content

    #Do some special processing here to return a json
    return result