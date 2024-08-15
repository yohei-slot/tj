import streamlit as st
from display import tjz
from display import zentz

def muso():
    st.title("スマスロ真北斗無双")
    st.write("狙い目はすべて液晶の宿命pt")
    
    morning = st.checkbox("朝一リセット～駆け抜けないSTまで", value=False)
    if morning:
        thru_n = st.selectbox("連続駆け抜け回数",[1,2,3,4,5,6])
        if thru_n == 1:
            g = 400
        elif thru_n == 2:
            g = 200
        elif thru_n == 3 or thru_n == 4 or thru_n == 6:
            g = 0
        else:
            g = 200
    else:
        thru = st.checkbox("前回ST駆け抜け", value=False)
        if thru:
            thru_n = st.selectbox("連続駆け抜け回数",[1,2,3,4,5,6])
            if thru_n == 1:
                g = 580
            elif thru_n == 2:
                g = 560
            elif thru_n == 3:
                g = 320
            elif thru_n == 4:
                g = 560
            elif thru_n == 5:
                g = 200
            else:
                g = 0
        else:
            samai500 = st.selectbox("有利差枚",["+500枚以上","+500枚未満"])
            if samai500 == "+500枚以上":
                g = 840
            else:
                g = 760
    
    all2 = st.checkbox("全ての奥義ポイントが2pt以下ならチェック", value=False)
    if all2:
        g = g + 30

    with st.container(border=True):
        tjz(g)
    
    st.subheader("以下に当てはまったら、上位ブレイク確定のため解放まで打つ！")
    st.markdown("""
                ・チェリーが6pt以上
                ・チャンスベルが6pt以上
                ・スイカが8pt以上
                ・チャンス目が4pt以上
                 """)
    st.subheader("その他出てきたら無条件で打てる示唆")
    st.markdown("""
                ・キリン柄ステチェン（32宿命以内当選&ブルーセブンモード濃厚）
                ・1000宿命以上での赤ステチェン（100宿命以内当選&ブルーセブンモード濃厚）
                ・ユリアポイント示唆「最強」
                """)
    st.subheader("やめどき")
    st.write("五車星ステージ・天国示唆以外は即ヤメ")

    st.divider()
    st.caption("L スマスロ真北斗無双 FS、AT、天井1536宿命+α、純増5枚/G")

    
