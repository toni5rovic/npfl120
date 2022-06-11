python conllu2vectors.py bert-base-multilingual-uncased < data/cs_ru_pud.conllu > embeddings/cs_ru_pud.mbert
python conllu2vectors.py bert-base-multilingual-uncased < data/pt_fr_it_pud.conllu > embeddings/pt_fr_it_pud.mbert
python conllu2vectors.py bert-base-multilingual-uncased < data/de_en_sv_pud.conllu > embeddings/de_en_sv_pud.mbert
python conllu2vectors.py bert-base-multilingual-uncased < data/en_cs_pt_pud.conllu > embeddings/en_cs_pt_pud.mbert

python train_mlp.py models/cs_ru_pud.mbert.model < embeddings/cs_ru_pud.mbert
python train_mlp.py models/pt_fr_it_pud.mbert.model < embeddings/pt_fr_it_pud.mbert
python train_mlp.py models/de_en_sv_pud.mbert.model < embeddings/de_en_sv_pud.mbert
python train_mlp.py models/en_cs_pt_pud.mbert.model < embeddings/en_cs_pt_pud.mbert

echo "Evaluating Spanish on model trained on Czech and Russian"
python eval_mlp.py models/cs_ru_pud.mbert.model < embeddings/es_pud.mbert

echo "Evaluating Spanish on model trained on Portuguese, French and Italian"
python eval_mlp.py models/pt_fr_it_pud.mbert.model < embeddings/es_pud.mbert

echo "Evaluating Spanish on model trained on German, English and Swedish"
python eval_mlp.py models/de_en_sv_pud.mbert.model < embeddings/es_pud.mbert

echo "Evaluating Spanish on model trained on English, Czech and Portuguese"
python eval_mlp.py models/en_cs_pt_pud.mbert.model < embeddings/es_pud.mbert