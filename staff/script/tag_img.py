from PIL import Image
import sys, os, ImageDraw

#Param in percent
LOGO_WIDTH = 10
LOGO_HEIGHT = 10
RIGHT_MARGE = 1
BOTTOM_MARGE = 1


if len(sys.argv) == 3:   
    logo_path = sys.argv[1]
    img_path = sys.argv[2]

    if os.path.exists(logo_path) and os.path.isfile(logo_path): #add extenxion control
        if os.path.exists(img_path) and os.path.isfile(img_path): #add extenxion control
            #ouvrir le logo
            logo = Image.open(logo_path)
            #recuperer taille logo
            logo_w, logo_h = logo.size
            #print logo.size

            #ouvrir l image
            img = Image.open(img_path)
            #recuperer taille img
            img_w, img_h = img.size
            #print img.size

            #resize du logo
            l_w = int((img_w * (LOGO_WIDTH/100.0)))
            if logo_w != logo_h:
                l_h = int((img_h * (LOGO_HEIGHT/100.0)))
            else:
                l_h = l_w
            logo = logo.resize((l_w,l_h))
            logo_w, logo_h = logo.size
            #print logo.size

            #calcul repere logo
            m_x = int((img_w * (RIGHT_MARGE/100.0)))
            m_y = int((img_h * (BOTTOM_MARGE/100.0)))
            if m_x < m_y:
                m_y = m_x
            else:
                m_x = m_y            
            l_x = img_w - logo_w - m_x
            l_y = img_h - logo_h - m_y
            #print logo.size
            #print((m_x,m_y))
            #print((img_w,img_h))
            #print((l_x,l_y))

            #copie
            img.paste(logo, (l_x, l_y, l_x + logo_w, l_y + logo_h))

            #save
            img.save("test.jpg", "JPEG")
            
            #im = Image.new("RGB", (500,400), "white")
            #draw = ImageDraw.Draw(im)
            #into = Image.open("explication.png")
            #w,h=into.size
            #im.paste(into, (0,0,w,h))
            #im.paste(into, (300,0,300+w,h))
            #im.paste(into, (200,200,200+w,200+h))
            #del draw
            #im.save("dessin.jpg", "JPEG")
        else:
            print('Picture failed')
    else:
        print('Logo failed')
else:
    print('[usage]: python ' + sys.argv[0] + ' "logo path" ' +'"picture path"')
