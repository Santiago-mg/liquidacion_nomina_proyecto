import sys
sys.path.append("src")
from Model import SecretConfig

import psycopg2
from psycopg2 import Error

def conectar():
    try:
        # Reemplazar con los valores de configuración de tu base de datos
        DATABASE = SecretConfig.PGDATABASE
        USER = SecretConfig.PGUSER
        PASSWORD = SecretConfig.PGPASSWORD
        HOST = SecretConfig.PGHOST
        PORT = SecretConfig.PGPORT
        
        connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT, sslmode='require')
        return connection
    
    except (Exception, Error) as error:
        print("Error al conectar a la base de datos:", error)
        return None

def crear_tabla():
    try:
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS LiquidacionesNomina (
                    ID_Liquidacion SERIAL PRIMARY KEY,
                    ID_Empleado INT NOT NULL,
                    Fecha_Liquidacion DATE NOT NULL,
                    Salario_Base_Mensual DECIMAL(10, 2) NOT NULL,
                    Tiempo_Laborado_Horas DECIMAL(5, 2) NOT NULL,
                    Tiempo_Festivo_Laborado_Dias DECIMAL(4, 2),
                    Horas_Extra_Diurnas DECIMAL(4, 2),
                    Horas_Extra_Nocturnas DECIMAL(4, 2),
                    Horas_Extra_Festivas DECIMAL(4, 2),
                    Tiempo_Incapacidades_Dias DECIMAL(4, 2),
                    Tiempo_Licencias_No_Remuneradas_Dias DECIMAL(4, 2)
                )
            """)
            conexion.commit()
            print("Tabla 'LiquidacionesNomina' creada correctamente.")
        else:
            print("No se pudo conectar a la base de datos.")
    
    except (Exception, Error) as error:
        print("Error al crear la tabla:", error)
    
    finally:
        if conexion is not None:
            conexion.close()

# Llamar a la función para crear la tabla


# Función para insertar un nuevo registro en la tabla LiquidacionesNomina
def insertar_registro(datos):
    try:
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("""INSERT INTO LiquidacionesNomina (
                                    ID_Empleado, 
                                    Fecha_Liquidacion, 
                                    Salario_Base_Mensual, 
                                    Tiempo_Laborado_Horas, 
                                    Tiempo_Festivo_Laborado_Dias, 
                                    Horas_Extra_Diurnas, 
                                    Horas_Extra_Nocturnas, 
                                    Horas_Extra_Festivas, 
                                    Tiempo_Incapacidades_Dias, 
                                    Tiempo_Licencias_No_Remuneradas_Dias
                                ) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                           datos)
            conexion.commit()
            print("Registro insertado correctamente.")
    except (Exception, Error) as error:
        print("Error al insertar registro:", error)
    finally:
        if conexion is not None:
            conexion.close()

# Función para eliminar un registro de la tabla LiquidacionesNomina
def eliminar_registro(id_empleado):
    try:
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM LiquidacionesNomina WHERE ID_Empleado = %s", (id_empleado,))
            conexion.commit()
            print("Registro eliminado correctamente.")
            return True
    except (Exception, Error) as error:
        print("Error al eliminar registro:", error)
        return False
    finally:
        if conexion is not None:
            conexion.close()

def consultar_registro(id_empleado):
    datos_usuario = None
    try:
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT ID_Empleado, 
                    Fecha_Liquidacion, 
                    Salario_Base_Mensual, 
                    Tiempo_Laborado_Horas, 
                    Tiempo_Festivo_Laborado_Dias, 
                    Horas_Extra_Diurnas, 
                    Horas_Extra_Nocturnas, 
                    Horas_Extra_Festivas, 
                    Tiempo_Incapacidades_Dias, 
                    Tiempo_Licencias_No_Remuneradas_Dias 
                FROM LiquidacionesNomina 
                WHERE ID_Empleado = %s""", (id_empleado,))
            registro = cursor.fetchone()
            if registro is not None:
                datos_usuario = {
                    "ID_Empleado": registro[0],
                    "Fecha_Liquidacion": registro[1],
                    "Salario_Base_Mensual": registro[2],
                    "Tiempo_Laborado_Horas": registro[3],
                    "Tiempo_Festivo_Laborado_Dias": registro[4],
                    "Horas_Extra_Diurnas": registro[5],
                    "Horas_Extra_Nocturnas": registro[6],
                    "Horas_Extra_Festivas": registro[7],
                    "Tiempo_Incapacidades_Dias": registro[8],
                    "Tiempo_Licencias_No_Remuneradas_Dias": registro[9]
                }
            else:
                print("No se encontró ningún registro con el ID de empleado proporcionado.")
    except (Exception, Error) as error:
        print("Error al consultar registro:", error)
    finally:
        if conexion is not None:
            conexion.close()
    return datos_usuario

def eliminar_tabla():
    try:
        conexion = conectar()
        if conexion is not None:
            cursor = conexion.cursor()
            cursor.execute("DROP TABLE IF EXISTS LiquidacionesNomina")
            conexion.commit()
            print("Tabla 'LiquidacionesNomina' eliminada correctamente.")
        else:
            print("No se pudo conectar a la base de datos.")
    
    except (Exception, Error) as error:
        print("Error al eliminar la tabla:", error)
    
    finally:
        if conexion is not None:
            conexion.close()

# Ejemplo de uso
if __name__ == "__main__":
    # Insertar un nuevo registro
    

    consultar_registro(3)


"""    # Eliminar un registro por su ID
    eliminar_registro(1)"""
