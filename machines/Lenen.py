import streamlit as st
from display import tjz
from display import zentz

def Lenen():
    st.title("L炎炎ノ消防隊")
    st.write("狙い目はすべて液晶のG数")
    st.write("台の仕様上、正確な当選G数をデータから完全に把握することが難しいため、保守的に狙い目を設定しています。")
    morning = st.checkbox("朝一リセット", value=False)
    thru = st.slider("スルー回数", 0,3,0,1,help="4以上の場合は3を選択でOK")

    if morning:
        if thru == 0:
            g = 400
            z1 = 65
            z2 = 88
        elif thru == 1:
            g = 580
            z1 = 75
            z2 = 88
        elif thru == 2:
            g = 580
            z1 = 70
            z2 = 88
        else:
            g = 590
            z1 = 70
            z2 = 88
        with st.container(border=True):
            tjz(g)
            tjz(z1=z1,z2=z2)
        
    else:
        if thru == 0:
            g = 600
            z1 = 65
            z2 = 88
        elif thru == 1 or thru == 2:
            g = 540
            z1 = 65
            z2 = 88
        else:
            g = 570
            z1 = 65
            z2 = 88
        with st.container(border=True):
            tjz(g)
            tjz(z1=z1,z2=z2)
        
    st.subheader("炎炎激闘間天井狙い")
    with st.container(border=True):
        tjz(t=2300,ttext="炎炎ループ間")

    st.subheader("やめどき")
    st.write("ボナ後・ST後にはストックがあっても一度通常時に戻ります。即ヤメしないようにしましょう。")
    st.write("初当たりRB後は伝導者の影を消化してやめ")
    st.write("ST後・ボーナス後は潜伏を確認してやめ（30~40Gくらい？)")
    st.write("終了画面が「119」（ワンワンニャイン）の場合は天国まで打ってやめ")
    
    st.divider()
    st.caption("L炎炎ノ消防隊jG、AT、ボーナス天井850G+α AT天井2500G+α、純増5枚/G")

