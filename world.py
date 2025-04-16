import streamlit as st
import geopandas as gpd
import pandas as pd
import plotly.express as px

# 국가 정보 DataFrame 생성
data = {
    'country': ['대한민국', '미국', '프랑스', '일본', '영국', '독일', '중국', '인도'],
    'capital': ['서울', '워싱턴 D.C.', '파리', '도쿄', '런던', '베를린', '베이징', '뉴델리'],
    'population': [51780579, 331002651, 65273511, 126476461, 67886011, 83783942, 1439323776, 1380004385],
    'languages': ['한국어', '영어', '프랑스어', '일본어', '영어', '독일어', '중국어', '힌디어']
}

country_info = pd.DataFrame(data)

# Streamlit 앱 제목
st.title("세계 지도 국가 선택기")

# 세계 지도 데이터 로드
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plotly로 세계지도 그리기
fig = px.choropleth(world,
                     locations='name',
                     geojson=world.geometry,
                     hover_name='name',
                     title='세계 각국 선택하기')

fig.update_geos(fitbounds="locations", visible=False)

# Streamlit에서 지도 표시
st.plotly_chart(fig)

# 국가 선택
selected_country = st.selectbox("국가를 선택하세요:", country_info['country'])

# 선택된 국가 정보 표시
if selected_country:
    capital = country_info[country_info['country'] == selected_country]['capital'].values[0]
    population = country_info[country_info['country'] == selected_country]['population'].values[0]
    languages = country_info[country_info['country'] == selected_country]['languages'].values[0]

    st.subheader(f"{selected_country} 정보")
    st.write(f"수도: {capital}")
    st.write(f"인구: {population}명")
    st.write(f"사용 언어: {languages}")

