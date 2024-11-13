import openai
from dotenv import load_dotenv
import os

def load_article(filename="article.txt"):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"Błąd: Plik '{filename}' nie został znaleziony.")
        return None


def get_openai_response(article_text):
    # load .env 
    load_dotenv()

    # set API
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # prompt + article
    prompt = (
        "Przetwórz poniższy tekst artykułu na kod HTML. "
        "Użyj odpowiednich tagów HTML, takich jak <h1>, <p>, itp., aby dobrze strukturyzować treść. "
        "W miejscach, gdzie sugerowane są grafiki, dodaj tag <img src='image_placeholder.jpg' alt='Opis grafiki'>. "
        "Dodaj podpisy pod obrazkami, jeśli są konieczne, używając tagu <figcaption>. "
        "Zwróć tylko zawartość pomiędzy <body> i </body>. "
        "Oto treść artykułu:\n\n" + article_text
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Jesteś ekspertem od generowania kodu HTML."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.5
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Błąd: {e}"

def main():
    article_text = load_article()
    response = get_openai_response(article_text)
    print(response)

if __name__ == '__main__':
    main()