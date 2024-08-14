import streamlit as st
from display import tjz

def monkeyv():
    st.header("スマスロ　モンキーターンV")
    st.markdown("""
            <style>
            .big-font{
                font-size:50px !important;
                background: linear-gradient(to right,#e60000,#f39800,#fff100,#009944,#0068b7,#1d2088,#920783);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: bold;
                display: inline-block;
            }
            </style>
            """, unsafe_allow_html=True)
    morning = st.checkbox("朝一リセット", value=False)
    reduce = st.checkbox("天井短縮", value=False, help="波多野vs青島敗北後と上位AT後は天井短縮")
    if morning:
        shuki = st.radio("何周期目？", options=("1", "2", "3以上"))
        if shuki == "1":
            with st.container(border=True):
                st.subheader("ゾーン狙い 40G~優出まで")
        elif shuki == "2":
            with st.container(border=True):
                tjz(150)
        else:
            with st.container(border=True):
                st.markdown('<p class="big-font">ツッパ</p>',unsafe_allow_html=True)
    
    else:
        if reduce:
            with st.container(border=True):
                tjz(150)
        else:
            with st.container(border=True):
                tjz(410)
                st.caption("上記を基準に優出ptsや示唆で押し引き")

    st.divider()
    st.caption("Lモンキーターン5 CE、AT、下位純増2.5枚/G 上位純増4枚/G、天井795G+α or 6周期目、リセット時・青島バトル敗北後・上位AT終了後は495+α or 4周期目")