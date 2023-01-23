# Mycobacterium tuberculosis inhibitor prediction

Identification of active molecules against Mycobacterium tuberculosis using an ensemble of data from ChEMBL25 (Target IDs 360, 2111188 and 2366634). The final model is a stacking model integrating four algorithms, including support vector machine, random forest, extreme gradient boosting and deep neural networks.

## Identifiers

* EOS model ID: `eos46ev`
* Slug: `chemtb`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Probability of M.tb inhibition (measured as IC50 at cut-off 5 uM)

## References

* [Publication](https://academic.oup.com/bib/article-abstract/22/5/bbab068/6209685)
* [Source Code](http://cadd.zju.edu.cn/chemtb/)
* Ersilia contributor: [Amna-28](https://github.com/Amna-28)

## Citation

If you use this model, please cite the [original authors](https://academic.oup.com/bib/article-abstract/22/5/bbab068/6209685) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!