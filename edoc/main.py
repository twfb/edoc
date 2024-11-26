import olefile


def extract_streams(file_path):
    if not olefile.isOleFile(file_path):
        raise ValueError("The provided file is not a valid .doc file.")

    with olefile.OleFileIO(file_path) as ole:
        streams = ole.listdir()

        if ["WordDocument"] in streams:
            data = ole.openstream("WordDocument").read()
            return data
        else:
            raise ValueError("WordDocument stream not found.")


def extraxt_txt(file_path):
    data = extract_streams(file_path)
    decoded_text = data.decode("utf-16-le", errors="ignore").replace("\r", "\n")
    return "".join(i for i in decoded_text.split("\00") if i and "\n" in i)
