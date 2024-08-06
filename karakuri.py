import streamlit as st
from display import tjz
from display import zentz

def karakuri():
    st.title("L からくりサーカス")
    st.write("狙い目はすべて液晶右下のG数です")
    morning = st.checkbox("朝一リセット", value=False)
    thru = st.slider("CZスルー回数", 0,4,0,1, help="データカウンター上で直近にRBが連続している回数。10G以内のRBはカウントしない")
    if morning:
        if thru == 0:
            g = 560
        elif thru == 1:
            g = 530
        elif thru == 2:
            g = 210

        if g:
            tjz(g)
        else:
            zentz()

    else:
        st.write("細かい狙い目調整要素（分かれば入力）")
        prev_mode = st.selectbox("前回モード",['A','B','C','天国'] )
        yuri_atama = st.checkbox("現在有利区間頭", value=True)
        if yuri_atama:
            samai_disable = True
        else:
            samai_disable = False
        samai = st.selectbox("有利区間差枚",["-500枚未満","-500~+1300枚","+1300~+2400枚"],disabled=samai_disable)
        zenkai_1100 = st.checkbox("前回の当たりが液晶1100Gを超えていたことが分かる場合チェック", value=False)

        

        if zenkai_1100:
            zentz()
        else:
            if thru == 0:
                g = 500

