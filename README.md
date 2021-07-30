## Como funciona
## Crear base de datos y tablas
Para crear una base de datos e integrar los datos del archivo HR_Employee_Attrition.csv proporcionado, utilice docker-compose. Para crear el contenedor para esta base de datos, insertar los datos con las puntuaciones de los colaboradores hay que ejecutar el comando:

```bash
$ docker-compose up --build postgres
```

Y posteriormente ejecutar el script
```bash
$ python load_data.py
```
para crear el esquema e insertar los datos.

## Para usar el servicio
Bien puede usarse un ambiente virtual

```bash
$ conda activate myenv
```

instalar los paquetes necesarios
```bash
$ pip install -r requirements.txt
```

y correr el **flask** en la carpeta **/model**

```bash
$ export FLASK_APP=api.py
```

```bash
$ flask run
```

Los registros y las puntuaciones pueden consultarse, por ejemplo con un curl,
```bash
$ curl http://localhost:5000/employees/scores/<employee_number>
```
y las predicciones para un colaborador nuevo haciendo un post en la url http://localhost:5000/employees/predictions
