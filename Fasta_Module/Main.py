from Fasta_Files.File_Manager import FastaFileManager
from Fasta_Module.Fasta import Fasta

species = ['Arabidopsis_Thaliana',
           'Caenorhabdits_Elegans',
           'Homo_Sapien',
           'Xenopus_Laevis',
           'Dictyostelium_Discoideum']


def main():
    fasta_file_manager = FastaFileManager(*species)
    fasta = Fasta(fasta_file_manager.get_sequence('mRna_Sequence.fasta'))
    print(fasta.get_gc())
    print(fasta.get_sequence_length())
    print(fasta)


if __name__ == '__main__':
    main()











