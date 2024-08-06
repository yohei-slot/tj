import streamlit as st
from display import tjz
from display import zentz

def tenzen():
    st.markdown("""
                <style>
                .big-font{
                    font-size:50px !important;
                    background: linear-gradient(to right,#e60000,#f39800,#fff100,#009944,#0068b7,#1d2088,#920783);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-weight: bold;
                    display: inline-block;
                }
                </style>
                """, unsafe_allow_html=True)
    

    st.header("バジリスク絆2 天膳BLACK")
    st.write("""有利切れの恩恵が強い台なので、有利差枚が浮いている台ほど期待値が高くなります。
             有利区間切れ条件は、有利差枚+1000枚以上です。穢れ契機の宿怨チャレンジでは切れないものと予想されます。
             宿怨チャレンジ突入の際は、8G以上のBT直撃履歴が残ります。
             有利切れ条件を満たさずに宿怨ループをしている台については有利切れが不明なので、ここでは狙い目を記載しません。狙う際は十分注意してください。
             """)

    morning = st.radio("リセ状態", options=("朝一以外", "朝一"), index=0, horizontal=True)
    thru = st.radio("BCスルー回数", options=(0,1,2,3,4), index=0, horizontal=True)
    shukuen = st.radio("当該有利区間にて、穢れ契機による宿怨チャレンジ履歴が", options=("あり","なし" ))
    if morning == "朝一以外":
        if thru == 4:
            with st.container(border=True):
                st.markdown('<p class="big-font">BT当選まで全ツ!</p>')
        
        elif thru == 0:
            if shukuen == "あり":
                diff = st.slider("有利差枚(前回BC終了時時点)", -1500,1000,0,1)
                g  = 237.437621 - 0.0188185767*diff - 1.03004925**(diff/4.14118384)
                if diff <= -1500:
                    g = 270
                if g <= 0:
                    g = 0
                print(g)
                

            elif shukuen == "なし":
                diff = st.slider("有利差枚(前回BC終了時時点)", 0,1000,0,1)
                g = 253 - 0.00779891544*diff - 1.00968813**(diff/1.32165226)
                if diff <= 100:
                    g = 250
                if g < 0:
                    g = 0
                


        elif thru == 1:
            if shukuen == "あり":
                samai = st.slider("有利差枚(前回BC終了時時点)", -4500,1000,0,1)
                btg = st.slider("0スのG数", 0,333,0,1)
                g = 185.84031 - 0.0332579531*samai - 0.281781894*btg - 0.000899453468*btg*btg + 4.73745084*samai*btg/100000 - 1.02226623**(samai/3.78449473)
                if g <= 0:
                    g = 0
                elif g >= 333:
                    g = 333
                
                

            elif shukuen == "なし":
                samai = st.slider("有利差枚(前回BC終了時時点)", -4500,1000,0,1)
                btg = st.slider("0スのG数", 0,333,0,1)
                g = 220.50933 - 0.059265*samai - 0.267112137*btg - 0.001060607*btg*btg + 0.0002073843*samai*btg/100000 - 1.7326**(samai/84.0124)
                if g <= 0:
                    g = 0
                elif g >= 333:
                    g = 333
                
                

        elif thru == 2:
            if shukuen == "あり":
                samai = st.slider("有利差枚(前回BC終了時時点)", -4500,1000,0,1)
                btg = st.slider("BT間G数(前回BC終了時時点)", 0,666,0,1)
                g = 141 - 0.0332579531*samai - 0.281781894*btg - 0.000899453468*btg*btg + 4.73745084*samai*btg/100000 - 1.02226623**(samai/3.78449473)
                if g <= 0:
                    g = 0
                elif g >= 333:
                    g = 333
                
                

            elif shukuen == "なし":
                samai = st.slider("有利差枚(前回BC終了時時点)", -4500,1000,0,1)
                btg = st.slider("BT間G数(前回BC終了時時点)", 0,666,0,1)
                g = 180.50933 - 0.059265*samai - 0.267112137*btg - 0.001060607*btg*btg + 0.0002073843*samai*btg/100000 - 1.7326**(samai/84.0124)
                if g <= 0:
                    g = 0
                elif g >= 333:
                    g = 333

             

        elif thru == 3:
            if shukuen == "あり":
                samai = st.slider("有利差枚(前回BC終了時時点)", -4500,1000,0,1)
                btg = st.slider("BT間G数(前回BC終了時時点)", 0,666,0,1)
                g = 60 - 0.0332579531*samai - 0.281781894*btg - 0.000899453468*btg*btg + 4.73745084*samai*btg/100000 - 1.02226623**(samai/3.78449473)
                if g <= 0:
                    g = 0
                elif g >= 333:
                    g = 333

               

            elif shukuen == "なし":
                samai = st.slider("有利差枚(前回BC終了時時点)", -4500,1000,0,1)
                btg = st.slider("BT間G数(前回BC終了時時点)", 0,666,0,1)
                g = 180.50933 - 0.059265*samai - 0.267112137*btg - 0.001060607*btg*btg + 0.0002073843*samai*btg/100000 - 1.7326**((samai+2300)/84.0124)
                if g <= 0:
                    g = 0
                elif g >= 333:
                    g = 333
                if btg <= 100:
                    if g > 100:
                        g = 100

                

    elif morning == "朝一":
        if thru == 0:
            g = 260
        

        elif thru == 1:
            btg = st.slider("BT間G数(前回BC終了時時点)", 0,333,0,1)
            g = -0.0023*btg**2 + 0.0276*btg + 254.5
            if g <= 0:
                g = 0
            elif g >= 333:
                g = 333
        


        elif thru == 2:
            btg = st.slider("BT間G数(前回BC終了時時点)", 0,666,0,1)
            g = -0.96*btg + 289.5
            if g <= 0:
                g = 0
            elif g >= 333:
                g = 333
            
    with st.container(border=True):
        if g > 0:
            tjz(int(g))
        else:
            zentz()
            print("fire")


    st.divider()

    st.markdown("""
                ## 穢れ狙いについて
                天膳BC終了時の穢れ示唆によって打ち分けができます。  \n
                ＊メイン液晶横全部まで点灯：打てない  \n
                ＊リール横点灯：ボーダーを大幅に下げる  \n
                ＊下パネル横まで・下パネル消灯：穢れ開放まで続行  \n
                解放まで時間がかかる場合もありますので、閉店まで4時間以上は確保して狙いましょう。
                """)
    
    st.divider()
    st.caption("L/バジリスク絆2～天膳～/ZN、AT、純増2.9枚/G、BC天井333G+α、BT天井 BC8回")