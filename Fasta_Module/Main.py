from Fasta_Files.File_Manager import FastaFileManager
from Fasta_Module.Fasta import Fasta
import matplotlib.pyplot as plt
import numpy as np


species = ['Arabidopsis_Thaliana',
           'Caenorhabdits_Elegans',
           'Homo_Sapien',
           'Xenopus_Laevis',
           'Dictyostelium_Discoideum']


def show_doublebar_chart(bar_width: float, opacity: float,
                         first_set_values: list, second_set_values: list, xticks: list, n_groups: int,
                         title: str, ylabel: str, xlabel: str, first_set_label: str, second_set_label: str):
    index = np.arange(n_groups)

    plt.bar(index, first_set_values, bar_width,
            alpha=opacity,
            color='b',
            label=first_set_label)

    plt.bar(index + bar_width, second_set_values, bar_width,
            alpha=opacity,
            color='g',
            label=second_set_label)

    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(index + bar_width, xticks)
    plt.legend()

    plt.show()


def main():
    file_manager = FastaFileManager(*species)
    fasta_manager = Fasta(file_manager.get_sequence('Rna_Sequence.fasta'))

    gc_results = fasta_manager.get_gc()
    gc_known = [50, 50, 50, 50, 50]

    length_results = fasta_manager.get_sequence_length()
    length_known = [2000, 2000, 2000, 2000, 2000]

    show_doublebar_chart(0.4, 0.8, gc_results.values(), gc_known, gc_results.keys(), 5,
                         "GC% in different genomes for different organisms",
                         "GC% in genome",
                         "Genome name",
                         "Calculated GC%",
                         "Known GC%")

    show_doublebar_chart(0.4, 0.8, length_results.values(), length_known, length_results.keys(), 5,
                         "Length of different genomes for different organisms",
                         "Length of genome",
                         "Genome name",
                         "Calculated Length",
                         "Known Length")


if __name__ == '__main__':
    main()
