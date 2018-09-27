import csv


class CsvWriter:
    def __init__(self, csvReader_inst, userInput_inst):
        self.write_dir = csvReader_inst.read_dir.split('.')[0]+"_zmienione.csv"
        self.csv_reader_file = csvReader_inst.csv_file
        self.csv_reader_dict = csvReader_inst.csv_reader

        self.pesel = userInput_inst.pesel
        self.npwz = userInput_inst.npwz
        self.couner = 0

    def write_file(self):
        try:
            moded_file = open(self.write_dir, 'w', encoding='windows-1250')
            csv_writer = csv.writer(moded_file, delimiter=';', lineterminator='\n')
        except FileNotFoundError:
            return "Nie znaleziono pliku podczas zapisu"

        self.csv_reader_file.seek(0)

        for line in self.csv_reader_dict:
            line[88] = self.pesel
            line[87] = self.npwz
            csv_writer.writerow(line)
            self.couner += 1

        self.csv_reader_file.close()
        moded_file.close()

