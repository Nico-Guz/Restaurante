from flask import Flask
from flask import render_template as render
from flask import redirect
from flask import request

app = Flask(__name__)

lista_usuarios = ["user1", "user2", "user3"]
lista_platos = {
    1: "papas",
    2: "arroz",
    3: "jugo"
}

sesion_iniciada = False
is_admin = False


@app.route("/", methods=["GET"])
def inicio():
    return render("inicio.html")


@app.route("/ingreso", methods=["POST"])
def ingreso():
    if request.method == "GET":
        return render("ingreso.html")
    else:
        sesion_iniciada = True
        return redirect('/perfil/<id_usuario>')


@app.route("/salir", methods=["POST"])
def salir():
    sesion_iniciada = False
    is_admin = False
    return redirect('/inicio')


@app.route("/registro", methods=["GET", "POST"])
def registro():
    return "Pagina Registro"


@app.route("/perfil/<id_usuario>", methods=["GET"])
def perfil(id_usuario):
    if id_usuario in lista_usuarios:
        return f"Perfil Usuario: {id_usuario}"
    else:
        return f"{id_usuario} No Existe"


@app.route("/perfil/<id_usuario>/pedidos", methods=["GET"])
def pedidos(id_usuario):
    if id_usuario in lista_usuarios:
        return f"Pedidos Usuario: {id_usuario}"
    else:
        return f"{id_usuario} No Existe"


@app.route("/perfil/<id_usuario>/deseos", methods=["GET"])
def deseos(id_usuario):
    if id_usuario in lista_usuarios:
        return f"Deseos Usuario: {id_usuario}"
    else:
        return f"{id_usuario} No Existe"


@app.route("/menu", methods=["GET"])
def menu():
    return "Pagina Menu"


@app.route("/menu/<id_plato>", methods=["GET"])
def detalle(id_plato):
    try:
        id_plato = int(id_plato)
    except Exception as e:
        id_plato = 0

    if id_plato in lista_platos:
        return lista_platos[id_plato]
    else:
        return f"{id_plato} No Existe"


@app.route("/carrito", methods=["GET"])
def carrito():
    return "Pagina Carrito"


@app.route("/admin", methods=["GET"])
def admin():
    if request.method == "GET":
        return render("ingreso.html")
    else:
        is_admin = True
        return redirect('admin.html')


@app.route("/admin/platos", methods=["GET", "POST"])
def gplatos():
    return "Pagina Gestion Platos"


@app.route("/admin/usuarios", methods=["GET", "POST"])
def gusuarios():
    return "Pagina Gestion Usuarios"


if __name__ == "__main__":
    app.run(port=80, debug=True)