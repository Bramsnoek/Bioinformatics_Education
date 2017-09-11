class Fasta(dict):
    """
    A manager for multiple Fasta files containing multiple functions that will gather data about the containing
    sequences
    """
    def __init__(self, *args):
        dict.__init__(self)
        self.current_sequence_reference = ''
        self.current_sequence = []

        for file in enumerate(args):
            self.__fasta_to_dict(file[1])

    def __fasta_to_dict(self, file):
        """
        :param file: The Fasta file containing sequence(s)
        """
        try:
            for line in open(file):
                if line.startswith(">") and self.current_sequence_reference == '':
                    self.current_sequence_reference = line.split(' ')[0]

                elif line.startswith(">") and self.current_sequence_reference != '':
                    self[self.current_sequence_reference] = ''.join(self.current_sequence)
                    self.current_sequence_reference = line.split(' ')[0]
                    self.current_sequence = []

                else:
                    self.current_sequence.append(line.rstrip())

            self[self.current_sequence_reference] = ''.join(self.current_sequence)
        except FileNotFoundError as e:
            print(e)
