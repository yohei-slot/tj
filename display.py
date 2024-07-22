import streamlit as st

def tjz(t,ttext="天井狙い",z1=False,z2=False, ztext="ゾーン狙い"):
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
    if t != False:
        st.markdown(f'<p>{ttext} <span class="big-font">{t}G～</span>', unsafe_allow_html=True)
    if z1 != False and z2 != False:
        st.markdown(f'<p>{ztext} <span class="big-font">{z1}～{z2}G</span>', unsafe_allow_html=True)