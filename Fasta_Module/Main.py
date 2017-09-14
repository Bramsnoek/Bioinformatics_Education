from Fasta_Files.File_Manager import FastaFileManager
from Fasta_Module.Fasta import Fasta
import matplotlib.pyplot as plt
import numpy as np


species = {'Arabidopsis_Thaliana': 36.6,
           'Caenorhabdits_Elegans': 35.4659,
           'Homo_Sapien': 40.9,
           'Xenopus_Laevis': 40.2325,
           'Dictyostelium_Discoideum': 22.4631
           }


def show_doublebar_chart(bar_width: float, opacity: float,
                         first_set_values: list, second_set_values: list, xticks: list, n_groups: int,
                         title: str, ylabel: str, xlabel: str, first_set_label: str, second_set_label: str, fullscreen: bool = False):
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
    plt.tight_layout()

    plt.show()


def show_triplebar_chart(bar_width: float, opacity: float,
                         first_set_values: list, second_set_values: list, third_set_values: list,
                         xticks: list, n_groups: int,
                         title: str, ylabel: str, xlabel: str, first_set_label: str, second_set_label: str, third_set_label: str, fullscreen: bool = False):
    index = np.arange(n_groups)

    plt.bar(index, first_set_values, bar_width,
            alpha=opacity,
            color='b',
            label=first_set_label)

    plt.bar(index + bar_width, second_set_values, bar_width,
            alpha=opacity,
            color='g',
            label=second_set_label)

    plt.bar(index + (2*bar_width), third_set_values, bar_width,
            alpha=opacity,
            color='r',
            label=third_set_label)

    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(index + bar_width, xticks)
    plt.legend()
    plt.tight_layout()

    plt.show()



def main():
    file_manager = FastaFileManager(*species.keys())
    fasta_manager_genome = Fasta(file_manager.get_sequence('Rna_Sequence.fasta'))
    fasta_manager_mRNA = Fasta(file_manager.get_sequence('mRna_Sequence.fasta'))

    gc_results_genome = fasta_manager_genome.get_gc()
    gc_results_mRNA = fasta_manager_mRNA.get_gc()

    length_results_genome = fasta_manager_genome.get_sequence_length()
    length_results_mRNA = fasta_manager_mRNA.get_sequence_length()
    length_known = [10000, 12000, 12832, 7432, 29320]

    show_triplebar_chart(0.3, 0.8, gc_results_genome.values(), list(species.values()), gc_results_mRNA.values(), list(species.keys()), 5,
                         "GC% in different genomes for different organisms",
                         "GC% in genome",
                         "Specie name",
                         "Genome sequence GC%",
                         "Known GC%",
                         "mRNA sequence GC%")

    show_triplebar_chart(0.3, 0.8, length_results_genome.values(), length_known, length_results_mRNA.values(), list(species.keys()), 5,
                         "Length of different genomes for different organisms",
                         "Length of genome",
                         "Specie name",
                         "Genome sequence Length",
                         "Known Length",
                         "mRNA sequence length")


if __name__ == '__main__':
    main()
