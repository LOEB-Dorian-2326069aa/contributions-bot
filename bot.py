import os
import datetime

# Générer un fichier avec un timestamp pour simuler une modification
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
filename = "commit.txt"

with open(filename, "a") as file:
    file.write(f"Commit at {date}\n")

# Git commands pour ajouter, committer et pousser les changements
os.system("git add commit.txt")
os.system(f'git commit -m "Automated commit at {date}"')
os.system("git push origin main")
