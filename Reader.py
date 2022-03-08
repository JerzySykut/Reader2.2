import pathlib
import json
import csv
import pickle
from os import path


class Reader(object):
    data: list

    def __init__(self) -> None:
        self.data = list()

    @staticmethod
    def init_object(path_to_file: str):
        split_name = path.splitext(path_to_file)
        if split_name[1] == '.csv':
            return ReaderCsv()
        elif split_name[1] == '.json':
            return ReaderJson()
        elif split_name[1] == '.pickle':
            return ReaderPickle()
        else:
            print('Nieznane/nieobsługiwane rozszerzenie pliku!!!')
            return Reader()

    # zwraca true jeśli udało się załadować plik, false jeśli nie
    def load_from_file(self, path_to_file: str) -> bool:
        return False

    def print_data(self) -> None:
        print(*self.data, sep='\n')

    def set_value(self, x: int, y: int, val: str) -> None:
        if y >= len(self.data) or x >= len(self.data[y]):
            print("Wspolrzedne poza rozmiaru tablicy")
        else:
            self.data[y][x] = val

    def save_to_file(self, path_to_file: str):
        split_name = path.splitext(path_to_file)
        if split_name[1] == '.csv':
            ReaderCsv.save_to_file(self.data, path_to_file)
        elif split_name[1] == '.json':
            ReaderJson.save_to_file(self.data, path_to_file)
        elif split_name[1] == '.pickle':
            ReaderPickle.save_to_file(self.data, path_to_file)
        else:
            print('Nieznane/nieobsługiwane rozszerzenie pliku!!!')

    def print_files_in_folder(path_to_file: str):
        folder = pathlib.Path(path_to_file)
        for f in folder.glob('*.csv'):
            print(f)
        for f in folder.glob('*.json'):
            print(f)
        for f in folder.glob('*.pickle'):
            print(f)


class ReaderCsv(Reader):
    def load_from_file(self, path_to_file: str) -> bool:
        # Sprawdzamy czy istnieje katalog/plik
        if path.exists(path_to_file):
            # sprawadzamy czy to jest plik
            if path.isfile(path_to_file):
                # otwieramy plik
                with open(path_to_file, newline="") as f:
                    rdr = csv.reader(f, delimiter=';')
                    for line in rdr:
                        self.data.append(line)
                return True
            else:
                # istnieje, a to nie jest plik czyli katalog
                self.print_files_in_folder(path_to_file)
                return False
        else:
            # wyciągamy nazwę katalogu (Folderu)
            path_dir = path.dirname(path_to_file)
            # sprawdzamy, czy istnieje i czy jest folderem (nie jest plikiem)
            if path.exists(path_dir) and path.isfile(path_dir) == False:
                self.print_files_in_folder(path_to_file)
            else:
                print("Nie istnieje plik lub folder pod podaną scieżką")  # nie istnieje
            return False

    @staticmethod
    def save_to_file(data: list, path_to_file: str):
        with open(path_to_file, "w", newline="") as f:
            writer = csv.writer(f, delimiter=';')
            for line in data:
                writer.writerow(line)


class ReaderJson(Reader):
    def load_from_file(self, path_to_file: str) -> bool:
        # Sprawdzamy, czy istnieje katalog/plik
        if path.exists(path_to_file):
            # sprawadzamy, czy to jest plik
            if path.isfile(path_to_file):
                # otwieramy plik
                with open(path_to_file, newline="") as f:
                    self.data = json.load(f)
                return True
            else:
                # istnieje, a to nie jest plik czyli katalog
                self.print_files_in_folder(path_to_file)
                return False
        else:
            # wyciągamy nazwę katalogu (Folderu)
            path_dir = path.dirname(path_to_file)
            # sprawdzamy, czy istnieje i czy jest folderem(nie jest plikien)
            if path.exists(path_dir) and path.isfile(path_dir) == False:
                self.print_files_in_folder(path_to_file)
            else:
                print("Nie istnieje plik lub folder pod podana sciezka")  # nie istnieje
            return False

    @staticmethod
    def save_to_file(data: list, path_to_file: str):
        with open(path_to_file, "w", newline="") as f:
            json.dump(data, f, indent=4)


class ReaderPickle(Reader):
    def load_from_file(self, path_to_file: str) -> bool:
        # Sprawdzamy, czy istnieje katalog/plik
        if path.exists(path_to_file):
            # sprawadzamy, czy to jest plik
            if path.isfile(path_to_file):
                # otwieramy plik
                with open(path_to_file, 'rb') as f:
                    self.data = pickle.load(f)
                return True
            else:
                # istnieje, a to nie jest plik czyli katalog
                self.print_files_in_folder(path_to_file)
                return False
        else:
            # wyciągamy nazwe katalogu (Folderu)
            path_dir = path.dirname(path_to_file)
            # sprawdzamy, czy istnieje i czy jest folderem(nie jest plikien)
            if path.exists(path_dir) and path.isfile(path_dir) == False:
                self.print_files_in_folder(path_to_file)
            else:
                print("Nie istnieje plik lub folder pod podana sciezka")  # nie istnieje
            return False

    @staticmethod
    def save_to_file(data: list, path_to_file: str):
        with open(path_to_file, "wb") as f:
            pickle.dump(data, f)

