from dataclasses import replace
from datetime import datetime
import sqlite3

from flask import flash
import templates.enviaremail as enviaremail

DB_NAME='bdecommerce.s3db'

def conexion():
    conn=sqlite3.connect(DB_NAME)
    return conn

def adicionar_registros(nombre,apellido,usuario,p1):
    cod_ver=str(datetime.now())
    cod_ver=cod_ver.replace("-","")
    cod_ver=cod_ver.replace(" ","")
    cod_ver=cod_ver.replace(":","")
    cod_ver=cod_ver.replace(".","")

    try:
        db=conexion()
        cursor=db.cursor()
        sql='INSERT INTO usuario(nombre,apellido,usuario,passwd,cod_verificacion,verificado,id_rol) VALUES(?,?,?,?,?,?,?)'
        cursor.execute(sql,[nombre,apellido,usuario,p1,cod_ver,1,1])
        db.commit()
        enviaremail.enviar_email(usuario,cod_ver)
        return True
    except:
        return False

def validacion_login(usu):
    
    try:
        db=conexion()
        cursor=db.cursor()
        sql='SELECT * FROM usuario WHERE usuario=?'
        cursor.execute(sql,[usu])
        resultado=cursor.fetchone()
        datos=[
            {
                'id':resultado[0],
                'nombre':resultado[1],
                'apellido':resultado[2],
                'usuario':resultado[3],
                'passwd':resultado[4],
                'codverificacion':resultado[5],
                'verificado':resultado[6],
                'rol':resultado[7]
            }
                ]
        return datos
    except:
        return False   


def activar_cuenta(usu,codver):
    try:
        db=conexion()
        cursor=db.cursor()
        sql='UPDATE usuario SET verificado=1 WHERE usuario=? AND cod_verificacion=?'
        cursor.execute(sql,[usu,codver])
        db.commit()
        return True      
    except:
        return False


def listar_usuario(usu):
    try:
        db=conexion()
        cursor=db.cursor()
        sql='SELECT * FROM usuario WHERE usuario<>?'
        cursor.execute(sql,[usu])
        resultado=cursor.fetchall()
        usuarios=[]
        for u in resultado:
            registro={
                    'id':u[0],
                    'nombre':u[1],
                    'apellido':u[2],
                    'usuario':u[3],
                    'rol':u[7]
                }
            usuarios.append(registro)        
                    
        return usuarios
    except:
        return False   


def adicionar_mensajes(rem,dest,asunto,cuerpo):
    try:
        db=conexion()
        cursor=db.cursor()
        sql='INSERT INTO mensajeria(remitente,destinatario,asunto,mensaje) VALUES(?,?,?,?)'
        cursor.execute(sql,[rem,dest,asunto,cuerpo])
        db.commit()
        return True
    except:
        return False

def listar_mensajes(usu):
    try:
        db=conexion()
        cursor=db.cursor()
        sql='SELECT * FROM mensajeria WHERE remitente=? OR destinatario=?'
        cursor.execute(sql,[usu,usu])
        resultado=cursor.fetchall()
        usuarios=[]
        for u in resultado:
            registro={
                    'id':u[0],
                    'remitente':u[1],
                    'destinatario':u[2],
                    'asunto':u[3],
                    'mensaje':u[4],
                    'fecha':u[5]
                }
            usuarios.append(registro)        
                    
        return usuarios
    except:
        return False   