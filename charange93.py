import csv

movies = [["TopGun","Riskey Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]

with open("movie.csv","w",encoding="utf-8") as f:
    f1 = csv.writer(f,delimiter=",")
    for movie_list in movies:
        f1.writerow(movie_list)

    
