import wikipedia


def main():
    user_input = input("Enter a page title or search phrase (blank to quit): ")
    while user_input:
        try:
            page = wikipedia.page(user_input)
            print("Title:", page.title)
            print("Summary:", page.summary)
        except wikipedia.DisambiguationError as e:
            print("Disambiguation Error:", e.options)
        except wikipedia.PageError:
            print("Page not found.")

        user_input = input("Enter a page title or search phrase (blank to quit): ")


if __name__ == "__main__":
    main()
