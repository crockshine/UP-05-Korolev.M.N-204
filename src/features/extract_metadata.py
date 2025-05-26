import os
import base64
from pathlib import Path
from typing import Optional, Dict, Union

from tinytag import TinyTag
from mutagen import File
from mutagen.id3 import ID3
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis
from mutagen.wave import WAVE


def extract_metadata(filepath: str) -> Optional[Dict[str, Union[str, bytes, None]]]:
    if not os.path.exists(filepath):
        return None

    # Получаем базовые метаданные через TinyTag
    try:
        tag = TinyTag.get(filepath, encoding="latin1")
        print(tag.artist)
        # metadata = {
        #     'title': tag.title or Path(filepath).stem,
        #     'artist': tag.artist or 'Автор не найден',
        #     'cover': None,  # Обложка будет добавлена через Mutagen
        #     'source': filepath
        # }
    except Exception as e:
        print(f"Ошибка TinyTag: {e}")
        metadata = {
            'title': Path(filepath).stem,
            'artist': 'Автор не найден',
            'cover': None,
            'source': filepath
        }

    # Получаем обложку через Mutagen
    try:
        audio = File(filepath)
        filetype = type(audio).__name__.lower()

        if filetype == 'mp3':
            audio = ID3(filepath)
            for key in audio.keys():
                if key.startswith('APIC'):
                    metadata['cover'] = audio[key].data  # Байты обложки
                    break

        elif filetype == 'flac':
            audio = FLAC(filepath)
            if audio.pictures:
                metadata['cover'] = audio.pictures[0].data

        elif filetype == 'oggvorbis':
            audio = OggVorbis(filepath)
            if 'metadata_block_picture' in audio:
                metadata['cover'] = base64.b64decode(audio['metadata_block_picture'][0])

        elif filetype == 'wave':
            audio = WAVE(filepath)
            try:
                id3 = ID3(filepath)
                for key in id3.keys():
                    if key.startswith('APIC'):
                        metadata['cover'] = id3[key].data
                        break
            except:
                pass

        # Конвертируем обложку в строку байтов (если нужно)
        if isinstance(metadata['cover'], bytes):
            metadata['cover'] = str(metadata['cover'])  # Или base64.b64encode(cover).decode()

    except Exception as e:
        print(f"Ошибка Mutagen: {e}")

    return metadata