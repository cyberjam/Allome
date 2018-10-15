#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import csv
import pandas as pd

#url = "http://www.eatsight.com/portal/searchDetail/result"
result = '{'
for fudId in range(10051312,10051323):
	print("----------------------------------------- <JSON> ---------------------------------------------------")
	print("-------------------------------------- fudId : "+str(fudId)+"------------------------------------------------")
	data = {
		'query':{
			'fudId' : fudId,
			#'fudNm' : '비빙수'
		}
	}
	headers = {'Content-Type': 'application/json; charset=utf-8'} #post 전송방식이기 때문에 header 필요

	req = requests.post('http://www.eatsight.com/portal/searchDetail/result', data =json.dumps(data),headers=headers)

	#print("POST 주소확인 : " + req.url )
	html = req.text
	print(html)
	#print("상태코드 : " , req.status_code,"\n")
	
	

	result=result+'\"pdt_'+str(fudId)+'\":'+html+',' #datafram에 넣기 위한 전처리
	print('\n')
	
result = result + '}'
with open("JsonTest.json", "w") as outfile: #json 파일로 저장
		json.dump(result, outfile)
		
print("----------------------------------------- <JSON END> ---------------------------------------------------\n")
print("---------------------------------------- <DataFrame> ---------------------------------------------------")
df=pd.read_json(result, orient='index')
df.mta06 = df.mta06.str.replace('\n', '')# csv 변환을 위한 전처리: \n 제거
print(df)
print("-------------------------------------- <CSV> ------------------------------------------------")
print(df.to_csv())

df.to_csv("csvTest.csv", mode='w',sep=',',header = True, na_rep='NaN')



#----------------------------------------참고-----------------------------------------------------

# - 크롤링
# 참고 : https://dgkim5360.tistory.com/entry/python-requests // POST, 헤더 추가
# http://docs.python-requests.org/en/master/user/quickstart/
# 선용이형 json을 받을 수 있도록 도와준 1등 공신 최고!

# - 전처리
#아래는 json -> dataframe -> csv 
#https://stackoverflow.com/questions/1871524/how-can-i-convert-json-to-csv# //df 아이디어 
#https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_json.html //json -> dataframe예시
#https://docs.python.org/3/library/csv.html //dataframe -> csv 예시

#https://www.lesstif.com/pages/viewpage.action?pageId=54952504 //엘셀CSV 열기 깨짐문제

#https://stackoverflow.com/questions/34550120/pandas-escape-carriage-return-in-to-csv //df->to_csv \n 전처리
