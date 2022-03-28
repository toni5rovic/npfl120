
output_name=$1
udpipe=~/tools/udpipe-1.2.0-bin/bin-linux64/udpipe

# Harmonize
python3 harmonize.py < data/en-ud-dev-orig.conllu > output/$output_name.conllu

# Parse the harmonized file and save it
cat output/$output_name.conllu | $udpipe --parse models/en.sup.parser.udpipe > output/$output_name.parsed.conllu

# Get accuracy of the harmonized file
cat output/$output_name.conllu | $udpipe --parse --accuracy models/en.sup.parser.udpipe