import streamlit as st
from display import tjz
from display import zentz

def karakuri():
    st.title("L からくりサーカス")
    st.write("狙い目はすべて液晶右下のG数です。")
    st.write("クソ荒いので時間と軍資金には余裕をもって挑みましょう。18時回ったらこの狙い目メモよりボーダーを上げていかないと打てません。")
    morning = st.checkbox("朝一リセット", value=False)
    thru = st.slider("CZスルー回数", 0,4,0,1, help="データカウンター上で直近にRBが連続している回数。10G以内のRBはカウントしない")
    if morning:
        if thru == 0:
            g = 560
        elif thru == 1:
            g = 530
        elif thru == 2:
            g = 210
        else:
            g = 0

        with st.container(border=True):
            tjz(g)

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
            with st.container(border=True):
                zentz()
        else:
            if thru == 0 or thru == 1:
                g = 500
            elif thru == 2:
                at1400 = st.checkbox("AT間1500G以上の場合チェック（液晶右下ではなくデータカウンター上の実回転数）", value=False)
                if at1400:
                    g = 0
                else:
                    g = 280
            else:
                g = 0

            if g == 0:
                pass
            else:
                if prev_mode == "A":
                    g = g -20
                elif prev_mode == "B" or prev_mode == "C":
                    g = g -10
                else:
                    g = g + 40

                if yuri_atama:
                    g = g + 50
                else:
                    if samai == "-500枚未満":
                        g = g - 10
                    elif samai == "+1300~+2400枚":
                        g = g + 50
            with st.container(border=True):  
                tjz(g)

    st.divider()
    st.caption("LからくりサーカスG、AT、CZ天井1200G+α、AT天井CZ5スルー or AT間2500G、純増2.8枚/G or 7.6枚/G")


