# Homework assignment 7 - Tree Projection

NPFL120 - Multilingual NLP

Antonije Petrović

# Assignment description

- implement the projections somehow
- ensure the produced tree is a rooted, acyclical tree
- evaluate the solution for several language pairs and report the scores

# Report

The algorithm that I have used for projecting the dependency relations from one treebank to another is the following:
- Algorithm processes one sentence at a time, iterating over source tokens and considering all target tokens aligned with a particular source token
- For a given source token we know its head and dependency relation
- Dependency relation for each target token is copied from the source token
- In order to find the head for that particular target token, we consider the following sub-algorithm:
  - Take all potential heads in the target treebank by using the alignment of the source head
  - Remove all potential heads that may cause a cyclical dependency
  - If there are potential heads left, take the first one and finish
  - Else, we can consider a pair of part-of-speech tags in the source sentence that are involved in the particular dependency relation. Then, we try to find the same pair in the target sentence, where the child is the current target token.
  - If nothing is found using this approach, we then consider statistics that were acquired by processing the source treebank. For each dependency relation we count the pair of part-of-speech tags, and we save this information. When searching for a head of a particular target token, we try to find the token in the target sentence that has the tag that is most common for a given dependency relation. If it doesn't exist, we try to find the second-most common, etc. 
  - Lastly, if none of the previous approaches were fruitful, we use the statistics of the most common part-of-speech tag of the head of each dependency relation, build upon the source trebank. Then we try to find the token with the most common tag for a particular dep. relation, and we resort to less common tags if needed.
  - Lastly, if nothing helped, we return -1.
  - Note: in all of the previous steps, we are careful not to choose a head that causes a cyclical dependency.

Idea:
- for each PoS tag pair -> what's the most frequent dependency relation?
- use this to set the baseline relations
- should I copy from source by default, and then use this statistics regarding PoS pairs only in the cases when no alignment exists for a particular target token

# Results

## LAS evaluation

| Semantic relation | Arabic | Czech  | Spanish | Portuguese | Russian | Turkish |
| ----------------- | ------ | ------ | ------- | ---------- | ------- | ------- |
| NOUN              | 0.0909 | 0.1667 | 0.2580  | 0.3423     | 0.1434  | 0.0382  |
| VERB              | 0.0376 | 0.0519 | 0.1456  | 0.2078     | 0.0834  | 0.0049  |
| PRON              | 0.1362 | 0.0346 | 0.1200  | 0.3049     | 0.2826  | 0.0586  |
| ADP               | 0.1508 | 0.2317 | 0.2772  | 0.3521     | 0.2182  | 0.0615  |
| DET               | 0.0723 | 0.1439 | 0.3194  | 0.3458     | 0.1385  | 0.1197  |
| PROPN             | 0.1709 | 0.2456 | 0.3649  | 0.3521     | 0.2230  | 0.0990  |
| ADJ               | 0.1037 | 0.1537 | 0.2429  | 0.2851     | 0.1794  | 0.0556  |
| ADV               | 0.1312 | 0.1802 | 0.2475  | 0.3817     | 0.1922  | 0.0517  |
| AUX               | 0.1046 | 0.2176 | 0.2768  | 0.4146     | 0.2316  | 0.0057  |
| PUNCT             | 0.2846 | 0.2801 | 0.3077  | 0.3039     | 0.2306  | 0.1745  |
| CONJ              | 0.0000 | 0.0000 | 0.0000  | 0.0000     | 0.0000  | 0.0000  |
| CCONJ             | 0.2546 | 0.3298 | 0.4278  | 0.5017     | 0.3116  | 0.1400  |
| PART              | 0.0194 | 0.1964 | 0.0000  | 0.0000     | 0.1803  | 0.0000  |
| NUM               | 0.1375 | 0.2200 | 0.3931  | 0.3970     | 0.2189  | 0.0851  |
| SCONJ             | 0.1283 | 0.1482 | 0.0000  | 0.0000     | 0.0966  | 0.0000  |
| X                 | 0.0000 | 0.0000 | 0.1000  | 0.0000     | 0.0659  | 0.0377  |
| INTJ              | 0.0000 | 0.0000 | 0.0000  | 0.0000     | 0.0000  | 0.0000  |
| SYM               | 0.0000 | 0.2000 | 0.1905  | 0.3235     | 0.1000  | 0.0000  |

Join LAS evaluation:

|     | Arabic | Czech  | Spanish | Portuguese | Russian | Turkish |
| --- | ------ | ------ | ------- | ---------- | ------- | ------- |
|     | 0.1331 | 0.1854 | 0.2677  | 0.3285     | 0.1808  | 0.0691  |


## Head evaluation

| Semantic relation | Arabic | Czech  | Spanish | Portuguese | Russian | Turkish |
| ----------------- | ------ | ------ | ------- | ---------- | ------- | ------- |
| NOUN              | 0.1707 | 0.2430 | 0.3337  | 0.4113     | 0.2231  | 0.1251  |
| VERB              | 0.2804 | 0.2228 | 0.2904  | 0.3300     | 0.2550  | 0.2228  |
| PRON              | 0.1877 | 0.1609 | 0.3520  | 0.5103     | 0.3267  | 0.1368  |
| ADP               | 0.2090 | 0.2735 | 0.3070  | 0.3857     | 0.2684  | 0.0901  |
| DET               | 0.1687 | 0.3063 | 0.3492  | 0.3840     | 0.2876  | 0.1854  |
| PROPN             | 0.2480 | 0.3355 | 0.4595  | 0.4305     | 0.2853  | 0.1553  |
| ADJ               | 0.1846 | 0.2566 | 0.3141  | 0.3584     | 0.2753  | 0.1382  |
| ADV               | 0.2030 | 0.2497 | 0.3256  | 0.4376     | 0.2693  | 0.0940  |
| AUX               | 0.1373 | 0.3040 | 0.3460  | 0.4939     | 0.3053  | 0.0571  |
| PUNCT             | 0.2895 | 0.2900 | 0.3108  | 0.3059     | 0.2480  | 0.1903  |
| CONJ              | 0.0000 | 0.0000 | 0.0000  | 0.0000     | 0.0000  | 0.0000  |
| CCONJ             | 0.2684 | 0.3616 | 0.4570  | 0.5554     | 0.3389  | 0.1602  |
| PART              | 0.1799 | 0.2679 | 0.0000  | 0.0000     | 0.2077  | 0.0000  |
| NUM               | 0.2049 | 0.2832 | 0.5310  | 0.5287     | 0.2512  | 0.1915  |
| SCONJ             | 0.1765 | 0.2389 | 0.0000  | 0.0000     | 0.1989  | 0.0769  |
| X                 | 0.2000 | 0.0000 | 0.1000  | 0.0000     | 0.1557  | 0.1509  |
| INTJ              | 0.0000 | 0.0000 | 0.0000  | 0.0000     | 0.0000  | 0.0000  |
| SYM               | 0.0000 | 0.2667 | 0.3810  | 0.4118     | 0.1500  | 0.0000  |

Joint head evaluation:

|     | Arabic | Czech  | Spanish | Portuguese | Russian | Turkish |
| --- | ------ | ------ | ------- | ---------- | ------- | ------- |
|     | 0.2124 | 0.2656 | 0.3367  | 0.3919     | 0.2572  | 0.1435  |

## Deprel evaluation

| Semantic relation | Arabic | Czech  | Spanish | Portuguese | Russian | Turkish |
| ----------------- | ------ | ------ | ------- | ---------- | ------- | ------- |
| NOUN              | 0.2103 | 0.3008 | 0.4164  | 0.5125     | 0.2622  | 0.1182  |
| VERB              | 0.1643 | 0.2399 | 0.3923  | 0.5127     | 0.2807  | 0.0353  |
| PRON              | 0.3354 | 0.0727 | 0.1957  | 0.4411     | 0.4810  | 0.1857  |
| ADP               | 0.3351 | 0.4715 | 0.4381  | 0.5001     | 0.4458  | 0.3076  |
| DET               | 0.1807 | 0.2522 | 0.4774  | 0.4834     | 0.2490  | 0.3533  |
| PROPN             | 0.3302 | 0.3721 | 0.5154  | 0.5148     | 0.3698  | 0.2189  |
| ADJ               | 0.2132 | 0.2684 | 0.3657  | 0.4196     | 0.2805  | 0.1697  |
| ADV               | 0.3391 | 0.3463 | 0.4290  | 0.5779     | 0.3477  | 0.2115  |
| AUX               | 0.2157 | 0.4367 | 0.4740  | 0.5640     | 0.5053  | 0.0190  |
| PUNCT             | 0.8443 | 0.6719 | 0.8813  | 0.8378     | 0.5830  | 0.6757  |
| CONJ              | 0.0000 | 0.0000 | 0.0000  | 0.0000     | 0.0000  | 0.0000  |
| CCONJ             | 0.6672 | 0.7126 | 0.8385  | 0.8668     | 0.7398  | 0.6511  |
| PART              | 0.0688 | 0.3750 | 0.0000  | 0.0000     | 0.4372  | 0.0000  |
| NUM               | 0.3854 | 0.3355 | 0.5494  | 0.5435     | 0.3955  | 0.2128  |
| SCONJ             | 0.3529 | 0.3916 | 0.0000  | 0.0000     | 0.2330  | 0.0769  |
| X                 | 0.0000 | 0.0000 | 0.2000  | 0.0000     | 0.1497  | 0.0849  |
| INTJ              | 0.0000 | 0.0000 | 0.0000  | 0.0000     | 0.0000  | 0.0000  |
| SYM               | 0.1333 | 0.6000 | 0.5238  | 0.5882     | 0.5000  | 0.1667  |

Joint deprel evaluation:

|     | Arabic | Czech  | Spanish | Portuguese | Russian | Turkish |
| --- | ------ | ------ | ------- | ---------- | ------- | ------- |
|     | 0.3311 | 0.3802 | 0.4787  | 0.5450     | 0.3757  | 0.2362  |
