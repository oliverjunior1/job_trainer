import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extracrall(dest_dir)

if __name__ == '__main__':
    extract_archive('compressed.zip', '')