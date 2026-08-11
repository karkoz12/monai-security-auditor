
from monai.transforms import Compose, LoadImaged, EnsureChannelFirstd, ScaleIntensityd, RandAffined, RandGaussianNoised
from monai.data import Dataset, DataLoader

train_transforms = Compose([
    LoadImaged(keys=["image", "label"]),
    EnsureChannelFirstd(keys=["image", "label"]),
    ScaleIntensityd(keys=["image"]),
    RandAffined(keys=["image", "label"], prob=0.5, rotate_range=(0.1, 0.1, 0.1)),
    RandGaussianNoised(keys=["image"], prob=0.5, mean=0.0, std=0.05),
])
