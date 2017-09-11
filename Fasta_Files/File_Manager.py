import os


class FastaFileManager(object):
    def __init__(self, *species):
        self._species = []

        for specie in enumerate(species):
            self._species.append(specie[1])

    def get_species(self):
        return self._species

    def get_sequence(self, sequence_file_standard, key=None):
        try:
            if key is None:
                sequences = []
                for specie in self._species:
                    sequences.append(
                        open(self.__get_joined_sequence_path(specie, sequence_file_standard)))

                return sequences

            return open(self.__get_joined_sequence_path(key, sequence_file_standard))

        except FileNotFoundError as e:
            print(e)

    def __get_joined_sequence_path(self, specie, standard):
        return str('/'.join([str(os.path.dirname(__file__)), specie, standard]))