"""
<publications>
        <publication type="Ad">
            <text> Sample text for advertisement for XML lab</text>
            <expiration_date>2025-01-01</expiration_date>
        </publication>
        <publication type="Tip">
            <text> Sample text for tip of the day for XML lab</text>
            <rating>0.05</rating>
        </publication>
        <publication type="News">
            <text> Sample text for news for XML lab</text>
            <city>Prague</city>
        </publication>
</publications>
"""
from util import XMLPublisher


def show_formatting() -> None:
    with open("util/FileFormats/xml_pub_file_format.txt", mode='r', encoding='utf8') as file:
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
            pub_reader = XMLPublisher.XMLPublisher(user_file_path)
            pub_reader.file_processing()
        elif user_choice == "2":
            pub_reader = XMLPublisher.XMLPublisher()
            pub_reader.file_processing()
        elif user_choice == "3":
            print(XMLPublisher.XMLPublisher.show_publications())
        elif user_choice == "q":
            break
