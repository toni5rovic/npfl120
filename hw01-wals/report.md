# Homework assignment 1 - WALS

NPFL120 - Multilingual NLP

Antonije Petrović

# Task 1

Calculating the similarity scores between a given language and all other languages available in WALS. 

The similarity score between languages $X$ and $Y$ is calculated as:

$$s(X, Y) = \frac{m(X, Y)}{t}$$

where $m$ is the number of matching features between languages $X$ and $Y$, and $t$ is the total number of features in WALS (excluding codes, geographical location and similar non-linguistic data).

For Serbo-Croatian (wals code: **scr**), the top 10 most similar languages are:

| id   | wals_code | name           | genus    | family        | macroarea | matching_features | similarity_score |
| ---- | --------- | -------------- | -------- | ------------- | --------- | ----------------- | ---------------- |
| 2038 | rus       | Russian        | Slavic   | Indo-European | Eurasia   | 50                | 0.256410         |
| 783  | grk       | Greek (Modern) | Greek    | Indo-European | Eurasia   | 43                | 0.220513         |
| 1931 | pol       | Polish         | Slavic   | Indo-European | Eurasia   | 43                | 0.220513         |
| 1321 | lit       | Lithuanian     | Baltic   | Indo-European | Eurasia   | 41                | 0.210256         |
| 650  | eng       | English        | Germanic | Indo-European | Eurasia   | 39                | 0.200000         |
| 2123 | slo       | Slovene        | Slavic   | Indo-European | Eurasia   | 38                | 0.194872         |
| 385  | bul       | Bulgarian      | Slavic   | Indo-European | Eurasia   | 38                | 0.194872         |
| 2434 | ukr       | Ukrainian      | Slavic   | Indo-European | Eurasia   | 37                | 0.189744         |
| 2154 | spa       | Spanish        | Romance  | Indo-European | Eurasia   | 37                | 0.189744         |
| 543  | cze       | Czech          | Slavic   | Indo-European | Eurasia   | 36                | 0.184615         |

Fairly surprising results are that Greek, Lithuanian and English are more similar than some other Slavic languages (Slovene, Bulgarian), but this may be explained by the fact that Greek and English are much better represented in WALS (having data for >150 features), while Slovene and Bulgarian have the number of features similar to the one of Serbo-Croatian (ranging 40-80). If the features represented for these languages were to be full, we could expect different results.

However, it might be possible to achieve better results by using slightly better similarity metric that would take into account the number of features that exist in both languages that we compare.



# Task 2

In this task, we calculate the centroid language of a given genus. This is done by calculating similarities between all pairs of languages in a given genus, and then summing the similarity scores for all languages and finding the maximum value.

For the Slavic genus, we will construct a symmetric matrix of scores like so:

|     | blr        | bos        | bul        | cze        | ksu        | mcd        | plb        | pol        | rus        | scr        | slo        | sou        | srb        | srl        | svc        | svk        | ukr        |
| --- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| blr | 0.         | 0.01538462 | 0.0974359  |            | 0.09230769 | 0.02051282 | 0.06666667 | 0.01538462 | 0.12307692 | 0.12307692 | 0.1025641  | 0.09230769 | 0.03589744 | 0.03076923 | 0.02051282 | 0.01538462 | 0.05128205 | 0.12307692 |
| bos | 0.01538462 | 0.         | 0.02051282 | 0.01538462 | 0.01538462 | 0.01538462 | 0.01538462 | 0.01538462 | 0.01538462 | 0.02051282 | 0.01538462 | 0.01538462 | 0.01538462 | 0.01538462 | 0.01538462 | 0.01538462 | 0.01538462 |
| bul | 0.0974359  | 0.02051282 | 0.         | 0.15897436 | 0.02051282 | 0.16923077 | 0.01538462 | 0.28717949 | 0.33333333 | 0.19487179 | 0.16923077 | 0.03076923 | 0.05128205 | 0.02051282 | 0.01538462 | 0.03589744 | 0.19487179 |
| cze | 0.09230769 | 0.01538462 | 0.15897436 | 0.         | 0.02051282 | 0.11282051 | 0.01538462 | 0.20512821 | 0.22051282 | 0.18461538 | 0.14871795 | 0.04102564 | 0.09230769 | 0.02051282 | 0.01538462 | 0.07692308 | 0.18974359 |
| ksu | 0.02051282 | 0.01538462 | 0.02051282 | 0.02051282 | 0.         | 0.02051282 | 0.01538462 | 0.02051282 | 0.02051282 | 0.02051282 | 0.02051282 | 0.02051282 | 0.01538462 | 0.02051282 | 0.01538462 | 0.02051282 | 0.02051282 |
| mcd | 0.06666667 | 0.01538462 | 0.16923077 | 0.11282051 | 0.02051282 | 0.         | 0.01538462 | 0.16410256 | 0.15897436 | 0.14358974 | 0.15897436 | 0.03076923 | 0.05128205 | 0.02051282 | 0.01538462 | 0.03589744 | 0.14358974 |
| plb | 0.01538462 | 0.01538462 | 0.01538462 | 0.01538462 | 0.01538462 | 0.01538462 | 0.         | 0.01538462 | 0.02051282 | 0.02051282 | 0.02051282 | 0.01538462 | 0.01538462 | 0.01538462 | 0.02051282 | 0.01538462 | 0.01538462 |
| pol | 0.12307692 | 0.01538462 | 0.28717949 | 0.20512821 | 0.02051282 | 0.16410256 | 0.01538462 | 0.         | 0.38461538 | 0.22051282 | 0.18461538 | 0.04102564 | 0.06153846 | 0.02051282 | 0.01538462 | 0.06153846 | 0.23076923 |
| rus | 0.12307692 | 0.01538462 | 0.33333333 | 0.22051282 | 0.02051282 | 0.15897436 | 0.02051282 | 0.38461538 | 0.         | 0.25641026 | 0.21025641 | 0.04102564 | 0.05128205 | 0.02051282 | 0.02564103 | 0.05641026 | 0.28717949 |
| scr | 0.1025641  | 0.02051282 | 0.19487179 | 0.18461538 | 0.02051282 | 0.14358974 | 0.02051282 | 0.22051282 | 0.25641026 | 0.         | 0.19487179 | 0.03589744 | 0.05641026 | 0.02051282 | 0.02564103 | 0.04615385 | 0.18974359 |
| slo | 0.09230769 | 0.01538462 | 0.16923077 | 0.14871795 | 0.02051282 | 0.15897436 | 0.02051282 | 0.18461538 | 0.21025641 | 0.19487179 | 0.         | 0.04102564 | 0.04615385 | 0.02051282 | 0.02564103 | 0.04102564 | 0.18461538 |
| sou | 0.03589744 | 0.01538462 | 0.03076923 | 0.04102564 | 0.02051282 | 0.03076923 | 0.01538462 | 0.04102564 | 0.04102564 | 0.03589744 | 0.04102564 | 0.         | 0.01538462 | 0.02051282 | 0.01538462 | 0.03589744 | 0.04102564 |
| srb | 0.03076923 | 0.01538462 | 0.05128205 | 0.09230769 | 0.01538462 | 0.05128205 | 0.01538462 | 0.06153846 | 0.05128205 | 0.05641026 | 0.04615385 | 0.01538462 | 0.         | 0.01538462 | 0.01538462 | 0.03589744 | 0.04615385 |
| srl | 0.02051282 | 0.01538462 | 0.02051282 | 0.02051282 | 0.02051282 | 0.02051282 | 0.01538462 | 0.02051282 | 0.02051282 | 0.02051282 | 0.02051282 | 0.02051282 | 0.01538462 | 0.         | 0.01538462 | 0.02051282 | 0.02051282 |
| svc | 0.01538462 | 0.01538462 | 0.01538462 | 0.01538462 | 0.01538462 | 0.01538462 | 0.02051282 | 0.01538462 | 0.02564103 | 0.02564103 | 0.02564103 | 0.01538462 | 0.01538462 | 0.01538462 | 0.         | 0.01538462 | 0.01538462 |
| svk | 0.05128205 | 0.01538462 | 0.03589744 | 0.07692308 | 0.02051282 | 0.03589744 | 0.01538462 | 0.06153846 | 0.05641026 | 0.04615385 | 0.04102564 | 0.03589744 | 0.03589744 | 0.02051282 | 0.01538462 | 0.         | 0.05128205 |
| ukr | 0.12307692 | 0.01538462 | 0.19487179 | 0.18974359 | 0.02051282 | 0.14358974 | 0.01538462 | 0.23076923 | 0.28717949 | 0.18974359 | 0.18461538 | 0.04102564 | 0.04615385 | 0.02051282 | 0.01538462 | 0.05128205 | 0.         |


If we sum the rows we will get the following total similarities:

| blr        | bos        | bul        | cze        | ksu        | mcd        | plb        | pol        | rus        | scr        | slo        | sou        | srb        | srl        | svc        | svk        | ukr        |
| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| 1.02564103 | 0.25641026 | 1.81538462 | 1.61025641 | 0.30769231 | 1.32307692 | 0.26666667 | 2.05128205 | 2.22564103 | 1.73333333 | 1.57435897 | 0.47692308 | 0.61538462 | 0.30769231 | 0.28205128 | 0.61538462 | 1.76923077 |

The maximum value is 2.22564103 for Russian langauge, which appears to be the centroid language of this genus.

A few more examples:
- Genus: Romance $\rightarrow$ Centroid language: Spanish [similarity: 2.435897] 
- Genus: Semitic $\rightarrow$ Centroid language: Arabic (Egyptian) [similarity: 3.128205]


# Task 3

In this task, we are trying to find the weirdest (the least similar) language in a give genus/family or in the whole WALS. This is again done by using the matrix of similarity scores, but here we take the language with the minimal total similarity value.

Interesting results:

| Genus   | Family        | The "weirdest" language | WALS code | ISO code | Similarity score |
| ------- | ------------- | ----------------------- | --------- | -------- | ---------------- |
|         | Indo-European | Romani (Sepecides)      | rse       |          | 0.007575           |
|         | Niger-Congo   | Urhobo                  | urh       | urh      | 0.010382          |
|         | Dravidian     | Gadaba (Kondekor)       | gdk       | gdb      | 0.010702          |
| Slavic  |               | Bosnian                 | bos       | bos      | 0.015083          |
| Romance |               | Moldavian               | mol       | ron      | 0.014957         |
| Turkic  |               | Dolgan                  | dol       | dlg      | 0.015009        |
