import streamlit as st

def monkeyv():
    st.header("スマスロ　モンキーターンV")
    morning = st.checkbox("朝一リセット", value=False)
    reduce = st.checkbox("天井短縮", value=False, help="波多野vs青島敗北後と上位AT後は天井短縮")
    if morning:
        shuki = st.radio("何周期目？", options=("1", "2", "3以上"))
        if shuki == "1":
            st.subheader("データカウンター 40G~優出まで、スルー時は2周期目のボーダーで押し引き")
        elif shuki == "2":
            st.subheader("データカウンター 150G～天井まで")
        else:
            st.subheader("ツッパ")
    
    else:
        if reduce:
            st.subheader("データカウンター 150G～天井まで")
        else:
            st.subheader("データカウンター 410G～を基準に優出ptsや示唆で押し引き")

    st.divider()
    st.caption("Lモンキーターン5 CE、AT、下位純増2.5枚/G 上位純増4枚/G、天井795G+α or 6周期目、リセット時・青島バトル敗北後・上位AT終了後は495+α or 4周期目")