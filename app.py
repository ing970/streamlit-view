import streamlit as st
import pandas as pd
import numpy as np

# 타이틀 적용 예시
st.title("SeokMin_Streamlit :rocket:")

# 특수 이모티콘 삽입 예시
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
# Header 적용
st.header("1. 텍스트 입력 sample")
st.subheader("헤더를 입력할 수 있어요! :sparkles:")

# Subheader 적용
st.subheader("이것은 subheader 입니다.")

# 캡션 적용         
st.caption("캡션을 한 번 넣어 봤습니다.")

# 코드 표시
sample_code = '''
def function():
    print("hello, world")
'''
st.code(sample_code, language = "python")

# 일반 택스트
st.text("일반적인 텍스트를 입력해 보았습니다.")

# 마크다운 문법 지원
st.markdown("streamlit은 **마크다운 문법을 지원** 합니다.")
# 컬러코드: blue, green, orange, red, violet
st.markdown("택스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼트체로 설정할 수 있습니다.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] 와 같이 latex 문법의 수식 표현도 가능합니다. :pencil:")

# LaTex 수식 지원
st.latex(r'\sqrt{x^2+y^2}=1')

st.subheader("2. 데이터프레임 튜토리얼")

# DataFrame 생성
dataframe = pd.DataFrame({
    'firtst column': [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
})
st.dataframe(dataframe, use_container_width = True)

# 테이블(static)
# DataFrame과는 다르게 interactive 한 UI 를 제공하지 않습니다.
st.table(dataframe) # 단순히 데이터를 조회할 때 사용한다.

# 메트릭
st.metric(label = "온도", value = "10℃", delta = "1.2℃")
st.metric(label = "삼성전자", value = "61,000 원", delta = "-1,200 원")

# 컬럼으로 영역을 나누어 표기한 경우
col1, col2, col3, = st.columns(3)
col1.metric(label = "달러USD", value = "1,228 원", delta = "-12.00 원")
col2.metric(label = "일본JPY(100엔)", value = "958.63 원", delta = "-7.44 원")
col3.metric(label = "유럽연합EUR", value = "1,335.82 원", delta = "11.44 원")