import svg
from intersection import Intersection as it
import math
import random

#平行線の角度　±27°の範囲でランダムな角度を設定
angle_para = int(27*random.random())*random.choice([1,-1])
#交差する角度　±45°〜90°の範囲でランダムな角度を設定
angle_cross = int(45*random.random()+45)*random.choice([1,-1])
#平行線となす角
angle_x = angle_para - angle_cross

#描写するエリアの広さを設定
width = 450
height = 530

#平行線の距離
d_para = int((0.2*random.random() + 0.1)*height)

#平行線の位置を決める
s_1 = (0.5*width, 0.5*height-d_para)
s_2 = (0.5*width, 0.5*height+d_para)

#平行線l,mを描画するための座標を求める
Vector_lm = (math.cos(math.radians(angle_para)), math.sin(math.radians(angle_para)))
l_0 = it((0,0), (0,1), s_1, Vector_lm)
l_1 = it((width,0), (0,1), s_1, Vector_lm)

m_0 = it((0,0), (0,1), s_2,  Vector_lm)
m_1 = it((width,0), (0,1), s_2,  Vector_lm)

#交差する直線pの描画するための座標を求める
Vector_p = (math.cos(math.radians(angle_cross)), math.sin(math.radians(angle_cross)))
p_0 = it((0,0), (1,0), (0.5*width, 0.5*height), Vector_p)
p_1 = it((0,height), (1,0), (0.5*width, 0.5*height),Vector_p)

#交点A,Bを求める
A = it(l_0, Vector_lm, (0.5*width, 0.5*height), Vector_p)
B = it(m_0, Vector_lm, (0.5*width, 0.5*height), Vector_p)

if angle_x < 0:
    angle_xx =180+angle_x
else:
    angle_xx = angle_x

#svgに描画
font = "Ubuntu Mono"
angle_poss = math.degrees(0.5*(180-angle_x))
d_poss = 14
poss =(abs(d_poss*math.cos(angle_poss)), abs(d_poss*math.sin(angle_poss)))
q = svg.Svg()
q.create_text("angle_para:{}".format(angle_para),5,25,font,14)
q.create_text("angle_cross:{}".format(angle_cross),5,40,font,14)
q.create_text("angle_xx:{}".format(angle_xx),5,55,font,14)
q.create_text("d_para:{}".format(d_para),5,70,font,14)
q.create_text("{}".format(angle_xx),A[0]+poss[0],A[1]-poss[1], font, 12)
q.create_text("x",B[0]+poss[0],B[1]-poss[1], font, 12)
q.create_line(l_0[0],l_0[1], l_1[0],l_1[1]) #線lの描写
q.create_line(m_0[0],m_0[1], m_1[0],m_1[1]) #線mの描写
q.create_line(p_0[0],p_0[1], p_1[0],p_1[1]) #線pの描写
q.set_svg(0,0,width,height)

#svgファイルに出力
q.save(name = "testParallel.svg")

