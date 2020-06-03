from wordcloud import WordCloud,STOPWORDS

f = open('ntweets.csv', 'r',encoding='UTF-8').read()
f = f.lower()

# wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(f)
stopwords = set(STOPWORDS)
stopwords.add("")
stopwords.update(["positive", "rt", "strongly"])
wordcloud = WordCloud(background_color="white", width=800, height=660, margin=2, stopwords=stopwords).generate(f)

wordcloud.to_file("ntweets.jpg")