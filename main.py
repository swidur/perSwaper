from classes.userInput import UserInput
from classes.csvReader import CsvReader
from classes.csvWriter import CsvWriter


def main():
    get = UserInput()

    get.input_dir()

    reader = CsvReader(get.dir)

    if reader.open_file():

        excec_number = reader.one_benefits_executor()

        if excec_number == 0:
            print("Plik pusty, lub nie uzupełniono peseli osoby realizującej świadczenia")
            get.abort_ask()
            if get.abort:
                quit()

        elif excec_number > 1:
            print("Znaleziono więcej niż jedną osobę realizującą świadczenia")
            get.abort_ask()
            if get.abort:
                quit()

        elif excec_number == 1:
            print("Stwierdzono jedną osoba realizujacą świadczenia")

        get.input_pesel()
        get.input_npwz()

        writer = CsvWriter(reader, get)
        writer.write_file()

        print("Zapisano plik. Chyba. {} rekordów w tabeli wynikowej".format(writer.couner))
    else:
        print("Nie znaleziono pliku")
        main()

while True:
    main()
