import fileMaster
__author__ = 'bison'


fm = fileMaster.FileMaster('test.txt')
fm.create_size(4096, ord('*'))
fm.close()

# create sample file
fm = fileMaster.FileMaster('test.txt')
fm.create_size(2048, 48)

fm.write_to_end(23, 50)
fm.write_to_start(23, 49)

fm.write_to_end(4, 63)
fm.write_to_start(4, 62)

fm.write_to_end(2, ord('-'))
fm.write_to_start(2, ord('+'))
fm.close()

#fm = fileMaster.FileMaster('test.txt')
#fm.create_size(1000000, ord('*'))
