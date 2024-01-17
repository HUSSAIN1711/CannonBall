from graphics import *
from Cannon import*
import math
import time

def isClicked(pClick,button):#to check if the buttons is pressed
    p1 = button.getP1()
    p2 = button.getP2()
    if p2.getX()>pClick.getX()>p1.getX() and p2.getY()>pClick.getY()>p1.getY():
        return True
    else:
        return False
    
def drawWin(win): #to draw the main template of the game
    win.setBackground('light blue')
    ground = Rectangle(Point(0,7.5),Point(50,17.5))
    ground.setFill('black')
    ground.draw(win)
    wintab = Rectangle(Point(0,0), Point(50,12.5))
    wintab.setFill('dark green')
    wintab.draw(win)
    sun = Circle(Point(45,35),2.5)
    sun.setFill('orange')
    sun.draw(win)
    instruct1 = Text(Point(32.5,10),"Click on the right and left arrows to change the angle")
    instruct2 = Text(Point(32.5,8), "Click on the up and down arrows to change the angle")
    instruct3 = Text(Point(32.5,6), "Finally, shoot")
    instruct1.setTextColor('orange')
    instruct1.setStyle('bold')
    instruct1.setSize(12)
    instruct2.setTextColor('orange')
    instruct2.setStyle('bold')
    instruct2.setSize(12)
    instruct3.setTextColor('orange')
    instruct3.setStyle('bold')
    instruct3.setSize(12)
    instruct1.draw(win)
    instruct2.draw(win)
    instruct3.draw(win)
    buttonList= []
    LeftArrowCircle = Circle(Point(2.5,6),2.5)
    LeftArrowCircle.setFill('light gray')
    LeftArrowCircle.draw(win)
    LeftArrowBody = Rectangle(Point(2.25,5.75),Point(3.5,6.25))
    LeftArrowBody.setFill('dark gray')
    LeftArrowBody.draw(win)
    LeftArrowHead = Polygon(Point(2.25,5.25),Point(2.25,6.75),Point(1.75,6))
    LeftArrowHead.setFill('dark gray')
    LeftArrowHead.draw(win)
    RightArrowCircle = Circle(Point(14.5,6),2.5)
    RightArrowCircle.setFill('light gray')
    RightArrowCircle.draw(win)
    RightArrowBody = Rectangle(Point(14.75,5.75),Point(13.5,6.25))
    RightArrowBody.setFill('dark gray')
    RightArrowBody.draw(win)
    RightArrowHead = Polygon(Point(14.75,5.25),Point(14.75,6.75),Point(15.25,6))
    RightArrowHead.setFill('dark gray')
    RightArrowHead.draw(win)
    UpArrowCircle = Circle(Point(8.5,9),2.5)
    UpArrowCircle.setFill('light gray')
    UpArrowCircle.draw(win)
    UpArrowBody = Rectangle(Point(8.25,8.25),Point(8.75,9.5))
    UpArrowBody.setFill('dark gray')
    UpArrowBody.draw(win)
    UpArrowHead = Polygon(Point(7.75,9.5),Point(9.25,9.5),Point(8.5,10))
    UpArrowHead.setFill('dark gray')
    UpArrowHead.draw(win)
    DownArrowCircle = Circle(Point(8.5,3),2.5)
    DownArrowCircle.setFill('light gray')
    DownArrowCircle.draw(win)
    DownArrowBody = Rectangle(Point(8.25,2.5),Point(8.75,3.75))
    DownArrowBody.setFill('dark gray')
    DownArrowBody.draw(win)
    DownArrowHead = Polygon(Point(7.75,2.5),Point(9.25,2.5),Point(8.5,1.75))
    DownArrowHead.setFill('dark gray')
    DownArrowHead.draw(win)
    shootButton = Rectangle(Point(27.5,1.5),Point(37.5,4.5))
    shootButton.setFill("light gray")
    shootButton.draw(win)
    shootText = Text(Point(32.5, 3), "SHOOT")
    shootText.draw(win)
    exitButton = Rectangle(Point(2,35),Point(5,37))
    exitButton.setFill('light gray')
    exitButtontext = Text(Point(3.5,36),"Exit")
    exitButton.draw(win)
    exitButtontext.draw(win)
    buttonList.append(LeftArrowCircle)
    buttonList.append(RightArrowCircle)
    buttonList.append(UpArrowCircle)
    buttonList.append(DownArrowCircle)
    buttonList.append(shootButton)
    buttonList.append(exitButton)
    return buttonList

def main(): #main function
    win = GraphWin("CannonBall", 1000,800 )
    win.setCoords(0,0,50,40)
    buttonList = drawWin(win)
    theta = math.pi/2
    vel=2.5
    AngleText = Text(Point(18.5,11), "Angle : "+(str((180/math.pi)*theta)))
    AngleText.setTextColor("orange")
    AngleText.setStyle("bold")
    AngleText.draw(win)
    VelText = Text(Point(18.5,9), "Velocity : "+(str(vel)))
    VelText.setTextColor("orange")
    VelText.setStyle('bold')
    VelText.draw(win)
    res = Rectangle(Point(20,18),Point(30,26))
    res.setFill('white')
    resText = Text(Point(25,22),"")
    c1 = cannon(win,1)
    c2 = cannon(win,2)
    projectedPath = cannon.drawProjectedPath(c1,win,vel,theta)
    while True:
        pClick = win.checkMouse()
        if pClick != None:
            
            if isClicked(pClick,buttonList[0]):#check if left arrow clicked
                theta = cannon.rotateLeft(c1,win,theta)
                AngleText.setText(f"Angle : {(180/math.pi)*theta:.2f}")
                cannon.undrawProjectedPath(projectedPath)
                projectedPath = cannon.drawProjectedPath(c1,win,vel,theta)
            elif isClicked(pClick,buttonList[1]): #check if right arrow is clicked
                theta = cannon.rotateRight(c1,win,theta)
                AngleText.setText(f"Angle : {(180/math.pi)*theta:.2f}")
                cannon.undrawProjectedPath(projectedPath)
                projectedPath = cannon.drawProjectedPath(c1,win,vel,theta)
            elif isClicked(pClick, buttonList[2]): #check if the Up arrow is clicked
                vel = vel+0.1
                VelText.setText(f"Velocity : {vel:.1f}")
                cannon.undrawProjectedPath(projectedPath)
                projectedPath = cannon.drawProjectedPath(c1,win,vel,theta)
            elif isClicked(pClick, buttonList[3]): #check if the down arrow is clicked
                vel = vel-0.1
                VelText.setText(f"Velocity : {vel:.1f}")
                cannon.undrawProjectedPath(projectedPath)
                projectedPath = cannon.drawProjectedPath(c1,win,vel,theta)
            elif isClicked(pClick,buttonList[4]): #check if shoot button is clicked
                x,y = cannon.getCoords(c2)
                hit = cannon.shoot(c1,x,y,win,vel,theta)
                if hit == True: #checks if the other cannon is hit
                    resText.setText("YOU WIN!")
                    resText.setSize(10)
                    resText.setStyle('bold')
                    res.draw(win)
                    resText.draw(win)
                    time.sleep(2.5)
                    break
                else:
                    resText.setText("Better Luck Next Time :(")
                    resText.setSize(10)
                    res.draw(win)
                    resText.draw(win)
                    time.sleep(1.5)
                    resText.setText("Try again or exit")
                    time.sleep(1.5)
                    res.undraw()
                    resText.undraw()
            
            elif isClicked(pClick,buttonList[5]): #checks if the exit button is clicked
                break
                
            else: 
                continue
    win.close()
    exit
main()
