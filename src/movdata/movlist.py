import requests
import os
import json
import time #API를 너무 빨리 호출하면 에러발생 -> sleep 필요
from tqdm import tqdm
import shutil 

API_KEY = os.getenv('MOVIE_API_KEY')


def save_json(data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    # exist_okf=True 디렉토리가 있으면 skip하는 옵션
    with open(file_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    pass

    # 파일 저장 경로 mkdir 
def req(url):
    r = requests.get(url)
    j = r.json()
    return j

def save_movies(start_year=2015, end_year=2024, per_page=10, sleep_time=1):
    file_path = f'/home/hahahellooo/data/movies/year={year}/data.json'
    for year in range(start_year, end_year+1):
        if os.exists(file_path):
            print(f"데이터가 이미 존재합니다: {file_path}")
        else:
            pass

    # 위 경로가 있으면 API 호출을 멈추고  프로그램 종료
    # totCnt  가져오고 total_pages 계산
    url_base = f"https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key={API_KEY}&openStartDt={year}&openEndDt={year}"
    r = req(url_base + "&curPage=1")
    tot_cnt = r['movieListResult']['totCnt']
    total_pages = (tot_cnt // per_page) + 1
    # total_pages 만큼 loop 돌면서 API 호출
    all_data=[]

    for page in range(1, total_pages + 1):
        time.sleep(sleep_time)
        r = req(url_base + f"&curPage={page}")
        d = r['movieListResult']['movieList']
        all_data.extend(d)

    save_json(all_data, file_path)
    return True

