# diskWriter
Writes dummy file with defined bytes.  
I needed some activity on a HDD to record working sounds, this should do the trick without writing control commands to it.

## Shell
```bash
.\start.py 1024 --file_name=test2.txt --fill_byte=a
```

## TODO
Can currently only overwrite/create new files and should work for my purposes.  
If the file should not be overwritten each start, try mmap (Memory-mapped file support https://docs.python.org/3.5/library/mmap.html).
