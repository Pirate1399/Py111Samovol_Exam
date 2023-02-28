from statistics import mode


def dna_reader(dna_checklist: list) -> str:
    """
        re-checking the dna list if dna reading results are not clear enough
        :param dna_checklist: list of string with same length
        :return: result of dna scanning -> string
        """
    if not dna_checklist:
        print("The result of first check is clear. No need to re-check")

    nucleotide = {i: [] for i, dna in enumerate(dna_checklist)}

    for index, dna in enumerate(dna_checklist):
        for j in range(0, len(dna)):
            nucleotide[j].append(dna[j])

    results_list = [v for k, v in nucleotide.items() if v]
    print(results_list)
    final_dna = list(map(mode, results_list))

    return "".join(final_dna)


if __name__ == '__main__':
    Atta_list = ["ATTA", "ACTA", "AGCA", "ACAA", "ATTA", "ACTA", "AGCA", "ACAA"]
    print(dna_reader(Atta_list))

