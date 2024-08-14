#yoshimune_rising.py
import streamlit as st
from display import tjz
from display import zentz

def one_two():
    bonusG = st.slider("ボーナス間G数", 0,800,0,1)
    G = -0.3527*bonusG + 671.1
    if bonusG >= G:
        zentz()
    else:
        tjz(G,ttext="狙い目: AT間")

def yoshimune_r():
    st.title("スマスロ　吉宗RISING")
    morning = st.checkbox("朝一", value=False )
    reduce = st.checkbox("天井短縮", value=False, disabled=morning, help="前回AT単発で短縮")
    if morning:
        tjz(220, ttext="AT間狙い目")
        st.caption("ATまで打ち切り")

    else:
        if reduce:
            tjz(140, ttext="AT間狙い目")
            st.caption("ATまで打ち切り")

        else:
            thru = st.slider("RBスルー回数",0,4,0,1)
            if thru == 0:
                tjz(t=None,z1=85,z2=280,ztext="前兆までカバー、300まで続くこともあるのでやめるタイミングは注意")
                st.caption("150GのゾーンでRB当選でAT非当選の場合、AT間240Gから拾い直し")
                st.caption("ゾーン狙いは非短縮時のみ!!")
                tjz(520)

            elif thru == 1:
                one_two()

            elif thru == 2:
                one_two()

            elif thru == 3:
                bonusG = st.slider("ボーナス間G数", 0,800,0,1)
                G = -0.3527*bonusG + 671.1
                if bonusG >= G:
                    zentz()
                else:
                    tjz(G,"狙い目：AT間")

            elif thru == 4:
                zentz()


    st.divider()

    st.markdown("""
    ## そのほか注意事項
    ＊やめ時：ボナ後は前兆確認してやめ、AT後は1G連確認の上即やめ。 \n
    ＊G数の前兆はかなり引っ張られるケースあり。 \n
    ＊同行キャラ：二人いたら不問で消えるまで打てる。一人しかいない場合はボーダーちょい下げ（あまり気にしなくてよし） \n
    ＊穢れ：保有示唆 中・強 と 獲得示唆 強 の場合は解放まで打つ \n
    ＊ライジングポイント：基本わからない。リプレイで800p示唆が出ればATまで打つ
    """)

    st.divider()
    st.caption("L吉宗ライジング SA2、AT、純増4枚/G、ボナ間天井800G+α、AT間天井1200G+α（設定変更後とAT駆け抜け後は800G+α）、RBスルー回数天井5回")