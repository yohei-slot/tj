import streamlit as st
import machines

st.title("ハイエナボーダーメモ")
machine = st.selectbox(
    '機種を選択',
    ('機種を選択','L北斗の拳', 'ヴァルヴレイヴ', 'チバリヨ2', 'L北斗無双','からくりサーカス','Lシンフォギア','L炎炎ノ消防隊', '絆2天膳','沖ドキGOLD','番長4', '戦国乙女4','防振り', '吉宗RISING',  'Lキン肉マン', "モンキーターンV", "バイオヴィレッジ", "マクロスF4")
)

st.session_state['machine'] = machine

def home():
    st.markdown("""
    ## 注意事項
    ＊このサイトの狙い目は全て等価交換105%ボーダーです。 \n
    ＊閉店減算は考慮されていません。 \n
    ＊作者が収集したデータを基に、独自に算出した狙い目です。参考にする際は自己責任で。
    """)


if st.session_state['machine'] == '機種を選択':
    home()
elif st.session_state['machine'] == 'L北斗の拳':
    machines.hokuto.hokuto()
elif st.session_state['machine'] == '沖ドキGOLD':
    machines.okigold.okidoki_gold()
elif st.session_state['machine'] == '絆2天膳':
    machines.tenzen.tenzen()
elif st.session_state['machine'] == '吉宗RISING':
    machines.yoshimune_rising.yoshimune_r()
elif st.session_state['machine'] == 'ヴァルヴレイヴ':
    machines.vvv.vvv()
elif st.session_state['machine'] == 'Lキン肉マン':
    machines.niku.niku()
elif st.session_state['machine'] == 'モンキーターンV':
    machines.monkeyv.monkeyv()
elif st.session_state['machine'] == "バイオヴィレッジ":
    machines.village.village()
elif st.session_state['machine'] == "マクロスF4":
    machines.macrossf4.macrossf4()
elif st.session_state['machine'] == "番長4":
    machines.bancho4.bancho4()
elif st.session_state['machine'] == "チバリヨ2":
    machines.chibariyo2.chibariyo2()
elif st.session_state['machine'] == "防振り":
    machines.bofuri.bofuri()
elif st.session_state['machine'] == "ToLOVEる":
    machines.tolove.tolove()
elif st.session_state['machine'] == "からくりサーカス":
    machines.karakuri.karakuri()
elif st.session_state['machine'] == "Lシンフォギア":
    machines.synpho_seigi.synpho_seigi()
elif st.session_state['machine'] == 'L炎炎ノ消防隊':
    machines.Lenen.Lenen()
elif st.session_state['machine'] == "L北斗無双":
    machines.muso.muso()
elif st.session_state['machine'] == "戦国乙女4":
    machines.otome4.otome4()
else:
    st.header("工事中...")

