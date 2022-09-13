# On définit la question en tant que variable s,appelant "phrase"
phrase = input("Écrivez un mot")
# On définit le nombre de mots comme variable. Ensuite on utilise la fonction "len" pour compter le nombre de mots,
# et la fonction "split" pour s'assurer que les espaces ne sont pas tenus en compte pour le nombre de mots.
word_count = len(phrase.split(" "))
# On print le nombre de mots
print("le nombre de mots est:", word_count)