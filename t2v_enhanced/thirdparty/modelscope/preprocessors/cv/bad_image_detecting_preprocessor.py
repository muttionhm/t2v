# These codes are copied from modelscope revision c58451baead80d83281f063d12fb377fad415257 
# Copyright (c) Alibaba, Inc. and its affiliates.
import math
from typing import Any, Dict

import torch
import torch.nn.functional as F
from numpy import ndarray
from PIL import Image
from torchvision import transforms

from modelscope.metainfo import Preprocessors
from modelscope.preprocessors.base import Preprocessor
from modelscope.preprocessors.builder import PREPROCESSORS
from modelscope.utils.constant import Fields
from modelscope.utils.type_assert import type_assert


@PREPROCESSORS.register_module(
    Fields.cv, module_name=Preprocessors.bad_image_detecting_preprocessor)
class BadImageDetectingPreprocessor(Preprocessor):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transform_input = transforms.Compose([
            transforms.Resize(224),
            transforms.CenterCrop(224),
            transforms.ToTensor()
        ])

    @type_assert(object, object)
    def __call__(self, data: ndarray) -> Dict[str, Any]:
        image = Image.fromarray(data)
        data = self.transform_input(image)
        data = data.unsqueeze(0)
        return {'input': data.float()}
