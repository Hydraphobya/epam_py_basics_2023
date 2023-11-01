from util.PubTypes import News, PrivateAd, TipOfTheDay, BasicPublication
import os
import xml.etree.ElementTree as ET
import Lab_4
import decimal

XML_FILE = "c:\\Users\\Hanna_Hlushakova\\Documents\\Cources\\Python\\Files\\new_publish.xml"


class XMLPublisher:
    def __init__(self, file_path: str = XML_FILE) -> None:
        self._file_path = file_path

    def _read_xml_file(self) -> ET.Element:
        draft = []
        if os.path.exists(self._file_path):
            with open(self._file_path, mode='r', encoding='utf8') as file:
                draft = ET.parse(file).getroot()
                #xml_root = draft
                # loads(file.read())["publications"]
        else:
            print(f"File under path {self._file_path} not found!")
        return draft

    def _delete_file(self) -> None:
        if os.path.exists(self._file_path):
            os.remove(self._file_path)
        else:
            print(f"File under path {self._file_path} not found!")
        return

    def file_processing(self) -> None:
        draft = self._read_xml_file()
        if len(draft) > 0:
            for pub in draft:
                XMLPublisher._publication_processing(pub)
            self._delete_file()

    @staticmethod
    def _publication_processing(draft: ET.Element) -> None:
        #   load text

        #   load publication type
        pub_type = draft.attrib['type']
        if pub_type == "News":
            pub_text = ''
            pub_city = ''
            for atr in draft:
                if atr.tag == "text":
                    pub_text = atr.text
                elif atr.tag == "city":
                    pub_city = atr.text
            normalized_text = Lab_4.normalize_str(pub_text)
            News.News(normalized_text, pub_city).publish()
        elif pub_type == "Ad":
            pub_text = ''
            pub_expiration_date = ''
            for atr in draft:
                if atr.tag == "text":
                    pub_text = atr.text
                elif atr.tag == "expiration_date":
                    pub_expiration_date = atr.text
            normalized_text = Lab_4.normalize_str(pub_text)
            try:
                PrivateAd.PrivateAd.from_str(normalized_text, pub_expiration_date).publish()
            except ValueError as exp_dt_error:
                print("Invalid date.")
                print(exp_dt_error)
                return
        elif pub_type == "Tip":
            pub_text = ''
            pub_rating = ''
            for atr in draft:
                if atr.tag == "text":
                    pub_text = atr.text
                elif atr.tag == "rating":
                    pub_rating = atr.text
            normalized_text = Lab_4.normalize_str(pub_text)
            try:
                TipOfTheDay.TipOfTheDay.from_str(normalized_text, pub_rating).publish()
            except decimal.InvalidOperation as rating_error:
                print("Invalid rating.")
                print(rating_error)
                return

    @staticmethod
    def show_publications() -> str:
        return BasicPublication.BasicPublication.show_publications()


if __name__ == "__main__":
    xml_pub = XMLPublisher()
    # xml_pub.file_processing()
    print(xml_pub.show_publications())
