import pyexcel as pe
import os

class Defaulter:

    def __init__(self):

        return

    def run(self, input_path, archieve_path):
        for file in os.listdir(input_path):
            if file.endswith(".xlsx"):
                try:
                    records = pe.iget_records(file_name="Book2.xlsx")
                    for record in records:
                        print(record['Account_no'], record['balance'])

                except Exception as e:
                    None

        return

if __name__ == "__main__":
    object = Defaulter()
    object.run("input/defaulter/")