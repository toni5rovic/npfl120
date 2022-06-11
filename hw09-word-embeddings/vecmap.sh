cut -f 3,4 es-sr-dict | awk 'NF' | tr -s '\t' ' ' | awk -F " " "NF<=2" > dict_processed.txt

python3 /home/toni/repos/vecmap/map_embeddings.py --supervised dict_processed.txt cc.es.300.less.vec cc.sr.300.less.vec es_mapped_embeddings.emb sr_mapped_embeddings.emb