
FILE_NAME = "c:\\Users\\Hanna_Hlushakova\\Documents\\Cources\\Python\\Lab_5_publications.txt"
DATE_FORMAT = "%Y-%m-%d"


class BasicPublication:
    def __init__(self, def_text: str) -> None:
        self._text = def_text

    @staticmethod
    def _write_to_file(text_to_publish: str, file_name: str = FILE_NAME) -> None:
        with open(file_name, mode="a") as file:
            file.write(text_to_publish)

    @staticmethod
    def show_publications(file_name: str = FILE_NAME) -> str:
        with open(file_name, mode='r') as file:
            file_data = file.read()
        return file_data

