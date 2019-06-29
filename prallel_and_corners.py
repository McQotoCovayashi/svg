import line
import svg
from intersection import Intersection as ints
import random as rdm
import numpy as np

width = 600
height = 400
center = (0.5*width, 0.5*height)


frame = [line.Line() for i in range(4)]
frame[0].set_2points((0,0),(width,0))
frame[1].set_2points((0,height),(width,height))
frame[2].set_2points((0,0),(0,height))
frame[3].set_2points((width,0),(width,height))

angle_l = int(rdm.choice([-1,1]) * rdm.random() * 20)
angle_m = int(rdm.choice([-1,1]) * rdm.random() * 20)+45
angle_q = int(rdm.choice([-1,1]) * (angle_l+angle_m)/2 + (rdm.random()+10) * 10)

d_l1 = 0.1*(rdm.random() + 1) * height
d_l2 = 0.1*(rdm.random() + 1) * height
d_m = 0.1*(rdm.random() + 1) * width
d_l = [-d_l1,0,d_l2]

l_n = [line.Line() for i in range(3)]
for l in range(3):
    l_n[l].set_angle_point(angle_l, (center[0],center[1] +d_l[l]))
    l_n[l].extention_xy((width,height),(0,0))

m_n = [line.Line() for i in range(2)]
for m in range(2):
    m_n[m].set_angle_point(angle_m, (center[0] + 0.5*d_m*(-1)**(m+1),center[1]))
    m_n[m].extention_xy((width,height),(0,0))

P_lm =[[[None,None],[None,None]],[[None,None],[None,None]],[[None,None],[None,None]]]
for l in range(3):
    for m in range(2):
        P_lm[l][m] = l_n[l].x_point(m_n[m])

p = line.Line()
p.set_2points(P_lm[0][0], P_lm[1][1])
p.extention_xy((width,height),(0,0))
point_pl3 = p.x_point(l_n[2])

q = line.Line()
q.set_angle_point(angle_q, P_lm[0][1])
q.extention_xy((width,height),(0,0))
Q_l = [q.x_point(l_n[0]), q.x_point(l_n[1]), q.x_point(l_n[2])]
Q_m = [q.x_point(m_n[0]), q.x_point(m_n[0])]
Q_p = q.x_point(p)

P_names = [["A","B"],["C","D"],["E","F"]]
Q_names = ["","K","L"]
Q_m_name =["M",""]
Q_p_name = "O"
point_pl3_name = "N"

text1 = ["AB//CD//EF　かつ　AE//BF である。",
    "∠{0} = {1},　∠{2} = {3},　∠{4} = {5}".format(
        "MAO",int(np.round(p.get_angle2lines(m_n[0])[0])),
        "KLE",int(np.round(q.get_angle2lines(l_n[2])[0])),
        "DFE",int(np.round(l_n[2].get_angle2lines(m_n[1])[0]))),
    " のとき、次の角度を求めよ。"]
text2 = ["(1)∠{}　　　　　　　(2)∠{}".format("test","test") ,
    "(3)∠{}　　　　　　　(4)∠{}".format("test","test") ,
    "(5)∠{}　　　　　　　(6)∠{}".format("test","test") ,
    "(7)∠{}　　　　　　　(8)∠{}".format("test","test") ,
    "(9)∠{}　　　　　　　(10)∠{}".format("test","test") ,
    ]

svg = svg.Svg()
[frame[i].write_svg(svg, stroke_width=0.5) for i in range(4)]
[l_n[l].write_svg(svg) for l in range(3)]
[m_n[m].write_svg(svg) for m in range(2)]
p.write_svg(svg)
q.write_svg(svg)
#[svg.create_text("P_{0}{1}:({2},{3})".format(l+1,m+1,int(P_lm[l][m][0]),int(P_lm[l][m][1])),width+150*m+5,25*l+15,font_size=14) for l in range(3) for m in range(2)]
#[svg.create_text("Q_l{0}:({1},{2})".format(n+1,int(Q_l[n][0]),int(Q_l[n][1])),width+5,150+12.5*n,font_size=14) for n in (0,2)]
#svg.create_text("Q_m:({0},{1})".format(int(Q_m[0][0]),int(Q_m[0][1])),width+5,200,font_size=14)
[svg.create_text(P_names[l][m],P_lm[l][m][0],P_lm[l][m][1],font_size=11) for l in range(3) for m in range(2)]
[svg.create_text(Q_names[n],Q_l[n][0],Q_l[n][1],font_size=11) for n in range(3)]
svg.create_text(Q_m_name[0],Q_m[0][0],Q_m[0][1],font_size=11)
svg.create_text(point_pl3_name,point_pl3[0],point_pl3[1],font_size=11)
svg.create_text(Q_p_name,Q_p[0],Q_p[1], font_size=11)
[svg.create_text(text1[i],5,height+16*(i+1),font_size=14) for i in range(len(text1))]
[svg.create_text(text2[i],5,height+48+60*(i+1),font_size=14) for i in range(len(text2))]
svg.set_svg(0, 0, width, height+400)
svg.save("parallels.svg")

