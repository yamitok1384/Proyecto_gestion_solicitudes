Guía de Instalación del Proyecto

Esta guía te ayudará a configurar y ejecutar el proyecto tanto en el frontend como en el backend.
1. Backend (Django REST Framework)

Para poner en marcha el backend, sigue estos pasos:

    Asegúrate de tener Python y pip instalados.

    Crea y activa un entorno virtual:

        En macOS/Linux:

        python3 -m venv nombre-de-tu-entorno
        source nombre-de-tu-entorno/bin/activate

        En Windows:

        python3 -m venv nombre-de-tu-entorno
        nombre-de-tu-entorno\Scripts\activate

    Instala las dependencias del proyecto:

        Navega a la carpeta donde se encuentra el archivo requirements.txt.

        Ejecuta el siguiente comando para instalar todos los paquetes necesarios:

        pip install -r requirements.txt

2. Frontend (Angular)

Para el frontend de Angular, el proceso es muy similar:

    Clona o descarga el proyecto. Ten en cuenta que la carpeta node_modules no estará presente en el repositorio.

    Asegúrate de tener Node.js y npm instalados.

    Abre la terminal en la carpeta raíz de tu proyecto.

    Instala las dependencias:

        Ejecuta el siguiente comando para que npm lea el archivo package.json e instale todas las librerías necesarias:

        npm install

    Ejecuta el proyecto:

        Una vez que todas las dependencias estén instaladas, puedes iniciar la aplicación con:

        ng serve

    Esto iniciará un servidor de desarrollo y tu aplicación estará disponible en http://localhost:4200/.

3. Configuración Adicional

Asegúrate de que el backend y el frontend están correctamente configurados para comunicarse entre sí. Revisa los archivos de configuración (como environment.ts en Angular o settings.py en Django) para verificar que las URLs de las APIs sean correctas.
