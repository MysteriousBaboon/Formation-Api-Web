# ============================================================
# 1_endpoint_simple.py — Le webhook le plus basique
# ============================================================
# Lance ce fichier :   python 1_endpoint_simple.py
# Test :
#   curl -X POST http://127.0.0.1:5001/echo \
#        -H "Content-Type: application/json" \
#        -d '{"hello": "world"}'
# ============================================================

from flask import Flask, request, jsonify

app = Flask(__name__)


# ============================================================
# Un endpoint qui renvoie ce qu'il recoit (echo)
# ============================================================
@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    print("Recu :", data)
    return jsonify({
        "tu_as_envoye": data,
        "status": "ok",
    })


# ============================================================
# Un endpoint qui calcule quelque chose
# ============================================================
@app.route("/somme", methods=["POST"])
def somme():
    data = request.get_json()
    nombres = data.get("nombres", [])
    return jsonify({
        "total": sum(nombres),
        "nb_elements": len(nombres),
    })


# ============================================================
# Healthcheck (toujours utile)
# ============================================================
@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(port=5001, debug=True)
