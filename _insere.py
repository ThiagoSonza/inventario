import psycopg2, datetime, sys

# abre conexão com o banco
connection = psycopg2.connect(user      = "tecnos",
                              password  = "pos200",
                              host      = "192.168.22.242",
                              port      = "5432",
                              database  = "inventario")


def getPC(nome):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM inventario.devices WHERE lower(name) = '" + nome.lower() + "';")
    pc = cursor.fetchone()
    cursor.close()
    return pc


def saveIpAddr(ip, pc):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM inventario.ipaddresses WHERE ipaddr = '" + ip + "' AND device_id = " + str(pc) + ";" )
    id_ipaddr = cursor.fetchone()

    if id_ipaddr is None:
        cursor.execute("INSERT INTO inventario.ipaddresses (ipaddr, device_id, created) VALUES (%s, %s, %s);", (ip, pc, datetime.datetime.now()) )
    else:
        cursor.execute("UPDATE inventario.ipaddresses SET ipaddr = %s, updated = %s WHERE id = %s;", ( ip, datetime.datetime.now(), id_ipaddr[0] ))
    
    cursor.close()


def saveHardDisks(hd, pc):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM inventario.harddisks WHERE partition = '" + hd[0] + "' AND device_id = " + str(pc) + ";")
    id_hd = cursor.fetchone()
    
    if id_hd is None:
        cursor.execute("INSERT INTO inventario.harddisks (partition, capacity, used, available, device_id, created) VALUES (%s, %s, %s, %s, %s, %s);", (hd[0], hd[1], hd[2], hd[3], pc, datetime.datetime.now()) )
    else:
        cursor.execute('UPDATE inventario.harddisks SET capacity = %s, used = %s, available = %s, updated =  %s WHERE id = %s;', ( hd[1], hd[2], hd[3], datetime.datetime.now(), id_hd[0] ))
    
    cursor.close()   


def saveVideoCards(vc, pc):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM inventario.videocards WHERE cardname = '" + vc[0] + "' AND device_id = " + str(pc) + ";")
    id_vc = cursor.fetchone()

    if id_vc is None:
        cursor.execute("INSERT INTO inventario.videocards (cardname, memory, device_id, created) VALUES (%s, %s, %s, %s);", (vc[0], vc[1], pc, datetime.datetime.now()) )
    else:
        cursor.execute("UPDATE inventario.videocards SET cardname = %s, memory = %s, updated = %s WHERE id = %s;", ( vc[0], vc[1], datetime.datetime.now(), id_vc[0] ))

    cursor.close()  

def saveMemories(mem, pc):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM inventario.memory WHERE partnumber = '" + mem[4] + "' AND serialnumber = '" + mem[5] + "' AND device_id = " + str(pc) + ";")
    id_mem = cursor.fetchone()

    if "linux" in sys.platform.lower():
        mem[0] = int(mem[0]) /1024
    elif "win" in sys.platform.lower():
        mem[0] = int(mem[0]) /1024/1024

    if id_mem is None:
        cursor.execute("INSERT INTO inventario.memory (manufacturer, locator, type, capacity, speed, partnumber, serialnumber, device_id, created) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", ( mem[2], mem[1], mem[3], mem[0], mem[6], mem[4], mem[5], pc, datetime.datetime.now()) )
    else:
        cursor.execute("UPDATE inventario.memory SET manufacturer = %s, locator = %s, type = %s, capacity = %s, speed = %s, partnumber = %s, serialnumber = %s, updated = %s WHERE id = %s;", ( mem[2], mem[1], mem[3], mem[0], mem[6], mem[4], mem[5], datetime.datetime.now(), id_mem[0] ))

    cursor.close()

def saveSoftwares(sw, pc):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM inventario.softwares WHERE productname = '" + sw[0] + "' AND device_id = " + str(pc) + ";")
    id_sw = cursor.fetchone()[0]

    if id_sw is None:
        cursor.execute('INSERT INTO inventario.softwares (productname, version, publisher, installdata, device_id, created) values (%s, %s, %s, %s, %s, %s);', (sw[0], sw[1], sw[2], sw[3], pc, datetime.datetime.now()) )
    else:
        cursor.execute("UPDATE inventario.softwares SET version = %s, publisher = %s, installdata = %s, updated = %s WHERE id = %s;", ( sw[1], sw[2], sw[3], datetime.datetime.now(), id_sw ))
    
    cursor.close()


def saveData(idDevice, device, ipaddr, memory, hds, softwares = None, placaVideo = None):
    if idDevice is None:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO inventario.devices (manufacturer, model, serialnumber, name, macaddress, system, created, processor, lastlogin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;", ( device[0], device[1], device[2], device[3], device[4], device[6], datetime.datetime.now(), device[5], device[7], ) )
            connection.commit()
            # pega o id do computador inserido acima
            pc = cursor.fetchone()[0]
         
            # insere dados nas tabelas secundárias
            for a in ipaddr:
                saveIpAddr(a, pc)      

            for b in hds:
                saveHardDisks(b, pc)                

            if "win" in sys.platform.lower():
                for c in placaVideo:
                    saveVideoCards(c, pc)

                for e in softwares:
                    saveSoftwares(e, pc)

            for d in memory:
                saveMemories(d, pc)             

            connection.commit()
            cursor.close()
            connection.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    else:
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE inventario.devices SET manufacturer = %s, model = %s, serialnumber = %s, macaddress = %s, system = %s, updated = %s, lastlogin = %s WHERE name = %s RETURNING id;", ( device[0], device[1], device[2], device[4], device[6], datetime.datetime.now(), device[7], device[3] ))
            # pega o id do computador atualizado acima
            pc = cursor.fetchone()[0]
            cursor.close()

            for a in ipaddr:
                saveIpAddr(a, pc)
            
            for b in hds:
                saveHardDisks(b, pc)

            if "win" in sys.platform.lower():
                for c in placaVideo:
                    saveVideoCards(c, pc)

                for e in softwares:
                    saveSoftwares(e, pc)

            for d in memory:
                saveMemories(d, pc)
            
            connection.commit()            
            connection.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)