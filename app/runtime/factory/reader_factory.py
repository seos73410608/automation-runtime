from app.excel.excel_reader import read_excel


class ReaderFactory:

    @staticmethod
    def get(reader_name):

        if reader_name == "ExcelReader":
            return read_excel

        raise ValueError(
            f"Unknown reader: {reader_name}"
        )