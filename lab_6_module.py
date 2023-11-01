"""
{
    "publications": [
        {
            "type": "News" or "Ad" or "Tip", -- mandatory
            "text": "main text", -- mandatory
            "city": "Prague", -- mandatory for News
            "rating": "0,5", -- mandatory for Tip
            "expiration_date": "YYYY-MM-DD" -- mandatory for ad
        },
        {
            "type": "News" or "Ad" or "Tip", -- mandatory
            "text": "main text", -- mandatory
            "city": "Prague", -- mandatory for News
            "rating": "0,5", -- mandatory for Tip
            "expiration_date": "YYYY-MM-DD" -- mandatory for ad
        }
    ]
}
"""
from util import JSONPublisher


def show_formatting() -> None:
    with open("util/file_format.txt", mode='r', encoding='utf8') as file:
        print(file.read())


if __name__ == "__main__":
    while True:
        user_choice = input(" 0. Show the file formatting rules"
                            + "\n 1 - Load file"
                            + "\n 2 - Use default file"
                            + "\n 3 - Show publication file"
                            + "\n q - Quit"
                            + "\n")
        if user_choice == "0":
            show_formatting()
        elif user_choice == "1":
            user_file_path = input("Please, enter the file path: ")
            pub_reader = JSONPublisher.JSONPublisher(user_file_path)
            pub_reader.file_processing()
        elif user_choice == "2":
            pub_reader = JSONPublisher.JSONPublisher()
            pub_reader.file_processing()
        elif user_choice == "3":
            print(JSONPublisher.JSONPublisher.show_publications())
        elif user_choice == "q":
            break
