from typing import ClassVar, Sequence

from ..ADT import TypedFile, TypedFileImpl


class Sound(TypedFile):
    class WAV(TypedFileImpl):

        mimetypes = ["audio/x-wav", "audio/wav"]
        extensions = ["wav"]

        def load(self):
            raise NotImplementedError()

    class FLAC(TypedFileImpl):
        mimetypes: ClassVar[Sequence[str]] = []
        extensions: ClassVar[Sequence[str]] = []

        def load(self):
            raise NotImplementedError()

    class Ogg(TypedFileImpl):
        mimetypes: ClassVar[Sequence[str]] = []
        extensions: ClassVar[Sequence[str]] = []

        def load(self):
            raise NotImplementedError()

    class MP3(TypedFileImpl):
        mimetypes: ClassVar[Sequence[str]] = []
        extensions: ClassVar[Sequence[str]] = []

        def load(self):
            raise NotImplementedError()

    preferred_impls = [WAV, FLAC, Ogg, MP3]

    def __init__(self):
        super().__init__()
