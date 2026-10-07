# Mycobacterium tuberculosis inhibitor prediction

Flags likely inhibitors of Mycobacterium tuberculosis H37Rv growth. Ye and colleagues pooled minimum inhibitory concentrations for three ChEMBL targets, called a compound active below 5 uM and ended with 2,424 inhibitors against 6,094 inactives. The served predictor is their best configuration, a stacked ensemble of support vector machine, random forest, XGBoost and deep neural network predictions over RDKit descriptors and Morgan fingerprints. It reached an AUC of 0.94 on a scaffold-split test set but 0.75 on compounds published later, so unfamiliar scaffolds are read with caution.

This model was incorporated on 2022-06-28.Last packaged on 2025-12-04.

## Information
### Identifiers
- **Ersilia Identifier:** `eos46ev`
- **Slug:** `chemtb`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Tuberculosis`
- **Target Organism:** `Mycobacterium tuberculosis`
- **Tags:** `IC50`, `Antimicrobial activity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of Mycobacterium tuberculosis growth inhibition, with actives defined by a minimum inhibitory concentration below 5 uM.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| proba_chemtb | float | high | Probability of inhibiting Mtuberculosis growth |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos46ev](https://hub.docker.com/r/ersiliaos/eos46ev)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos46ev.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos46ev.zip)

### Resource Consumption
- **Model Size (Mb):** `109`
- **Environment Size (Mb):** `2095`
- **Image Size (Mb):** `2190.84`

**Computational Performance (seconds):**
- 10 inputs: `27.85`
- 100 inputs: `21.29`
- 10000 inputs: `260.25`

### References
- **Source Code**: [http://cadd.zju.edu.cn/chemtb/](http://cadd.zju.edu.cn/chemtb/)
- **Publication**: [https://doi.org/10.1093/bib/bbab068](https://doi.org/10.1093/bib/bbab068)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [Amna-28](https://github.com/Amna-28)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos46ev
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos46ev
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
