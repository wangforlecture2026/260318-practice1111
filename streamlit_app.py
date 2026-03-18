import streamlit as st
import pandas as pd
import numpy as np
import time
st.title("🎈 Streamlit 기본 요소 예시 페이지")

st.markdown("이 페이지는 Streamlit의 주요 기본 요소들을 보여줍니다. 각 요소를 시연하고 설명합니다.")

# 텍스트 요소
st.header("1. 텍스트 요소")
st.subheader("제목과 부제목")
st.text("일반 텍스트입니다.")
st.markdown("**마크다운**을 사용할 수 있습니다. *이탤릭*, `코드` 등.")
st.write("st.write()는 다양한 타입의 데이터를 출력할 수 있습니다:", 123, [1, 2, 3])

# 입력 위젯
st.header("2. 입력 위젯")
col1, col2 = st.columns(2)

with col1:
    st.subheader("버튼과 체크박스")
    if st.button("클릭하세요"):
        st.success("버튼이 클릭되었습니다!")
    agree = st.checkbox("동의합니다")
    if agree:
        st.write("동의하셨습니다.")

with col2:
    st.subheader("라디오와 셀렉트박스")
    genre = st.radio("좋아하는 장르를 선택하세요", ("코미디", "드라마", "액션"))
    option = st.selectbox("옵션을 선택하세요", ("옵션 1", "옵션 2", "옵션 3"))

st.subheader("슬라이더와 숫자 입력")
age = st.slider("나이를 선택하세요", 0, 100, 25)
number = st.number_input("숫자를 입력하세요", min_value=0.0, max_value=100.0, value=50.0)

st.subheader("텍스트 입력")
name = st.text_input("이름을 입력하세요", "홍길동")
message = st.text_area("메시지를 입력하세요", "여기에 메시지를 작성하세요...")

# 데이터 표시
st.header("3. 데이터 표시")
st.subheader("데이터프레임")
df = pd.DataFrame({
    '이름': ['Alice', 'Bob', 'Charlie'],
    '나이': [25, 30, 35],
    '점수': [85, 90, 95]
})
st.dataframe(df)

st.subheader("테이블")
st.table(df)

st.subheader("메트릭")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("온도", "70 °F", "1.2 °F")
with col2:
    st.metric("습도", "86%", "-8%")
with col3:
    st.metric("압력", "30.4 inHg", "0.5 inHg")

# 미디어
st.header("4. 미디어")
st.subheader("이미지")
st.image("https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", caption="Streamlit 로고")

# 프로그레스와 스피너
st.header("5. 프로그레스와 스피너")
st.subheader("프로그레스 바")
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)
st.success("완료되었습니다!")

st.subheader("스피너")
with st.spinner("처리 중..."):
    time.sleep(2)
st.success("처리가 완료되었습니다!")

# 메시지
st.header("6. 메시지")
st.success("성공 메시지")
st.info("정보 메시지")
st.warning("경고 메시지")
st.error("에러 메시지")

# 사이드바
st.sidebar.header("사이드바")
st.sidebar.write("이것은 사이드바입니다.")
sidebar_option = st.sidebar.selectbox("사이드바 옵션", ["옵션 A", "옵션 B", "옵션 C"])

# 익스팬더
st.header("7. 익스팬더")
with st.expander("더 자세한 정보 보기"):
    st.write("여기에 추가 정보를 넣을 수 있습니다.")
    st.image("https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png")

# 풍선과 눈
st.header("8. 재미 요소")
if st.button("풍선 터뜨리기"):
    st.balloons()
if st.button("눈 내리기"):
    st.snow()

st.markdown("---")
st.write("더 많은 요소와 기능을 확인하려면 [Streamlit 문서](https://docs.streamlit.io/)를 방문하세요!")
