# Bioinformatics & Forensic DNA Projects

**Author:** Zanyar Erkozan

---

## 📋 Overview

This repository contains multiple projects related to Bioinformatics and Forensic DNA Analysis, including individual research notebooks and a comprehensive Forensic DNA Kinship Analysis system.

---

## 🧬 Forensic DNA Kinship Project (Phase 1)
**Directory:** `/team-project`

A Python application designed for use in forensic DNA analysis that determines the kinship relationship between two individuals using a family tree structure. 

### Features:
- **Relationship Detection:** Identifies complex family relationships including parent-child, siblings, grandparents, uncles/aunts, and various degrees of cousins.
- **Tree Traversal:** Utilizes Breadth-First Search (BFS) to map generations.
- **LCA Algorithm:** Computes the Lowest Common Ancestor (LCA) to determine genetic distance and exact relationship strings.
- **Object-Oriented Structure:** Custom classes (`male_person`, `female_person`, `partnership`) to model complex family configurations.

### Usage:
```bash
cd team-project
python run_example.py
```
*(Unit tests available via `pytest test_kinship.py`)*

---

## 🔬 Bioinformatics Notebooks

**Files:**
- `cng465-fall-2025-2026-semester-project-phase1of2-zanyar-erkozan-2584985.ipynb`
- `cng465-fall-2025-2026-semester-project-phase2of2-zanyar-erkozan-2584985.ipynb`

Jupyter Notebooks containing extensive data analysis, algorithm implementation, and computational biology workflows. 

### Highlights:
- Data parsing and preprocessing for biological sequences.
- Algorithmic approaches to DNA/RNA or protein sequence analysis.
- Visualization of biological data structures.

---

## 🛠️ Requirements

- Python 3.6+
- Jupyter Notebook / Lab (for `.ipynb` files)
- Standard Python libraries (`typing`, `dataclasses`, `collections`)
