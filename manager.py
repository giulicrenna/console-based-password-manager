from sqlite3.dbapi2 import connect
import sys, os
import sqlite3
import time
import re
import pandas as pd

class Db:   # Drives the data base
    def __init__(self, account, password, web, category):
        try:
            self.connector = sqlite3.connect("data_base.db")
            self.cursor = self.connector.cursor()
            self.account = account
            self.password = password
            self.category = category  
            self.web = web
        except:
            pass
    def action(self):  #Creates the DB if not exists
        cat = ['cuentas_de_correo', 'cuentas_bancarias', 'entretenimiento',
        'juegos', 'redes_sociales', 'otros',]
        for i in cat:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS {} (web TEXT UNIQUE, account TEXT, password TEXT)'''.format(i))
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS pass (pass TEXT UNIQUE)''')
    def pass_select(self):
        selection = self.cursor.execute('''SELECT * from pass''')
        return selection
    def pass_add(self):
        self.cursor.execute('''INSERT INTO pass(pass) values ('{}')'''.format(self.password))
        self.connector.commit()
        self.connector.close()
    def see_data(self):  #Shows the data
        result = self.cursor.execute('''SELECT * FROM {}'''.format(self.category))
        return(result)
    def add_data(self): #Add the data into the db
        self.cursor.execute('''INSERT INTO {cat}(account, password, web) values
                    ('{acc}', '{passw}', '{wb}')'''.format(cat=self.category, acc=self.account, passw=self.password, wb=self.web))
        self.connector.commit()
        self.connector.close()
    def erase_data(self):
        self.cursor.execute('DELETE FROM "{cat}" WHERE web= "{wb}"'.format(cat=self.category, wb=self.web))
        self.connector.commit()
        self.connector.close()

def first_time():
    try:
        data_base = Db('', '', '', '')
        data_base.action()
        os.system('color 01')
    except:
        pass
    try:
        def Checker():
            checker = Db('', '', '', '')
            checker_select = checker.pass_select()
            count = 0
            for i in checker_select:
                count += 1
            if count == 0:
                print('ESTABLEZCA  UNA CONTRASEÑA:')
                passw = input('>> ')
                print('REPITA LA CONTRASEÑA')
                passw_2 = input('>> ')
                if passw != passw_2:
                    print('LAS CONTRASEÑAS NO COINCIDEN')
                    time.sleep(3)
                    Checker()
                elif passw == passw_2:
                    data_base_2 = Db('', '{}'.format(passw), '', '')
                    data_base_2.pass_add()
                    print('CONTRASEÑA AÑADIDA EXITOSAMENTE!')
                    time.sleep(3)
            elif count != 0:
                pass
    except:
        pass
    Checker()
def visualizer():
    os.system('cls')
    try:
        category = input('SELECCIONAR CATEGORIA A VISUALIZAR:\n• 1-cuentas de correo\n• 2-cuentas bancarias\n• 3-entretenimiento\n• 4-juegos\n• 5-redes sociales\n• 6-otros\n >> ')
        if category:
            if category == '1':
                category = 'cuentas_de_correo'
            elif category == '2':
                category = 'cuentas_bancarias'
            elif category == '3':
                category = 'entretenimiento'
            elif category == '4':
                category = 'juegos'
            elif category == '5':
                category = 'redes_sociales'
            elif category == '6':
                category = 'otros'
            else:
                pass
        else:
            print('No existe esa categoría')
            time.sleep(2)
            visualizer()
        os.system('cls')
        connection = sqlite3.connect("data_base.db")
        table = pd.read_sql_query('SELECT * FROM {};'.format(category), connection)
        print(table.head())
        connection.close()
        input('\nAPRETAR ENTER PARA VOLVER AL MENÚ > ')
    except:
        pass
def delete():
    os.system('cls')
    try:
        os.system('cls')
        category = input('SELECCIONAR CATEGORIA:\n• 1-cuentas de correo\n• 2-cuentas bancarias\n• 3-entretenimiento\n• 4-juegos\n• 5-redes sociales\n• 6-otros\n >> ')
        if category:
            if category == '1':
                category = 'cuentas_de_correo'
            elif category == '2':
                category = 'cuentas_bancarias'
            elif category == '3':
                category = 'entretenimiento'
            elif category == '4':
                category = 'juegos'
            elif category == '5':
                category = 'redes_sociales'
            elif category == '6':
                category = 'otros'
            else:
                pass
        else:
            print('No existe esa categoría')
            time.sleep(2)
            delete()
        os.system('cls')

        connection = sqlite3.connect("data_base.db")
        table = pd.read_sql_query('SELECT * FROM {};'.format(category), connection)
        print(table.head())
        connection.close()

        web = input('Dominio a eliminar >> ')
        os.system('cls')
        opcion = input('¿Son los datos correctos? (si o no) \n Dominio > {web} \n'.format(web=web))
        if opcion.lower() == 'si':
            db = Db('', '', web, category)
            db.erase_data()
        elif opcion.lower() == 'no':
            time.sleep(2)
            delete()
        else:
            print('Mala elección')
            time.sleep(2)
            delete()
        print('\nCuenta eliminada exitosamente')
        time.sleep(3)
    except:
        print('\nEsa cuenta no existe')
        time.sleep(3)
        os.system('cls')
        delete()
def add():
    os.system('cls')
    try:
        os.system('cls')
        category = input('SELECCIONAR CATEGORIA:\n• 1-cuentas de correo\n• 2-cuentas bancarias\n• 3-entretenimiento\n• 4-juegos\n• 5-redes sociales\n• 6-otros\n >> ')
        if category:
            if category == '1':
                category = 'cuentas_de_correo'
            elif category == '2':
                category = 'cuentas_bancarias'
            elif category == '3':
                category = 'entretenimiento'
            elif category == '4':
                category = 'juegos'
            elif category == '5':
                category = 'redes_sociales'
            elif category == '6':
                category = 'otros'
            else:
                pass
        else:
            print('No existe esa categoría')
            time.sleep(2)
            add()
        
        connection = sqlite3.connect("data_base.db")
        table = pd.read_sql_query('SELECT * FROM {};'.format(category), connection)
        print(table.head())
        connection.close()

        web = input('\nDominio >> ')
        mail = input('Nombre de usuario >> ')
        passw = input('Contraseña >> ')
        os.system('cls')
        opcion = input('¿Son los datos correctos? (si o no) \n Dominio > {us}\n Usuario > {ma}\n Contraseña > {pa}\n >> '.format(us=web, ma=mail, pa=passw))
        if opcion.lower() == 'si':
            db = Db(mail, passw, web, category)
            db.add_data()
        elif opcion.lower() == 'no':
            time.sleep(2)
            add()
        else:
            print('Mala elección')
            time.sleep(2)
            add()
        print('\nCuenta agregada exitosamente')
        time.sleep(3)
    except:
        print('No puede haber dos dominios iguales')
        time.sleep(3)
        add()
def passw_changer():
    try:
        os.system('cls')
        print('\nCAMBIAR CONTRASEÑA DEL PROGRAMA\n\n')
        connection = sqlite3.connect('data_base.db')
        cursor = connection.cursor()
        old_passw = cursor.execute('SELECT pass from pass')
        for i in old_passw:
            old_passw = i
        old_passw = str(old_passw)
        old_passw = old_passw.strip("(),'")
        check = input('Escriba la contraseña anterior >> ')
        if check == old_passw:
            new_passw = input("\nEscriba la nueva contraseña >> ")
            new_check = input("Reescriba la nueva contraseña >> ")
            if new_passw == new_check:
                cursor.execute('UPDATE pass SET pass=REPLACE(pass,"{old}","{new}")'.format(new=new_passw, old=old_passw))
                print("\nContraseña actualizada exitosamente")
                connection.commit()
                connection.close()  
                time.sleep(4)
            else:
                print('\nLas contraseñas no coinciden')
                time.sleep(3)
                passw_changer()
        else:
            print("Las contraseñas no coinciden")
          
    except Exception as e:
        print(e)
        time.sleep(7)
def blocker():
    os.system('cls')
    try:
        conn = sqlite3.connect("data_base.db")
        cur = conn.cursor()
        passw = cur.execute("SELECT * FROM pass")
        for i in passw:
            passw = i
        passw = str(passw)
        passw = passw.strip("(),'")
        check = input('\nContraseña > ')
        if check == passw:
            print('Contraseña correcta!')
            time.sleep(3)
            while True:
                manager()
        else:
            print('\n\nContraseña incorrecta')
            time.sleep(3)
            blocker()
    except:
        pass
def manager():
    os.system('cls')
    print("      PASSWORD MANAGER OPTIONS \n\n")
    print(" 1 >> Agregar Usuario y contraseña\n")
    print(" 2 >> Eliminar Usuario y contraseña\n")
    print(" 3 >> Visualizar contraseñas\n")
    print(" 4 >> Cambiar pass del programa\n")
    print(" 5 >> cerrar programa\n\n\n")
    opcion = input("O >> ")
    if opcion == '1':
        add()
    elif opcion == '2':
        delete()
    elif opcion == '3':
        visualizer()
    elif opcion == '4':
        passw_changer()
    elif opcion == '5':
        sys.exit()
    else:
        print('Mala elección')
        time.sleep(2)
        manager()
if __name__ == "__main__":
    first_time()
    blocker()
