import streamlit as st

def hokuto():
    st.header("スマスロ北斗の拳")
    reset = st.radio("リセット状態", options=("朝一以外", "朝一", "朝二"), horizontal=True)
    if reset == "朝一以外":
        before = st.radio("前回あたりの一撃獲得枚数", options=("799枚以下", "800枚〜1299枚", "1300枚以上"), horizontal=True)
        if before == "799枚以下":
            samai = st.slider("直近1600G差枚", -1500, 1500, 0, 1)
            neraime = int(samai*0.1158+490)
            st.subheader(f"狙い目は {neraime}G")

        elif before == "800枚〜1299枚":
            st.write("＊直近の差枚がマイナスでも、前回ATで一撃大量獲得した場合は辛くなります \n \n")
            st.subheader("狙い目は 600G")
        
        elif before == "1300枚以上":
            st.write("＊直近の差枚がマイナスでも、前回ATで一撃大量獲得した場合は辛くなります \n \n")
            st.subheader("狙い目は 650G")

    elif reset == "朝一":
        st.write("＊リセット時は天井が800G+前兆に短縮 \n \n")
        st.subheader("狙い目は 80G")

    elif reset == "朝二":
        st.write("＊朝二はデータ上甘めになっています。 \n \n")
        samai = st.slider("前回差枚", -750, 1000, 0, 1)
        neraime = int(samai*0.2312+400)
        st.subheader(f"狙い目は{neraime}G")
    st.write("\n")
    st.write("\n")

    st.markdown("""
    注意事項 \n
    ＊狙い目は内部状態不問で立てています。落ちている台は地獄の可能性が高くなるので、表記されたG数より少し深めから打ちましょう。 \n
    ＊逆に、通常以上の可能性が上がる台（マミヤ同行・ジャギステ・北斗カウンター点灯など）は少し浅めに狙えます。 \n
    ＊スイカを溢さないように！溢す人は深めから狙いましょう。
    """)

    st.divider()
    st.caption("L北斗の拳、AT、純増4枚/G、天井1268G+α、リセット天井800G+α")