from graphics import*
import math 
import time
import random
class cannon(Rectangle):
    def __init__(self,win,number): #initialises both the cannons
        if number == 1:
            self.color = 'dark red'
            self.P1 = Point(3,17.5)
            self.P2 = Point(5,18.25)
            self.c = Rectangle(self.P1,self.P2)
            self.c.setFill(self.color)
            self.c.setOutline(self.color)
            self.c.draw(win)
            self.cpivot = Circle(Point(4,18.25),0.35)
            self.cpivot.setFill(self.color)
            self.cpivot.setOutline(self.color)
            self.cpivot.draw(win)
            self.cshooter = Line(Point(4,18.25),Point(4,19.5))
            self.cshooter.setOutline(self.color)
            self.cshooter.setWidth(5)
            self.cshooter.draw(win)
        if number == 2:
            self.color = 'dark blue'
            x = random.randint(26,48)
            self.P1 = Point(x,17.5)
            self.P2 = Point(x+2,18.25)
            self.c = Rectangle(self.P1,self.P2)
            self.c.setFill(self.color)
            self.c.setOutline(self.color)
            self.c.draw(win)
            self.cpivot = Circle(Point(x+1,18.25),0.35)
            self.cpivot.setFill(self.color)
            self.cpivot.setOutline(self.color)
            self.cpivot.draw(win)
            self.cshooter = Line(Point(x+1,18.25),Point(x+1,19.5))
            self.cshooter.setOutline(self.color)
            self.cshooter.setWidth(5)
            self.cshooter.draw(win)
            
    def rotateLeft(self,win, theta): #to change the angle to the left
        P1 = self.cshooter.getP1()
        x = self.cshooter.getP2().getX()
        y = self.cshooter.getP2().getY()
        if theta< math.pi/2:
            theta = theta + math.pi/90
            self.cshooter.undraw()
            self.cshooter = Line(Point(4,18.25),Point(4+ math.cos(theta)*1.25,18.25 +math.sin(theta)*1.25))
            self.cshooter.setOutline(self.color)
            self.cshooter.setWidth(5)
            self.cshooter.draw(win)
        return theta
    def rotateRight(self,win, theta): #change the angle to the right
        P1 = self.cshooter.getP1()
        x = self.cshooter.getP2().getX()
        y = self.cshooter.getP2().getY()
        if theta>0:
            theta = theta - math.pi/90
            self.cshooter.undraw()
            self.cshooter = Line(Point(4,18.25),Point(4 + math.cos(theta)*1.25, 18.25 +math.sin(theta)*1.25))
            self.cshooter.setOutline(self.color)
            self.cshooter.setWidth(5)
            self.cshooter.draw(win)
        return theta
    def shoot(self, targetP1, targetP2, win, vel, theta): #to shoot the projectile and print on the screen
        g = 9.8
        x = self.cshooter.getP2().getX()
        y = self.cshooter.getP2().getY()
        ball = Circle(self.cshooter.getP2(),0.2)
        ball.setFill(self.color)
        ball.setOutline(self.color)
        ball.draw(win)
        start_time = time.time()
        while True:
            current_time=time.time()
            if ball.getP1().getX()<=50 and 17.5<ball.getP1().getY():
                x = vel*math.cos(theta)*(current_time-start_time)
                y = vel*math.sin(theta)*(current_time-start_time) - (1/2)*g*(current_time-start_time)*(current_time-start_time)
                ball.move(x,y)
                if targetP1.getX()-0.5<=ball.getCenter().getX()<=targetP2.getX()+0.5 and targetP1.getY()-0.5<=ball.getCenter().getY()<=targetP2.getY()+0.5:
                    ball.undraw()
                    explosion = Circle(ball.getCenter(),1)
                    explosion.setFill("dark orange")
                    explosion.setOutline("dark orange")
                    explosion.draw(win)
                    time.sleep(0.25)
                    explosion.undraw()
                    explosionBreak1 = Circle(ball.getP1(),0.75)
                    explosionBreak1.setFill("dark orange")
                    explosionBreak1.setOutline("dark orange")
                    explosionBreak1.draw(win)
                    explosionBreak2 = Circle(ball.getP2(),0.9)
                    explosionBreak2.setFill("dark orange")
                    explosionBreak2.setOutline("dark orange")
                    explosionBreak2.draw(win)
                    time.sleep(0.25)
                    explosionBreak1.undraw()
                    explosionBreak2.undraw()
                    return True
                    break
                time.sleep(0.005)
            else:
                ball.undraw()
                return False
                break

    def getCoords(self): #returns the coordinates of the cannon object called
        return self.P1,self.P2


    def drawProjectedPath(self,win,vel,theta): #draws the projected path
        projectedPath = []
        time = 0
        c = 0
        x = self.cshooter.getP2().getX()
        y = self.cshooter.getP2().getY()
        for i in range(40):
            time = time + 0.005
            x = x + vel*math.cos(theta)*time
            y = y + vel*math.sin(theta)*time - (1/2)*9.8*time*time 
            if i%5==0 and i>10:
                ball = Circle(Point(x,y),0.1)
                ball.setFill(self.color)
                projectedPath.append(ball)
                projectedPath[c].draw(win)
                c = c+1
        return projectedPath

    def undrawProjectedPath(projectedPath): #deletes the projected path everytime it changes
        for i in range(len(projectedPath)):
            projectedPath[i].undraw()
            
            
