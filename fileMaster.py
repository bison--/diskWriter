import os
__author__ = 'bison'


class FileMaster:

    def __init__(self, file_path=''):
        self.is_closed = False
        self.file_path = file_path
        self.file_handle = open(file_path, 'wb+')
        self.chunk_size = 4096
        self.file_size = 0

    def write_bytes(self, bytes_to_write, byte_value=0):
        if bytes_to_write > self.file_size:
            raise ValueError('Data to write is bigger than file size {0}/{1}'.format(bytes_to_write, self.file_size))
        if self.is_closed:
            raise IOError('File has been closed!')

        written_bytes = 0
        fixed_byte_array = [byte_value] * self.chunk_size
        while written_bytes < bytes_to_write:
            bytes_written = 0
            byte_array_to_write = fixed_byte_array
            theoretical_new_size = written_bytes + self.chunk_size
            if theoretical_new_size > bytes_to_write:
                bytes_written = bytes_to_write - written_bytes
                byte_array_to_write = [byte_value] * bytes_to_write
            else:
                bytes_written = self.chunk_size

            self.file_handle.write(bytearray(byte_array_to_write))
            written_bytes += bytes_written

        self.file_handle.flush()
        return written_bytes

    def create_size(self, file_size, byte_value=0, enforce=False):
        if file_size > self.file_size or enforce:
            self.file_size = file_size
            self.write_bytes(file_size, byte_value)

    def write_to_start(self, bytes_to_write, byte_value=0):
        self.file_handle.seek(0)
        self.write_bytes(bytes_to_write, byte_value)

    def write_to_end(self, bytes_to_write, byte_value=0):
        self.file_handle.seek(self.file_size - bytes_to_write)
        self.write_bytes(bytes_to_write, byte_value)

    def close(self):
        self.is_closed = True
        self.file_handle.close()
