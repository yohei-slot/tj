import streamlit as st


def bofuri():
	st.title('スマスロ 痛いのは嫌なので防御力に極振りしたいと思います')
	morning = st.checkbox('朝イチ',value=False)
	if morning:
		st.subheader('天井狙い 200G〜')
		st.subheader('駆け抜け後 240〜')
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
		st.subheader(f'天井狙い {t}G〜')
		if z150 != 'nan':
			if hakaio:
				z150 = z150 - 20
			st.subheader(f'150のゾーン狙い {z150}〜150G')
		if hakaio:
			z300 = z300 - 20
		st.subheader(f'300のゾーン狙い{z300}〜300G')
	
		
	st.divider()
	st.subheader('やめ時')
	st.text('基本的には80Gまで回す！')
	st.caption('防御レベルが2以下且つ演出が弱ければ50Gでやめても良し。演出の詳細については下記ボタン先の"状態示唆"項目を参照。')
	st.link_button('演出情報','https://www.slopachi-quest.com/article/bouhuri-tenjou/#i-17')
	
	st.divider()
	st.caption("L防振り FN、AT、純増5.5枚/G、天井：950G+α")
		
		
