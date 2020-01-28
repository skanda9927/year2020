#
# 41 :Python program to display astrological sign 
#  
#        PSEUDOCODE
#1: Enter the date of birth
#2: Check month with date for a specific English Astrological sign using If else condition and set astrological sign to specific astrological sign
#3:conditions for determining astrological sign is
#Aries (March 21-April 19)
#Taurus (April 20-May 20)
#Gemini (May 21-June 20)
#Cancer (June 21-July 22)
#Leo (July 23-August 22)
#Virgo (August 23-September 22)
#Libra (September 23-October 22)
#Scorpio (October 23-November 21)
#Sagittarius (November 22-December 21)
#Capricorn (December 22-January 19)
#Aquarius (January 20-February 18)
#Pisces (February 19-March 20) 



day = int (input("enter the day"))
month = int (input("enter the month"))
year = int (input("enter the year"))

# checks month and date within the valid range  of a specified zodiac

if month == 12 : 
    if (day < 22) : astro_sign = 'Sagittarius' 
    else : astro_sign = 'capricorn'

elif month == 1 : 
    if (day < 20) :   
        astro_sign = 'Capricorn'  
    else : astro_sign ='aquarius'
        
elif month == 2 : 
    if (day < 19) :
        astro_sign = 'Aquarius'  
    else : astro_sign ='pisces'
        
elif month == 3 : 
    if (day < 21) :
        astro_sign = 'Pisces'  
    else : astro_sign = 'aries'
        
elif month == 4 : 
    if (day < 20) :
        astro_sign = 'Aries'  
    else : astro_sign = 'taurus'
        
elif month == 5 : 
    if (day < 21) :
       astro_sign = 'Taurus'
    else : astro_sign = 'gemini'
        
elif month == 6 : 
    if (day < 21) :
        astro_sign = 'Gemini'  
    else : astro_sign = 'cancer'
        
elif month == 7 : 
    if (day < 23) : 
        astro_sign = 'Cancer'  
    else : astro_sign ='leo'
        
elif month == 8 : 
    if (day < 23) :   
        astro_sign = 'Leo'  
    else : astro_sign = 'virgo'
        
elif month == 9 : 
    if (day < 23) :    
        astro_sign = 'Virgo'  
    else : astro_sign = 'libra'
        
elif month == 10 : 
    if (day < 23) :    
        astro_sign = 'Libra'  
    else : astro_sign = 'scorpio'
        
elif month == 11 : 
    if (day < 22) :
        astro_sign = 'scorpio'  
    else : astro_sign = 'sagittarius'

print(astro_sign," is your English astrological sign is according to given date")     
