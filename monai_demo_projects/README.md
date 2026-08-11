# MonoAI Demo Projects

Synthetic demo projects for testing MonoAI audit reports.
No clinical data is included.

Copy `monoai.py` next to this folder, then run examples:

## 01_healthy_project

```bash
python monoai.py audit monoai_demo_projects/01_healthy_project --dataset monoai_demo_projects/01_healthy_project/data --model monoai_demo_projects/01_healthy_project/models --out audit_01_healthy_project
```

## 02_missing_model

```bash
python monoai.py audit monoai_demo_projects/02_missing_model --dataset monoai_demo_projects/02_missing_model/data --model monoai_demo_projects/02_missing_model/models --out audit_02_missing_model
```

## 03_missing_bundle

```bash
python monoai.py audit monoai_demo_projects/03_missing_bundle --dataset monoai_demo_projects/03_missing_bundle/data --model monoai_demo_projects/03_missing_bundle/models --out audit_03_missing_bundle
```

## 04_corrupted_dataset

```bash
python monoai.py audit monoai_demo_projects/04_corrupted_dataset --dataset monoai_demo_projects/04_corrupted_dataset/data --model monoai_demo_projects/04_corrupted_dataset/models --out audit_04_corrupted_dataset
```

## 05_wrong_labels

```bash
python monoai.py audit monoai_demo_projects/05_wrong_labels --dataset monoai_demo_projects/05_wrong_labels/data --model monoai_demo_projects/05_wrong_labels/models --out audit_05_wrong_labels
```

## 06_untrusted_pt_model

```bash
python monoai.py audit monoai_demo_projects/06_untrusted_pt_model --dataset monoai_demo_projects/06_untrusted_pt_model/data --model monoai_demo_projects/06_untrusted_pt_model/models --out audit_06_untrusted_pt_model
```

## 07_incomplete_metadata

```bash
python monoai.py audit monoai_demo_projects/07_incomplete_metadata --dataset monoai_demo_projects/07_incomplete_metadata/data --model monoai_demo_projects/07_incomplete_metadata/models --out audit_07_incomplete_metadata
```

## 08_research_prototype

```bash
python monoai.py audit monoai_demo_projects/08_research_prototype --dataset monoai_demo_projects/08_research_prototype/data --model monoai_demo_projects/08_research_prototype/models --out audit_08_research_prototype
```

## 09_clinical_candidate

```bash
python monoai.py audit monoai_demo_projects/09_clinical_candidate --dataset monoai_demo_projects/09_clinical_candidate/data --model monoai_demo_projects/09_clinical_candidate/models --out audit_09_clinical_candidate
```

## 10_bad_mask_values

```bash
python monoai.py audit monoai_demo_projects/10_bad_mask_values --dataset monoai_demo_projects/10_bad_mask_values/data --model monoai_demo_projects/10_bad_mask_values/models --out audit_10_bad_mask_values
```

## 11_nan_image

```bash
python monoai.py audit monoai_demo_projects/11_nan_image --dataset monoai_demo_projects/11_nan_image/data --model monoai_demo_projects/11_nan_image/models --out audit_11_nan_image
```

Special explicit missing model test:

```bash
python monoai.py audit monoai_demo_projects/02_missing_model --dataset monoai_demo_projects/02_missing_model/data --model monoai_demo_projects/02_missing_model/models/missing_model.pt --out audit_02_missing_model_explicit
```
