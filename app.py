from flask import Flask ,jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)
CORS(app)
# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://dafqmexdyxwzcr:73616370bef154291dbd14a6b0598a160d2061b9526dd59746c2f9fb8db44002@ec2-54-157-16-196.compute-1.amazonaws.com:5432/d3d9d0t9gqvmrj'
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://sbqpukpltgbsob:81a92444fd4a550fa8113b687e5fe6edcc4bb72cd8f86732ae7da9b3d90ae513@ec2-3-225-213-67.compute-1.amazonaws.com:5432/dpasaokdnj2qr'
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:gonzalo@localhost/Pacientes'
#                                                   user:clave@localhost/nombreBaseDatos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)
ma=Marshmallow(app)
# defino la tabla
class Paciente(db.Model): # la clase Paciente hereda de db.Model
    id=db.Column(db.Integer, primary_key=True) #define los campos de la tabla
    nombre=db.Column(db.String(100))
    apellido=db.Column(db.String(100))
    dni=db.Column(db.Integer)
    def __init__(self,nombre,apellido,dni): #crea el constructor de la clase
        self.nombre=nombre # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.apellido=apellido
        self.dni=dni
db.create_all() # crea las tablas


# ************************************************************
class PacienteSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','apellido','dni')
paciente_schema=PacienteSchema() # para crear un paciente
pacientes_schema=PacienteSchema(many=True) # multiples registros


# crea los endpoint o rutas (json)
@app.route('/pacientes',methods=['GET'])
def get_Pacientes():
    all_pacientes=Paciente.query.all() # query.all() lo hereda de db.Model
    result=pacientes_schema.dump(all_pacientes) # .dump() lo hereda de ma.schema
    return jsonify(result)

@app.route('/pacientes/<id>',methods=['GET'])
def get_paciente(id):
    paciente=Paciente.query.get(id)
    return paciente_schema.jsonify(paciente)

@app.route('/pacientes/<id>',methods=['DELETE'])
def delete_paciente(id):
    paciente=Paciente.query.get(id)
    db.session.delete(paciente)
    db.session.commit()
    return paciente_schema.jsonify(paciente)

@app.route('/pacientes', methods=['POST']) # crea ruta o endpoint
def create_paciente():
    print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    apellido=request.json['apellido']
    dni=request.json['dni']
    new_paciente=Paciente(nombre,apellido,dni)
    db.session.add(new_paciente)
    db.session.commit()
    return paciente_schema.jsonify(new_paciente)

@app.route('/pacientes/<id>' ,methods=['PUT'])
def update_paciente(id):
    paciente=Paciente.query.get(id)
   
    nombre=request.json['nombre']
    apellido=request.json['apellido']
    dni=request.json['dni']

    paciente.nombre=nombre
    paciente.apellido=apellido
    paciente.dni=dni
    db.session.commit()
    return paciente_schema.jsonify(paciente)

# programa principal *******************************

if __name__=='__main__':
    app.run(debug=False)
    #app.run(debug=True, port=5000)
