import numpy as np
import pandas as pd

#-*- coding: utf-8 -*-

# 데이터 불러오기 _ 가로등 관련 공공 데이터
d2 =pd.read_csv("C:/Users/0105l/Desktop/pycham/KU_data/data1.csv", encoding='CP949')
d2.head()
d2.info()

d2[d2["소재지지번주소"].str.contains("조치원읍")]
# 하지만 "조치원읍" 주소가 존재하지 않아서 불가

pd.DataFrame(d2['소재지지번주소'].value_counts())


# 필요한 column -> dataframe 생성
light = pd.DataFrame(d2, columns=['소재지도로명주소', '소재지지번주소', '카메라대수', '위도', '경도', '데이터기준일자'])
light

# ----------------------------------------------------------------------------------

# 세종특별자치시 cctv 데이터 불러오기
d1 = pd.read_csv("C:/Users/0105l/Desktop/pycham/KU_data/cctv_data.csv", encoding='CP949')
d1.head()
d1.info()

# 조치원읍 cctv 현황 확인
cctv = d1[d1["소재지지번주소"].notnull() & d1["소재지지번주소"].str.contains("조치원읍")]

# 각종 column 확인
cctv['소재지지번주소']
cctv['설치목적구분']

pd.DataFrame(cctv['소재지지번주소'].value_counts())
pd.DataFrame(cctv['설치목적구분'].value_counts())
pd.DataFrame(cctv['카메라대수'].value_counts())

# 필요한 column -> dataframe 생성 1
cctv2 = pd.DataFrame(cctv, columns=['소재지지번주소', '카메라대수', '위도', '경도', '데이터기준일자'])

cctv2_1 = cctv2[cctv2['소재지지번주소'].str.contains("조치원읍")]
cctv2_1

# 필요한 column -> dataframe 생성2
cctv2_1.value_counts().sort_index()

new = pd.DataFrame(cctv2_1['소재지지번주소'].value_counts().sort_index())
new

df = pd.DataFrame.from_dict(new)
df
# 새로 만든 데이터 저장하기
df.to_csv('C:/Users/0105l/Desktop/pycham/KU_data/cho_new_data.csv', encoding='CP949')

# cctv 빈도수
describe = new.describe()
describe


# cctv 지도 표시
import folium as g
from pandas import DataFrame  #데이터 분석 패키지
from pandas import ExcelFile  #엑셀파일 가져오기

sejong_map = g.Map(location=[36.6, 126.98],
                   tiles='Stamen Terrain',
                   zoom_start=12)
sejong_map

for i in range(len(cctv2)):
    marker01 = g.Marker([cctv2.loc[i]['위도'], cctv2.loc[i]['경도']],
                        popup = cctv2.loc[i]['소재지지번주소'],
                        icon = g.Icon(color='blue')).add_to(sejong_map)
sejong_map.save('map.html')


# light 지도 표시 추가
sejong_light_map = g.Map(location=[36.6, 126.98],
                   tiles='Stamen Terrain',
                   zoom_start=12)
sejong_light_map

for i in range(len(d2)):
    marker01 = g.Marker([d2.loc[i]['위도'], d2.loc[i]['경도']],
                        popup = d2.loc[i]['소재지지번주소'],
                        icon = g.Icon(color='pink')).add_to(sejong_light_map)
sejong_light_map.save('light_map.html')


# 조치원읍만 따로 빼낸 csv파일
new_new_data =pd.read_csv("C:/Users/0105l/Desktop/pycham/KU_data/cho_new_data.csv", encoding='CP949')
new_new_data.head()
new_new_data.info()

# 컬럼 이름 변경 (이미 컬럼이 있으므로 이름만 변경할 것)
new_new_data.columns = ['조치원읍 지번', 'cctv']
new_new_data

# 지번별 cctv 개수 데이터프레임
count = pd.DataFrame(new_new_data.value_counts().sort_index())
count

# plot 그리기
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

count.plot(by='cctv', kind='bar', title='조치원 지번별 cctv')


# 파이차트 그리기  (x)
#count_list = count.values.tolist()

#plt.pie(count_list, shadow=True, autopct='%0.1f%%')
#plt.show()

# ------------------------------------------------------------------------------------

### 전국 스마트 가로등 표준데이터
d3 = pd.read_csv("C:/Users/0105l/Desktop/pycham/KU_data/smart_light_data.csv", encoding='CP949')
d3.info()
pd.DataFrame(d3["시도명"].value_counts())
pd.DataFrame(d3["시군구명"].value_counts())

# 충청북도 데이터 불러오기
smart_light_north = d3[d3["시도명"].str.contains("충청북도")]
smart_light_north
smart_light_north["시군구명"].value_counts()


# 충청남도 데이터 불러오기
smart_light_south = d3[d3["시도명"].str.contains("충청남도")]
smart_light_south
smart_light_south["시군구명"].value_counts()


# 세종에 대한 데이터는 없음.
# d3[d3["시군구명"].str.contains("세종")]  # empty


# 전라북도 데이터 불러오기
smart_light_g = d3[d3["시도명"].str.contains("전라북도")]
smart_light_g
smart_light_g["시군구명"].value_counts()


# 전라남도 데이터 불러오기
smart_light_g1 = d3[d3["시도명"].str.contains("전라남도")]
smart_light_g1
smart_light_g1["시군구명"].value_counts()


# 경기도 데이터 불러오기
smart_light_gyeongi = d3[d3["시도명"].str.contains("경기도")]
smart_light_gyeongi
smart_light_gyeongi["시군구명"].value_counts()

# 서울특별시 데이터 불러오기
smart_light_gyeongi = d3[d3["시도명"].str.contains("경기도")]
smart_light_gyeongi
smart_light_gyeongi["시군구명"].value_counts()


# -------------------------------------------------------------------

# 전국 cctv 설치 운영 현황
all_cctv = pd.read_csv("C:/Users/0105l/Desktop/pycham/KU_data/all_cctv_.csv", encoding='CP949')
all_cctv

all_cctv.info()

# 열 삭제
all_cctv.drop(['구분(1)'], axis=1, inplace=True)
# or all_cctv.drop(['구분(1)'], axis='columns', inplace=True)
# axis=1 또는 0으로 지정 / inplace=True일 경우 현재 데이터에 그대로 반영

all_cctv.info()

# 컬럼명 바꾸기
all_cctv.rename(columns={'구분(2)':'지역', '2014':'전체 사업체(개)', '2014.1':'CCTV 설치/운영 사업체 수(개)','2014.2':'CCTV 설치/운영 사업체 비율(%)','2014.3':'CCTV 미설치/미운영 사업체 수(개)','2014.4':'CCTV 미설치/미운영 사업체 비율(%)','2014.5':'CCTV 설치/운영'}, inplace=True)
all_cctv.info()

# 필요없는 행, 열 삭제하기
all_cctv['구분(3)']
all_cctv.drop(['구분(3)'], axis=1, inplace=True) # 열 삭제
all_cctv.info()

all_cctv.drop(index=0, axis=0, inplace=True) # 행 삭제
all_cctv.drop(index=1, axis=0, inplace=True)


# 필요한 데이터프레임 만들기
need_all_cctv_df = all_cctv[['지역', 'CCTV 설치/운영']][0:17]
need_all_cctv_df.head(17)

# plot 그리기
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 데이터 타입 바꾸기
need_all_cctv_df.info()
need_all_cctv_df.dtypes
need_all_cctv_df1 = need_all_cctv_df.astype({'지역':str, 'CCTV 설치/운영':int})
need_all_cctv_df1.dtypes
need_all_cctv_df1

plt.ylim([0, 20000000])
need_all_cctv_df1.plot(x='지역', y='CCTV 설치/운영', kind='bar',title='전국 cctv 현황', color='red')
plt.show()

# -------------------------------------------------------------------
import pandas as pd
import numpy as np

# 야간_보행의_안전도_및_야간_보행이_불안한_이유__13세_이상_인구__20210929202615 data
night_walking = pd.read_csv("C:/Users/0105l/Desktop/pycham/KU_data/night_walking.csv", encoding='CP949')
night_walking
night_walking.info
night_walking.columns

# 첫번째 행을 칼럼명으로 바꾸기
header = night_walking.iloc[0]
night_walking1 = night_walking[1:]
night_walking1

night_walking1.rename(columns=header, inplace=True)
night_walking1
night_walking1.columns

# 전국 x / 세종특별자치시만 뽑아내기
night_walking1 = night_walking1[night_walking1["행정구역(시도)별(1)"].str.contains("세종특별자치시")]
night_walking1.columns

# 원하는 컬럼명으로 바꾸기
night_walking1.rename(columns={'행정구역(시도)별(1)':'시도별'}, inplace=True)
night_walking1.rename(columns={' -불안 이유: 생활권 내에 CCTV 등 야간 보행 안전 시설 부족':'안전 시설 부족'}, inplace=True)
night_walking1.rename(columns={' -불안 이유: 생활권 내에 경찰서 등 치안 시설 부족':'치안 시설 부족'}, inplace=True)
night_walking1.rename(columns={' -불안 이유: 생활권 내에는 야간에 인적이 드묾':'인적 드묾'}, inplace=True)
night_walking1.rename(columns={' -불안 이유: 생활권 내에 우범 지역 존재':'우범 지역 존재'}, inplace=True)
night_walking1.rename(columns={' -불안 이유: 신문·뉴스 등에서 사건 사고를 자주 접함':'사건 사고 자주 접함'}, inplace=True)
night_walking1.rename(columns={' -불안 이유: 기타':'기타'}, inplace=True)

night_walking1
night_walking1.info()

# 필요한 column -> dataframe 생성
night_walking1_five_df = pd.DataFrame(night_walking1, columns=['매우 안전', '비교적 안전', '약간 불안', '매우 불안'])
night_walking1_five_df


# 차트 종류, 제목, 차트 크기, 범례, 폰트 크기 설정

# cctv 전체/남/여 생각 비교 plot1
# 데이터 종류 변경
night_walking1_five_df = night_walking1_five_df.astype({'매우 안전':float, '비교적 안전':float, '약간 불안':float, '매우 불안':float})
night_walking1_five_df.dtypes

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

night_walking1_five_df.rename(index={60:'전체'}, inplace=True)
night_walking1_five_df.rename(index={61:'남자'}, inplace=True)
night_walking1_five_df.rename(index={62:'여자'}, inplace=True)

# (쓰기에 부적합) ax = night_walking1_five_df.plot(kind='bar', title='야간보행 안전도에 대한 생각 (전체/남/여)', figsize=(12, 4), fontsize=12, subplots=True)
ax2 = night_walking1_five_df.plot(kind='bar', title='야간보행 안전도에 대한 생각 (전체/남/여)')

night_walking1_five_df
night_walking1.info()


# 필요한 column -> dataframe 생성
night_walking_reason_df = pd.DataFrame(night_walking1, columns=['안전 시설 부족', '치안 시설 부족', '인적 드묾',
                                                                '우범 지역 존재', '사건 사고 자주 접함'])
night_walking_reason_df

# 야간보행이 불안한 이유 plot
# 데이터 종류 변경
night_walking_reason_df1 = night_walking_reason_df.astype({'안전 시설 부족':float, '치안 시설 부족':float, '인적 드묾':float, '우범 지역 존재':float,
                                                           '사건 사고 자주 접함':float})
night_walking_reason_df1.dtypes

night_walking_reason_df1.rename(index={60:'전체(세종시)'}, inplace=True)
night_walking_reason_df1.rename(index={61:'남자(세종시)'}, inplace=True)
night_walking_reason_df1.rename(index={62:'여자(세종시)'}, inplace=True)

night_walking_reason_df1.rename(index={'전체(세종시)':'전체'}, inplace=True)
night_walking_reason_df1.rename(index={'남자(세종시)':'남자'}, inplace=True)
night_walking_reason_df1.rename(index={'여자(세종시)':'여자'}, inplace=True)

night_walking_reason_df1

ax3 = night_walking_reason_df1.plot(kind='bar', title='야간보행이 불안한 이유 (세종)', fontsize=12)


# -------------------------------------------------------------------
# <야간_보행에_대한_안전도_시도__20210929202442.csv> 데이터

night_walking_safe = pd.read_csv("C:/Users/0105l/Desktop/pycham/KU_data/night_walking_safe.csv", encoding='CP949')
night_walking_safe
night_walking_safe.columns
night_walking_safe.info()
night_walking_safe.head(10)

# 첫번째 행을 칼럼명으로 바꾸기
header = night_walking_safe.iloc[0]
night_walking_safe1 = night_walking_safe[1:]
night_walking_safe1

night_walking_safe1.rename(columns=header, inplace=True)
night_walking_safe1
night_walking_safe1.columns

# 원하는 컬럼명으로 바꾸기
night_walking_safe1.rename(columns={'행정구역별(1)':'행정구역별'}, inplace=True)
night_walking_safe1.rename(columns={'혼자 걷기 두려운 이유-가로등이 없어서':'가로등이 없어서'}, inplace=True)
night_walking_safe1.rename(columns={'혼자 걷기 두려운 이유-우범지역이므로':'우범지역이므로'}, inplace=True)
night_walking_safe1.rename(columns={'혼자 걷기 두려운 이유-인적이 드물어서':'인적 드묾'}, inplace=True)
night_walking_safe1.rename(columns={'혼자 걷기 두려운 이유-CCTV가 없어서':'CCTV가 없어서'}, inplace=True)
night_walking_safe1.rename(columns={'혼자 걷기 두려운 이유-기타':'기타'}, inplace=True)


# 필요없는 행, 열 삭제하기
night_walking_safe1['계']
night_walking_safe1.drop(['계'], axis=1, inplace=True) # 열 삭제
night_walking_safe1.info()

night_walking_safe1['소계']
night_walking_safe1.drop(['소계'], axis=1, inplace=True) # 열 삭제
night_walking_safe1.info()


# 필요한 column -> dataframe 생성
night_walking_safe1_df = pd.DataFrame(night_walking_safe1, columns=['행정구역별', '두려운 곳이 있다', '두려운 곳이 없다'])
night_walking_safe1_df.info()
# plot 그리기
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 데이터 타입 바꾸기
night_walking_safe1_df.dtypes

night_walking_safe1_df = night_walking_safe1_df.astype({'행정구역별':str, '두려운 곳이 있다':float, '두려운 곳이 없다':float})
night_walking_safe1_df.dtypes

ax4 = night_walking_safe1_df.plot(x='행정구역별', y=['두려운 곳이 있다', '두려운 곳이 없다'], kind='bar',title='행정구역별 야간보행 두려운 정도', alpha=0.5)
plt.show()

ax5 = night_walking_safe1_df.plot(x='행정구역별', y='두려운 곳이 있다', kind='bar',title='행정구역별 야간보행 두려운 정도1', color='pink', alpha=0.6)
plt.show()

ax6 = night_walking_safe1_df.plot(x='행정구역별', y='두려운 곳이 없다', kind='bar',title='행정구역별 야간보행 두려운 정도2', alpha=0.6)
plt.show()


# 필요한 column -> dataframe 생성  &  plot 그리기
night_walking_safe1.info()

# 데이터 타입 바꾸기
night_walking_safe1 = night_walking_safe1.astype({'행정구역별':str, '가로등이 없어서':float, '우범지역이므로':float,
                                                  '인적 드묾':float, 'CCTV가 없어서':float})
night_walking_safe1.dtypes


df2 = pd.DataFrame(night_walking_safe1, columns=['행정구역별', '가로등이 없어서'])
df2
df2_ax = df2.plot(x='행정구역별', y='가로등이 없어서', kind='bar',title='행정구역별 야간보행이 두려운 이유1', alpha=0.6)
df2_ax

df3 = pd.DataFrame(night_walking_safe1, columns=['행정구역별', '우범지역이므로'])
df3_ax = df3.plot(x='행정구역별', y='우범지역이므로', kind='bar',title='행정구역별 야간보행이 두려운 이유2', alpha=0.6, color='navy')

df4 = pd.DataFrame(night_walking_safe1, columns=['행정구역별', '인적 드묾'])
df4_ax = df4.plot(x='행정구역별', y='인적 드묾', kind='bar',title='행정구역별 야간보행이 두려운 이유3', alpha=0.6, color='purple')

df5 = pd.DataFrame(night_walking_safe1, columns=['행정구역별', 'CCTV가 없어서'])
df5_ax = df5.plot(x='행정구역별', y='CCTV가 없어서', kind='bar',title='행정구역별 야간보행이 두려운 이유4', alpha=0.6, color='gray')


# 세종 지역만 따로 빼서 확인해보기 (야간보행이 두려운 이유)
night_walking_safe_sejong = night_walking_safe1[night_walking_safe1["행정구역별"].str.contains("세종")]
night_walking_safe_sejong.columns

night_walking_safe_sejong.drop(['기타'], axis=1, inplace=True) # 열 삭제
night_walking_safe_sejong.drop(['특성별(1)', '특성별(2)', '두려운 곳이 있다', '두려운 곳이 없다'], axis=1, inplace=True) # 열 삭제

night_walking_safe_sejong.info()

# plot
sejong_ax = night_walking_safe_sejong.plot(x='행정구역별', y=['가로등이 없어서', '우범지역이므로', '인적 드묾', 'CCTV가 없어서'], kind='pie',title='세종시 야간보행이 두려운 이유', alpha=0.6)

labels = ['가로등이 없어서', '우범지역이므로', '인적 드묾', 'CCTV가 없어서']

# 원그래프 실패
# sejong_ax = night_walking_safe_sejong.plot(x='행정구역별', y=labels, kind='pie',title='세종시 야간보행이 두려운 이유', alpha=0.6)