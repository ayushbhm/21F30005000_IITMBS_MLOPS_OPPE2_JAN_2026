# Deliverable 7: Input Drift Detection

## Method: KS Test (Training data vs 100-row synthetic data)

| Feature    | KS Stat | p-value | Status |
|------------|---------|---------|--------|
| age        | 0.0948  | 0.4740  | OK     |
| gender     | 0.0032  | 1.0000  | OK     |
| cp         | 0.0570  | 0.9534  | OK     |
| trestbps   | 0.0461  | 0.9942  | OK     |
| chol       | 0.0899  | 0.5420  | OK     |
| fbs        | 0.0115  | 1.0000  | OK     |
| restecg    | 0.0151  | 1.0000  | OK     |
| thalach    | 0.0574  | 0.9517  | OK     |
| exang      | 0.0033  | 1.0000  | OK     |
| oldpeak    | 0.0459  | 0.9944  | OK     |
| slope      | 0.0307  | 1.0000  | OK     |
| ca         | 0.0676  | 0.8544  | OK     |
| thal       | 0.0240  | 1.0000  | OK     |

## Conclusion
No significant input drift detected (all p > 0.05). The synthetic 100-row prediction data closely mirrors the training distribution across all 13 features.
