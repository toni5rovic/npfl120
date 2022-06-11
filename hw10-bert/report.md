# Homework assignment 10 - BERT

NPFL120 - Multilingual NLP

Antonije Petrović

## Report

The assignment is to try to do cross-lingual POS tagging with mBERT.

1. I used the PUD data and converted every treebank to the vector format for POS tags by using the given `conllu2vectors.py` script without improvements.
2. In the first experiment, I trained different models using single source languages and then evaluated on Spanish.
3. In the second experiment, I concatenated different languages and tried to profit from the related languages.
4. In the final approach, I used models trained on single languages and evaluated them on all other languages.


## Training on different source languages and evaluating on Spanish

| Language used for training | Accuracy on Spanish |
| -------------------------- | ------------------- |
| Arabic                     | 64.635%             |
| Czech                      | 69.68%              |
| German                     | 81.20%              |
| English                    | 76.354%             |
| Finnish                    | 48.73%              |
| French                     | 89.36%              |
| Hindi                      | 49.15%              |
| Italian                    | 87.412%             |
| Portuguese                 | **90.70%**          |
| Russian                    | 76.06%              |
| Swedish                    | 73.86%              |
| Turkish                    | 47.083%             |
| Chinese                    | 8.899%              |

- As expected, Portuguese model performs the best
- French and Italian are very close
- Followed by German, English and Russian
- Chinese model performs terribly, but the script is not the reason since Arabic performs comparable to i.e. Czech with accuracy of 64.635%

## Concatenating source languages

| Concatenated training languages | Accuracy on Spanish |
| ------------------------------- | ------------------- |
| Czech and Russian               | 80.20%              |
| Portuguese, French and Italian  | **94.6942%**        |
| German, English and Swedish     | 84.91%              |
| English, Czech and Portuguese   | 92.435%             |

- As expected, training on concatenated Romance languages performs really well on Spanish data
- Mixing Romance, Germanic and Slavic language also performs almost as well


## Trying different target languages 

| src\tgt | ar     | cs         | de     | en         | es         | fi         | fr         | hi     | it     | pt         | ru         | sv         | tr         | zh         |
| ------- | ------ | ---------- | ------ | ---------- | ---------- | ---------- | ---------- | ------ | ------ | ---------- | ---------- | ---------- | ---------- | ---------- |
| ar      | -      | 67.29%     | 59.67% | 60.03%     | 64.21%     | 60.68%     | 59.34%     | 59.73% | 57.53% | 64.64%     | **73.18%** | 63.69%     | 55.29%     | 28.57%     |
| cs      | 71.60% | -          | 74.69% | 69.58%     | 70.60%     | 77.16%     | 67.84%     | 64.44% | 67.91% | 69.87%     | **85.57%** | 78.68%     | 71.10%     | 42.86%     |
| de      | 70.10% | 82.30%     | -      | **86.15%** | 82.72%     | 78.54%     | 80.96%     | 64.44% | 83.87% | 78.69%     | 80.86%     | 83.14%     | 72.01%     | 71.43%     |
| en      | 69.89% | 72.99%     | 81.40% | -          | 76.35%     | 78.74%     | 75.68%     | 66.76% | 75.41% | 77.55%     | 80.67%     | **82.09%** | 68.07%     | 42.86%     |
| es      | 72.95% | 76.45%     | 81.01% | 80.80%     | -          | 74.77%     | **93.24%** | 59.05% | 88.51% | 93.04%     | 80.53%     | 78.85%     | 64.90%     | 42.86%     |
| fi      | 52.44% | 68.73%     | 58.88% | 56.84%     | 48.73%     | -          | 50.99%     | 54.11% | 55.31% | 50.93%     | 66.66%     | 64.95%     | 66.34%     | **71.43%** |
| fr      | 73.87% | 75.96%     | 82.48% | 83.36%     | 89.36%     | 75.53%     | -          | 64.25% | 86.62% | **89.55%** | 80.39%     | 78.81%     | 67.81%     | 57.14%     |
| hi      | 58.36% | 57.63%     | 59.84% | 57.00%     | 49.15%     | 63.72%     | 51.46%     | -      | 52.87% | 53.98%     | 64.54%     | 56.77%     | **66.25%** | 28.57%     |
| it      | 72.31% | 72.97%     | 76.91% | 75.29%     | **87.41%** | 75.79%     | 86.15%     | 59.12% | -      | 82.08%     | 77.33%     | 74.49%     | 57.67%     | 57.14%     |
| pt      | 73.02% | 70.42%     | 73.56% | 72.95%     | 90.70%     | 73.58%     | **91.00%** | 61.63% | 84.38% | -          | 77.52%     | 71.83%     | 64.30%     | 42.86%     |
| ru      | 73.73% | **82.51%** | 72.36% | 74.86%     | 76.06%     | 74.81%     | 68.29%     | 57.50% | 75.43% | 71.09%     | -          | 77.22%     | 67.07%     | 42.86%     |
| sv      | 69.25% | 79.37%     | 76.79% | 80.67%     | 73.86%     | 80.64%     | 70.44%     | 59.82% | 76.65% | 70.79%     | **80.96%** | -          | 67.05%     | 57.14%     |
| tr      | 49.17% | 56.28%     | 51.79% | 48.77%     | 47.08%     | **66.93%** | 48.09%     | 61.34% | 51.25% | 49.85%     | 61.47%     | 52.49%     | -          | 42.86%     |
| zh      | 10.64% | 8.73%      | 9.38%  | **11.96%** | 8.90%      | 11.42%     | 8.41%      | 6.51%  | 9.23%  | 7.61%      | 8.59%      | 11.77%     | 8.12%      | -          |

- Most of the results are expected - languages from the same language groups perform well:
  - Czech and Russian perform well on one another
  - German model gave the best performance on English and English model performed well on Swedish data
  - Spanish and Portuguese models performed well on French data, and French model performed well on Portuguese
  - Chinese model performs terribly on all of the languages on which it was evaluated
- Some more interesting results:
  - Interestingly, Hindi model gave the best result (66.25%) on Turkish data
  - Arabic worked decently on Russian data (73.18%)
  - Finnish gave the biggest accuracy on Chinese data
  - Turkish model worked the best on Finnish data