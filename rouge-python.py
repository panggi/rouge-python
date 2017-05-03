import sys
import os
from libraries.pythonrouge.pythonrouge import Pythonrouge

ROUGE_PL = "libraries/ROUGE-RELEASE-1.5.5/ROUGE-1.5.5.pl"
ROUGE_DATA = "libraries/ROUGE-RELEASE-1.5.5/data/"
cwd = os.getcwd()

# initialize setting of ROUGE, eval ROUGE-1, 2, SU4, L
rouge = Pythonrouge(n_gram=2, ROUGE_SU4=True, ROUGE_L=True, stemming=True, stopwords=True, word_level=True, length_limit=False, length=50, use_cf=False, cf=95, scoring_formula="average", resampling=True, samples=1000, favor=True, p=0.5)

setting_file = rouge.setting(files=True, summary_path="./summaries", reference_path="./references")

result = rouge.eval_rouge(setting_file, recall_only=True, ROUGE_path=ROUGE_PL, data_path=ROUGE_DATA)
print(result)
