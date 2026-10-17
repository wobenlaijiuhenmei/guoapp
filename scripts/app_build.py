import base64
from dataclasses import dataclass


@dataclass(frozen=True)
class BuildVariant:
    all_sources: bool = False
    without_hongguo: bool = False

    @property
    def full_sources(self):
        return self.all_sources or self.without_hongguo

    @property
    def name(self):
        if self.without_hongguo:
            return '真果鉴-无红果'
        return '真果鉴' if self.all_sources else '红果鉴'

    @property
    def slug(self):
        if self.without_hongguo:
            return 'zhenguojian-no-hongguo'
        return 'zhenguojian' if self.all_sources else 'hongguojian'

    @property
    def arguments(self):
        if self.without_hongguo:
            return ['--without-hongguo']
        return ['--all-sources'] if self.all_sources else []

    @property
    def flutter_arguments(self):
        return [
            '--dart-define=ALL_SOURCES=' + str(self.full_sources).lower(),
            '--dart-define=WITHOUT_HONGGUO=' + str(self.without_hongguo).lower(),
        ]

    @property
    def linker_flags(self):
        return (
            '-s -w -X duanjuapp/native/core.buildAllSources=' + str(self.full_sources).lower()
            + ' -X duanjuapp/native/core.buildWithoutHongguo=' + str(self.without_hongguo).lower()
        )

    @classmethod
    def from_dart_defines(cls, encoded):
        values = {}
        for item in encoded.split(','):
            if not item:
                continue
            key, separator, value = base64.b64decode(item, validate=True).decode('utf-8').partition('=')
            if separator:
                values[key] = value
        return cls(
            values.get('ALL_SOURCES') == 'true',
            values.get('WITHOUT_HONGGUO') == 'true',
        )


def add_variant_argument(parser):
    variants = parser.add_mutually_exclusive_group()
    variants.add_argument('--all-sources', action='store_true',
                          help='构建包含全部站源的真果鉴；默认构建仅红果的红果鉴')
    variants.add_argument('--without-hongguo', action='store_true',
                          help='构建包含红果以外全部站源的真果鉴')
