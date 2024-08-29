import time

def relogio():
    horas=10
    minutos=19
    segundos=30
    
    while True:
        print(f"{horas:02}:{minutos:02}:{segundos:02}")
        time.sleep(1)
        segundos+=1
        
        if segundos==60:
            segundos=0
            minutos+=1
        
        if minutos==60:
            minutos=0
            horas+=1
        
        if horas==24:
            horas=0
            
relogio()
            