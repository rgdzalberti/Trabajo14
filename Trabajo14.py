import xml.etree.ElementTree as ET

finished = False

while finished != True:

    print('Introduce el número correspondiente a la instrucción que deseas realizar')
    print('========================================================================')
    print('0 - Cerrar programa')
    print('1 - Insertar nueva nota')
    print('2 - Imprimir todas las notas por pantalla')
    print('3 - Modificar una nota')
    print('4 - Buscar una nota')
    print('========================================================================')
    print(' ')

    switch = int(input())

    tree = ET.parse('notas.xml')
    root = tree.getroot()

    if switch == 0:
        finished = True
    if switch == 1:
        print('Opción 1 elegida')
        texto = input('Escribe el contenido de la nota a crear: ')

        notasA = ET.Element('notas')
        nota = ET.SubElement(notasA,'nota')
        contenido = ET.SubElement(nota, 'contenido')
        contenido.text = texto

        myData = ET.tostring(notasA)
        myFile = open("notas.xml", "w")
        myFile.write(myData)

        print(' ')
    if switch == 2:
        print('Opción 2 elegida')
        for nota in root:
            print("Nota" + nota.attrib['id'] + ' ' + nota[0].text)
        print(' ')
    if switch == 3:
        print('Opción 3 elegida')

        idNota = int(input("Introduce el id de la nota que quieres modificar: "))
        for nota in root.iter('nota'):
            if int(nota.attrib['id']) == idNota:
                contenidoNuevo = input('Introduce el nuevo contenido de la nota: ')
                nota[0].text = contenidoNuevo

        print(' ')
    if switch == 4:
        print('Opción 4 elegida')

        idNota = int(input("Introduce el id de la nota que quieres buscar: "))
        for nota in root.iter('nota'):
            if int(nota.attrib['id']) == idNota:
                print("Nota" + nota.attrib['id'] + ' ' + nota[0].text)

        print(' ')
    if switch > 4:
        print('Error: Número introducido incorrecto')
        print(' ')