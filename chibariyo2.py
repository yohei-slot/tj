import streamlit as st

def chibariyo2():
    st.title("スマスロ チバリヨ２")
    morning = st.checkbox("朝一", value=False)
    thru = st.slider("スルー回数", 0,6,0,1)
    st.caption("1G連は天国じゃないものとする")
    if morning:
        if thru < 7:
            zone = [0,240,240,220,210,200,200]
            tenjo = [70,730,680,640,650,600,500]
            if thru == 0:
                st.subheader(f'天井狙い {tenjo[thru]}G~')
            else:
                st.subheader(f'ゾーン狙い{zone[thru]}~360G')
                st.subheader(f'天井狙い {tenjo[thru]}G~')
        else:
            st.subheader("天国まで全ツ")
            st.caption("閉店時間（最低５時間）と持ちメダルには余裕をもって！（スルー回数天井はないです）")

    else:
        if thru == 0:
            samai = st.slider("有利差枚（大体でおk）",-2600,1300,0,50)
            
            if samai >= 1250 or samai <=-2500:
                z0 = 32
            elif (samai > -2500 and samai <= -2000) or (samai >= 250 and samai < 1250):
                z0 = 60
            else:
                z0 = 90
            
            if samai >= 250:
                t0 = 840
            elif samai >= -2000:
                t0 = 800
            else:
                t0 = 720
            
            st.subheader(f'ゾーン狙い {z0}~360G')
            st.subheader(f'天井狙い {t0}G~')

        
        elif thru == 6:
            st.subheader("天国まで全ツ")
            st.caption("閉店時間（最低５時間）と持ちメダルには余裕をもって！（スルー回数天井はないです）")

        elif thru == 1 or thru == 2:
            zenkai = st.checkbox("前回、34～130Gあるいは320～360Gで当選の場合チェック", value=False)
            if zenkai:
                if thru == 1:
                    z0 = 280
                    t0 = 760
                else:
                    z0 = 250
                    t0 = 700
            else:
                if thru == 1:
                    z0 = 240
                    t0 = 670
                else:
                    z0 = 200
                    t0 = 650
            st.subheader(f'ゾーン狙い {z0}~360G')
            st.subheader(f'天井狙い {t0}G~')

        else:
            ztable = [190,100,100]
            ttable = [580,540,500]
            z0 = ztable[thru-3]
            t0 = ttable[thru-3]
            st.subheader(f'ゾーン狙い {z0}~360G')
            st.subheader(f'天井狙い {t0}G~')

    st.divider()
    st.header("その他")
    st.write("・リミットレス後は天国まで打ちましょう。")
    st.write("・ボナ終了時のトップランプが赤色の場合は天国まで打ちましょう。")
    st.write("・SBBを引いて天国に飛ばなかった場合、天国まで打ちましょう。")
    st.write("・チャンスAやチャンスBが確定する聴牌ボイスや特殊チカリが出た場合は天国まで打ちましょう。")
    st.link_button("演出情報", "https://chonborista.com/slot/net-slot/205860/")
        
    st.divider()
    st.caption("Lチバリヨ2 ZB、AT、純増3or4.5枚/G、G数天井999G+α（設定変更時600G+α）、チェリー回数天井45回")

        