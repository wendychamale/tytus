import os.path
from os import path
import webbrowser

def crear_tabla(tabla):
    filename = "TablaSimbolos.html"
    file = open(filename,"w",encoding='utf-8')
    file.write(reporte_tabla(tabla))
    file.close()
    webbrowser.open_new_tab(filename)

def isExist(dato):
        dato = "<td><center> - </center></td>\n"
        try:
            if hasattr(dato,"alias"):
                if dato.alias != "" or dato.alias != None:
                    dato = "<td><center>" + str(dato.alias) + "</center></td>\n"
            elif hasattr(dato,"nombre"):
                if dato.nombre != "" or dato.nombre != None:
                    dato = "<td><center>" + str(dato.nombre) + "</center></td>\n"
            elif hasattr(dato,"tipo"):
                if dato.tipo != "" or dato.tipo != None:
                    dato = "<td><center>" + str(dato.tipo) + "</center></td>\n"
            elif hasattr(dato,"columnas"):
                if dato.columnas != "" or dato.columnas != None:
                    dato = "<td><center>" + str(dato.columnas) + "</center></td>\n"
            elif hasattr(dato,"consideraciones"):
                if dato.consideraciones != "" or dato.consideraciones != None:
                    dato = "<td><center>" + str(dato.consideraciones) +"</center></td>\n"
            elif hasattr(dato,"fila"):
                if dato.fila != "" or dato.fila != None:
                    dato = "<td><center>" + str(dato.fila) + "</center></td>\n"
        except Exception:
            pass
        return dato

def reporte_tabla(tabla):
    cadena = ''
    cadena += "<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/><title>Reporte</title><style> \n"
    cadena += "table{ \n"
    cadena += "width:100%;"
    cadena += "} \n"
    cadena += "table, th, td {\n"
    cadena += "border: 1px solid black;\n"
    cadena += "border-collapse: collapse;\n"
    cadena += "}\n"
    cadena += "th, td {\n"
    cadena += "padding: 5px;\n"
    cadena += "text-align: left;\n"
    cadena += "}\n"
    cadena += "table#t01 tr:nth-child(even) {\n"
    cadena += "background-color: #eee;\n"
    cadena += "}\n"
    cadena += "table#t01 tr:nth-child(odd) {\n"
    cadena += "background-color:#fff;\n"
    cadena += "}\n"
    cadena += "table#t01 th {\n"
    cadena += "background-color: black;\n"
    cadena += "color: white;\n"
    cadena += "}\n"
    cadena += "</style></head><body><h1><center>Tabla de Símbolos</center></h1>\n"
    cadena += "<table id=\"t01\">\n"

    cadena += "<tr>\n"
    cadena += "<th><center>#</center></th>\n"
    cadena += "<th><center>Database</center></th>\n"
    cadena += "<th><center>Table</center></th>\n"
    cadena += "<th><center>ID</center></th>\n"
    cadena += "<th><center>Type</center></th>\n"
    cadena += "<th><center>Size</center></th>\n"
    cadena += "<th><center>Restriction</center></th>\n"
    #Para la tabla de simbolos de la fase 2
    cadena += "<th><center>Alias - Indice</center></th>\n"
    # cadena += "<th><center>Nombre</center></th>\n"
    cadena += "<th><center>Columnas en Indices</center></th>\n"
    cadena += "<th><center>Tipo Indice</center></th>\n"
    # cadena += "<th><center>Consideraciones</center></th>\n"
    # cadena += "<th><center>Fila</center></th>\n"
    cadena += "</tr>\n"

    # Recorrido
    contador = 0
    for db in tabla.listaBd:
        for t in db.tablas:
            for c in t.lista_de_campos:
                cadena += "<tr>\n"
                cadena += "<td><center>" + str(contador) + "</center></td>\n"
                cadena += "<td><center>" + db.nombreTabla + "</center></td>\n"
                cadena += "<td><center>" + t.nombreDeTabla + "</center></td>\n"
                cadena += "<td><center>" + c.nombre + "</center></td>\n"
                cadena += "<td><center>" + c.tipo.toString() + "</center></td>\n"
                if c.tipo.dimension != None:
                    cadena += "<td><center>" + str(c.tipo.dimension) + "</center></td>\n"
                else:
                    cadena += "<td><center> - </center></td>\n"
                if c.constraint != None:
                    listaC = []
                    for i in c.constraint:
                        listaC.append(i.toString()+":"+str(i.id))
                    cadena += "<td><center>" + ",".join(listaC) + "</center></td>\n"
                else:
                    cadena += "<td><center> - </center></td>\n"
                cadena += isExist(c)
                cadena += isExist(c)
                cadena += isExist(c)
                # cadena += isExist(c)
                # cadena += isExist(c)
                # cadena += isExist(c)
                cadena += "</tr>\n"
                contador += 1
                #print("-------------------->",db.nombreTabla,t.nombreDeTabla, c.nombre, c.tipo.toString(),c.tipo.dimension,c.constraint)

            for indice in t.lista_de_indices:
                cadena += "<tr>\n"
                cadena += "<td><center>" + str(contador) + "</center></td>\n"
                cadena += "<td><center>" + db.nombreTabla + "</center></td>\n"
                cadena += "<td><center>" + t.nombreDeTabla + "</center></td>\n"
                cadena += "<td><center>" + str(indice.nombre.id) + "</center></td>\n"
                cadena += "<td><center> INDEX" + "</center></td>\n"
                cadena += "<td><center> - </center></td>\n"
                
                cadena += isExist(indice)
                cadena += "<td><center>" + str(indice.nombre.id) + "</center></td>\n"   # ESTE ES EL ALIAS
                
                if len(indice.lRestricciones) > 0:
                    cadena += "<td><center>" + ",".join(indice.lRestricciones) + "</center></td>\n"
                else:
                    cadena += "<td><center> None </center></td>\n"
                
                cadena += "<td><center>" + " ASC </center></td>\n"   # TIPO, ASC POR DEFECTO

                cadena += "</tr>\n"
                contador += 1
    '''
    while tabla != None:
        for s in tabla.variables:
            cadena += "<tr>\n"
            cadena += "<td><center>" + str(contador) + "</center></td>\n"
            cadena += "<td><center>" + s.id + "</center></td>\n"
            cadena += "<td><center>" + s.tipo + "</center></td>\n"
            cadena += "<td><center>" + s.valor + "</center></td>\n"
            cadena += "<td><center>" + str(s.linea) + "</center></td>\n"
            cadena += "<td><center>" + str(s.columna) + "</center></td>\n"
            cadena += "</tr>\n"
            contador += 1
        tabla = tabla.anterior
    '''
    cadena += "</table>\n"
    cadena += "</body>\n"
    cadena += "</html>"
    return cadena
