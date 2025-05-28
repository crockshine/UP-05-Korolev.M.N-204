import os
from pathlib import Path

from mutagen import File
from mutagen.flac import FLAC
from mutagen.id3 import ID3
from mutagen.oggvorbis import OggVorbis
from mutagen.wave import WAVE
from mutagen.wavpack import WavPack
from tinytag import TinyTag


def extract_metadata(filepath: str) -> dict | None:
    audio = File(filepath)
    filetype = type(audio).__name__.lower()

    if not os.path.exists(filepath):
        return None

    default_title = Path(filepath).stem
    default_artist = 'Автор не найден'

    metadata = {
        'title': default_title,
        'artist': [default_artist],
        'cover': None,
        'source': filepath
    }

    try:
        if filetype == 'mp3':
            audio = ID3(filepath)
            metadata['title'] = audio.get('TIT2', [default_title])[0]
            metadata['artist'] = audio.get('TPE1', [default_artist])


            for key in audio.keys():
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
            file = File(filepath)

            # id3
            metadata['title'] = file.get('TIT2', [default_title])[0]
            metadata['artist'] = file.get('TPE1', [default_artist])

            # riff
            if metadata["title"] == default_title:
                metadata["title"] = file.get("INAM",[default_title])[0]

            if metadata["artist"] == default_artist:
                metadata["artist"] = file.get("IART",[default_artist])

            # # tinytag
            # if metadata["title"] == default_title and tag.title != "??????":
            #     metadata["title"] = tag.title
            #
            # if metadata["artist"] == default_artist and tag.artist != "??????":
            #     metadata["artist"] = tag.artist
            # print('3', metadata)

            # обложка
            for key in audio.keys():
                if key.startswith('APIC'):
                    metadata['cover'] = audio[key].data
                    break




    except Exception as e:
        print(e)


    metadata['artist'] = ', '.join(metadata['artist'])
    return metadata