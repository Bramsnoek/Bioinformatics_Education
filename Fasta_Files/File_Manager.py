import os


class FastaFileManager(object):
    """
    A manager for accessing the sequence files of the species given
    """
    def __init__(self, *species):
        self.__species = []

        for specie in enumerate(species):
            self.__species.append(specie[1])

    def get_species(self):
        """
        :return: All species given when initialized
        """
        return self.__species

    def get_sequence(self, sequence_file_standard, key=None):
        """
        Gets the sequence files
        :param sequence_file_standard: The type of file e.g mRna_Sequence.fasta, Rna_Sequence.fasta
        :param key: You can provide a key if you want to only get the file of a specific specie
        :return: a list with the paths (string)/ all the files
        """
        try:
            if key is None:
                sequences = []
                for specie in self.__species:
                    sequences.append(self.__get_joined_sequence_path(specie, sequence_file_standard))

                return sequences

            return self.__get_joined_sequence_path(key, sequence_file_standard)

        except FileNotFoundError as e:
            print(e)

    def __get_joined_sequence_path(self, specie, standard):
        return str('/'.join([str(os.path.dirname(__file__)), specie, standard]))