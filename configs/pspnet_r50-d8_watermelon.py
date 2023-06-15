_base_ = [
    '../_base_/models/pspnet_r50-d8.py', '../_base_/datasets/watermelon_pipeline.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
crop_size = (64, 64) # 杈撳叆鍥惧儚灏哄锛屾牴鎹嚜宸辨暟鎹泦鎯呭喌淇敼
data_preprocessor = dict(size=crop_size)
model = dict(data_preprocessor=data_preprocessor)

