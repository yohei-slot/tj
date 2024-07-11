import streamlit as st
import hokuto
import okigold
import tenzen
import vvv
import chibariyo2
import bancho4
import bofuri
import yoshimune_rising
import niku
import monkeyv
import village
import macrossf4

st.title("ハイエナボーダーメモ")
machine = st.selectbox(
    '機種を選択',
    ('機種を選択','L北斗の拳', '沖ドキGOLD', '絆2天膳', 'ヴァルヴレイヴ', 'チバリヨ2', '番長4', '防振り', '吉宗RISING',  'Lキン肉マン', "モンキーターンV", "バイオヴィレッジ", "マクロスF4")
)

st.session_state['machine'] = machine

def home():
    st.markdown("""
    ## 注意事項
    ＊このサイトの狙い目は全て20円等価交換105%ボーダーです。 \n
    ＊閉店減算は考慮されていません。 \n
    ＊作者が収集したデータを基に、独自に算出した狙い目です。参考にする際は自己責任で。
    """)


if st.session_state['machine'] == '機種を選択':
    home()
elif st.session_state['machine'] == 'L北斗の拳':
    hokuto.hokuto()
elif st.session_state['machine'] == '沖ドキGOLD':
    okigold.okidoki_gold()
elif st.session_state['machine'] == '絆2天膳':
    tenzen.tenzen()
elif st.session_state['machine'] == '吉宗RISING':
    yoshimune_rising.yoshimune_r()
elif st.session_state['machine'] == 'ヴァルヴレイヴ':
    vvv.vvv()
elif st.session_state['machine'] == 'Lキン肉マン':
    niku.niku()
elif st.session_state['machine'] == 'モンキーターンV':
    monkeyv.monkeyv()
elif st.session_state['machine'] == "バイオヴィレッジ":
    village.village()
elif st.session_state['machine'] == "マクロスF4":
    macrossf4.macrossf4()
else:
    st.header("工事中...")

