import streamlit as st
from display import tjz

def niku():
    st.header("スマスロ キン肉マン 7人の悪魔超人編")
    morning = st.checkbox("リセット後 魔界の荒野移行あり", value=False)
    if not morning:
        thru = st.slider("朝一からの初当たり回数",0,14,0,1)
        nikudict = {0:340,1:290,2:250,3:240,4:190,5:170,6:140,7:80,8:0,9:330,10:370,11:370,12:380,13:380,14:380}
        with st.container(border=True):
            tjz(nikudict[thru])
            st.caption("狙い目はすべて液晶の数字（万pts）")
    elif morning:
        st.write("荒野後3回目の当たりまでに75%でSPが来ます。2スルーは状態不問では0G～と甘くなっていますが、前任者が1,2スルー中にSP発動を確認してやめた場合期待値が大きく下がります。")
        thru = st.slider("魔界の荒野後初当たり回数",0,9,0,1)
        nikudict = {0:130,1:80,2:0,3:300,4:250,5:250,6:250,7:250,8:250,9:260}
        with st.container(border=True):
            tjz(nikudict[thru])
            st.caption("狙い目はすべて液晶の数字（万pts）")

    st.write("正義超人チャレンジに700G当たっていない台は正義超人アタック狙いで打てます。（カウンターで前回900G以上ハマっていて現在液晶とデータカウンターのG数が一致している台など）")
    
    st.divider()

    st.markdown("""
                ## メニュー画面示唆
                打てるもの: \nキン肉マン（朝一以外）\nモンゴルマン（前回終了画面との矛盾の場合のみ）\n悪魔将軍（次回SP濃厚）\n謎の悪魔超人(次回SP強)\nバッファローマン(5回以内SP濃厚、バッファローSP示唆)\nステカセキング(5回以内SP中, シナリオSP示唆)\nアシュラマン(5回以内SP濃厚)\nサンシャイン(5回以内SP強)\nミート君(5回以内SP濃厚、シナリオSP示唆)
                """)
    
    st.markdown("""
                ## 終了画面示唆
                打てるもの（復活は無効）：　\nバッファローマン（5回以内SP濃厚、バッファローSP示唆）\n悪魔将軍（次回SP濃厚）
                """)
    
    st.markdown("""
                ## その他
                打てるもの（1回当たるまで）：　\nアイキャッチ赤orモノクロ\nセリフ赤or紫
                """)
    
    st.divider()
    st.caption("Lパチスロキンニクマン 4SLDC、AT、純増6.1枚/G、天井液晶900G+α")
