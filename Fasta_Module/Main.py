from Fasta_Files.File_Manager import FastaFileManager
from Fasta_Module.Fasta import Fasta
import matplotlib.pyplot as plt
from pprint import pprint


species = ['Arabidopsis_Thaliana',
           'Caenorhabdits_Elegans',
           'Homo_Sapien',
           'Xenopus_Laevis',
           'Dictyostelium_Discoideum']


def main():
    file_manager = FastaFileManager(*species)
    fasta_manager = Fasta(file_manager.get_sequence('mRna_Sequence.fasta'))

    pprint(fasta_manager)

    gc_results = fasta_manager.get_gc()
    length_results = fasta_manager.get_sequence_length()

    plt.bar(range(len(gc_results)), gc_results.values(), align='center')
    plt.xticks(range(len(gc_results)), gc_results.keys())
    plt.title("GC% in different genomes for different organisms")
    plt.ylabel("Gc% in genome")
    plt.xlabel("Genome name")

    plt.show()

    plt.bar(range(len(length_results)), length_results.values(), align='center')
    plt.xticks(range(len(length_results)), length_results.keys())
    plt.title("Length of different genomes for different organisms")
    plt.ylabel("Length of genome sequence")
    plt.xlabel("Genome name")

    plt.show()


if __name__ == '__main__':
    main()
