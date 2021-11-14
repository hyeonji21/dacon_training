## 따릉이 대여량 예측 경진대회 EDA

# 필요한 library 불러오기
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# 데이터 불러오기
bicycle = pd.read_csv('dacon_bicycle/train.csv')
bicycle.head()

# 결측치 확인
def check_missing_col(dataframe):
    counted_missing_col = 0
    for i,col in enumerate(bicycle.columns):
        missing_values = sum(bicycle[col].isna())
        is_missing = True if missing_values >= 1 else False
        if is_missing:
            counted_missing_col += 1
            print('결측치가 있는 컬럼은: {col}입니다')
            print('총 {missing_values}개의 결측치가 존재합니다.')

        if i == len(bicycle.columns) - 1 and counted_missing_col == 0:
            print('결측치가 존재하지 않습니다')
check_missing_col(bicycle)

# date_time 날짜 처리
# 년,월,일로 나눔

def seperate_datetime(dataframe):
    year=[]
    month=[]
    day=[]

    for date in dataframe.date_time:
        year_point, month_point, day_point=date.split('-')
                                    # - 기준으로 string을 나누고 list로 만듦
                                    # ex) '2016-04-01' => ['2016', '04', '01']
        year.append(int(year_point))
        month.append(int(month_point))
        day.append(int(month_point))
    return year, month, day

    year,month,day = seperate_datetime(bicycle)

    bicycle['year']=year
    bicycle['month']=month
    bicycle['day']=day

bicycle.head()

# 데이터 기초 통계 분석
data_description = bicycle.describe()
data_description

# 데이터 분포 확인
# 히스토그램
# ex) wind_direction => 평균 202.75, 가장 분포가 많이 되어있는 값 : 200-250
#     남서풍이 가장 많이 부는 시기 : 4, 5, 6월 .. 월을 유추할 수 있을 것임.
bicycle.columns
interest_coloumns = ['wind_direction', 'sky_condition', 'precipitation_form',
                     'wind_speed', 'humidity', 'low_temp', 'high_temp',
                     'Precipitation_Probability', 'number_of_rentals']
plt.style.use('fivethirtyeight')
fig,ax = plt.subplots(3, 3, figsize=(20, 20))
fig.suptitle('Histogram of interesting feautres', fontsize=40)

column_idx = 0
for i in range(3):
    for j in range(3):
        ax[i][j].hist(bicycle[interest_coloumns[column_idx]], bins=30, color='#eaa18a',
        edgecolor='#7bcabf')
        ax[i][j].set_title(interest_coloumns[column_idx])
        ax[i][j].axvline(data_description[interest_coloumns[column_idx]]['mean'], c='#f55354',
                         label=f"mean = {round(data_description[interest_coloumns[column_idx]]['mean'], 2)}")
        ax[i][j].axvline(data_description[interest_coloumns[column_idx]]['50%'], c='#518d7d',
                         label=f"median = {round(data_description[interest_coloumns[column_idx]]['50%'], 2)}")
        ax[i][j].legend()
        column_idx += 1

# 요일 표시하기 (앞서 만든 날짜데이터에 요일 추가)
week_day = pd.to_datetime(bicycle['date_time']).dt.day_name()
bicycle['week_day'] = week_day
bicycle.head()

# 상관관계 확인
bicycle_number = bicycle.select_dtypes(np.number)
# 상관분석은 숫자로 계산할 수 있으므로 데이터에서 숫자로 이루어진 컬럼만을 뽑는다.
# 우리가 관심 있는 것 : 따릉이 대여량(number_of_rentals)와 어떤 컬럼이 가장 상관관계가 높은지?
# : years가 가장 높은 상관관계가 있는 것으로 나타남. -> 시간이 지날수록 따릉이 가입수가 늘어났기 때문.
corr = bicycle_number.corr()
plt.figure(figsize=(20,10))
ax = sns.heatmap(
    corr,
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True,
    annot=True
)

ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
)

plt.title('Correlation heatmap', fontsize=30)
plt.show()