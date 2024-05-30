import sys
sys.path.append("src")
from Model.LiquidadorNomina import FuncionesDeEntradaySalida, LiquidadorNominaCode
from Controller.DataBase import Manejo_de_datos

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\nMenú:")
    print("1. Calcular liquidación de nómina")
    print("2. Modificar parámetros")
    print("3. Como usar")
    print("4. Crear tabla de Liquidaciones de Nómina")
    print("5. Insertar registro en la tabla")
    print("6. Eliminar registro de la tabla")
    print("7. Consultar registro de la tabla")
    print("8. Eliminar tabla de Liquidaciones de Nómina")
    print("9. Salir")

def main():
    """Función principal del programa."""
    print("Bienvenido al sistema de liquidación de nómina")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            LiquidadorNominaCode.calcular_liquidacion_nomina()

        elif opcion == "2":
            LiquidadorNominaCode.modificar_parametros()

        elif opcion == "3":
            FuncionesDeEntradaySalida.mostrar_como_usar()

        elif opcion == "4":
            Manejo_de_datos.crear_tabla()

        elif opcion == "5":
            datos = (
                input("ID Empleado: "),
                input("Fecha de Liquidación (YYYY-MM-DD): "),
                input("Salario Base Mensual: "),
                input("Tiempo Laborado en Horas: "),
                input("Tiempo Festivo Laborado en Días: "),
                input("Horas Extra Diurnas: "),
                input("Horas Extra Nocturnas: "),
                input("Horas Extra Festivas: "),
                input("Tiempo de Incapacidades en Días: "),
                input("Tiempo de Licencias No Remuneradas en Días: ")
            )
            Manejo_de_datos.insertar_registro(datos)

        elif opcion == "6":
            id_empleado = input("ID del Empleado a eliminar: ")
            Manejo_de_datos.eliminar_registro(id_empleado)

        elif opcion == "7":
            id_empleado = input("ID del Empleado a consultar: ")
            registro = Manejo_de_datos.consultar_registro(id_empleado)
            if registro:
                print(f"\nRegistro del Empleado ID {registro['ID_Empleado']}:")
                print(f"Fecha de Liquidación: {registro['Fecha_Liquidacion']}")
                print(f"Salario Base Mensual: {registro['Salario_Base_Mensual']}")
                print(f"Tiempo Laborado en Horas: {registro['Tiempo_Laborado_Horas']}")
                print(f"Tiempo Festivo Laborado en Días: {registro['Tiempo_Festivo_Laborado_Dias']}")
                print(f"Horas Extra Diurnas: {registro['Horas_Extra_Diurnas']}")
                print(f"Horas Extra Nocturnas: {registro['Horas_Extra_Nocturnas']}")
                print(f"Horas Extra Festivas: {registro['Horas_Extra_Festivas']}")
                print(f"Tiempo de Incapacidades en Días: {registro['Tiempo_Incapacidades_Dias']}")
                print(f"Tiempo de Licencias No Remuneradas en Días: {registro['Tiempo_Licencias_No_Remuneradas_Dias']}\n")
            else:
                print("Registro no encontrado.")

        elif opcion == "8":
            Manejo_de_datos.eliminar_tabla()

        elif opcion == "9":
            print("Gracias por usar el sistema de liquidación de nómina")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
