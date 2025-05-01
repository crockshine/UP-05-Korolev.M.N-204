import os

from mutagen import File
from mutagen.flac import FLAC
from mutagen.id3 import ID3
from mutagen.oggvorbis import OggVorbis
from mutagen.wave import WAVE


def extract_metadata(filepath: str) -> dict | None:
    audio = File(filepath)
    filetype = type(audio).__name__.lower()

    if not os.path.exists(filepath):
        return None

    default_title = 'Без названия'
    default_artist = 'Автор не найден'

    metadata = {
        'title': default_title,
        'artist': default_artist,
        'cover': None
    }

    try:
        if filetype == 'mp3':
            audio = ID3(filepath)

            metadata['title'] = audio.get('TIT2', [default_title])[0]
            _artist = audio.get('TPE1', [default_artist])
            metadata['artist'] = ', '.join(_artist)

            for key in audio:
                if key.startswith('APIC'):
                    metadata['cover'] = audio[key].data
                    break

        elif filetype == 'flac':
            audio = FLAC(filepath)
            print(audio, 'flac')

            metadata['title'] = audio.get('title', [None])[0]
            metadata['artist'] = audio.get('artist', [None])

            if audio.pictures:
                metadata['cover'] = audio.pictures[0].data

        elif filetype == 'oggvorbis':
            audio = OggVorbis(filepath)
            print(audio, 'ogg')

            metadata['title'] = audio.get('title', [None])[0]
            metadata['artist'] = audio.get('artist', [None])

            if 'metadata_block_picture' in audio:
                import base64
                metadata['cover'] = base64.b64decode(audio['metadata_block_picture'][0])

        elif filetype == 'wave':
            audio = WAVE(filepath)
            print(audio, 'wave')

            if audio.tags:
                metadata['title'] = audio.tags.get('TITL', [None])[0]
                metadata['artist'] = audio.tags.get('IART', [None])

            for key in audio:
                if key.startswith('APIC'):
                    metadata['cover'] = audio[key].data
                    break

    except Exception as e:
        return metadata

    return metadata
