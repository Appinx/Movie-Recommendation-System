# coding=utf-8
"""
@time: 2021/4/9 11:03 AM
@author: colaplusice
@contact: fjl2401@163.com vx:18392358995
"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie.settings")
import django

django.setup()
from user.models import Movie

movies = Movie.objects.all()
all_images=os.listdir('../media/movie_cover')
print(all_images[:3])
for movie in movies:
    s=str(movie.image_link.name).split('/')[-1]
    print(s)
    all_images.remove(s)
    # if not os.path.exists('../media/' + str(movie.image_link)):
    #     print(movie.image_link)

print(all_images)