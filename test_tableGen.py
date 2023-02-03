
import unittest
import csv_to_stdout
import sys
import io

class TestYourFile(unittest.TestCase):
    def test_single_file(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        csv_to_stdout.answer(['fixtures/test.csv'])
        sys.stdout = sys.__stdout__

        answer = "|email_hash|category|filename|\n|----------|--------|--------|\n|b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6|Satchels|test.csv|\n|c2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7|Watches|test.csv|\n|faaee0ff7d06b05313ecb75d46a9aed014b11023ca1af5ec21a0607848071d18|Watches|test.csv|\n|5cd72da5035f2b36b604a16efc639cd04b6cfae7e487dcba60db88d3ef870f1e|Purses|test.csv|\n"
        self.assertEqual(capturedOutput.getvalue(), answer)


    def test_multiple_files(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        csv_to_stdout.answer(['fixtures/test.csv', 'fixtures/test2.csv'])
        sys.stdout = sys.__stdout__
        
        answer = "|email_hash|category|filename|\n|----------|--------|--------|\n|b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6|Satchels|test.csv|\n|c2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7|Watches|test.csv|\n|faaee0ff7d06b05313ecb75d46a9aed014b11023ca1af5ec21a0607848071d18|Watches|test.csv|\n|5cd72da5035f2b36b604a16efc639cd04b6cfae7e487dcba60db88d3ef870f1e|Purses|test.csv|\n|b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6|Bathroom Cleaner|test2.csv|\n|c2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7|Bathroom Cleaner|test2.csv|\n|faaee0ff7d06b05313ecb75d46a9aed014b11023ca1af5ec21a0607848071d18|Bathroom Cleaner|test2.csv|\n"

        self.assertEqual(capturedOutput.getvalue(), answer)

    def test_extra_columns(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        csv_to_stdout.answer(['fixtures/multiple_columns.csv'])
        sys.stdout = sys.__stdout__
        answer = "|email_hash|category|price|filename|\n|----------|--------|-----|--------|\n|b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6|Satchels|$30|multiple_columns.csv|\n|c2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7|Watches|$4350|multiple_columns.csv|\n|faaee0ff7d06b05313ecb75d46a9aed014b11023ca1af5ec21a0607848071d18|Watches|$1000|multiple_columns.csv|\n|5cd72da5035f2b36b604a16efc639cd04b6cfae7e487dcba60db88d3ef870f1e|Purses|$250|multiple_columns.csv|\n"
        self.assertEqual(capturedOutput.getvalue(), answer)

if __name__ == '__main__':
    unittest.main()