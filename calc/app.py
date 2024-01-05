# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
  a = float(request.args.get('a'))
  b = float(request.args.get('b'))
  result = add(a, b)
  return str(result)

@app.route('/sub')
def substraction():
  a = float(request.args.get('a'))
  b = float(request.args.get('b'))
  result = sub(a,b)
  return str(result)

@app.route('/mult')
def multiplication():
  a = float(request.args.get('a'))
  b = float(request.args.get('b'))
  result = mult(a,b)
  return str(result)

@app.route('/div')
def division():
  a = float(request.args.get('a'))
  b = float(request.args.get('b'))
  result =  div(a,b)
  return str(result)


#FURTHER STUDY SECTION

operations = {
  'add': add,
  'sub': sub,
  'mult': mult,
  'div': div,
}

@app.route('/math/<operation>')
def math_operation(operation):
  operation_func = operations.get(operation)
  
  if not operation_func:
    return f"Invalid operation: {operation}", 400
  
  a = float(request.args.get('a'))
  b = float(request.args.get('b'))

  result = operation_func(a,b)
  return str(result)

