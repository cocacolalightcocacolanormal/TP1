# On définit la question en tant que variable s,appelant "phrase"
phrase = input("Écrivez une phrase")
# on définit "count_word" comme une fonction qui exécutera les actions du "string"
def count_word(string):
# On crée "nombre" comme une fonction qui compte le nombre de mots et qui ne compte pas les espaces comme un mot
    nombre = len(phrase.split(" "))
# ON demande au programme de retourner le nombre de mots
    return nombre
# On crée une variable qui appelle la fonction count_word et la variable phrase pour crée une réponse pour le nombre de mots
resultat = count_word(phrase)
# On print le nombre de mots en appelant la variable de la ligne précédente
print("le nombre de mots est:", resultat)
