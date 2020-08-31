import wikipedia as wp

article = input("веди искомую статью: ")
allArticle = wp.search(article, results=3)
print("Есть несколько статей: " + str(allArticle))

chose = input("выбери конкретную статью: ")

if chose == allArticle[0]:
    print(wp.summary(allArticle[0]))
elif chose == allArticle[1]:
    print(wp.summary(allArticle[1]))
elif chose == allArticle[2]:
    print(wp.summary(allArticle[2]))
else:
    print("Нет такой статьи")
