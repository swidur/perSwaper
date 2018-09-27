import csv
from os import getcwd

class CsvReader:
    def __init__(self, read_dir):
        self.read_dir = read_dir
        self.csv_file = None

    def open_file(self):
        try:
            self.csv_file = open(self.read_dir, 'r', encoding='windows-1250')
            self.csv_reader = csv.reader(self.csv_file, delimiter=';')
            return True
        except FileNotFoundError:
            return False


    def one_benefits_executor(self):
        pesel_list = []
        next(self.csv_reader)
        if self.csv_file is not None:
            for line in self.csv_reader:
                pesel_list.append(line[88])

            return len(set(pesel_list))




