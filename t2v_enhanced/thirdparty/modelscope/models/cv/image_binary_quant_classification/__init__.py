# These codes are copied from modelscope revision c58451baead80d83281f063d12fb377fad415257 
# Copyright 2021-2022 The Alibaba Fundamental Vision Team Authors. All rights reserved.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if TYPE_CHECKING:
    from .binary_quant_model import BinaryQuantClassificationModel

else:
    _import_structure = {
        'binary_quant_model': ['BinaryQuantClassificationModel'],
    }

    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )