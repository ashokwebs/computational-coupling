# 🗄️ Dataset Repository & Configuration

This directory contains metadata configs, BIDS download scripts, and schema definitions for datasets used across our research program.

---

## 📌 Public Open-Access Datasets Used

1. **DUET (Dyadic Understanding, EEG and Turn-taking)**
   - **Access:** OpenNeuro `ds007764`
   - **Modality:** Dual 64-channel EEG (18 dyads, face-to-face French dialogue)
   - **Paper Usage:** Paper 2 (Biological Hyperscanning)

2. **Joint Agency EEG Dataset**
   - **Access:** OpenNeuro `ds007471`
   - **Modality:** Dual EEG (piano duet joint action task)
   - **Paper Usage:** Paper 2 (Motor Coordination Asymmetry)

3. **Natural Scenes Dataset (NSD)**
   - **Access:** Amazon S3 (`s3://natural-scenes-dataset`)
   - **Modality:** 7T fMRI (8 subjects, 73,000 COCO visual trials)
   - **Paper Usage:** Pre-training semantic encoders (MindEye2 baseline)

---

## 🚫 Data Storage Rule
**Never commit raw binary dataset files (`.edf`, `.nii.gz`, `.mat`) directly to Git!** Keep them in `datasets/raw/` (ignored by `.gitignore`).
