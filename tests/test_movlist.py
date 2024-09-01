#from movdata.movlist import save_movies
from movdata.mov_detail import make_detail_list, save_detail_list, get_detail_data,load_movie_list

#def test_save_movies():
#    r = save_movies()
#    assert r

def test_make_detail_list():
    r = make_detail_list(year=2015)
    assert r

