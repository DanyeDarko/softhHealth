from flask import Flask,jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return "Index!"

@app.route("/hello")
def hello():
   return jsonify({"saludo":"HOLA MUNDO"})

@app.route("/dispositivos")
def dispositivos():
    return jsonify({
        "softhealthCLIENT":[{
            "DATOS USUARIO":[
                {
                 "DATOS PERSONALES":[
                     {
                       "ID_USER":"dbz",
                       "CORREO":"danielbrzen@outlook.com",
                       "NOMBRE":"DANIEL",
                       "APELLIDO MAT ":"BRITO",
                       "APELLIDO PAT":"ZENDEJAS"
                     }
                  ],
                 "DATOS DIRECCION":[
                     {
                       "MUNICIPIO":"TLANEPANTLA",
                       "CALLE":"AV.SAN RAFAEL ",
                       "NUM_INT":"150",
                       "NUM_EXT":"1B",
                       "COLONIA":"TENAYO",
                       "ESTADO":"MEXICO"
                     }
                  ],    
                }  
            ],
            "DATOS DISPOSITIVO":[
                {
                 "CARACTERISTICAS":[
                     {
                       "ID_DISPOSITIVO":"SFTHLT230001",
                       "TARJETA":"NodeMCU",
                       "MODULO":"ESP8266EX",
                       "FRECUENCIA":"2.4 GHZ",
                       "AP_IF_ACTIVE":"True",
                       "CLIENT_IF_ACTIVE":"True"
                     }
                  ],
                 "NETWORK":[
                     {
                       "IP_ADD":"192.168.0.100/24",
                       "MAC":"0F:34:C2:10:F1:B5:AA:00",
                       "SSID_CLIENT_1":"RED_1",
                       "SSID_AP_1":"FALSE"
                     }
                  ],    
                }  
            ]
            }
                      
        ]}
    )

@app.route("/dispositivos/<string:dispositivo>:<string:user>:<string:correo>")
def getMember(dispositivo,user,correo):
    return jsonify({
      "DISPOSITIVO":dispositivo,
      "USER":user,
      "CORREO":correo
    
    })

if __name__ == "__main__":
     app.run(debug=True,host='10.100.34.182')