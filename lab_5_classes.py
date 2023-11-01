"""
Create a tool, which will do user generated news feed:

1.User select what data type he wants to add

2.Provide record type required data

3.Record is published on text file in special format

You need to implement:

1.News – text and city as input. Date is calculated during publishing.

2.Privat ad – text and expiration date as input. Day left is calculated during publishing.

3.Your unique one with unique publish rules.
Each new record should be added to the end of file. Commit file in git for review.
"""
import util


def user_interation() -> None:
    pub_pub = util.ConsolePublisher.ConsolePublisher()
    input_text = ""
    while input_text.lower() != "q":
        input_text = input(pub_pub.initial_message_get())
        if input_text == "1":
            pub_pub.publish_news()
        elif input_text == "2":
            pub_pub.publish_private_ad()
        elif input_text == "3":
            pub_pub.publish_tip()


if __name__ == '__main__':
    user_interation()
