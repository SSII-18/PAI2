
file = "KPI.txt"

def generateKPI(mensajesIntegros, mensajesNoIntegros, mensajesTotales):
    with open(file, 'w') as f:
        f.write("--------------KPI-------------- \n")
        f.write("Mensajes totales recibidos: "+str(mensajesTotales)+"\n")
        f.write("Mensajes totales integros: "+str(mensajesIntegros)+"\n")
        f.write("Mensajes totales modificados o replicados: "+str(mensajesNoIntegros)+"\n")
        f.write("Porcentaje de mensajes enviados de forma integra: "+str(mensajesIntegros*100/mensajesTotales)+"%")
        f.write("\n")
        
        