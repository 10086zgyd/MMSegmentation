from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class watermelonDataset(BaseSegDataset):

    METAINFO = {
        'classes': ['red', 'green', 'white', 'seed-black', 'seed-white', 'unlabeled'],
        'palette': [[132, 41, 246], [228, 193, 110], [152, 16, 60], [58, 221, 254], [41, 169, 226], [155, 155, 155]]

    }

def __init__(self,
             img_suffix='.jpg',
             seg_map_suffix='.png',
             reduce_zero_label=False,
             **kwargs) -> None:
    super().__init__(
        img_suffix=img_suffix,
        seg_map_suffix=seg_map_suffix,
        reduce_zero_label=reduce_zero_label,
        **kwargs)
