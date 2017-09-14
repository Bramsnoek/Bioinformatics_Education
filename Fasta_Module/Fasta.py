class Fasta(dict):
    """
    A manager for multiple Fasta files containing multiple functions that will gather data about the containing
    sequences
    """
    def __init__(self, *files: list):
        dict.__init__(self)
        self.__current_sequence_reference = ''
        self.__current_sequence = []

        for file in enumerate(files):
            self.__fasta_to_dict(file[1])
    
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

    def get_gc(self, key: str = None) -> [dict, float]:
        """
        :param key: The sequence of which the GC% is being calculated
        :return: The function returns the GC% of a single sequence, if no key is provided
        it will return a dictionary of every sequence and their GC%
        """
        try:
            if key is None:
                seq_dict = {}
                for reference, sequence in self.items():
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
                        self[self.__current_sequence_reference] = ''.join(self.__current_sequence)
                        self.__current_sequence_reference = line.split(' ')[0]
                        self.__current_sequence = []

                    else:
                        self.__current_sequence.append(line.rstrip())

                self[self.__current_sequence_reference] = ''.join(self.__current_sequence)
        except FileNotFoundError as e:
            print(e)
