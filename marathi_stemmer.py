"""
Date: 21st feb 20222
Author: Swapnil Gaikwad
Reference: https://ijarcce.com/wp-content/uploads/2016/10/IJARCCE-54.pdf
datasets:
	wordnet: https://github.com/cfiltnlp/pyiwn/blob/master
	Names: https://www.kaggle.com/ananysharma/indian-names-dataset
	relationships: https://en.wikibooks.org/wiki/Marathi/Family_Relationships

	others:
		https://github.com/juand-r/entity-recognition-datasets
		https://github.com/arshadansari27/python-marathi-wordnet


"""
import re
import pandas as pd
import pyiwn


class MarathiStemmer:

    def __init__(self):
        self.stopwords_file = "C:/Users/Anang Raj/Downloads/marathi_stopwords.csv"
        self.names_file = "C:/Users/Anang Raj/Downloads/Indian_Names_in_marathi.xlsx"
        self.relations_file = "C:/Users/Anang Raj/Downloads/relations_data.csv"
        self.suffixes_file = "C:/Users/Anang Raj/Downloads/marathi_suffixes.csv"

    def load_stopwords(self):
        df = pd.read_csv(self.stopwords_file)
        stopwords_list = list(df["Stopwords"])
        # print("\n stopwords_list size = ", len(stopwords_list))
        return stopwords_list

    def load_names(self):
        df = pd.read_excel(self.names_file)
        names_list = list(df["नाव"])
        # print("\n names_list size = ", len(names_list))
        return names_list

    def load_relations(self):
        df = pd.read_csv(self.relations_file)
        relations_list = list(df["Relations"])
        # print("\n relations_list size = ", len(relations_list))
        return relations_list

    def load_wordnet(self):
        wordnet = pyiwn.IndoWordNet(lang=pyiwn.Language.MARATHI)
        words = wordnet.all_words()
        # print("\n wordnet size = ", len(words))
        return words

    def load_suffixes(self):
        df = pd.read_csv(self.suffixes_file)
        suffixes_list = list(df["Suffixes"])
        # print("\n suffixes_list size = ", len(suffixes_list))
        return suffixes_list

    def remove_suffix(self, tok, suffixes):
        for suff in suffixes:
            # if suff in tok:
            split_tok = tok.split(suff)
            if split_tok[-1] == "":
                tok = tok[:len(tok)-len(suff)]
        return tok

    def remove_inflection(self, tok):
        inflection_dict = {"त": ["ता", "णत", "ती", "तु", "तू", "ते", "तै", "तो", "तौ"],
                           "न": ["ना", "णन", "नी", "नु", "नू", "ने", "नै", "नो", "नौ"],
                           "ण": ["ना" "ण", "न", "नी" "नु", "नू", "ने", "नै", "नो", "नौ"],
                           "ल": ["ला", "ली", "लां", "ल"],
                           "षा": ["षे", "षां"]}
        for key, val_list in inflection_dict.items():
            for val in val_list:
                split_tok = tok.split(val)
                if split_tok[-1] == "":
                    tok = tok[:len(tok)-len(val)] + key
        return tok

    def stem(self, text, tokens):
        """ the received text is already preprocessed.
        step1: filtration (already done)
        step2: Tokenization (already done)

        """
        # wordnet = self.load_wordnet()
        names_list = self.load_names()
        relations_list = self.load_relations()
        suffixes = self.load_suffixes()
        # print("\n suffixes : ", suffixes)
        total_list = names_list + relations_list
        "For text(sentences) with tokens"
        # stemmed_text = ""
        # for tok in tokens:
        #     if tok not in total_list:
        #         cleaned_tok = self.remove_suffix(tok, suffixes)
        #         cleaned_tok = self.remove_inflection(cleaned_tok)
        #         stemmed_text += " " + cleaned_tok
        #     else:
        #         stemmed_text += " " + tok
        # stemmed_text = re.sub(r"\s\s+", "", stemmed_text)
        # stemmed_text = stemmed_text.strip()
        # print("\n stemmed_text = ", stemmed_text)
        "For testing (supplying one token at a time)"
        cleaned_tok = tokens
        if tokens not in total_list:
            cleaned_tok = self.remove_suffix(tokens, suffixes)
            cleaned_tok = self.remove_inflection(cleaned_tok)
        stemmed_text = cleaned_tok
        return stemmed_text

    def testing(self):
        df = pd.read_excel("testing script.xlsx")
        total_words = len(df)
        correct_pred = 0
        for index, word in enumerate(df["Original_Word"]):
            stemmed_word = self.stem(word, word)
            if stemmed_word == df["Stem_Word"][index]:
                correct_pred += 1
            else:
                print("word: {}, index: {},  my_stem: {}, correct_stem: {}, ".format(word, index, stemmed_word, df["Stem_Word"][index]))
        return correct_pred, total_words



if __name__ == "__main__":
    try:
        obj = MarathiStemmer()
        correct_pred, total_words = obj.testing()
        accuracy = (correct_pred/total_words) * 100
        print(accuracy)
        # # text = "आधार पडताळणी करताना वेतन कार्ड अपग्रेड करण्यासाठी समस्या येत आहे"
        # text = "भारतामध्ये मराठीमधला लीपीवर शबदांचा शोधण्याचे णमळवता मराठीतील सुलभपणे संशोधनासाठी स्पॅमिंग थांबवा, कोणतेही संदेश पाठवू नका"
        # print("\n input text = ", text)
        # tokens = text.split()
        # obj.stem(text, tokens)
    except Exception as e:
        print(e)
