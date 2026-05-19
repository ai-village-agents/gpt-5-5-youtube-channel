#!/usr/bin/env python3
"""Generate v5 visual proof frames for the thinking-partner video."""
from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W,H=1280,720
ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'assets'/'day413_thinking_partner_mockups'
OUT=ASSETS/'v5_visual_proofs'
OUT.mkdir(parents=True, exist_ok=True)
BG='#10131a'; PANEL='#151923'; CARD='#1b2130'; CARD2='#202738'; WARM='#f4f1ea'; MUTED='#b9c0cf'; DIM='#7d8597'
GOAL='#7dd3fc'; EVID='#a7f3d0'; OWN='#fbcfe8'; AMBER='#fbbf24'; RED='#fb7185'; BORDER='#3a4255'
FONT_DIR=Path('/usr/share/fonts/truetype/dejavu')
def font(size,bold=False,italic=False):
    name='DejaVuSans-Bold.ttf' if bold else ('DejaVuSans-Oblique.ttf' if italic else 'DejaVuSans.ttf')
    return ImageFont.truetype(str(FONT_DIR/name), size)
def size(d,t,f):
    b=d.textbbox((0,0),t,font=f); return b[2]-b[0], b[3]-b[1]
def center(d,xy,t,f,fill=WARM):
    x,y=xy; tw,th=size(d,t,f); d.text((x-tw/2,y-th/2),t,font=f,fill=fill)
def wrap(d,t,f,maxw):
    words=t.split(); lines=[]; cur=''
    for w in words:
        test=w if not cur else cur+' '+w
        if size(d,test,f)[0]<=maxw: cur=test
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines
def draw_wrap(d,xy,t,f,maxw,fill=WARM,gap=8):
    x,y=xy; lh=size(d,'Ag',f)[1]+gap
    for line in wrap(d,t,f,maxw):
        d.text((x,y),line,font=f,fill=fill); y+=lh
    return y
def base(title, subtitle=None):
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    d.rounded_rectangle((70,58,1210,646), radius=32, fill=PANEL, outline='#263044', width=2)
    d.ellipse((930,70,1120,260), fill='#172637', outline='#234a61', width=3)
    d.arc((110,500,245,635),200,50,fill='#463141',width=5)
    d.text((104,92),title,font=font(38,True),fill=WARM)
    if subtitle: d.text((104,142),subtitle,font=font(23),fill=MUTED)
    return im,d
def card(d,box,title=None,accent=EVID,fill=CARD):
    d.rounded_rectangle(box,radius=22,fill=fill,outline=BORDER,width=2)
    x1,y1,x2,_=box; d.rounded_rectangle((x1,y1,x2,y1+10),radius=5,fill=accent)
    if title: d.text((x1+24,y1+30),title,font=font(28,True),fill=accent)
def chip(d,xy,t,color,fs=28):
    x,y=xy; f=font(fs,True); tw,th=size(d,t,f); pad=18
    d.rounded_rectangle((x,y,x+tw+pad*2,y+th+22),radius=22,fill='#111722',outline=color,width=3)
    d.text((x+pad,y+9),t,font=f,fill=color)
    return x+tw+pad*2

def save(im,name):
    p=OUT/name
    im.save(p)
    p360=OUT/(p.stem+'_360p.png')
    im.resize((640,360),Image.Resampling.LANCZOS).save(p360)
    return p

def f1():
    im,d=base('A good answer can still be premature','Use the model as a tool — and stay the owner of the question.')
    boxes=[(126,270,430,448,'GOAL','What are we trying to do?',GOAL),(488,245,792,472,'EVIDENCE','What facts would change it?',EVID),(850,270,1154,448,'OWNERSHIP','What is mine to choose?',OWN)]
    for b in boxes:
        x1,y1,x2,y2,title,body,col=b; card(d,(x1,y1,x2,y2),title,col,CARD2); draw_wrap(d,(x1+26,y1+88),body,font(31,True),x2-x1-52,fill=WARM,gap=10)
    center(d,(640,570),'The answer should help fill the frame — not replace it.',font(30,True),WARM)
    return save(im,'v5_01_goal_evidence_ownership.png')

def f2():
    im,d=base('Evidence: what would change the answer?','Do not only ask for an explanation. Ask what would move the conclusion.')
    card(d,(105,245,570,555),'Assumptions',GOAL,CARD)
    for i,t in enumerate(['Users want fewer steps','The button is unclear','Price is not the issue']):
        d.text((140,330+i*62),'• '+t,font=font(25),fill=MUTED)
    card(d,(710,245,1175,555),'Evidence',EVID,CARD2)
    for i,t in enumerate(['Drop-off at step two','Support tickets mention sentence','Small test changes behavior']):
        d.text((745,330+i*62),'• '+t,font=font(25),fill=WARM)
    d.line((600,400,680,400),fill=EVID,width=5)
    d.polygon([(680,400),(650,382),(650,418)],fill=EVID)
    center(d,(640,620),'Turn the answer into a checklist for reality.',font(31,True),EVID)
    return save(im,'v5_03_evidence_checklist.png')

def f3():
    im,d=base('A modest habit, not a safety guarantee','Keep the choice visible — do not treat the frame as proof that advice is safe.')
    cx,cy=640,435; ro,ri=220,172
    for a0,a1,col in [(180,238,GOAL),(238,302,EVID),(302,360,RED)]:
        d.pieslice((cx-ro,cy-ro,cx+ro,cy+ro),start=a0,end=a1,fill=col)
    d.pieslice((cx-ri,cy-ri,cx+ri,cy+ri),start=180,end=360,fill=PANEL)
    d.rectangle((cx-ro-5,cy,cx+ro+5,cy+ro+10),fill=PANEL)
    center(d,(cx-ro+12,cy+42),'No help',font(21,True),GOAL)
    center(d,(cx,cy+42),'Appropriate\nreliance',font(20,True),EVID)
    center(d,(cx+ro-8,cy+42),'Blind\nacceptance',font(21,True),RED)
    import math
    angle=math.radians(180+0.47*180); nx=cx+math.cos(angle)*185; ny=cy+math.sin(angle)*185
    d.line((cx,cy,nx+4,ny+4),fill='#05070b',width=12); d.line((cx,cy,nx,ny),fill=WARM,width=9); d.ellipse((cx-17,cy-17,cx+17,cy+17),fill=WARM,outline='#05070b',width=3)
    x=168
    for label,body,col in [('GOAL','What are we trying to do?',GOAL),('EVIDENCE','What facts would change it?',EVID),('OWNERSHIP','What is mine to choose?',OWN)]:
        card(d,(x,530,x+300,610),None,col,'#101622'); d.text((x+18,546),label,font=font(18,True),fill=col); d.text((x+18,577),body,font=font(17),fill=WARM); x+=328
    d.text((104,630),'Motivated by decision-support research; not a validated intervention.',font=font(18),fill=AMBER)
    return save(im,'v5_04_modest_gauge_evidence.png')

def f4():
    im,d=base('Ownership: what is this email for?','The model can draft words. It cannot choose the relationship goal for you.')
    card(d,(170,250,1110,395),None,OWN,CARD2)
    d.text((220,300),'Draft an email: the timeline is slipping.',font=font(42,True),fill=WARM)
    x=130
    for t,c in [('repair trust?',GOAL),('set boundary?',OWN),('get a new date?',EVID),('document accountability?',AMBER)]:
        x=chip(d,(x,475),t,c,fs=25)+18
    center(d,(640,610),'Same facts. Different purpose. Different risk.',font(31,True),OWN)
    return save(im,'v5_05a_email_purpose.png')

def f5():
    im,d=base('Gentle, direct, or firm?','Concrete wording makes the human choice visible.')
    cards=[(96,245,402,535,'Gentle','“Could we revisit the timeline?”','Warmer, less boundary',GOAL),(487,215,793,565,'Direct','“I need a new date by Friday.”','Clear ask, moderate heat',OWN),(878,245,1184,535,'Firm','“I cannot commit without a new date.”','Strong boundary, higher heat',AMBER)]
    for x1,y1,x2,y2,title,quote,trade,col in cards:
        card(d,(x1,y1,x2,y2),title,col,CARD2); draw_wrap(d,(x1+24,y1+92),quote,font(28,True),x2-x1-48,fill=WARM,gap=8); draw_wrap(d,(x1+24,y2-92),trade,font(22),x2-x1-48,fill=MUTED,gap=6)
    center(d,(640,625),'The model can show options. You choose the posture.',font(31,True),OWN)
    return save(im,'v5_05b_three_wordings.png')

def f6():
    im,d=base('What am I willing to stand behind?','This is the Ownership step.')
    card(d,(120,275,560,520),'Model can show',EVID,CARD)
    draw_wrap(d,(152,378),'versions, tradeoffs, missing context, second drafts',font(28),360,fill=MUTED)
    card(d,(720,275,1160,520),'I choose',OWN,CARD2)
    draw_wrap(d,(752,378),'purpose, posture, risk, responsibility',font(28,True),360,fill=WARM)
    d.line((600,320,680,475),fill=DIM,width=5)
    center(d,(640,610),'Options are useful. Ownership is not optional.',font(32,True),OWN)
    return save(im,'v5_05c_stand_behind.png')

def f7():
    im,d=base('Keep the decision visible','Delegate options. Keep judgment.')
    y=255
    d.text((155,y),'Delegate:',font=font(32,True),fill=EVID); d.text((390,y),'options, drafts, assumptions, missing questions',font=font(30),fill=WARM)
    d.text((155,y+88),'Keep:',font=font(32,True),fill=OWN); d.text((390,y+88),'purpose, evidence standard, risk tolerance, final call',font=font(30),fill=WARM)
    x=230
    for t,c in [('Goal',GOAL),('Evidence',EVID),('Ownership',OWN)]:
        x=chip(d,(x,455),t,c,fs=36)+34
    center(d,(640,600),'Let the model widen the table. Keep your hands on the question.',font(30,True),WARM)
    return save(im,'v5_08_delegate_keep.png')

def contact(paths):
    sheet=Image.new('RGB',(1280,900),BG); d=ImageDraw.Draw(sheet)
    d.text((42,26),'Day 413 v5 visual proof contact sheet',font=font(32,True),fill=WARM)
    d.text((42,68),'Evidence label + split Ownership beats; proof only, not a render.',font=font(22),fill=MUTED)
    positions=[(40,112),(350,112),(660,112),(970,112),(40,430),(350,430),(660,430)]
    labels=['01 triplet','03 evidence','04 caveat','05a purpose','05b wordings','05c stand behind','08 ending']
    for p,(x,y),lab in zip(paths,positions,labels):
        thumb=Image.open(p).resize((270,152),Image.Resampling.LANCZOS)
        d.rounded_rectangle((x-3,y-3,x+273,y+155),radius=12,fill=PANEL,outline=BORDER,width=2)
        sheet.paste(thumb,(x,y)); d.text((x+8,y+164),lab,font=font(18,True),fill=EVID if 'evidence' in lab else OWN if '05' in lab else GOAL)
        d.text((x+8,y+190),p.name,font=font(13),fill=MUTED)
    sheet.save(ASSETS/'v5_visual_proof_contact_sheet.png')
    sheet.resize((640,450),Image.Resampling.LANCZOS).save(ASSETS/'v5_visual_proof_contact_sheet_360p.png')

def main():
    paths=[f1(),f2(),f3(),f4(),f5(),f6(),f7()]
    contact(paths)
    for p in paths: print(p.relative_to(ROOT))
    print((ASSETS/'v5_visual_proof_contact_sheet.png').relative_to(ROOT))
    print((ASSETS/'v5_visual_proof_contact_sheet_360p.png').relative_to(ROOT))
if __name__=='__main__': main()
