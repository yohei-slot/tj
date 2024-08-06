import streamlit as st
from display import tjz
from display import zentz

def vvv():
    st.header("L 革命機ヴァルヴレイヴ")
    st.write("正確な期待値計算が難しい台のため、安全のため106～107%想定のボーダーを記載します")
    mimizu = st.checkbox("ミミズ", value=False,  help="ミミズ判別は下記参照")
    rbthru = st.radio("決戦ボーナススルー回数", options=(0,1,2,3,4), index=0, horizontal=True)
    czthru = st.radio("CZスルー回数", options=(0,1,2,3,4), index=0, horizontal=True)
    ekisho = st.slider("液晶G数", 0,1000,0,1)
    if not mimizu:
        if rbthru == 0:
            st.write("CZ・ボナ・ATまで打ったのち押し引き")
            if czthru == 0:
                eg = 510
            elif czthru == 1:
                if ekisho <= 300:
                    g = -0.33*ekisho+900
                else:
                    g = -8.889*ekisho+3466.7
                if g < 0:
                    g = 0
                elif g > 1000:
                    g = 1000

            elif czthru == 2:
                if ekisho <= 80:
                    g = -1.625*ekisho+830
                else:
                    g = -8.75*ekisho+1400
                if g < 0:
                    g = 0
                elif g > 1000:
                    g = 1000

            elif czthru == 3:
                g = -9.375*ekisho + 750
                if g < 0:
                    g = 0
                elif g > 1000:
                    g = 1000

            else:
                g = 0
            
            with st.container(border=True):
                if czthru == 0:
                    tjz(t=eg,ttext="液晶 ")
                elif g == 0:
                    zentz()
                else:
                    tjz(t=int(g),ttext="ボーナス間 ")

        elif rbthru == 1:
            st.write("CZ・ボナ・ATまで打ったのち押し引き")
            zerocz = st.radio("0スルー時のCZ回数", options=(1,2,3,4,5), index=0, horizontal=True)
            with st.container(border=True):
                if zerocz == 1:
                    if czthru == 0:
                        eg = 320
                        tjz(t=eg,ttext="液晶 ")
                    elif czthru == 1:
                        g = -4.4444*ekisho + 800
                        if g < 0:
                            g = 0
                        elif g > 1000:
                            g = 1000
                        tjz(t=int(g),ttext="ボーナス間 ")
                    elif czthru == 2:
                        g = -4.375*ekisho + 700
                        if g < 0:
                            g = 0
                        elif g > 1000:
                            g = 1000
                        tjz(t=int(g),ttext="ボーナス間 ")
                    elif czthru == 3:
                        zentz()
                elif zerocz == 2:
                    if czthru == 0:
                        eg = 200
                        tjz(t=eg,ttext="液晶 ")
                    elif czthru == 1:
                        g = -4.375*ekisho + 700
                        if g < 0:
                            g = 0
                        elif g > 1000:
                            g = 1000
                        tjz(t=int(g),ttext="ボーナス間 ")
                    elif czthru == 2:
                        g = -10*ekisho + 700
                        if g < 0:
                            g = 0
                        elif g > 1000:
                            g = 1000
                        tjz(t=int(g),ttext="ボーナス間 ")
                    elif czthru == 3:
                        zentz()
                elif zerocz == 3:
                    if czthru == 0:
                        eg = 180
                        tjz(t=eg,ttext="液晶 ")
                    elif czthru == 1:
                        g = -7*ekisho + 700
                        if g < 0:
                            g = 0
                        elif g > 1000:
                            g = 1000
                        tjz(t=int(g),ttext="ボーナス間 ")
                    elif czthru >= 2:
                        zentz()
                elif zerocz == 4:
                    if czthru == 0:
                        eg = 50
                        tjz(t=eg,ttext="液晶 ")
                    else:
                        zentz()
                else:
                    zentz()

        elif rbthru == 2:
            zerocz = st.radio("0、１スルー時のCZ回数合計", options=(2,3,4), index=0, horizontal=True)
            with st.container(border=True):
                if zerocz == 2:
                    if czthru == 0:
                        g = -3.5*ekisho + 700
                        if g < 0:
                            g = 0
                        elif g > 1000:
                            g = 1000
                        tjz(t=int(g),ttext="ボーナス間 ")
                    elif czthru == 1:
                        g = -8.5714*ekisho + 600
                        if g < 0:
                            g = 0
                        elif g > 1000:
                            g = 1000
                        tjz(t=int(g),ttext="ボーナス間 ")
                    else:
                        zentz()

                elif zerocz == 3:
                    if czthru == 0:
                        g = -8.125*ekisho + 650
                        if g < 0:
                            g = 0
                        elif g > 1000:
                            g = 1000
                        tjz(t=int(g),ttext="ボーナス間 ")
                    elif czthru == 1:
                        g = -12*ekisho + 600
                        if g < 0:
                            g = 0
                        elif g > 1000:
                            g = 1000
                        tjz(t=int(g),ttext="ボーナス間 ")
                    else:
                        zentz()
                else:
                    zentz()
        else:
            with st.container(border=True):
                zentz()
    
    elif mimizu:
        with st.container(border=True):
            if rbthru == 0:
                if czthru == 0:
                    eg = 210
                    tjz(t=eg,ttext="液晶 ")
                elif czthru == 1:
                    eg = 70
                    tjz(t=eg,ttext="液晶 ")
                else:
                    zentz()
            elif rbthru == 1:
                if czthru == 0:
                    eg = 70
                    tjz(t=eg,ttext="液晶 ")
                else:
                    zentz()
            else:
                zentz()

    st.divider()

    st.markdown("""
                ## 辞め時
                非ミミズ時のボーナス後は即やめ（0から打てる状態でなければ）  \n
                非ミミズ時のAT後は引き戻し確認後やめ
                ミミズ時は全て即やめ
                """)
    
    st.markdown("""
                ## ミミズ判別
                1. データカウンター250～400でのCZ当たりが多い（410Gまでに9割）
                2. 一撃で1150枚を超えない
                3. CZがとても成功しやすい（目安9割）
                4. AT後の引き戻しが少ない
                5. RBよりBBに偏る（BB8 : RB2）
                """)
    
    st.divider()
    st.caption("L革命機ヴァルヴレイヴ D、AT、純増7.2枚/G、CZ天井液晶1000G+α、ボナ天井実1500G+α、CZスルー天井 8回目、RBスルー天井 5回目")
