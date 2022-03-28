# Homework assignment 3 - Machine Translation

NPFL120 - Multilingual NLP

Antonije Petrović

# Intro

After compiling Moses and GIZA, creating the alignments using Moses and GIZA++ was done with the script [make_alignments.sh](./make_alignments.sh)

I chose to work with Greek and Serbian, and chose SETIMES dataset [OPUS SETIMES en-sr (in the moses format)](https://object.pouta.csc.fi/OPUS-SETIMES/v2/moses/el-sr.txt.zip) which covers news from the Balkan peninsula. The corpus contains around 0.2 million sentence pairs with 4.9 million Greek and 4.8 Serbian tokens.

# Task 1

**Visually compare the left, right and intersection alignments. Check in how many sentences you see the 'garbage alignments' that all fall onto one word. Compare the intersection alignment for the baseline and improved alignments.**

Printing the alignments is done by using my script [show_alignments.sh](./show_alignments.sh) where three parameters are provided:

- alignment type (3=left, 4=right, 5=intersection, 6=union)
- source language code
- target language code

![Sentence 1 - Left, right and intersection alignments](/hw03/images/1_el_sr_345.png "Sentence 1 - Left, right and intersection alignments")

*Figure 1. Sentence 1 - Left, right and intersection alignments*

English translation: "Serbia easily passed the IMF's assessment right before the elections"

---

![Sentence 2 - Left, right and intersection alignments](/hw03/images/2_el_sr_345.png "Sentence 2 - Left, right and intersection alignments")

*Figure 2. Sentence 2 - Left, right and intersection alignments*

English translation: "The first IMF assessment under the precautionary stand-by arrangement went well."

---

![Sentence 3 - Left, right and intersection alignments](/hw03/images/3_el_sr_345.png "Sentence 3 - Left, right and intersection alignments")

*Figure 3. Sentence 3 - Left, right and intersection alignments*

English translation: "The agreement is being respected and the Serbian banking system is stable."

---

## 2.1 Visual analysis

- Feminine definite nominative article "Η" (example: Η Σερβία) and other definite articles (του, της) are captured in the left alignment only. In other types of alignments, the definite articles are ignored.
- Left alignemnts tend to align multiple source words with one target word 
  - Observable as vertical lines in the left-most alignment pictures above
- In the right alignemnts it is commonly observable that we have multiple target words aligned to a single source word.
  - Observable as horizontal lines in the middle alignment pictures above
  - Examples:
  - "επισκόπηση" (*assessment*) -> "lako prošla procenu" (*easily passed the assessment*)
  - "εφεδρικής" (*reserve, backup*) -> "stend-baj aranžmana" (*stand-by arrangement*)

## 2.2 "Garbage" alignments

![](/hw03/images/example_garbage_alignment.png "")

This image shows an example of multiple "garbage" alignments that are all mapped to the word "poredimo" in Serbian (*eng. compare, 1st person plural, present tense*)

## 2.3 Comparing baseline and improved alignments

![](/hw03/images/1_el_sr_compare_aligns.png)

![](/hw03/images/2_el_sr_compare_aligns.png)

![](/hw03/images/3_el_sr_compare_aligns.png)

Most of the alignments are pertained, but in some cases the "improved" alignments (on the right side) are worse. It seems that stemming the words doesn't really help.

However, stemming helps in the above-mentioned case of garbage alignments:

![](/hw03/images/garbage_align_improved.png)

---

# Task 2

**Write a small script that reads:**

1. **source tokens**
2. **target tokens**
3. **alignment**

**and emits all pairs of aligned words.**

Script [get_aligned_words.py](./get_aligned_words.py) has 4 arguments:
- --src: source language
- --dst: destination language
- --align_type: Alignment type (3=left, 4=right, 5=intersection, 6=union)
- --improved: Use improved alignemnts (lowercase+stemming)

The script provides word pairs on the standard output. We run the script:

`python get_aligned_words.py --src el --dst sr --align_type 5 --improved False`

and get the following output:

```console
Δημήτρη Demetrisom
Χριστόφια, Kristofijasom,
τοπικούς lokalnim
πολιτικούς političkim
ηγέτες liderima
και i
Αρχιεπίσκοπο arhiepiskopom
Χρυσόστομο Krisostomosom
διάρκεια tokom
διήμερης dvodnevne
επίσκεψης posete
που koja
ξεκίνησε počela
```

If run like so: 

`python get_aligned_words.py --src el --dst sr --align_type 5 --improved False | sort | uniq -c | sort -n` 

word pairs are sorted in the ascending order by the number of occurrences.

Example output:
```console
   2515 που koja
   2530 ωστόσο ali
   2586 αλλά ali
   2591 Δευτέρα ponedeljak
   2774 για na
   2784 οποία koja
   2813 μετά posle
   2863 Ωστόσο, Međutim,
   2979 ευρώ evra
   2982 δήλωσε izjavio
   3044 μόνο samo
   3168 Β-Ε BiH
   3176 Σύμφωνα Prema
   3200 κυβέρνηση vlada
   3314 θα bi
   3346 υπουργός ministar
```

