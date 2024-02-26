# py-books-to-scrape

Part 1 : Fichier single_book.py pour extraire les informations d'un livre au choix
Exécuter : 
data = single_book("https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html")
save_to_csv(data) pour enregistrer les informations d'un livre sous forme csv.

Part 2 : Fichier category.py pour récupérer toutes les données d'une catégorie d'ouvrage.
Exécuter : 
data = category("https://books.toscrape.com/catalogue/category/books/travel_2")
Attention : Svp utilisez le url original , pas ajouter "/" ou "index.html" (ex: "https://books.toscrape.com/catalogue/category/books/biography_36", pas "https://books.toscrape.com/catalogue/category/books/biography_36/index.html")
save_to_csv(data) pour enregistrer les données d'une catégorie d'ouvrage sous forme csv.

Part 3 : Fichier scrape_all_book.py pour récupérer toutes les données  des livres présents sur le site "Books to scrape" et conserverer les données scrapées dans plusieurs fichiers CSV, à savoir un fichier CSV par catégorie.
Exécuter : scrape_all_books("https://books.toscrape.com")

Part 4 :Fichier telecharge_img.py pour télécharger l'image de couverture de chaque livre scrapé et la ranger dans un dossier nommé "/images . Les images une fois téléchargées doivent respecter la nomenclature 
suivante : <category_name>_<random_str>.png. La chaîne de caractères aléatoire doit avoir une longueur de 8 caractères
Exécuter : scrawl_img("https://books.toscrape.com")

Bonus 1 : bonus1.py
Fonction create_csv_category() pour générer un fichier CSV "books_details_by_category.csv" comprenant les colonnes : category , books_count , average_price
Exécuter : create_csv_category()
Fonction circle_diagram() pour garder les 20 premières catégories contenant le plus de livres réaliser un diagramme circulaire représentant le nombre de livres par catégorie avec l'affichage d'un pourcentage calculé sur le nombre total de livres.
Exécuter : circle_diagram()

Bonus 2 : bonus2.py
Fonction histogram() pour réaliser un histogramme représentant les prix moyens des livres par catégorie , dans l'ordre du plus petit au plus grand.
Exécuter :  histogram()
