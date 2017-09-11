import os


def _get_joined_sequence_path(specie, standard):
    return str('/'.join([str(os.path.dirname(__file__)), specie, standard]))


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
                        open(_get_joined_sequence_path(specie, sequence_file_standard)))

                return sequences

            return open(_get_joined_sequence_path(key, sequence_file_standard))

        except FileNotFoundError as e:
            print(e)
