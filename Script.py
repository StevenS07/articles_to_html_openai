from openai import OpenAI
#Add key
OpenAI_API_KEY = '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'
client = OpenAI(api_key=OpenAI_API_KEY)
#Read files to edit
with open('Files/artykul.txt', 'r', encoding='utf-8') as file:
    content = file.read()
#Prompt to chat
prompt_edit_text = (f"""
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
        {"role": "system", "content": prompt_edit_text},
        {
            "role": "user",
            "content": "wykonaj polecenie systemowe"
        }
    ]
)
#Read files to marge
with open('Files/szablon.html', 'r', encoding='utf-8') as file:
    template = file.read()
#Get response
result = response.choices[0].message.content
#Save to files
with open('Files/artykul.html', 'w', encoding='utf-8') as file:
    file.write(result)

prompt_merge = (f"""
        Wczytaj zmienną o nazwie 'template' oraz zmienną o nazwię 'result'. Twoim zadaniem połączenie tych zmiennych zawartość z zmiennej result dodaj między znaczniki <body> </body> w zmienej template. nie dodawaj własnych oznaczen, opisów
        
        Zmienne do połączenia:
        {template}
        {result}
        
        Instrukcja modyfikacji:
        - scal tekst w wyznaczonym miejscu
        - nie dodawaj własych opisów 
        """)

response_marge = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": prompt_merge},
        {
            "role": "user",
            "content": "wykonaj polecenie systemowe"
        }
    ]
)
#Get response
marge_result = response_marge.choices[0].message.content
#Save to files
with open('Files/podglad.html', 'w', encoding='utf-8') as file:
    file.write(marge_result)