# These codes are copied from modelscope revision c58451baead80d83281f063d12fb377fad415257 
# Copyright (c) Alibaba, Inc. and its affiliates.

from modelscope.msdatasets.dataset_cls.custom_datasets import ASRDataset
from modelscope.utils.logger import get_logger

logger = get_logger()
logger.warning(
    'The reference has been Deprecated, '
    'please use `from modelscope.msdatasets.dataset_cls.custom_datasets import ASRDataset`'
)
