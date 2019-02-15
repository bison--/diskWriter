import os
__author__ = 'bison'


class FileMaster:

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_handle = open(file_path, 'a+')
        self.chunk_size = 4096
        self.file_size = 0

        if os.path.isfile(file_path):
            self.file_size = os.path.getsize(file_path)

    def write_bytes(self, bytes_to_write, byte_value=''):
        if bytes_to_write > self.file_size:
            raise ValueError('Data to write is bigger than file size {0}/{1}'.format(bytes_to_write, self.file_size))

        written_bytes = 0
        fixed_byte_array = str(byte_value) * self.chunk_size
        while written_bytes < bytes_to_write:
            bytes_written = 0
            byte_array_to_write = fixed_byte_array
            theoretical_new_size = written_bytes + self.chunk_size
            if theoretical_new_size > bytes_to_write:
                bytes_to_write = bytes_to_write - written_bytes
                byte_array_to_write = byte_value * bytes_to_write
            else:
                bytes_to_write = self.chunk_size

            self.file_handle.write(byte_array_to_write)
            written_bytes += bytes_to_write

        return written_bytes

    def create_size(self, file_size, byte_value='', enforce=False):
        if file_size > self.file_size or enforce:
            self.file_size = file_size
            self.write_bytes(file_size, byte_value)

    def write_to_start(self, bytes_to_write, byte_value=''):
        self.file_handle.seek(0)
        self.write_bytes(bytes_to_write, byte_value)

    def write_to_end(self, bytes_to_write, byte_value=''):
        self.file_handle.seek(self.file_size - bytes_to_write)
        self.write_bytes(bytes_to_write, byte_value)
