import requests
import os
import json
import time #API를 너무 빨리 호출하면 에러발생 -> sleep 필요
from tqdm import tqdm
import shutil

API_KEY = os.getenv('MOVIE_API_KEY')
home_path=os.path.expanduser('~')

def load_movie_list(year):
    load_path = f'{home_path}/code/movdata/data/movies/year={year}/data.json'
    with open(load_path, "w", encoding='utf-8') as f:
              load_data = json.load(f)
    return load_data

def make_detail_list(year):

    # json 데이터 읽어오기
    load_data = load_movie_list(year)
    # for문 돌면서 detail_data 가져오기
    all_detail_data = []
    for ddata in tqdm(load_data):
        movieCd = ddata['movieCd']
        # movieCd 데이터 추출
        detail_data = get_detail_data(movieCd)
        all_detail_data.append(detail_data)
        # 추출한 데이터 저장
        save_detail_list(year, all_detail_data)
        return True

def save_detail_list(year, all_detail_data):

    # 데이터 저장
    file_path=f'{home_path}/code/movdata/data/movies_detail/year={year}/data.json'
    # 경로에 디렉토리 없으면 생성한 후 json으로 저장
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "2", encoding='utf-8') as f:
        json.dump(all_detial_dat, f, indent=4, ensure_ascii=False)

def get_detail_data(movieCd):
    # API 호출해서 movieCd 데이터를 가져옴
    url_base = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={MOVIE_API_KEY}"
    r = url_base + "&movieCd={movieCd}"
    # movieCd 데이터 sjon으로 추출
    req_data = requests.get(r).json()
    return req_data
