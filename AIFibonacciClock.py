import datetime
import pygame
import time
import sys
white = (255,255,255)
black = (0,0,0)
red = (255,0,0,125)
green = (0,100,0)
blue = (0, 0, 255)
    
color_of_5 = 0
color_of_3 = 0
color_of_2 = 0
color_of_1 = 0
    
gamedisplay = pygame.display.set_mode((415,265))
gamedisplay.fill(white)
pygame.display.set_caption('Fibonacci Clock') 
    
num_list = [5,3,2,1,1]

hdiff_factor=[]
mdiff_factor=[]

#---------------------------------------------------------------------------------------------------
#--------------------------------count by number----------------------------------------------------
def count():
    c = 0
    for i in range (0, len(hr_factors)):
        for j in range (0, len(hr1_factors)):
            if (hr_factors[i] == hr1_factors[j]):
                c += 2
            else:
                pass
    count = len(hr_factors)+ len(hr1_factors) - c
    c = 0
    for i in range (0, len(min_factors)):
        for j in range (0, len(min1_factors)):
            if (min_factors[i] == min1_factors[j]):
                c += 2
            else:
                pass
    count = count + len(min_factors)+ len(min1_factors) - c
    return count
#---------------------------------------------------------------------------------------------------
#----------------------------count misplaced tiles--------------------------------------------------
def count_tiles():
    count1 = 0
    if (color_of_5 == color5):
        pass
    elif(color_of_5 == white) and (color5 != white):
        count1 += 1
    elif(color_of_5 != white) and (color5 == white):
        count1 += 1
    elif(color_of_5 != white) and (color5 != white) and (color_of_5 != color5):
        count1 += 2
    count2 = 0
    if (color_of_3 == color3):
        pass
    elif(color_of_3 == white) and (color3 != white):
        count2 += 1
    elif(color_of_3 != white) and (color3 == white):
        count2 += 1
    elif(color_of_3 != white) and (color3 != white) and (color_of_3 != color3):
        count2 += 2
    count3 = 0
    if (color_of_2 == color2):
        pass
    elif(color_of_2 == white) and (color2 != white):
        count3 += 1
    elif(color_of_2 != white) and (color2 == white):
        count3 += 1
    elif(color_of_2 != white) and (color2 != white) and (color_of_2 != color2):
        count3 += 2
    count4 = 0
    if (color_of_1 == color1):
        pass
    elif(color_of_1 == white) and (color1 != white):
        count4 += 1
    elif(color_of_1 != white) and (color1 == white):
        count4 += 1
    elif(color_of_1 != white) and (color1 != white) and (color_of_1 != color1):
        count4 += 2
    count5 = 0
    if (color_of_11 == color11):
        pass
    elif(color_of_11 == white) and (color11 != white):
        count5 += 1
    elif(color_of_11 != white) and (color11 == white):
        count5 += 1
    elif(color_of_11 != white) and (color11 != white) and (color_of_11 != color11):
        count5 += 2
    return count1,count2,count3,count4,count5
#----------------------------------------------------------------------------------------------------
#------------------------takes factor of given input-------------------------------------------------
def hour1_factors(d1):
        
        j=0
        while(d1 != 0):
            if(d1 >= num_list[j]):
                d1 = d1-num_list[j]
                hr1_factors.append(num_list[j])
            j+=1
        print (hr1_factors)
        
def minute1_factors(d2):
             
             j = 0
             while(d2 != 0):
                if(d2 >= num_list[j]):
                    d2 = d2-num_list[j]
                    min1_factors.append(num_list[j])
                j+=1 
             print (min1_factors)
                
#--------------------------------------------------------------------------------------------------
#---------------------takes factor of current time-------------------------------------------------
def hour_factors(d1):
        
        j=0
        while(d1 != 0):
            if(d1 >= num_list[j]):
                d1 = d1-num_list[j]
                hr_factors.append(num_list[j])
            j+=1
        print (hr_factors)
        
def minute_factors(d2):
             
             j = 0
             while(d2 != 0):
                if(d2 >= num_list[j]):
                    d2 = d2-num_list[j]
                    min_factors.append(num_list[j])
                j+=1 
             print (min_factors)

#--------------------------------------------------------------------------------------------------
#---------------------Finds the factors with least misplaced tiles---------------------------------            
def hdiff_factors(d1,d3):
    if (d1 == d3):
        hdiff_factor.append(hr1_factors)
    elif (d1>d3):
        if (5 in hr_factors) and (5 in hr1_factors):
            hdiff_factor.append(5)
        if (3 in hr_factors) and (3 in hr1_factors):
            hdiff_factor.append(3)
        if (2 in hr_factors) and (2 in hr1_factors):
            hdiff_factor.append(2)
        if (1 in hr_factors) and (1 in hr1_factors):
            hdiff_factor.append(1)
        a = 0
        b = 0
        for i in range (0, len(hdiff_factor)):
            a += hdiff_factor[i]
        for i in range (0, len(hr1_factors)):
            b += hr1_factors[i]   
        if (a == b):
            pass
        else:
            c = b - a
            j = 4
            while(c != 0):
                if(c >= num_list[j]):
                    c= c-num_list[j]
                    if (c not in hdiff_factor):
                        hdiff_factor.append(num_list[j])
                j-=1 
    else:
        if (5 in hr_factors) and (5 in hr1_factors):
            hdiff_factor.append(5)
        if (3 in hr_factors) and (3 in hr1_factors):
            hdiff_factor.append(3)
        if (2 in hr_factors) and (2 in hr1_factors):
            hdiff_factor.append(2)
        if (1 in hr_factors) and (1 in hr1_factors):
            hdiff_factor.append(1)
        a = 0
        b = 0
        for i in range (0, len(hdiff_factor)):
            a += hdiff_factor[i]
        for i in range (0, len(hr1_factors)):
            b += hr1_factors[i]
        c = b - a
        j = 4
        k = 0
        while(c != 0):
            if (c == 1):
                c = c-1
                hdiff_factor.append(1)
            if(c >= num_list[j]) and (c < 5):
                c= c-num_list[j]
                if (num_list[j] not in hdiff_factor):
                    hdiff_factor.append(num_list[j])
                elif (num_list[j] == 1):
                    hdiff_factor.append(num_list[j])
                elif (c == 1):
                    hdiff_factor.append(c)
                else:
                    c= c+num_list[j]
                j-=1
            elif(c >= num_list[k]) and (c >= 5):
                c= c-num_list[k]
                if (num_list[k] not in hdiff_factor):
                    hdiff_factor.append(num_list[k])
                else:
                    c= c+num_list[k]
                k += 1
    q = 0            
    for i in range (0, len(hdiff_factor)):
        if (hdiff_factor[i] == 1):
            q = q+1
    if (q > 2):
        hdiff_factor.remove(1)
        hdiff_factor.remove(1)
        if (2 not in hdiff_factor):
            hdiff_factor.append(2)
        else:
            hdiff_factor.remove(1)
            if (3 not in hdiff_factor):
                hdiff_factor.append(3)
    print(hdiff_factor)

def mdiff_factors(d2,d4):
    if(d2 == d4):
        mdiff_factor.append(min1_factors)
        
    elif (d2>d4):
        if (5 in min_factors) and (5 in min1_factors):
            mdiff_factor.append(5)
        if (3 in min_factors) and (3 in min1_factors):
            mdiff_factor.append(3)
        if (2 in min_factors) and (2 in min1_factors):
            mdiff_factor.append(2)
        if (1 in min_factors) and (1 in min1_factors):
            mdiff_factor.append(1)
        a = 0
        b = 0
        for i in range (0, len(mdiff_factor)):
            a += mdiff_factor[i]
        for i in range (0, len(min1_factors)):
            b += min1_factors[i]   
        if (a == b):
            pass
        else:
            c = b - a
            j = 4
            while(c != 0):
                if(c >= num_list[j]):
                    c= c-num_list[j]
                    if (c not in mdiff_factor):
                        mdiff_factor.append(num_list[j])
                j-=1
    else:
        if (5 in min_factors) and (5 in min1_factors):
            mdiff_factor.append(5)
        if (3 in min_factors) and (3 in min1_factors):
            mdiff_factor.append(3)
        if (2 in min_factors) and (2 in min1_factors):
            mdiff_factor.append(2)
        if (1 in min_factors) and (1 in min1_factors):
            mdiff_factor.append(1)
        a = 0
        b = 0
        for i in range (0, len(mdiff_factor)):
            a += mdiff_factor[i]
        for i in range (0, len(min1_factors)):
            b += min1_factors[i]
        c = b - a
        j = 4
        k = 0
        while(c != 0):
            if (c == 1):
                c = c-1
                mdiff_factor.append(1)
            elif(c >= num_list[j]) and (c < 5):
                c= c-num_list[j]
                if (num_list[j] not in mdiff_factor):
                    mdiff_factor.append(num_list[j])
                elif (num_list[j] == 1):
                    mdiff_factor.append(num_list[j])
                elif (c == 1):
                    mdiff_factor.append(c)
                else:
                    c= c+num_list[j]
                j-=1
            elif(c >= num_list[k]) and (c >= 5):
                c= c-num_list[k]
                if (num_list[k] not in mdiff_factor):
                    mdiff_factor.append(num_list[k])
                else:
                    c= c+num_list[k]
                k += 1
    q = 0            
    for i in range (0, len(mdiff_factor)):
        if (mdiff_factor[i] == 1):
            q = q+1
    if (q > 2):
        mdiff_factor.remove(1)
        mdiff_factor.remove(1)
        if (2 not in mdiff_factor):
            mdiff_factor.append(2)
        else:
            mdiff_factor.remove(1)
            if (3 not in mdiff_factor):
                mdiff_factor.append(3)
            
    print(mdiff_factor)
#---------------------------------------------------------------------------------------------------
#---------------------------Assigns color to current time ------------------------------------------            
def assign_colors():
     if (5 in hr_factors) and (5 in min_factors):
      color_of_5 = blue
     elif (5 in hr_factors):
      color_of_5 = red
     elif (5 in min_factors):
      color_of_5 = green
     else:    
      color_of_5 = white
     if (3 in hr_factors) and (3 in min_factors):
      color_of_3 = blue
     elif (3 in hr_factors):
      color_of_3 = red
     elif (3 in min_factors):
      color_of_3 = green
     else:    
      color_of_3 = white
     if (2 in hr_factors) and (2 in min_factors):
      color_of_2 = blue
     elif (2 in hr_factors):
      color_of_2 = red
     elif (2 in min_factors):
      color_of_2 = green
     else:    
      color_of_2 = white    
     if (1 in hr_factors) and (1 in min_factors):
      color_of_1 = blue
     elif (1 in hr_factors):
      color_of_1 = red
     elif (1 in min_factors):
      color_of_1 = green
     else:    
      color_of_1 = white 
     return color_of_1,color_of_11,color_of_2,color_of_3,color_of_5  
#---------------------------------------------------------------------------------------------------
#---------------------------Assigns color to input time---------------------------------------------

def reassign_colors():
    if (5 in hdiff_factor) and (5 in mdiff_factor):
        color5 = blue
    elif(5 in hdiff_factor) and (5 not in mdiff_factor):
        color5 = red
    elif(5 not in hdiff_factor) and (5 in mdiff_factor):
        color5 = green
    elif(5 not in hdiff_factor) and (5 not in mdiff_factor):
        color5 = white
    if (3 in hdiff_factor) and (3 in mdiff_factor):
        color3 = blue
    elif(3 in hdiff_factor) and (3 not in mdiff_factor):
        color3 = red
    elif(3 not in hdiff_factor) and (3 in mdiff_factor):
        color3 = green
    elif(3 not in hdiff_factor) and (3 not in mdiff_factor):
        color3 = white
    if (2 in hdiff_factor) and (2 in mdiff_factor):
        color2 = blue
    elif(2 in hdiff_factor) and (2 not in mdiff_factor):
        color2 = red
    elif(2 not in hdiff_factor) and (2 in mdiff_factor):
        color2 = green
    elif(2 not in hdiff_factor) and (2 not in mdiff_factor):
        color2 = white
    if (1 in hdiff_factor) and (1 in mdiff_factor):
        color1 = blue
    elif(1 in hdiff_factor) and (1 not in mdiff_factor):
        color1 = red
    elif(1 not in hdiff_factor) and (1 in mdiff_factor):
        color1 = green
    elif(1 not in hdiff_factor) and (1 not in mdiff_factor):
        color1 = white
    a = 0
    b = 0
    for i in range (0, len(hdiff_factor)):
        if (hdiff_factor[i] == 1 ):
            a +=1
    for i in range (0, len(mdiff_factor)):
        if (mdiff_factor[i] == 1 ):
            b +=1
    print(a,b)
    if (a == 2) and (b == 2):
        color11 = blue
    elif (a == 2) and (b != 2):
        color11 = red
    elif (a != 2) and (b == 2):
        color11 = green
    else:
        color11 = white
    return color1,color11,color2,color3,color5  
#--------------------------------------------------------------------------------------------------

t = datetime.datetime.now()
hr = 5#t.hour
mn = 30#t.minute
    
if (hr==00) or (hr==12):
    color_of_11 = red
    hr = 12
else:
    color_of_11 = white
    
mn5 = mn%5
if (mn5 == 0):
    mn = mn/5
else:
    mn = mn-mn5
    mn = mn/5
if(hr > 12):
    hr = hr-12
d1 = hr
d2 = mn
hr_factors = []
min_factors = []
    
hour_factors(d1)
minute_factors(d2)


#--------------------------------------------------------------------------------------------------
#-----------------------Displaying current time----------------------------------------------------
    
color_of_1,color_of_11,color_of_2,color_of_3,color_of_5 = assign_colors()  
 
pygame.draw.rect(gamedisplay,black,[0,0,5,265])
pygame.draw.rect(gamedisplay,black,[5,0,415,5])
r2 = pygame.draw.rect(gamedisplay,color_of_2,[5,5,100,105])
pygame.draw.rect(gamedisplay,black,[105,5,5,105])
r1 = pygame.draw.rect(gamedisplay,color_of_1,[110,5,50,50])
pygame.draw.rect(gamedisplay,black,[110,55,50,5])
r11 = pygame.draw.rect(gamedisplay,color_of_11,[110,60,50,50])
pygame.draw.rect(gamedisplay,black,[160,5,5,265])
pygame.draw.rect(gamedisplay,black,[5,110,160,5])
r3=pygame.draw.rect(gamedisplay,color_of_3,[5,115,155,150])
pygame.draw.rect(gamedisplay,black,[5,260,415,5])
pygame.draw.rect(gamedisplay,black,[160,5,5,400])
r4 = pygame.draw.rect(gamedisplay,color_of_5,[165,5,250,255])
pygame.draw.rect(gamedisplay,black,[410,5,5,405])
pygame.display.update()   

#--------------------------------------------------------------------------------------------------
 
hr1 = int(input("Enter hours:")) 
mn1 = int(input("Enter minutes:")) 
print(hr1,mn1)
    
mn5 = mn1%5
if (mn5 == 0):
    mn1 = mn1/5
else:
    mn1 = mn1-mn5
    mn1 = mn1/5
if(hr1 > 12):
    hr1 = hr1-12
d3 = hr1
d4 = mn1
hr1_factors = []
min1_factors = []
hour1_factors(d3)
minute1_factors(d4)
hdiff_factors(d1,d3)
mdiff_factors(d2,d4)
worst = count()
color1,color11,color2,color3,color5 = reassign_colors() 

count1,count2,count3,count4,count5 = count_tiles()
#--------------------------------------------------------------------------------------------------
#--------------------------assigning color to least misplaced tiles--------------------------------
while (1):
        
    
    pygame.time.wait(2000)
    pygame.draw.rect(gamedisplay,black,[0,0,5,265])
    pygame.draw.rect(gamedisplay,black,[5,0,415,5])
    r11 = pygame.draw.rect(gamedisplay,color11,[110,60,50,50])
    print ("least no of misplaced tiles for r11", count5)
    pygame.time.wait(1000)
    pygame.display.update(r11)
    r1 = pygame.draw.rect(gamedisplay,color1,[110,5,50,50])
    print ("least no of misplaced tiles for r1", count4)
    pygame.time.wait(1000)
    pygame.display.update(r1)
    r2 = pygame.draw.rect(gamedisplay,color2,[5,5,100,105])
    print ("least no of misplaced tiles for r2", count3)
    pygame.time.wait(1000)
    pygame.display.update(r2)
    pygame.draw.rect(gamedisplay,black,[105,5,5,105])
    pygame.draw.rect(gamedisplay,black,[110,55,50,5])
    pygame.draw.rect(gamedisplay,black,[160,5,5,265])
    pygame.draw.rect(gamedisplay,black,[5,110,160,5])
    r3=pygame.draw.rect(gamedisplay,color3,[5,115,155,150])
    print ("least no of misplaced tiles for r3", count2)
    pygame.time.wait(1000)
    pygame.display.update(r3)
    pygame.draw.rect(gamedisplay,black,[5,260,415,5])
    pygame.draw.rect(gamedisplay,black,[160,5,5,400])
    r5 = pygame.draw.rect(gamedisplay,color5,[165,5,250,255])
    print ("least no of misplaced tiles for r5", count1)
    pygame.time.wait(1000)
    pygame.display.update(r5)
    pygame.draw.rect(gamedisplay,black,[410,5,5,405])
    print ("total tiles misplaced to reach the solution", count1 + count2 + count3 + count4 + count5 )
    #print ("Max no of tiles misplaced to reach the solution", worst) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    