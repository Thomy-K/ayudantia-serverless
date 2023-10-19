# Creación y Despliegue de una Función Serverless en AWS con Serverless Framework

Este tutorial proporciona una guía detallada sobre cómo crear y desplegar una función serverless en AWS utilizando el Serverless Framework.

## Pre-requisitos:
- Asegúrese de tener instalado [Serverless Framework](https://www.serverless.com/framework/docs/getting-started/).
- Configure las credenciales de AWS.

## Creación de un Servicio Serverless:

### Paso 1: Crear un nuevo servicio serverless
Utilice el comando `sls create` para crear un nuevo servicio serverless. El flag `-n` permite nombrar el servicio, y el flag `-t` especifica la plantilla a utilizar, en este caso, `aws-python3`.

```bash
sls create -n ayudantia-serverless -t aws-python3
```

### Paso 2: Realizar deploy de nuestro servicio
Utilice el comando `sls deploy` para desplegar el servicio en AWS. El flag `--stage` permite especificar el entorno al que se quiere desplegar, en este caso, demo.

```bash
sls deploy --stage demo
```

## Creación de Capas Personalizadas:

### Paso 1: Crear entorno virtual de Python

```bash
python3 -m venv test_venv
```

### Paso 2: Activar el entorno virtual

```bash
# [En Ubuntu]
source test_venv/bin/activate

# [En Windows]
.\test_venv\Scripts\activate
```

### Paso 3: Verificar la versión de Python

```bash
python --version  
```

### Paso 4: Crear directorio con el nombre python

```bash
mkdir python  
```

### Paso 5: Instalar el paquete de requests en el directorio python creado en el Paso 4

```bash
pip install requests -t python  
```

### Paso 6: Creación de un archivo Zip del directorio python

```bash
# [En Ubuntu]
zip -r requests.zip python

# [En Windows]
powershell Compress-Archive python requests.zip  
```

### Paso 7: Agregar la Capa Personalizada en AWS
- En AWS, vaya a la sección de capas.
- Agregue una nueva capa y elija "Capa Personalizada".
- Seleccione y suba el archivo zip creado en el paso anterior.

### Paso 8: Asociar la Capa Personalizada a nuestra función
- En la configuración de nuestra función serverless, elija la capa personalizada recién creada.