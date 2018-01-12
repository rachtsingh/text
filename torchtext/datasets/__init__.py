from .language_modeling import LanguageModelingDataset, PennTreeBank, WikiText2  # NOQA
from .snli import SNLI
from .sst import SST
from .translation import TranslationDataset, Multi30k, IWSLT, WMT14  # NOQA
from .sequence_tagging import SequenceTaggingDataset, UDPOS # NOQA
from .trec import TREC
from .imdb import IMDB


__all__ = ['LanguageModelingDataset',
           'SNLI',
           'SST',
           'TranslationDataset',
           'Multi30k',
           'IWSLT',
           'WMT14'
           'PennTreeBank',
           'WikiText2',
           'TREC',
           'IMDB',
           'SequenceTaggingDataset',
           'UDPOS']
