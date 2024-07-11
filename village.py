import streamlit as st

def village(): 
    st.header("スマスロ バイオハザード:ヴィレッジ")
    morning = st.checkbox("朝一リセット", value=False, help="設定変更後は天井550Gに短縮")
    if morning:
        st.subheader("天井狙い 70G～")
    else:
        st.subheader("天井狙い 390G～")
        st.subheader("ゾーン狙い 85G～150G（前兆まで）")

    st.divider()

    st.markdown("""## メニュー画面 \n
                175G以降、メニュー画面にクリスがいればボーダーを下げれる。\n赤背景であれば問答無用で打つ。
                """)
    
    st.markdown("""## 辞め時 \n
                CLIMAX7敗北時は即ヤメ \n
                Hazard Rush 終了後は5G程回し即前兆を確認してヤメ
                """)
    
    st.divider()
    st.caption("Lバイオハザード ヴィレッジ、AT、純増2.5枚/G、天井750G+α")