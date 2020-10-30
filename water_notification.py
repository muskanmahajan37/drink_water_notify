from plyer import notification
import time

while True:
    name ="the Institute of Medicine set the amount at around 2.7 liters, or 91 fluid ounces (fl oz) of total water a day for women and an average of around 3.7 liters (125 fl oz) daily for men"

    notification.notify( 
    title = "DRINK WATER NOW", 
    message=name , 
    app_icon = "C:\\Users\\ag16000\\Desktop\\GIT\\PYTHON_PROJECTS\\drink_water_notify\\glass.ico",
                        
            # displaying time 
    timeout=10
        ) 

    time.sleep(60*60)


