import snowballstemmer

# from nltk.stem.snowball import SnowballStemmer
# from nltk.stem.porter import PorterStemmer

stemmer = snowballstemmer.stemmer('english')
# print(snowballstemmer.algorithms())
# print(len(snowballstemmer.algorithms()))
english_text = "Hindi (Devanagari: हिन्दी, हिंदी, ISO: Hindī), or more precisely Modern Standard Hindi (Devanagari: मानक हिन्दी, ISO: Mānak Hindī),[8] is an Indo-Aryan language spoken chiefly in the northern part of India. Hindi has been described as a standardised and Sanskritised register[9] of the Hindustani language, which itself is based primarily on the Khariboli dialect of Delhi and neighbouring areas of Northern India.[10][11][12] Hindi, written in the Devanagari script, is one of the two official languages of the Government of India, along with English.[13] It is an official language in 9 States and 3 Union Territories and an additional official language in 3 other states.[14][15][16][17] Hindi is also one of the 22 scheduled languages of the Republic of India."
hindi_text = "हिंदी ( देवनागरी : हिन्दी , हिंदी , आईएसओ : हिंद ), या अधिक सटीक रूप से आधुनिक मानक हिंदी ( देवनागरी : मानक हिन्दी , आईएसओ : मानक हिंद ), [8] भारत के उत्तरी भाग में मुख्य रूप से बोली जाने वाली एक इंडो-आर्यन भाषा है । हिंदी को हिंदुस्तानी भाषा का एक मानकीकृत और संस्कृतिकृत रजिस्टर [9] के रूप में वर्णित किया गया है , जो स्वयं मुख्य रूप से दिल्ली की खारीबोली बोली पर आधारित है। और उत्तरी भारत के पड़ोसी क्षेत्र । [10] [11] [12] देवनागरी लिपि में लिखी गई हिंदी, अंग्रेजी के साथ-साथ भारत सरकार की दो आधिकारिक भाषाओं में से एक है । [13] यह 9 राज्यों और 3 केंद्र शासित प्रदेशों में एक आधिकारिक भाषा है और 3 अन्य राज्यों में एक अतिरिक्त आधिकारिक भाषा है। [14] [15] [16] [17] हिंदी भी भारत गणराज्य की 22 अनुसूचित भाषाओं में से एक है ।"
marathi_text = "हिंदी ( देवनागरी : हिंदी , हिंदी , ISO : हिंदी ), किंवा अधिक तंतोतंत आधुनिक मानक हिंदी ( देवनागरी : मानक हिन्दी , ISO : मानक हिंदी ), [८] ही एक इंडो-आर्यन भाषा आहे जी प्रामुख्याने भारताच्या उत्तर भागात बोलली जाते . हिंदीचे वर्णन हिंदुस्थानी भाषेचे प्रमाणित आणि संस्कृतीकृत रजिस्टर [९] म्हणून केले गेले आहे, जी स्वतः दिल्लीच्या खरीबोली बोलीवर आधारित आहे. आणि उत्तर भारतातील शेजारील भाग . [१०] [११] [१२] देवनागरी लिपीमध्ये लिहिलेली हिंदी ही इंग्रजीसह भारत सरकारच्या दोन अधिकृत भाषांपैकी एक आहे . [१३] ही ९ राज्ये आणि ३ केंद्रशासित प्रदेशांमध्ये अधिकृत भाषा आहे आणि इतर ३ राज्यांमध्ये अतिरिक्त अधिकृत भाषा आहे. [१४] [१५] [१६] [१७] हिंदी ही भारतीय प्रजासत्ताकाच्या २२ अनुसूचित भाषांपैकी एक आहे ."
# tokens = ["consult", "consulting", "consultant", "consultants", "consultative"]
# print(stemmer.stemWords("We are the world".split()))
print(english_text.split())
print(stemmer.stemWords(english_text.split()))
