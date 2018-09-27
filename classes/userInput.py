from os import getcwd

class UserInput:
    def __init__(self):
        self.npwz = None
        self.pesel = None
        self.dir = None
        self.abort = None

    def check_pesel(self, pesel):
        pesel = str(pesel)

        if len(pesel) != 11:
            print("Pesel ma 11 znaków")
            return False

        for char in pesel:
            try:
                int(char)
            except ValueError:
                print('PESEL składa się wyłącznie z cyfr')
                return False

        if int(pesel[10]) == (
                9 * int(pesel[0]) + 7 * int(pesel[1]) + 3 * int(pesel[2]) + 1 * int(pesel[3]) + 9 * int(
                pesel[4]) + 7 * int(pesel[5]) + 3 * int(pesel[6]) + 1 * int(pesel[7]) + 9 * int(pesel[8]) + 7 * int(
                pesel[9])) % 10:
            return True

        else:
            print("PESEL nieprawidłowy")
            return False

    def input_pesel(self):
        pesel = input("PESEL zastępcy: ")
        if self.check_pesel(pesel):
            self.pesel = pesel
        else:
            return self.input_pesel()


    def input_npwz(self):
        npwz = input("NPWZ zastępcy: ")

        if npwz != "":
            self.npwz = npwz

        else:
            empty_npwz = input("Nie podano NPWZ, czy na pewno chcesz kontynuowac? [t/n]: ")

            if empty_npwz.lower() == 't':
                self.npwz = ""
            else:
                self.input_npwz()

    def input_dir(self):
        read_dir = input("Nazwa pliku: ")
        # if read_dir.count("/") or read_dir.count("\\"):
        #     print("Relative paths not supported. Move your file to {}".format(getcwd()))
        #     return self.input_dir()

        if read_dir.split(".")[-1].lower() != "csv":
            print("Proszę wskazać plik typu .csv")
            return self.input_dir()


        self.dir = read_dir

    def abort_ask(self):
        abort = input("Czy chcesz przerwać? [t/n]")
        if abort.lower() == 't':
            self.abort = 1
        else:
            self.abort = 0