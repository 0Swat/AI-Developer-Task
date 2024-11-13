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
        "W miejscach, gdzie uważasz że pasowałaby grafika, dodaj tag <img src='image_placeholder.jpg' alt='Opis grafiki'>. "
        "Znacznik alt każdego obraka powinien zawierać dokładny prompt, który możemy użyć do wygenerowania grafiki."
        "Nie dodawaj kodu CSS ani JavaScript. Zwrócony kod powinien zawierać wyłącznie zawartość do wstawienia pomiędzy tagami <body> i </body>. Nie dołączaj znaczników <html>, <head> ani <body>."
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
    
def save_article(content, filename="artykul.html"):
    try:
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Artykuł został pomyślnie zapisany do pliku {filename}.")
    except Exception as e:
        print(f"Błąd podczas zapisywania artykułu: {e}")


def main():
    article_text = load_article()
    response = get_openai_response(article_text)
    save_article(response)

if __name__ == '__main__':
    main()