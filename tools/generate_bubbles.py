from PIL import Image, ImageDraw
from pathlib import Path

OUT=Path('app/src/main/theme/drawable-xxhdpi'); OUT.mkdir(parents=True,exist_ok=True)
W,H=120,105

def bubble(name, fill, side, tail):
    # Render 4x then downsample for smooth edges. Geometry follows the supplied iOS 120x105 bubble artwork.
    s=4; im=Image.new('RGBA',(W*s,H*s),(0,0,0,0)); d=ImageDraw.Draw(im)
    # round body: approx x=7..104, y=5..101 in original artwork
    box=(7*s,5*s,104*s,101*s)
    d.ellipse(box, fill=fill, outline=(0,0,0,255), width=2*s)
    if tail:
        if side=='right':
            pts=[(98*s,31*s),(116*s,34*s),(101*s,53*s),(94*s,53*s)]
        else:
            pts=[(22*s,31*s),(4*s,34*s),(19*s,53*s),(26*s,53*s)]
        d.polygon(pts, fill=fill)
        d.line(pts+[pts[0]], fill=(0,0,0,255), width=2*s, joint='curve')
        # hide seam where tail joins body
        if side=='right': d.line([(95*s,35*s),(98*s,50*s)], fill=fill, width=4*s)
        else: d.line([(25*s,35*s),(22*s,50*s)], fill=fill, width=4*s)
    im=im.resize((W,H),Image.Resampling.LANCZOS)
    # Android 9-patch border. Stretch only the safe center; content padding mirrors iOS CSS edge-insets.
    dst=Image.new('RGBA',(W+2,H+2),(0,0,0,0)); dst.paste(im,(1,1)); px=dst.load(); black=(0,0,0,255)
    for x in range(58,63): px[x,0]=black
    for y in range(50,55): px[0,y]=black
    if side=='right': l,t,r,b=36,33,51,27
    else: l,t,r,b=54,33,36,27
    for x in range(1+l,1+W-r): px[x,H+1]=black
    for y in range(1+t,1+H-b): px[W+1,y]=black
    dst.save(OUT/name, optimize=True)

bubble('theme_chatroom_bubble_me_01_image.9.png',(255,202,205,255),'right',True)
bubble('theme_chatroom_bubble_me_02_image.9.png',(255,202,205,255),'right',False)
bubble('theme_chatroom_bubble_you_01_image.9.png',(255,255,255,255),'left',True)
bubble('theme_chatroom_bubble_you_02_image.9.png',(255,255,255,255),'left',False)
print('Generated four Normal Pink KakaoTalk 9-patch bubbles')
