from openai import OpenAI

OpenAI_API_KEY = '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'

client = OpenAI(api_key=OpenAI_API_KEY)

with open('Files/artykul.txt', 'r', encoding='utf-8') as file:
    content = file.read()