from sys import argv
import Reader


if __name__ == '__main__':
    # sprawdzamy czy mamy conajmniej 1 argument (plik wejsciowy)
    if len(argv) < 2:
        print("za mało argumentów")
        exit()
    reader = Reader.Reader.init_object(argv[1])
    if reader.load_from_file(argv[1]):
        # sprawdzamy czy mamy drugi argument (plik wyjsciowy)
        if len(argv) > 2:
            # analizujemy argumenty zmian
            for i in range(3, len(argv)):
                para = argv[i]
                p = para.split(',')
                x = int(p[0])
                y = int(p[1])
                reader.set_value(x, y, p[2])
            reader.print_data()
            Reader.Reader.save_to_file(reader, argv[2])
        else:
            reader.print_data()
