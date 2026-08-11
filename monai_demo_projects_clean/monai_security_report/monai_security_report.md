# MONAI Cybersecurity Report

## Scope

- Project root: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean`
- Dataset root: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean`
- Model path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\models\model.safetensors`

## Executive Summary

- Dependencies scanned: **7**
- Model files scanned: **1**
- Dataset files scanned: **121**
- MONAI transforms detected: **0**
- Issues found: **74**

## Issues

### WARNING

- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\requirements.txt`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\requirements.txt
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\train.py`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\train.py
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\bundle\configs\inference.json`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\configs\inference.json
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\bundle\docs\README.md`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\docs\README.md
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\bundle\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\data\case_000_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_000_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\data\case_001_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_001_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\requirements.txt`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\requirements.txt
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\train.py`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\train.py
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\bundle\configs\inference.json`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\configs\inference.json
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\bundle\docs\README.md`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\docs\README.md
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\bundle\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\data\case_000_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_000_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\data\case_001_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_001_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\requirements.txt`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\requirements.txt
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\train.py`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\train.py
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\bundle\configs\inference.json`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\configs\inference.json
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\bundle\docs\README.md`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\docs\README.md
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\bundle\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\data\case_000_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_000_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\data\case_001_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_001_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\requirements.txt`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\requirements.txt
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\train.py`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\train.py
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\bundle\configs\inference.json`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\configs\inference.json
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\bundle\docs\README.md`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\docs\README.md
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\bundle\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\data\case_000_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_000_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\data\case_001_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_001_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\requirements.txt`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\requirements.txt
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\train.py`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\train.py
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\bundle\configs\inference.json`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\configs\inference.json
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\bundle\docs\README.md`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\docs\README.md
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\bundle\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\data\case_000_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_000_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\data\case_001_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_001_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\requirements.txt`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\requirements.txt
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\train.py`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\train.py
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\bundle\configs\inference.json`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\configs\inference.json
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\bundle\docs\README.md`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\docs\README.md
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\bundle\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\data\case_000_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_000_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\data\case_001_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_001_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\requirements.txt`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\requirements.txt
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\train.py`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\train.py
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\bundle\configs\inference.json`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\configs\inference.json
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\bundle\docs\README.md`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\docs\README.md
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\bundle\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\data\case_000_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_000_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\data\case_001_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_001_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\requirements.txt`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\requirements.txt
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\train.py`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\train.py
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\bundle\configs\inference.json`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\configs\inference.json
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\bundle\docs\README.md`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\docs\README.md
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\bundle\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\data\case_000_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_000_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\data\case_001_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_001_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\requirements.txt`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\requirements.txt
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\train.py`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\train.py
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\bundle\configs\inference.json`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\configs\inference.json
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\bundle\docs\README.md`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\docs\README.md
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\bundle\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\data\case_000_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_000_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\data\case_001_image_mask.nii.gz`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_001_image_mask.nii.gz
- **dataset_metadata_scanner / duplicate_dataset_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\models\model.safetensors`
  - Message: Duplicate file content detected. Same as: C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors

### INFO

- **monai_transform_scanner / no_transforms_found**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean`
  - Message: No MONAI dictionary transforms detected in project Python files.

## Dependencies

| Package | Version |
|---|---|
| `monai` | `1.5.2` |
| `torch` | `2.10.0` |
| `numpy` | `2.2.6` |
| `nibabel` | `5.4.2` |
| `scipy` | `1.15.3` |
| `pydicom` | `3.0.1` |
| `matplotlib` | `3.10.8` |

## Model Files

| Path | Size | SHA256 | Notes |
|---|---:|---|---|
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\models\model.safetensors` | 4 | `10a87133a313ecf0...` |  |

## Dataset Metadata

| Path | Shape | Min | Max | SHA256 |
|---|---|---:|---:|---|
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\README.md` | `None` | None | None | `c6e1cdf97c4ef75b...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\requirements.txt` | `None` | None | None | `ade4f8007901e3ef...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\train.py` | `None` | None | None | `4fed5c73e1776a82...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\configs\inference.json` | `None` | None | None | `44136fa355b3678a...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\configs\metadata.json` | `None` | None | None | `f6c8ee61c0b37976...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\docs\README.md` | `None` | None | None | `6711975b8c8f15fa...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\bundle\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_000_image.nii.gz` | `(32, 32, 16)` | 0.013574415817856789 | 0.8999999761581421 | `1d80ab9bb52a8c2d...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_000_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `211cf4f88dfcc16d...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_001_image.nii.gz` | `(32, 32, 16)` | 0.01587422750890255 | 0.8999999761581421 | `5275bbd84675e7a8...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\data\case_001_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `6d85733a09c80988...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\01_brain_segmentation\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\requirements.txt` | `None` | None | None | `ade4f8007901e3ef...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\train.py` | `None` | None | None | `4fed5c73e1776a82...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\bundle\configs\inference.json` | `None` | None | None | `44136fa355b3678a...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\bundle\configs\metadata.json` | `None` | None | None | `8a6c75740d168efb...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\bundle\docs\README.md` | `None` | None | None | `6711975b8c8f15fa...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\bundle\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\data\case_000_image.nii.gz` | `(32, 32, 16)` | 0.012082410044968128 | 0.8999999761581421 | `bb226d154b90afd9...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\data\case_000_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `211cf4f88dfcc16d...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\data\case_001_image.nii.gz` | `(32, 32, 16)` | 0.007165626157075167 | 0.8999999761581421 | `aa6045451678ceee...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\data\case_001_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `6d85733a09c80988...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\02_lung_ct\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\requirements.txt` | `None` | None | None | `ade4f8007901e3ef...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\train.py` | `None` | None | None | `4fed5c73e1776a82...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\bundle\configs\inference.json` | `None` | None | None | `44136fa355b3678a...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\bundle\configs\metadata.json` | `None` | None | None | `de7577039edd838a...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\bundle\docs\README.md` | `None` | None | None | `6711975b8c8f15fa...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\bundle\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\data\case_000_image.nii.gz` | `(32, 32, 16)` | 0.0031470872927457094 | 0.8999999761581421 | `226bfaeeadf8881f...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\data\case_000_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `211cf4f88dfcc16d...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\data\case_001_image.nii.gz` | `(32, 32, 16)` | 0.011883405968546867 | 0.8999999761581421 | `db4199f7bc678975...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\data\case_001_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `6d85733a09c80988...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\03_liver_ct\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\requirements.txt` | `None` | None | None | `ade4f8007901e3ef...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\train.py` | `None` | None | None | `4fed5c73e1776a82...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\bundle\configs\inference.json` | `None` | None | None | `44136fa355b3678a...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\bundle\configs\metadata.json` | `None` | None | None | `412132c601334e40...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\bundle\docs\README.md` | `None` | None | None | `6711975b8c8f15fa...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\bundle\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\data\case_000_image.nii.gz` | `(32, 32, 16)` | 0.011031894013285637 | 0.8999999761581421 | `493f882cbc891b6a...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\data\case_000_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `211cf4f88dfcc16d...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\data\case_001_image.nii.gz` | `(32, 32, 16)` | 0.012301411479711533 | 0.8999999761581421 | `f435b54b50d8d663...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\data\case_001_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `6d85733a09c80988...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\04_glioma\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\requirements.txt` | `None` | None | None | `ade4f8007901e3ef...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\train.py` | `None` | None | None | `4fed5c73e1776a82...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\bundle\configs\inference.json` | `None` | None | None | `44136fa355b3678a...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\bundle\configs\metadata.json` | `None` | None | None | `b2930276a405d8ef...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\bundle\docs\README.md` | `None` | None | None | `6711975b8c8f15fa...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\bundle\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\data\case_000_image.nii.gz` | `(32, 32, 16)` | 0.011626980267465115 | 0.8999999761581421 | `fce4a3ea5878d5b9...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\data\case_000_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `211cf4f88dfcc16d...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\data\case_001_image.nii.gz` | `(32, 32, 16)` | 0.012443648651242256 | 0.8999999761581421 | `7e00e8b1dc0679e3...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\data\case_001_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `6d85733a09c80988...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\05_meningioma\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\requirements.txt` | `None` | None | None | `ade4f8007901e3ef...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\train.py` | `None` | None | None | `4fed5c73e1776a82...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\bundle\configs\inference.json` | `None` | None | None | `44136fa355b3678a...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\bundle\configs\metadata.json` | `None` | None | None | `c2b427642ed28299...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\bundle\docs\README.md` | `None` | None | None | `6711975b8c8f15fa...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\bundle\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\data\case_000_image.nii.gz` | `(32, 32, 16)` | 0.012621867470443249 | 0.8999999761581421 | `eda8cc9e0a757792...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\data\case_000_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `211cf4f88dfcc16d...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\data\case_001_image.nii.gz` | `(32, 32, 16)` | 0.006596564780920744 | 0.8999999761581421 | `c67dd39bd9e4ad8e...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\data\case_001_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `6d85733a09c80988...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\06_pituitary\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\requirements.txt` | `None` | None | None | `ade4f8007901e3ef...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\train.py` | `None` | None | None | `4fed5c73e1776a82...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\bundle\configs\inference.json` | `None` | None | None | `44136fa355b3678a...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\bundle\configs\metadata.json` | `None` | None | None | `b6e225972592a01b...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\bundle\docs\README.md` | `None` | None | None | `6711975b8c8f15fa...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\bundle\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\data\case_000_image.nii.gz` | `(32, 32, 16)` | 0.012591131962835789 | 0.8999999761581421 | `a437eee7d2ffd640...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\data\case_000_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `211cf4f88dfcc16d...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\data\case_001_image.nii.gz` | `(32, 32, 16)` | 0.011942518875002861 | 0.8999999761581421 | `1b810b111abd0612...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\data\case_001_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `6d85733a09c80988...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\07_multiclass\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\requirements.txt` | `None` | None | None | `ade4f8007901e3ef...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\train.py` | `None` | None | None | `4fed5c73e1776a82...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\bundle\configs\inference.json` | `None` | None | None | `44136fa355b3678a...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\bundle\configs\metadata.json` | `None` | None | None | `e7f1a8df3817784d...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\bundle\docs\README.md` | `None` | None | None | `6711975b8c8f15fa...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\bundle\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\data\case_000_image.nii.gz` | `(32, 32, 16)` | 0.009089997969567776 | 0.8999999761581421 | `574a514ea6c7d37c...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\data\case_000_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `211cf4f88dfcc16d...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\data\case_001_image.nii.gz` | `(32, 32, 16)` | 0.007441886700689793 | 0.8999999761581421 | `766e49f2f51a91ca...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\data\case_001_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `6d85733a09c80988...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\08_bundle\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\requirements.txt` | `None` | None | None | `ade4f8007901e3ef...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\train.py` | `None` | None | None | `4fed5c73e1776a82...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\bundle\configs\inference.json` | `None` | None | None | `44136fa355b3678a...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\bundle\configs\metadata.json` | `None` | None | None | `d3a1c65d27f5bef8...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\bundle\docs\README.md` | `None` | None | None | `6711975b8c8f15fa...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\bundle\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\data\case_000_image.nii.gz` | `(32, 32, 16)` | 0.011670447885990143 | 0.8999999761581421 | `8c8bde100c6c4c51...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\data\case_000_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `211cf4f88dfcc16d...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\data\case_001_image.nii.gz` | `(32, 32, 16)` | 0.009946398437023163 | 0.8999999761581421 | `315b52f4ca27b5c5...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\data\case_001_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `6d85733a09c80988...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\09_research\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\requirements.txt` | `None` | None | None | `ade4f8007901e3ef...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\train.py` | `None` | None | None | `4fed5c73e1776a82...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\bundle\configs\inference.json` | `None` | None | None | `44136fa355b3678a...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\bundle\configs\metadata.json` | `None` | None | None | `7ebf59db18d7efa6...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\bundle\docs\README.md` | `None` | None | None | `6711975b8c8f15fa...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\bundle\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\data\case_000_image.nii.gz` | `(32, 32, 16)` | 0.01380614098161459 | 0.8999999761581421 | `326dcb91d77544c4...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\data\case_000_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `211cf4f88dfcc16d...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\data\case_001_image.nii.gz` | `(32, 32, 16)` | 0.010791603475809097 | 0.8999999761581421 | `a7b083d2b87a3ce4...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\data\case_001_image_mask.nii.gz` | `(32, 32, 16)` | 0.0 | 1.0 | `6d85733a09c80988...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\10_clinical\models\model.safetensors` | `None` | None | None | `10a87133a313ecf0...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\monai_security_report\dataset_metadata.json` | `None` | None | None | `b9f3c1b02b869deb...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\monai_security_report\dependencies.json` | `None` | None | None | `ce41d0d561a69a68...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\monai_security_report\model_files.json` | `None` | None | None | `13ce5e1152c1db54...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\monai_security_report\monai_security_report.html` | `None` | None | None | `81a57f1ca83f75f7...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\monai_security_report\monai_security_report.json` | `None` | None | None | `4c428ea5562f5589...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\monai_security_report\monai_security_report.md` | `None` | None | None | `fce7ac7627eb6b6f...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\monai_security_report\monai_security_report.pdf` | `None` | None | None | `7d8dded111050b29...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\monai_security_report\monai_transforms.json` | `None` | None | None | `4f53cda18c2baa0c...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\monai_security_report\pip_freeze.txt` | `None` | None | None | `b25f4aff7bc0e7dd...` |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects_clean\monai_security_report\summary.txt` | `None` | None | None | `d144368399418785...` |

## MONAI Transform Review

No MONAI transforms detected.

## Defensive Notes

- Use signed or checksum-verified datasets and model artifacts.
- Avoid loading untrusted pickle-based PyTorch checkpoints.
- Keep raw intensity and affine metadata in audit logs.
- Run transform review before training and inference deployment.
- Keep generated JSON reports under version control or artifact storage.
