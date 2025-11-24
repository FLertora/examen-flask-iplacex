from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# --------------- RUTA PRINCIPAL ----------------
@app.route("/")
def index():
    return render_template("index.html")

# --------------- EJERCICIO 1 -------------------
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form.get("nombre", "")
        edad = int(request.form.get("edad", 0))
        cantidad = int(request.form.get("cantidad", 0))

        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario

        # Descuentos según enunciado
        if edad < 18:
            descuento_pct = 0
        elif 18 <= edad <= 30:
            descuento_pct = 0.15
        else:
            descuento_pct = 0.25

        monto_descuento = total_sin_descuento * descuento_pct
        total_pagar = total_sin_descuento - monto_descuento

        return render_template(
            "ejercicio1_resultado.html",
            nombre=nombre,
            total_sin_descuento=total_sin_descuento,
            monto_descuento=monto_descuento,
            total_pagar=total_pagar,
        )

    return render_template("ejercicio1.html")

# --------------- EJERCICIO 2 -------------------
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    usuarios = {
        "juan": "admin",
        "pepe": "user",
    }

    if request.method == "POST":
        usuario = request.form.get("usuario", "")
        password = request.form.get("password", "")

        if usuario in usuarios and usuarios[usuario] == password:
            if usuario == "juan":
                mensaje = "Bienvenido Administrador juan"
            else:
                mensaje = "Bienvenido Usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template("ejercicio2_resultado.html", mensaje=mensaje)

    return render_template("ejercicio2.html")


if __name__ == "__main__":
    app.run(debug=True)
