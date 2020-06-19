def read_write(filename, tofile):
    with open(filename, 'r') as rf:
        with open(tofile, 'w') as wf:
            for line in rf:
                if 'sudo' and 'COMMAND' in line:
                    wf.write(line)

# If this program was called directly (as opposed to imported)
if __name__ == "__main__":
    read_write("/var/log/secure", "/home/oguzhan/fromOz/sudosu.log")
