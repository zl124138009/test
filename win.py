

from pygame import *

Font = None
ImgOnOff=[]
LastKey = None

def showtext(win, pos, text, color, bgcolor):
    textimg = Font.render(text, 1, color, bgcolor)
    win.blit(textimg, pos)
    return pos[0] + textimg.get_width() + 5, pos[1]

def drawhistory(win, history):
    bgcolor = 50, 50, 50
    win.fill(bgcolor, (0, 0, 640, 120))
    win.blit(Font.render('Status Area', 1, (155, 155, 155), bgcolor), (2, 2))

    bgcolor = 50, 80, 80
    win.fill(bgcolor, (0, 120, 640, 480))    
    win.blit(Font.render('Event History Area', 1, (155, 155, 155), bgcolor), (2, 132))

    pos = showtext(win, (10, 30), 'Mouse Focus', (255, 255, 255), None)
    win.blit(ImgOnOff[mouse.get_focused()], pos)

    pos = showtext(win, (330, 30), 'Keyboard Focus', (255, 255, 255), None)
    win.blit(ImgOnOff[key.get_focused()], pos)

    pos = showtext(win, (10, 60), 'Input Grabbed', (255, 255, 255), None)
    win.blit(ImgOnOff[event.get_grab()], pos)

    pos = showtext(win, (330, 60), 'Last Keypress', (255, 255, 255), None)
    if LastKey:
        p = '%d, %s' % (LastKey, key.name(LastKey))
    else:
        p = 'None'
    pos = showtext(win, pos, p, bgcolor, (255, 255, 55))

    ypos = 450
    ypos_end = 150
    h = list(history)
    m = (ypos - ypos_end) / Font.get_height()
    n = len(history)
    h.reverse()
    for line in h:
        if m >= n:
            r = win.blit(line, (10, ypos - (m - n + 1) * Font.get_height()))
            ypos -= Font.get_height()
        elif m < n and ypos > ypos_end:
            r = win.blit(line, (10, ypos))
            ypos -= Font.get_height()

    p = '%s,%s' % mouse.get_pos()
    txt = Font.render(p, 1, (255, 0, 0), (50, 50, 50))
    win.blit(txt, (mouse.get_pos()[0]+15, mouse.get_pos()[1]-5))

def main():
    init()

    win = display.set_mode((640,480))
    display.set_caption("Win")

    global Font
    Font = font.Font(None,26)

    global ImgOnOff
    ImgOnOff.append(Font.render("Off", 1, (0, 0, 0), (255, 50, 50)))
    ImgOnOff.append(Font.render("On", 1, (0, 0, 0), (50, 255, 50)))

    history = []

    going = True
    while going:
        for e in event.get():
            if e.type == QUIT:
                going = False
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    going = False
                else:
                    global LastKey
                    LastKey = e.key
            if e.type == MOUSEBUTTONDOWN:
                event.set_grab(1)
            elif e.type == MOUSEBUTTONUP:
                event.set_grab(0)

            if e.type != MOUSEMOTION:
                txt = '%s:%s' % (event.event_name(e.type),e.dict)
                img = Font.render(txt, 1, (50, 200, 50), None)
                history.append(img)
                history = history[-30:]
                
        drawhistory(win,history)

        display.flip()
        time.wait(10)
    
    quit()




if __name__ == '__main__':
    main()
