
from monai.transforms import Compose, LoadImaged, EnsureChannelFirstd, ScaleIntensityd, Spacingd, Orientationd
from monai.data import Dataset, DataLoader

train_transforms = Compose([
    LoadImaged(keys=["image", "label"]),
    EnsureChannelFirstd(keys=["image", "label"]),
    Orientationd(keys=["image", "label"], axcodes="RAS"),
    Spacingd(keys=["image", "label"], pixdim=(1.0, 1.0, 1.5), mode=("bilinear", "nearest")),
    ScaleIntensityd(keys=["image"]),
])
