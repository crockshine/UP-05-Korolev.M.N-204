import hashlib
import os


def get_content_hash(filepath) -> str:
    h = hashlib.blake2b()
    file_size = os.path.getsize(filepath)
    chunk_size = 1024 * 256

    with open(filepath, 'rb') as f:
        h.update(f.read(chunk_size))

        if file_size >= chunk_size * 3:
            f.seek(file_size // 2)
            h.update(f.read(chunk_size))

            f.seek(file_size - chunk_size)
            h.update(f.read(chunk_size))
        elif file_size > chunk_size:
            f.seek(file_size - chunk_size)
            h.update(f.read(chunk_size))

    return h.hexdigest()