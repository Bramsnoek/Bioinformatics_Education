from enum import Enum


class Fasta(dict):
    """
    A manager for multiple Fasta files containing multiple functions that will gather data about the containing
    sequences
    """
    def __init__(self, *files: list):
        dict.__init__(self)
        self.__current_sequence_reference = ''
        self.__current_sequence = []
        self.__current_sequence_type = None

        self[SequenceType.PROTEIN] = {}
        self[SequenceType.GENOMIC] = {}

        for file_sequence in enumerate(files):
            self.__fasta_to_dict(file_sequence[1])

    def add_genome_files(self, files):
        self.__fasta_to_dict(files)

    def get_sequence_length(self, key: object = None) -> [dict, float]:
        """
        :param key: The sequence of which the length is being calculated
        :return: The function returns the length of a single sequence, if no key is provided
        it will return a dictionary of every sequence and their GC%
        """
        try:
            if key is None:
                seq_dict = {}
                for reference, sequence in self.items():
                    seq_dict[reference] = len(sequence)
                return seq_dict

            return len(self[key])
        except KeyError:
            print('Please provide an existing sequence name')

    def get_derk(self, key: str = None) -> [dict]:
        """
        :param key: The sequence of which the DERK% and net charge is being calculated
        :return: The function returns the DERK% and the net charge of a single sequence, if no key is provided
        it will return a dictionary of every sequence and their DERK% and net charge
        :format: sequence name: [derk count, net charge]
        """
        try:
            seq_dict = {}
            if key is None:
                for reference, sequence in self[SequenceType.PROTEIN].items():
                    r_k_count = sum([1.0 for amino_acid in sequence if amino_acid in ['R', 'K']])
                    d_e_count = sum([1.0 for amino_acid in sequence if amino_acid in ['D', 'E']])

                    seq_dict[reference] = [((r_k_count + d_e_count) / len(sequence)) * 100, r_k_count - d_e_count]

                return seq_dict

            sequence = self[SequenceType.PROTEIN][key]
            r_k_count = sum([1.0 for amino_acid in sequence if amino_acid in ['R', 'K']])
            d_e_count = sum([1.0 for amino_acid in sequence if amino_acid in ['D', 'E']])

            return [((r_k_count + d_e_count) / len(sequence)) * 100, r_k_count - d_e_count]
        except KeyError:
            print('Please provide an existing sequence name')

    def get_gc(self, key: str = None) -> [dict, float]:
        """
        :param key: The sequence of which the GC% is being calculated
        :return: The function returns the GC% of a single sequence, if no key is provided
        it will return a dictionary of every sequence and their GC%
        """
        try:
            if key is None:
                seq_dict = {}
                for reference, sequence in self[SequenceType.GENOMIC].items():
                    seq_dict[reference] = sum([1.0 for nucleotide in sequence if nucleotide in ['G', 'C']])\
                                          / len(sequence) * 100
                return seq_dict

            sequence = self[key]
            return(sum([1.0 for nucleotide in sequence if nucleotide in ['G', 'C']]) / len(sequence)) * 100
        except KeyError:
            print('Please provide an existing sequence name')

    def __fasta_to_dict(self, files: list):
        """
        :param files: The Fasta files containing sequence(s)
        """
        try:
            for file in files:
                for line in open(file):
                    if line.startswith(">") and self.__current_sequence_reference == '':
                        self.__current_sequence_reference = line.split(' ')[0]

                    elif line.startswith(">") and self.__current_sequence_reference != '':
                        self.__current_sequence_reference = line.split(' ')[0]
                        self.__current_sequence = []

                    else:
                        current_line = line.rstrip()
                        if self.__current_sequence_type is None:
                            self.__current_sequence_type = SequenceType.PROTEIN if SequenceType.check_is_protein(current_line) \
                                                            else SequenceType.GENOMIC

                        self.__current_sequence.append(current_line)

                self[self.__current_sequence_type][self.__current_sequence_reference] = ''.join(self.__current_sequence)
                self.__current_sequence_type = None
        except FileNotFoundError as e:
            print(e)


class SequenceType(Enum):
    PROTEIN = 1
    GENOMIC = 2

    @staticmethod
    def check_is_protein(sequence):
        for char in sequence:
            return char in ['L', 'P', 'W', 'Y', 'Q', 'E', 'R', 'V', 'I', 'F', 'M', 'S', 'N', 'D', 'K', 'H']
