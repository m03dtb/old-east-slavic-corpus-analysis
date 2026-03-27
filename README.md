# Old East Slavic Text Analysis Sample

## Overview
This project implements a reproducible corpus analysis pipeline for **Old East Slavic** texts
based on the _TOROT Treebank_. The pipeline can be readily adapted to the **(Old) Church Slavonic**
texts included in the treebank with only minor modifications.
The pipeline focuses on extracting, normalizing, and analyzing morphological and syntactic features
(e.g. verbs, negation, lemma normalization) from annotated XML sources,
with a particular emphasis on compound tense constructions and auxiliary verb structures.

### Problems addressed
#### Compound verbs
Compound tenses cannot be reliably extracted from the `morphology` annotations of the XML
source files, as auxiliary verbs and main verbs are annotated separately.
The pipeline identifies auxiliary–main verb relations and assigns auxiliary verbs to
their corresponding main verb recursively, enabling the analysis of compound tense constructions (e.g. perfect, pluperfect).

#### Negation
The analysis identifies and marks negated main and auxiliary verbs, making verbal negation explicitly
available for downstream analysis.

#### Pseudo-Aspect
Prefixes and suffixes are used as heuristic cues to approximate verbal aspect, e.g.:
- Verbal suffixes:
  - {-yva-} → secondary imperfectivization
  - {-nu-} → semelfactive derivation
- Verbal prefixes (including graphematic variants)

#### Metadata
An exemplary metadata file illustrates how the XML source files can be combined with
curated metadata (e.g. text titles and dating information) for corpus-based analysis.

## Data and Sources: 
Primary data source: 
- TOROT Treebank (20180919 release)
  https://github.com/torottreebank/treebank-releases/releases
  License: CC BY-NC-SA 3.0

Data download and preprocessing are handled in `01/1_Download_data.ipynb`.

## Analysis Pipeline
1. Data download and XML preprocessing
2. Conversion of XML annotations to Pandas DataFrames
3. Morphological feature extraction and normalization
4. Rule-based extraction of morphosyntactic patterns  
   (e.g. auxiliary chains, negation, verb–verb combinations)
5. Query-based evaluation of tense and verbal constructions

## Repository Structure
- `01/` – Data acquisition and preprocessing
- `02/` – Feature engineering and linguistic analysis
- `02/utils/` – Reusable Python modules

### Query Interface
The notebook `02/7_Evaluate_Tense.ipynb` provides a flexible query interface
that allows users to filter verbs in simple and compound tenses based on
morphological features and auxiliary verb configurations.

Example: retrieve compound tense constructions with two auxiliary verbs:

```python
find_forms(
    df_verbs,
    MAIN_MORPH={"tense": "s"},  # main verb in the resultative
    AUX_LEMMAS=["быти", "быти"],  # auxiliary lemmas
    AUX_MORPH=[
        {"tense": "p"},  # auxiliary in the present tense
        {"tense": "s"}   # auxiliary in the resultative
    ]
)
```


## How to run
The setup assumes a Unix-like environment (macOS or Linux) and Jupyter Lab being installed. On Windows, WSL2 is recommended.

```bash 
chmod +x install.sh
./install.sh
source venv/bin/activate
jupyter lab .
```


Select the kernel: 
**Python (OES)**

The notebooks must be executed in consecutive order:
- 01/:notebooks 1-3 
- 02/:notebooks 1-7

## Metadata
The file `02/metadata/metadata.yaml` contains curated metadata for the analyzed texts.
Metadata were compiled from multiple sources, including the original XML files of the
TOROT Treebank and relevant secondary literature (e.g. manuscript catalogues and
philological studies). Specific bibliographic references are not documented,
as the metadata are intended for exploratory and analytical use.
While compiled with care, the metadata may contain gaps or uncertainties due to
limitations in the available sources.

## Notes 
This project is based on analytical work developed during the author's MA thesis and serves as a research-oriented data analysis example rather than a production system.
