def load_article(filename="article.txt"):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"Błąd: Plik '{filename}' nie został znaleziony.")
        return None


def main():
    article_text = load_article()

if __name__ == '__main__':
    main()