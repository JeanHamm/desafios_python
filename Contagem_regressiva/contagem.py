from datetime import datetime, timedelta

hora = datetime.now()

hora_texto = hora.strftime('%H:%M:%S')
menos = timedelta(seconds = 2)

total_hora = hora + menos

print(total_hora)

while(hora != total_hora):
    print('teste')