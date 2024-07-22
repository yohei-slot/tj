import streamlit as st
from display import tjz

def bofuri():
	st.title('スマスロ 痛いのは嫌なので防御力に極振りしたいと思います')
	morning = st.checkbox('朝イチ',value=False)
	if morning:
		with st.container(border=True):
			tjz(200)
			tjz(240, ttext="駆け抜け後")
		st.caption('朝イチから連チャンするまでは、天井短縮状態がずっと続く')
	else:
		samai = st.slider('有利差枚(大体でおk)', -2000,1500,0,100)
		kakenuke = st.checkbox('前回駆け抜け', value=False)
		hakaio = st.checkbox('スキル「破壊王」を所持', value=False)
		if samai > 1000:
			t = 700
		elif samai > 0:
			t = 670
		else:
			t = 650
		
		if samai > 0:
			z150 = 'nan'
			z300 = 250
		elif samai >= -2000:
			z150 = 140
			z300 =250
		else:
			z150 = 130
			z300 = 240
		
		if kakenuke:
			t = t + 10
		if hakaio:
			t = t - 100
		if z150 != 'nan':
			if hakaio:
				z150 = z150 - 20
		else:
			z150 = False
		if hakaio:
			z300 = z300 - 20

		with st.container(border=True):
			tjz(t)
			tjz(t=False,z1=z150,z2=150,ztext="150のゾーン狙い")
			tjz(t=False,z1=z300,z2=300,ztext="300のゾーン狙い")
	
		
	st.divider()
	st.subheader('やめ時')
	st.text('基本的には80Gまで回す！')
	st.caption('防御レベルが2以下且つ演出が弱ければ50Gでやめても良し。演出の詳細については下記ボタン先の"状態示唆"項目を参照。')
	st.link_button('演出情報','https://www.slopachi-quest.com/article/bouhuri-tenjou/#i-17')
	
	st.divider()
	st.caption("L防振り FN、AT、純増5.5枚/G、天井：950G+α")
		
		
