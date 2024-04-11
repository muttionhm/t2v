# These codes are copied from modelscope revision c58451baead80d83281f063d12fb377fad415257 
"""
The implementation here is modified based on insightface, originally MIT license and publicly available at
https://github.com/deepinsight/insightface/tree/master/detection/scrfd/mmdet/models/detectors
"""
from .scrfd import SCRFD
from .tinymog import TinyMog

__all__ = ['SCRFD', 'TinyMog']
