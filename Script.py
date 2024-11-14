from openai import OpenAI
#Add key
OpenAI_API_KEY = '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'
client = OpenAI(api_key=OpenAI_API_KEY)
#Read files
with open('Files/artykul.txt', 'r', encoding='utf-8') as file:
    content = file.read()
#Prompt to chat
prompt = (f"""
        Wczytaj zmienną o nazwie 'content'. Twoim zadaniem jest zmodyfikowanie tekstu tak, aby wyglądał jak artykuł gotowy do opublikowania na stronie. Użyj znaczników HTML, takich jak <p>, <b>, <div>, <h1>, itd. Zaproponuj miejsca w artykule, gdzie można dodać zdjęcia, używając znacznika <img> z atrybutem src="image_placeholder.jpg". Dodaj atrybut alt do
        każdego obrazka z dokładnym opisem, który można wykorzystać do wygenerowania grafiki. Nie dodawaj niepotrzebnych oznaczeń, takich jak ''', html itp.

        Tekst do modyfikacji:
        {content}

        Instrukcja modyfikacji:
        - Nie dodawaj żadnych niepotrzebnych oznaczeń.
        - Zredaguj tekst.
        - Zaproponuj miejsca na zdjęcia.
        - Użyj znaczników HTML.
        

        """)
#Response to chat
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": prompt},
        {
            "role": "user",
            "content": "wykonaj polecenie systemowe"
        }
    ]
)

#Get response
result = response.choices[0].message.content
#Save to files
print(result)

with open('Files/artykul.html', 'w', encoding='utf-8') as file:
    file.write(result)