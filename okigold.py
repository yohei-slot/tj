import streamlit as st
import pandas as pd

def okidoki_gold():
    st.header("沖ドキGOLD")
    st.markdown("""この台は有利区間が切れるタイミングがよくわかりません。
                このページでは、一撃1000枚以上後 or 有利2000G後のボナ後に切れるものとした狙い目を記します。
                狙い目表にある有利区間G数とは、前回のボーナス終了時点での有利区間G消化数のこと（ボーナス中含む、疑似遊戯は除く）です。
                32G以内の連荘が含まれる履歴の場合はマタギ狙いの狙い目を参考にしてください。""")
    st.write(" ")

    select = st.radio("状況を選択", options=("朝一以外","朝一","マタギ狙い"), index=0, horizontal=True)

    
    if select == "朝一以外":
        thru = st.slider("スルー回数",0,5,0,1)
        if thru == 0:
            st.write("狙い目:")
            st.subheader("700G～（天井狙い）")
            st.subheader("100～130G（ゾーン狙い）")
            st.subheader("390～402G（ゾーン狙い）")

        elif thru == 1:
            st.write("有利区間G数：狙い目")
            st.subheader("不問：580G")
            st.subheader("1090G：500G")
            st.subheader("1200G：400G")
            st.subheader("1310G：300G")
            st.subheader("1260G：250G")

        elif thru == 2:
            st.write("有利区間G数：狙い目")
            st.subheader("不問：550G")
            st.subheader("750G：500G")
            st.subheader("860G：400G")
            st.subheader("970G：300G")
            st.subheader("1080G：200G")
            st.subheader("1090G：100G")
            st.subheader("1280G：32G")

        elif thru == 3:
            st.write("有利区間G数：狙い目")
            st.subheader("不問：300G")
            st.subheader("950G：200G")
            st.subheader("1060G：100G")
            st.subheader("1150G：32G")

        elif thru == 4:
            st.write("有利区間G数：狙い目")
            st.subheader("不問：200G")
            st.subheader("990G：100G")
            st.subheader("1080G：32G")

        elif thru == 5:
            st.subheader("天国or有利切れまで全ツ！")



    elif select == "朝一":
        thru = st.slider("スルー回数",0,5,0,1)
        if thru == 0:
            st.write("狙い目:")
            st.subheader("650G～（天井狙い）")
            st.subheader("0～32G（ゾーン狙い）")
            st.subheader("100～130G（ゾーン狙い）")
            st.subheader("360～403G（ゾーン狙い）")
        
        elif thru == 1:
            gbefore = st.radio("0スの当選G数", options=("32G以下", "33～149G", "150G以上"), index=0, horizontal=True)
            if gbefore == "32G以下":
                st.write("狙い目:")
                st.subheader("420G")      
            elif gbefore == "33～149G":
                st.write("狙い目:")
                st.subheader("440G")
            elif gbefore == "150G以上":
                st.write("有利区間G数：狙い目")
                st.subheader("不問：510G")
                st.subheader("1150G：400G")
                st.subheader("1260G：300G")
                st.subheader("1310G：250G")

        elif thru == 2:
            gbefore = st.radio("1スの当選G数", options=("149G以下", "150G以上"), index=0, horizontal=True)
            if gbefore == "149G以下":
                st.write("有利区間G数：狙い目")
                st.subheader("不問：270G")
                st.subheader("1040G：200G")
                st.subheader("1160G：100G")
                st.subheader("1250G：32G")
            
            elif gbefore == "150G以上":
                st.write("有利区間G数：狙い目")
                st.subheader("900G：400G")
                st.subheader("1050G：300G")
                st.subheader("1210G：200G")
                st.subheader("1290G：100G")
                st.subheader("1380G：32G")

        elif thru == 3:
            gbefore = st.radio("1スの当選G数", options=("149G以下", "150G以上"), index=0, horizontal=True)
            if gbefore == "149G以下":
                st.write("有利区間G数：狙い目")
                st.subheader("不問：200G")
                st.subheader("960G：100G")
                st.subheader("1050G：32G")
            
            elif gbefore == "150G以上":
                st.write("有利区間G数：狙い目")
                st.subheader("不問：300G")
                st.subheader("940G：200G")
                st.subheader("1060G：100G")
                st.subheader("1180G：32G")

        elif thru == 4:
            st.write("有利区間G数：狙い目")
            st.subheader("不問：200G")
            st.subheader("810G：100G")
            st.subheader("900G：32G")
        
        elif thru == 5:
            st.subheader("天国or有利切れまで全ツ！")
       
    elif select == "マタギ狙い":
        matagi = st.text_input("33G以上は0, 32以下は1で入力。", "0100")
        mtype = st.radio("「1」のゲーム数",("1～11G","12G～32G"), horizontal=True, args=[1,0] )
        if mtype == "1～11G":
            mtype = '1'
        else:
            mtype = '0'
        st.table(pd.read_csv(f'./okigold_data/okigold_matagi{mtype}_{matagi}.csv'))

        st.markdown(""" ## マタギ狙いの注意点
        ＊有利頭から現在の状態まで数えて、有利切れたらヤメ。 \n
        ＊「1」スタートで数えるのは危険
        ＊ダブルマタギは危険なので触らない。例：001010
        """)

    st.divider()
    st.caption("S/沖ドキGOLD/LS、AT、純増3枚/G、天井999G+α")