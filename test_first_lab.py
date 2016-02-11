import unittest
import os #to check current directory

class NumberOfFilesTest(unittest.TestCase):
    
    def test(self):
        ## of files in current working directory. os.listdir includes all files except . ..
        self.assertGreater(len(os.listdir(os.getcwd())), 4, msg="You did not add any files. Remember to use the 'touch' command")

if __name__ == '__main__':
    unittest.main()


