import sys
sys.path.append("src")
from Model.LiquidadorNomina import FuncionesDeCalculo
from Controller.DataBase import Manejo_de_datos

from flask import Flask, request, jsonify, render_template

# Crear tabla en la base de datos al iniciar la aplicación

app = Flask(__name__)

# Parámetros globales para el cálculo de la nómina
salario_minimo = 1300000
subsidio_transporte = 162000
porcentaje_aporte_salud = 0.04
porcentaje_aporte_pension = 0.04
porcentaje_extra_diurno = 0.25
porcentaje_extra_nocturno = 0.75
porcentaje_extra_festivo = 0.75
porcentaje_valor_de_incapacidad = 1.0

# Función para calcular la liquidación de nómina
def calcular_liquidacion_nomina(horas_extra_diurnas, horas_extra_nocturnas, horas_extra_festivos, tiempo_incapacidades, salario_base_mensual, tiempo_licencias_no_remuneradas, tiempo_laborado, tiempo_festivo_laborado):
    valor_hora_laborada = salario_base_mensual / 192
    valor_salario = valor_hora_laborada * tiempo_laborado
    valor_hora_extra_diurna = FuncionesDeCalculo.calcular_valor_hora_extra_diurna(valor_hora_laborada, horas_extra_diurnas)
    valor_hora_extra_nocturna = FuncionesDeCalculo.calcular_valor_hora_extra_nocturna(valor_hora_laborada, horas_extra_nocturnas)
    valor_hora_extra_festivo = FuncionesDeCalculo.calcular_valor_hora_extra_festivo(valor_hora_laborada, horas_extra_festivos)
    valor_dias_festivos = FuncionesDeCalculo.calcular_valor_dias_festivos(valor_hora_laborada, tiempo_festivo_laborado)
    valor_incapacidad = FuncionesDeCalculo.calcular_valor_incapacidad(valor_hora_laborada, tiempo_incapacidades)
    valor_licencia_no_remunerada = FuncionesDeCalculo.calcular_valor_licencia_no_remunerada(valor_hora_laborada, tiempo_licencias_no_remuneradas)
    valor_aporte_a_salud = ((valor_salario) + (subsidio_transporte) + (valor_dias_festivos) + (valor_hora_extra_diurna) + (valor_hora_extra_nocturna) + (valor_hora_extra_festivo)) * porcentaje_aporte_salud
    valor_aporte_a_pension = ((valor_salario) + (subsidio_transporte) + (valor_dias_festivos) + (valor_hora_extra_diurna) + (valor_hora_extra_nocturna) + (valor_hora_extra_festivo)) * porcentaje_aporte_pension
    valor_fondo_solidaridad_pensional = FuncionesDeCalculo.calcular_valor_fondo_solidaridad_pensional(salario_base_mensual)

    # Calcular el valor total de la nómina
    total_nomina = valor_salario + valor_hora_extra_diurna + valor_hora_extra_nocturna + valor_hora_extra_festivo - valor_licencia_no_remunerada - valor_incapacidad - valor_aporte_a_salud - valor_aporte_a_pension - valor_fondo_solidaridad_pensional

    # Devolver los componentes individuales y el total de la nómina
    return {
        "valor_salario": valor_salario,
        "valor_hora_extra_diurna": valor_hora_extra_diurna,
        "valor_hora_extra_nocturna": valor_hora_extra_nocturna,
        "valor_hora_extra_festivo": valor_hora_extra_festivo,
        "valor_licencia_no_remunerada": valor_licencia_no_remunerada,
        "valor_incapacidad": valor_incapacidad,
        "valor_aporte_a_salud": valor_aporte_a_salud,
        "valor_aporte_a_pension": valor_aporte_a_pension,
        "valor_fondo_solidaridad_pensional": valor_fondo_solidaridad_pensional,
        "total_nomina": total_nomina
    }

@app.route('/')
def inicio():
    return render_template('pagina_principal.html')

@app.route('/usuario')
def index():
    return render_template('usuario.html')

@app.route('/capturar_datos', methods=['POST'])
def capturar_datos():
    # Capturar los datos enviados desde el formulario
    cedula = request.form['Cedula']
    nombre = request.form['nombre']
    salario_base = float(request.form['salario-base'])
    tiempo_laborado = float(request.form['tiempo-laborado'])
    tiempo_festivo = float(request.form['tiempo-festivo'])
    licencias = float(request.form['licencias'])
    horas_extra_diurnas = float(request.form['horas-extras-diurnas'])
    horas_extra_nocturnas = float(request.form['horas-extras-nocturnas'])
    horas_extra_festivos = float(request.form['horas-extras-festivas'])
    incapacidades = float(request.form['incapacidades'])
    liquidacion_nomina = calcular_liquidacion_nomina(horas_extra_diurnas, horas_extra_nocturnas, horas_extra_festivos, incapacidades, salario_base, licencias, tiempo_laborado, tiempo_festivo)
    datos = (cedula, '2024-05-16', salario_base, tiempo_laborado, tiempo_festivo, horas_extra_diurnas, horas_extra_nocturnas, horas_extra_festivos, incapacidades, licencias)
    Manejo_de_datos.insertar_registro(datos)
    return jsonify({"nombre": nombre, **liquidacion_nomina})

@app.route('/eliminar')
def Eliminar_usuario():
    return render_template('Eliminar_usuario.html')

@app.route('/capturar_cedula', methods=['POST'])
def capturar_cedula():
    cedula = request.form['cedula']
    try:
        resultado = Manejo_de_datos.eliminar_registro(cedula)
        if resultado:
            return jsonify({"mensaje": "Usuario eliminado correctamente"})
        else:
            return jsonify({"error": "No se encontró el usuario con la cédula proporcionada"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/consultar')
def consultar_usuario():
    return render_template('Consultar_usuario.html')

@app.route('/consultar1', methods=['GET', 'POST'])
def consultar():
    if request.method == 'GET':
        return render_template('consultar.html')
    else:
        id_empleado = request.form['id_empleado']
        datos_usuario = Manejo_de_datos.consultar_registro(id_empleado)
        
        if datos_usuario:
            return render_template('Consultar_usuario.html', datos_usuario=datos_usuario)
        else:
            mensaje = 'Usuario no encontrado'
            return render_template('Consultar_usuario.html', mensaje=mensaje)

    


if __name__ == '__main__':
    app.run(debug=True)



