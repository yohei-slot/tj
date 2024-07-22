import streamlit as st
from display import tjz

def village(): 
    st.header("スマスロ バイオハザード:ヴィレッジ")
    morning = st.checkbox("朝一リセット", value=False, help="設定変更後は天井550Gに短縮")
    if morning:
        t = 70
        z1=False
        z2=False
    else:
        t = 390
        z1 = 85
        z2 = 150
    with st.container(border=True):
        tjz(t,z1=z1,z2=z2)


    st.divider()

    st.markdown("""## メニュー画面 \n
                175G以降、メニュー画面にクリスがいればボーダーを下げれる。\n赤背景であれば問答無用で打つ。
                """)
    
    st.markdown("""## 辞め時 \n
                CLIMAX7敗北時は即ヤメ \n
                Hazard Rush 終了後は5G程回し即前兆を確認してヤメ
                """)
    
    st.divider()
    st.caption("Lバイオハザード ヴィレッジ XA、AT、純増2.5枚/G、天井750G+α")