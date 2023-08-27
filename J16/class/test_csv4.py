import csv

HEADER = ['NAME' , 'GENER' , 'IMDB SCORE' , 'YEAR' , 'DURATION TIME']

data = [
    ['Oppenheimer' , 'Biographic' , 8.6 , 2023 , 150],
    ['Spider verse' , 'Sci-Fi' , 9 , 2023 , 120],
    ['Fast & Furious' , 'Action' , 7.5 , 2020 , 114],
    ['The Shining' , 'Horror' , 9.5 , 1977 , 90]
]

with open('J16/class/films.csv','w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(HEADER)
    csv_writer.writerows(data)