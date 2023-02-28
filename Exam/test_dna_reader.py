import unittest

from Exam.dna import dna_reader

class MyTestCase(unittest.TestCase):
    def test_dna_reader(self):
        dna_checklist = ["ATTA", "ACTA", "AGCA", "ACAA"]
        self.assertEqual("ACTA", dna_reader(dna_checklist))


    def test_empty_list(self):
        dna_checklist = []
        self.assertEqual("", dna_reader(dna_checklist), msg="The result of first check is clear. No need to re-check")



if __name__ == '__main__':
    unittest.main()
