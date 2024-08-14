import streamlit as st
from display import tjz

def bancho4():
	st.title('スマスロ 押忍！番長4')
	st.text('特訓間不問の狙い目とする')
	morning = st.checkbox('朝イチ',value=False)
	seven = st.checkbox('700超えの履歴あり', value=False)
	osu = st.checkbox('押忍モード確定(赤オーラ)', value=False)
	thru = st.slider('スルー回数', 0,4,0,1)
	reg = st.slider('うちRB回数', 0,3,0,1)
	samai = st.slider('0から有利差枚',-2100,1300,0,50)
	t = 65535
	if samai >= 1200:
		t = 0
	
	elif morning:
		if thru == 0:
			t = 400
		elif thru == 1:
			if seven:
				t = 0
			else:
				if reg == 0:
					if osu:
						t = 40
					else:
						t = 130
				elif reg == 1:
					t = 0
				else:
					st.write('エラー:RB回数がスルー回数より多くなっています')
		else:
			t = 0
	else:
		if thru == 0:
			t = 470
		elif thru == 1:
			if seven:
				t = 390
			else:
				t = 460
		elif thru == 2:
			if seven:
				if reg == 0:
					t = 200
				elif reg == 1:
					if osu:
						t = 40
					else:
						t = 150
				elif reg ==2:
					if osu:
						t = 20
					else:
						t = 100
				else:
					st.write('エラー:RB回数がスルー回数より多くなっています')
					
			else:
				if reg == 0 or reg ==1:
					t = 460
				elif reg ==2:
					t = 430
				else:
					st.write('エラー:RB回数がスルー回数より多くなっています')
		elif thru == 3:
			if seven:
				t =0
			else:
				if reg == 0:
					t =200
				elif reg ==1:
					if osu:
						t =40
					else:
						t = 150
				elif reg ==2:
					if osu:
						t =20
					else:
						t =100
				elif reg ==3:
					t = 0
				else:
					st.write('エラー:RB回数がスルー回数より多くなっています')
		elif thru >= 4:
			t =0
	
		else:
			st.write('Error')
		
		if samai >= 250 and samai < 1200:
			t = t-10
		elif samai <= -1000 and samai >= -2000:
			t = t + 10
		elif samai < -2000:
			t = t + 20
		
	with st.container(border=True):
		tjz(t)
		
		
	st.divider()
	st.caption("L押忍！番長4 A3、AT、下位純増2.7枚/G　上位純増4.5枚/G、ボーナス天井699G+α、スルー天井10回（設定変更時は7回）")
	
