import fileMaster
__author__ = 'bison'


fm = fileMaster.FileMaster('test.txt')
fm.create_size(2048)
fm.write_to_end(23, '2')
fm.write_to_start(23, '1')
