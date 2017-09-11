from Fasta_Files.File_Manager import FastaFileManager
from Fasta_Module.Fasta import Fasta
import matplotlib.pyplot as plt

species = ['Arabidopsis_Thaliana',
           'Caenorhabdits_Elegans',
           'Homo_Sapien',
           'Xenopus_Laevis',
           'Dictyostelium_Discoideum']


def main():
    fasta_file_manager = FastaFileManager(*species)
    fasta = Fasta(fasta_file_manager.get_sequence('mRna_Sequence.fasta'))

    gc_results = fasta.get_gc()
    length_results = fasta.get_sequence_length()

    plt.bar(range(len(gc_results)), gc_results.values(), align='center')
    plt.xticks(range(len(gc_results)), gc_results.keys())

    plt.show()

    plt.bar(range(len(length_results)), length_results.values(), align='center')
    plt.xticks(range(len(length_results)), length_results.keys())

    plt.show()


if __name__ == '__main__':
    main()











