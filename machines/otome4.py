import streamlit as st
from display import tjz
from display import zentz

def otome4():
    st.title("スマスロ 戦国乙女4 戦乱に閃く炯眼の軍師")
    st.write("この台は仕様上実践値が出せません。参考程度に考えてください。")
    thru = st.slider("ボーナススルー回数",0,6,0,1)
    if thru ==0:
        g = 410
        z1 = 65
        z2 = 100
    elif thru>0 and thru<5:
        g = 470
        z1 = 220
        z2 = 250
        zz1 = 290
        zz2 = 350
    elif thru == 5:
        g = 50
    else:
        g = 0
    
    miko = st.selectbox("巫女ポイント", ["600pt以上","300~599pt", "200pt以下"])
    if miko == "200pt以下":
        g = g - 20
    elif miko == "600pt以上":
        g = g + 20

    with st.container(border=True):
        if thru ==0:
            tjz(g)
            tjz(z1=z1,z2=z2)
        elif thru>0 and thru<5:
            tjz(g)
            tjz(z1=z1,z2=z2)
            tjz(z1=zz1,z2=zz2)
        else:
            tjz(g)
    
    st.subheader("やめどき")
    st.write("・ボーナス終了時はボタンプッシュで示唆を見てから判断")
    st.write("・AT後は引き戻しを確認してやめ、エンディング後と有利差枚+2000枚以上は天国まで確認")

    st.divider()
    st.caption("L戦国乙女4S3、AT、天井799G+α ボーナス6スルー、純増2.5枚/G or 5枚/G")
    
