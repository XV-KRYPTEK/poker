import numpy as np
import cv2
from PIL import ImageGrab
import glob
import re
import mysql.connector
import datetime

cnx = mysql.connector.connect(user='root', password='',host='localhost',database='db_poker')
cursor = cnx.cursor()

tab = [0,0,0,0]
cartes = []
carteVisible = False
files = glob.glob("cartes poker/"+"*.PNG")
couleurs = glob.glob("cartes poker/couleurs/*.PNG")


def probabilites():

        return 0
        
def paire(cartes):
        
        return 0

input('demarrer la capture en faisant Entree')

while(True):
        coords = []
        frame = ImageGrab.grab()
        img = np.array(frame.getdata(),dtype='uint8')\
        .reshape((frame.size[1],frame.size[0],3))
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img2 = img

        for i in couleurs:
                print(i)
                template = cv2.imread(i, 0)
                w, h = template.shape[::-1]
                
                res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

                threshold = 0.98
                loc = np.where( res >= threshold)

                zipe = zip(*loc[::-1])
                zipe = list(zipe)
                n_test = len(zipe)
                #print(n_test) #affiche la correspondance
                tab[couleurs.index(i)] = n_test
                
                for pt in zipe:
                        temp = str(i)
                        temp = temp.split('\\')[1].split('.')
                        coords.append(str(pt[0])+","+str(pt[1])+","+str(temp[0]))
                        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        print('--------------------------------------------------------')
        total = 0
        for couleur in tab:
            total += couleur
        print(total)
        if total!=0:
            for e in files:
                print(e)
                template = cv2.imread(e, 0)
                w, h = template.shape[::-1]
                res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
                threshold = 0.98
                loc = np.where( res >= threshold)
                           
                zipe = zip(*loc[::-1])
                zipe = list(zipe)
                n_test = len(zipe)
                print(n_test)
                for pt in zipe:
                        temp = str(e)
                        temp = temp.split('\\')[1].split('.')
                        #print("temp = "+ str(temp))
                        coords.append(str(pt[0])+","+str(pt[1]) + ","+str(temp[0]))
                        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
            print("True")
        xs = []
        couples = []
        for coord in coords:
                coord = coord.split(",")
                print("x :"+str(coord[0])+" y :"+str(coord[1])+" value: "+coord[2])
                xs.append((coord[0],coord[2]))
        xs.sort()
        print(xs)
        for i in range(len(xs)):        
                print(i)
                if len(xs)-1 != 0:
                        if (int(xs[i][0])<int(xs[i-1][0])+10) and (int(xs[i][0])>int(xs[i-1][0])-10):
                                print(str(xs[i][0])+" "+str(xs[i-1][0]))
                                couples.append((xs[i][1],xs[i-1][1]))
                                #couples.append((xs[i][0],xs[i-1][0],xs[i][1],xs[i-1][1]))
                                
        #print(xs)
        #print(couples)
        current_time = datetime.datetime.now()
        add = "INSERT INTO ensemble VALUES(NULL,'"+str(current_time)+"')"
        cursor.execute(add)
        cnx.commit()
        
        query = ("SELECT id_ensemble FROM ensemble WHERE date = '%s'")
        cursor.execute(query,(str(current_time)))
        
        for (id_ensemble) in cursor:
                print(id_ensemble)
                print("testetstetsefrd")
        
        for i in couples:
                if(len(i[1])>2):
                        #le truc est la couleur
                        print(i[1])
                        add = "INSERT INTO carte VALUES(NULL,'"+i[1]+"','"+i[0]+"','flop',NULL)"
                        cursor.execute(add)
                        cnx.commit()
                else:
                        add = "INSERT INTO carte VALUES(NULL,'"+i[0]+"','"+i[1]+"','flop',NULL)"
                        cursor.execute(add)
                        cnx.commit()
        height , width , layers =  img.shape
        new_h=int(height/1.5)
        new_w=int(width/1.5)

        resize = cv2.resize(img, (new_w, new_h)) 
        
        #cv2.imshow('Detected',resize[:,:,::-1])
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cnx.close()
cv2.destroyAllWindows()



