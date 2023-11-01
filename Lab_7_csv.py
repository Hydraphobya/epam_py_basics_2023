from util import FileStats
from util.PubTypes import BasicPublication

if __name__ == "__main__":
    file_path = BasicPublication.FILE_NAME
    text = BasicPublication.BasicPublication.show_publications(file_path)
    FileStats.print_text_stat(text, file_path)