from os import scandir

print("Verzeichnisinhalt ohne Einrückungen")

# Symbole für Verzeichnisstruktur
symbol_t = chr(9500) + chr(9472) + " "  # T-Stück
symbol_l = chr(9492) + chr(9472) + " "  # L-Stück
symbol_i = chr(9474) + "    "  # Vertikale Linie


# Funktion zum Drucken des Verzeichnisinhalts
def print_directory(path):
    with scandir(path) as dir:
        dir = sorted(dir, key=lambda f: f.name.lower())
        for data_file in dir:
            # Prüfen, ob es sich um das letzte Element handelt, um das richtige Symbol zu wählen
            print(symbol_l + data_file.name) if data_file == dir[-1] else print(symbol_t + data_file.name)


# Verzeichnisinhalt drucken
print_directory(".")

print("\nVerzeichnisinhalt mit Einrückungen")


# Erweiterte Funktion zum Drucken des Verzeichnisinhalts mit Einrückungen
def print_directory(path, indentation_level=0):
    nfiles, ndirectories = 0, 0

    with scandir(path) as dir:
        dir = sorted(dir, key=lambda f: f.name.lower())
        for data_file in dir:
            is_last_data_file = symbol_l if data_file == dir[-1] else symbol_t

            if data_file.is_dir():
                # Verzeichnis mit entsprechender Einrückung und Symbol drucken
                print(symbol_i * indentation_level + f"{is_last_data_file} {data_file.name}")
                # Rekursiver Aufruf für Unterverzeichnisse
                subdir_nfiles, subdir_ndirectories = print_directory(data_file.path, indentation_level + 1)
                # Anzahl Dateien und Verzeichnisse aktualisieren
                nfiles += subdir_nfiles
                ndirectories += subdir_ndirectories + 1
            else:
                # Datei mit entsprechender Einrückung und Symbol drucken
                print(symbol_i * indentation_level + f"{is_last_data_file} {data_file.name}")
                nfiles += 1

        return nfiles, ndirectories


# Verzeichnisinhalt mit Einrückungen drucken
total_nfiles, total_ndirectories = print_directory(".")
print("\nAnzahl files & directories")
print(f"{total_ndirectories} directories, {total_nfiles} files")
