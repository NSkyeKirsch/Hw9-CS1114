"""
Author: Noa Kirschbaum
Assignment / Part: HW9 - Q1
Date due: 2022-04-28
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
from pprint import pprint

def get_nucleotide_frequencies(nucleotides):
    nucleotides = nucleotides.upper()
    final_dict = {
        'A': nucleotides.count('A'),
        'C': nucleotides.count('C'),
        'G': nucleotides.count('G'),
        'T': nucleotides.count('T'),
        'Junk': {}
    }

    for chr in nucleotides:
        if chr != "A" and chr != "C" and chr != "G" and chr != "T":
            final_dict['Junk'].update({chr: nucleotides.count(chr)})

    return final_dict


def main():
    frequencies = get_nucleotide_frequencies("ACTGTCACGRFRTNHYCTCGACCSGTGTCACGT")
    pprint(frequencies)

main()

