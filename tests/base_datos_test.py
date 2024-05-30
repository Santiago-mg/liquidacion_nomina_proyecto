import unittest
from unittest.mock import patch, MagicMock
from psycopg2 import Error
import sys
sys.path.append("src")
from Controller.DataBase import Manejo_de_datos as md

class TestDatabaseFunctions(unittest.TestCase):

    @patch('psycopg2.connect')
    def test_crear_tabla_exito(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        md.crear_tabla()
        mock_conn.cursor().execute.assert_called_once()
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch('psycopg2.connect', side_effect=Error("Error de conexión"))
    def test_crear_tabla_error(self, mock_connect):
        with self.assertLogs(level='ERROR') as log:
            md.crear_tabla()
            if log.output:
                self.assertIn('Error al crear la tabla:', log.output[0])

    @patch('psycopg2.connect')
    def test_insertar_registro_exito(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        datos_nuevo_registro = (
            1, '2024-05-16', 1600000, 160, 0, 0, 0, 0, 0, 0
        )
        expected_sql = """INSERT INTO LiquidacionesNomina (
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
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        
        md.insertar_registro(datos_nuevo_registro)
        mock_conn.cursor().execute.assert_called_once_with(expected_sql, datos_nuevo_registro)
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch('psycopg2.connect', side_effect=Error("Error de conexión"))
    def test_insertar_registro_error(self, mock_connect):
        datos_nuevo_registro = (
            1, '2024-05-16', 1600000, 160, 0, 0, 0, 0, 0, 0
        )
        with self.assertLogs(level='ERROR') as log:
            md.insertar_registro(datos_nuevo_registro)
            if log.output:
                self.assertIn('Error al insertar registro:', log.output[0])

    @patch('psycopg2.connect')
    def test_eliminar_registro_exito(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        self.assertTrue(md.eliminar_registro(1))
        mock_conn.cursor().execute.assert_called_once_with(
            "DELETE FROM LiquidacionesNomina WHERE ID_Empleado = %s", (1,))
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch('psycopg2.connect', side_effect=Error("Error de conexión"))
    def test_eliminar_registro_error(self, mock_connect):
        with self.assertLogs(level='ERROR') as log:
            self.assertFalse(md.eliminar_registro(1))
            if log.output:
                self.assertIn('Error al eliminar registro:', log.output[0])

    @patch('psycopg2.connect')
    def test_consultar_registro_exito(self, mock_conectar):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = (
            1, '2024-05-16', 1600000, 160, 0, 0, 0, 0, 0, 0
        )
        mock_conn.cursor.return_value = mock_cursor
        mock_conectar.return_value = mock_conn

        resultado = md.consultar_registro(1)

        self.assertEqual(resultado, {
            "ID_Empleado": 1,
            "Fecha_Liquidacion": '2024-05-16',
            "Salario_Base_Mensual": 1600000,
            "Tiempo_Laborado_Horas": 160,
            "Tiempo_Festivo_Laborado_Dias": 0,
            "Horas_Extra_Diurnas": 0,
            "Horas_Extra_Nocturnas": 0,
            "Horas_Extra_Festivas": 0,
            "Tiempo_Incapacidades_Dias": 0,
            "Tiempo_Licencias_No_Remuneradas_Dias": 0
        })

    @patch('psycopg2.connect')
    def test_consultar_registro_error(self, mock_conectar):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None
        mock_conn.cursor.return_value = mock_cursor
        mock_conectar.return_value = mock_conn

        resultado = md.consultar_registro(999)

        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
