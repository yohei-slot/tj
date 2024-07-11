import streamlit as st

def macrossf4():
    st.header("スマスロ マクロスフロンティア4")
    st.write("このページでは、内部G数が実G数の1.5倍になるものとして算出した狙い目を表示します。もし打ち込んでいる人で、1.5倍ではないと思う方は下の欄を修正して利用してください。")
    factor = st.number_input("内部G数加算率（デフォルト1.5倍）", 1.0, 3.0, step=0.01, value=1.5, help="分からなければ触らなくてok")
    morning = st.checkbox("朝一リセット", value=False, help="朝一0スルーは甘い、1・2スルーは辛い")
    thru = st.slider("ボーナススルー回数", 0,6,0,1)
    if not morning:
        if thru == 0:
            g = 540*factor
        elif thru == 1:
            g = 570*factor
        elif thru == 2:
            g = 570*factor
        elif thru == 3:
            g = 650*factor
        elif thru == 4:
            g = 650*factor
        elif thru == 5:
            g = 220*factor
        else:
            g = 0

        st.subheader(f"液晶 {int(g)}G~ 天井まで")
        st.subheader("液晶 480G～500Gのゾーン狙い 前兆終了まで")
        st.caption("500Gのゾーンで前兆が来なければ良いモードなのでそのまま天井まで")

    else:
        if thru == 0:
            g = 210*factor
        elif thru == 1:
            g = 600*factor
        elif thru == 2:
            g = 640*factor
        elif thru == 3:
            g = 660*factor
        elif thru == 4:
            g = 650*factor
        elif thru == 5:
            g = 220*factor
        else:
            g = 0

        st.subheader(f"液晶 {int(g)}G~ 天井まで")

    st.divider()

    st.markdown("""## ヤメ時
                15G程回す \n
                歌即前兆があれば100Gまで回す。\n
                なければヤメ。
                """)
    
    st.divider()
    st.caption("Lマクロスフロンティア4、AT、純増1.5枚/G or 5枚/G")
    st.caption("天井:液晶1500G+α or 実ゲーム1000G+α、歌姫ボーナス11回目")

