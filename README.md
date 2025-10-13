# Mycobacterium tuberculosis inhibitor prediction

Identification of active molecules against Mycobacterium tuberculosis using an ensemble of data from ChEMBL25 (Target IDs 360, 2111188 and 2366634). The final model is a stacking model integrating four algorithms, including support vector machine, random forest, extreme gradient boosting and deep neural networks.

This model was incorporated on 2022-06-28.


## Information
### Identifiers
- **Ersilia Identifier:** `eos46ev`
- **Slug:** `chemtb`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Tuberculosis`
- **Target Organism:** `Mycobacterium tuberculosis`
- **Tags:** `M.tuberculosis`, `IC50`, `Tuberculosis`, `Antimicrobial activity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of M.tb inhibition (measured as IC50 at cut-off 5 uM)

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
- **Environment Size (Mb):** `1850`


### References
- **Source Code**: [http://cadd.zju.edu.cn/chemtb/](http://cadd.zju.edu.cn/chemtb/)
- **Publication**: [https://academic.oup.com/bib/article-abstract/22/5/bbab068/6209685](https://academic.oup.com/bib/article-abstract/22/5/bbab068/6209685)
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
