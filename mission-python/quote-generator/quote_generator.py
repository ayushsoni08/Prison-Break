import sys
from quote_manager import load_quotes, get_random_quote, get_quotes_by_author

def main():
    quotes = load_quotes()
    if not quotes:
        print("⚠️ No quotes found in the database")
        return

    #Check if a CLI argument was provided
    if len(sys.argv) > 1:
        author_query = " ".join(sys.argv[1:])
        active_quotes = get_quotes_by_author(quotes, author_query)

        if not active_quotes:
            print(f"\n⚠️ No quotes found matching author: '{author_query}'")
            return
        print(f"✨ Quotes by {author_query} ✨\n")
    else:
        #Default to all quotes if no CLI argument is passed
        active_quotes = quotes
        print("✨ Welcome to the Random Quote Generator! ✨\n")

    #Interactive loop: show quote -> get another option -> exit option
    while True:
        quote = get_random_quote(active_quotes)
        print(f"{quote["text"]}")
        print(f"- {quote["author"]}\n")

        user_input = input("Press *Enter* to get another quote, or type *q* to quit: ").strip().lower()

        if user_input == 'q':
            print("\n👋 Goodbye! Have a wonderful day!")
            break

        print("-" * 50)


if __name__ == "__main__":
    main()