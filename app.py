import pandas as pd

df = pd.DataFrame()

a_0 = [
    (u"\u0906\u0901", -1, -1),
    (u"\u093E\u0901", -1, -1),
    (u"\u0907\u092F\u093E\u0901", 1, -1),
    (u"\u0906\u0907\u092F\u093E\u0901", 2, -1),
    (u"\u093E\u0907\u092F\u093E\u0901", 2, -1),
    (u"\u093F\u092F\u093E\u0901", 1, -1),
    (u"\u0906\u0902", -1, -1),
    (u"\u0909\u0906\u0902", 6, -1),
    (u"\u0941\u0906\u0902", 6, -1),
    (u"\u0908\u0902", -1, -1),
    (u"\u0906\u0908\u0902", 9, -1),
    (u"\u093E\u0908\u0902", 9, -1),
    (u"\u090F\u0902", -1, -1),
    (u"\u0906\u090F\u0902", 12, -1),
    (u"\u0909\u090F\u0902", 12, -1),
    (u"\u093E\u090F\u0902", 12, -1),
    (u"\u0924\u093E\u090F\u0902", 15, -1, "_HindiStemmer__r_CONSONANT"),
    (u"\u0905\u0924\u093E\u090F\u0902", 16, -1),
    (u"\u0928\u093E\u090F\u0902", 15, -1, "_HindiStemmer__r_CONSONANT"),
    (u"\u0905\u0928\u093E\u090F\u0902", 18, -1),
    (u"\u0941\u090F\u0902", 12, -1),
    (u"\u0913\u0902", -1, -1),
    (u"\u0906\u0913\u0902", 21, -1),
    (u"\u0909\u0913\u0902", 21, -1),
    (u"\u093E\u0913\u0902", 21, -1),
    (u"\u0924\u093E\u0913\u0902", 24, -1, "_HindiStemmer__r_CONSONANT"),
    (u"\u0905\u0924\u093E\u0913\u0902", 25, -1),
    (u"\u0928\u093E\u0913\u0902", 24, -1, "_HindiStemmer__r_CONSONANT"),
    (u"\u0905\u0928\u093E\u0913\u0902", 27, -1),
    (u"\u0941\u0913\u0902", 21, -1),
    (u"\u093E\u0902", -1, -1),
    (u"\u0907\u092F\u093E\u0902", 30, -1),
    (u"\u0906\u0907\u092F\u093E\u0902", 31, -1),
    (u"\u093E\u0907\u092F\u093E\u0902", 31, -1),
    (u"\u093F\u092F\u093E\u0902", 30, -1),
    (u"\u0940\u0902", -1, -1),
    (u"\u0924\u0940\u0902", 35, -1, "_HindiStemmer__r_CONSONANT"),
    (u"\u0905\u0924\u0940\u0902", 36, -1),
    (u"\u0906\u0924\u0940\u0902", 36, -1),
    (u"\u093E\u0924\u0940\u0902", 36, -1),
    (u"\u0947\u0902", -1, -1),
    (u"\u094B\u0902", -1, -1),
    (u"\u0907\u092F\u094B\u0902", 41, -1),
    (u"\u0906\u0907\u092F\u094B\u0902", 42, -1),
    (u"\u093E\u0907\u092F\u094B\u0902", 42, -1),
    (u"\u093F\u092F\u094B\u0902", 41, -1),
    (u"\u0905", -1, -1),
    (u"\u0906", -1, -1),
    (u"\u0907", -1, -1),
    (u"\u0908", -1, -1),
    (u"\u0906\u0908", 49, -1),
    (u"\u093E\u0908", 49, -1),
    (u"\u0909", -1, -1),
    (u"\u090A", -1, -1),
    (u"\u090F", -1, -1),
    (u"\u0906\u090F", 54, -1),
    (u"\u0907\u090F", 54, -1),
    (u"\u0906\u0907\u090F", 56, -1),
    (u"\u093E\u0907\u090F", 56, -1),
    (u"\u093E\u090F", 54, -1),
    (u"\u093F\u090F", 54, -1),
    (u"\u0913", -1, -1),
    (u"\u0906\u0913", 61, -1),
    (u"\u093E\u0913", 61, -1),
    (u"\u0915\u0930", -1, -1, "_HindiStemmer__r_CONSONANT"),
    (u"\u0905\u0915\u0930", 64, -1),
    (u"\u0906\u0915\u0930", 64, -1),
    (u"\u093E\u0915\u0930", 64, -1),
    (u"\u093E", -1, -1),
    (u"\u090A\u0902\u0917\u093E", 68, -1),
    (u"\u0906\u090A\u0902\u0917\u093E", 69, -1),
    (u"\u093E\u090A\u0902\u0917\u093E", 69, -1),
    (u"\u0942\u0902\u0917\u093E", 68, -1),
    (u"\u090F\u0917\u093E", 68, -1),
    (u"\u0906\u090F\u0917\u093E", 73, -1),
    (u"\u093E\u090F\u0917\u093E", 73, -1),
    (u"\u0947\u0917\u093E", 68, -1),
    (u"\u0924\u093E", 68, -1, "_HindiStemmer__r_CONSONANT"),
    (u"\u0905\u0924\u093E", 77, -1),
    (u"\u0906\u0924\u093E", 77, -1),
    (u"\u093E\u0924\u093E", 77, -1),
    (u"\u0928\u093E", 68, -1, "_HindiStemmer__r_CONSONANT"),
    (u"\u0905\u0928\u093E", 81, -1),
    (u"\u0906\u0928\u093E", 81, -1),
    (u"\u093E\u0928\u093E", 81, -1),
    (u"\u0906\u092F\u093E", 68, -1),
    (u"\u093E\u092F\u093E", 68, -1),
    (u"\u093F", -1, -1),
    (u"\u0940", -1, -1),
    (u"\u090A\u0902\u0917\u0940", 88, -1),
    (u"\u0906\u090A\u0902\u0917\u0940", 89, -1),
    (u"\u093E\u090A\u0902\u0917\u0940", 89, -1),
    (u"\u090F\u0902\u0917\u0940", 88, -1),
    (u"\u0906\u090F\u0902\u0917\u0940", 92, -1),
    (u"\u093E\u090F\u0902\u0917\u0940", 92, -1),
    (u"\u0942\u0902\u0917\u0940", 88, -1),
    (u"\u0947\u0902\u0917\u0940", 88, -1),
    (u"\u090F\u0917\u0940", 88, -1),
    (u"\u0906\u090F\u0917\u0940", 97, -1),
    (u"\u093E\u090F\u0917\u0940", 97, -1),
    (u"\u0913\u0917\u0940", 88, -1),
    (u"\u0906\u0913\u0917\u0940", 100, -1),
    (u"\u093E\u0913\u0917\u0940", 100, -1),
    (u"\u0947\u0917\u0940", 88, -1),
    (u"\u094B\u0917\u0940", 88, -1),
    (u"\u0924\u0940", 88, -1, "_HindiStemmer__r_CONSONANT"),
    (u"\u0905\u0924\u0940", 105, -1),
    (u"\u0906\u0924\u0940", 105, -1),
    (u"\u093E\u0924\u0940", 105, -1),
    (u"\u0928\u0940", 88, -1, "_HindiStemmer__r_CONSONANT"),
    (u"\u0905\u0928\u0940", 109, -1),
    (u"\u0941", -1, -1),
    (u"\u0942", -1, -1),
    (u"\u0947", -1, -1),
    (u"\u090F\u0902\u0917\u0947", 113, -1),
    (u"\u0906\u090F\u0902\u0917\u0947", 114, -1),
    (u"\u093E\u090F\u0902\u0917\u0947", 114, -1),
    (u"\u0947\u0902\u0917\u0947", 113, -1),
    (u"\u0913\u0917\u0947", 113, -1),
    (u"\u0906\u0913\u0917\u0947", 118, -1),
    (u"\u093E\u0913\u0917\u0947", 118, -1),
    (u"\u094B\u0917\u0947", 113, -1),
    (u"\u0924\u0947", 113, -1, "_HindiStemmer__r_CONSONANT"),
    (u"\u0905\u0924\u0947", 122, -1),
    (u"\u0906\u0924\u0947", 122, -1),
    (u"\u093E\u0924\u0947", 122, -1),
    (u"\u0928\u0947", 113, -1, "_HindiStemmer__r_CONSONANT"),
    (u"\u0905\u0928\u0947", 126, -1),
    (u"\u0906\u0928\u0947", 126, -1),
    (u"\u093E\u0928\u0947", 126, -1),
    (u"\u094B", -1, -1),
    (u"\u094D", -1, -1)
]

# print(len(a_0))
# for i in range(0, 132):
#     df = df.append(
#         {"index": str(i),
#          "text": a_0[i]}, ignore_index=True)
# file_name = 'hindi_data.xlsx'
# df.to_excel(file_name)
text = "या"
df = pd.read_csv("marathi_stopwords.csv", index_col=None)
if text in df["Stopwords"][1]:
    print("yes")
else:
    print("no")

print(text, type(text), len(text))
print(df["Stopwords"][1], type(df["Stopwords"][1]), len(df["Stopwords"][1]))

for j in range(len(df["Stopwords"][1])):
    print(df["Stopwords"][1][j])

for i in range(len(text)):
    print(text[i])


# print(df["Stopwords"][1]
# print(df["Stopwords"][1])
print(df["Stopwords"])
