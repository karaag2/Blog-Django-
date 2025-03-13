import json
from pathlib import Path
from models import BlogPost

chemin = Path().home()/"Downloads"/"_@BoxZone_Udemy_La_Formation_Complète_Django_2021_MP4_Français_part1"/"Udemy - La Formation Complète Django 2021 MP4 [Français]"/"11.Lesrequetes/blog-blogpost.json"
lien = chemin
with open(lien, "r") as f:
    data = json.load(f)

for bp in data:
    BlogPost.objects.create(title=bp["title"],
                            published=bp["published"],
                            description=bp["description"],
                            date=bp["date"])