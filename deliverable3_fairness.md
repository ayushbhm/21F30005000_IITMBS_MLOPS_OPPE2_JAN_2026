# Deliverable 3: Fairness Testing with Fairlearn

## Sensitive Attribute: Age (binned: <40, 40-55, >55)

| Age Group | Accuracy | Selection Rate | FPR    | FNR    |
|-----------|----------|----------------|--------|--------|
| <40       | 0.750    | 0.250          | 0.000  | 0.500  |
| 40-55     | 0.926    | 0.333          | 0.056  | 0.111  |
| >55       | 0.833    | 0.567          | 0.167  | 0.167  |

## Disparity
| Metric              | Difference |
|---------------------|------------|
| Accuracy            | 0.176      |
| Selection Rate      | 0.317      |
| False Positive Rate | 0.167      |
| False Negative Rate | 0.389      |

## Summary
- **<40 group is most disadvantaged**: 50% FNR means the model misses heart disease in young patients half the time.
- **>55 group is over-predicted**: highest selection rate (0.567), meaning older patients are flagged more often.
- **Selection rate disparity of 0.317** indicates significant bias — older patients are twice as likely to be predicted positive than younger ones.
- Model requires fairness mitigation (e.g., reweighting or threshold adjustment per age group) before production use.
