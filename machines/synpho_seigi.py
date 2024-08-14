import streamlit as st
from display import tjz
from display import zentz

def synpho_seigi():
    st.title("L戦姫絶唱シンフォギア 正義の歌")
    morning = st.checkbox("朝一リセット", value=False)
    if morning:
        with st.container(border=True):
            tjz(200)
            tjz(z1=350,z2=100)
    else:
        zesho = st.checkbox("前回絶唱の場合チェック", value=False)
        if zesho:
            with st.container(border=True):
                tjz(380)
                tjz(z1=0,z2=250)
        else:
            st.write("前回ATの獲得枚数を選択")
            prev = st.selectbox(["単発（99枚以下）","100~800枚", "800枚以上"])
            if prev == "単発（99枚以下）" or prev == "100~800枚":
                prevg_280 = st.checkbox("前回AT当選G数が280G以上の場合チェック", value=True)
            
            with st.container(border=True):

                if prev == "単発（99枚以下）":
                    tjz(360)
                    tjz(z1=0,z2=100)
                    if not prevg_280:
                        tjz(z1=220,z2=250)
                    
                elif prev == "100~800枚":
                    tjz(360)
                    if not prevg_280:
                        tjz(z1=220,z2=250)
                
                else:
                    tjz(440)

    st.subheader("やめどき")
    now = st.selectbox("AT終了時の状態を選択",["絶唱後", "獲得枚数99枚以下", "エクスドライブステージにいった場合", "CZ天国確定時","CZ本前兆中にギアフラグを引いていた場合"])
    if now == "絶唱後":
        st.write("0~250ゾーンまで打ってやめ。280までにCZ以外で当たった場合はもう一度250まで。")
    elif now == "獲得枚数99枚以下":
        st.write("天国まで回す")
    elif now == "エクスドライブステージにいった場合":
        st.write("天国ループするので、天国まで辞めない。ループし続ける限り打つ")
    elif now == "CZ天国確定時":
        st.write("天国まで打つ。CZを引かずにAT当選の場合は次回のCZも打つ")
    elif now == "CZ本前兆中にギアフラグを引いていた場合":
        st.write("AT終了後に抽選が残っているので必ず確認")

    st.subheader("その他注意事項")
    st.write("- 画面右下の必殺技が「弾突砲雷」「夢幻掌破」の場合は打つ")
    st.write("- メニュー画面のアイテム")
    st.write("  ・「豪華テーブル」「黄金テーブル」はATまで打つ")
    st.write("  ・「アダムの電話」はCZまで打つ")
    st.write("  ・「全員集合」はエクスドライブ抜けまで打つ")
    st.write("- 画面左下のG数の横に「アダム（白い帽子の男）」が居たらCZまで打つ")
    st.write("- 画面左下赤色の抜剣メーターが8割以上貯まっていれば打てる。多少貯まっていればボーダーを下げれる。")

    st.divider()
    st.caption("L戦姫絶唱シンフォギア 正義の歌、AT、天井777G+α　リセット時498G+α、純増2.8枚/G or 5.0枚/G")
