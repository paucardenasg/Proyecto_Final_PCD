# Proyecto Final - Proyecto de Ciencia de Datos
Desde el 16 de mayo de 1929 la entrega del Premio de la Academia de Artes y Ciencias Cinematográficas, conocido popularmente como Premio Óscar, ha sido altamente famoso. Por ello, con este trabajo se creará un modelo de aprendizaje supervisado de clasificación para predecir si una película recibirá un Premio Óscar o no. Además, se realizará el *deployment* del modelo para crear todo el flujo de un sistema de ciencia de datos. Se trabajará con un conjunto de datos con información de distintas películas nominadas al Óscar con el objetivo de resolver el problema  mencionado, dicho conjunto de datos contiene $506$ registros (o filas) de películas y $19$ variables (o columnas) que explicarán más adelante. 

Una vez se hayan analizado, preprocesado y tratado los datos, se probarán distintos modelos para comparar su desempeño y elegir el más óptimo. El modelo seleccionado se utilizará dentro de la API para poder acceder a la predicción. Finalmente, se creará una imagen para subirla a *Docker* y se creará un contenedor en la plataforma *Azure* para poder acceder al servidor a través de la nube.

Este repositorio está estructurado de la siguiente manera:
+ EDA_MODEL $\Rightarrow$ Carpeta que contiene el Análisis Exploratorio de Datos (EDA por sus siglas en inglés) y el modelado
  + `Proyecto_Final.ipynb` $\rightarrow$ Jupyter Notebook que contiene el análisis exploratorio, preprocesamiento y tratamiento de datos, así como el entrenamiento, la prueba y selección del modelo
+ app $\Rightarrow$ Carpeta con lo necesario para la API
  + model $\rightarrow$ Carpeta con el modelo final seleccionado
    + `rf_classifier.pkl` Modelo de clasificación seleccionado (bosque aleatorio) en la archivo *Proyecto_Final.ipynb*
  + `Dockerfile` $\rightarrow$ Imagen para Docker
  + `deployment_project.yaml` $\rightarrow$ Manifiesto
  + `main.py` $\rightarrow$ Archivo con el desarrollo de la API y los *endpoints* necesarios
  + `requirements.txt` $\rightarrow$ Archivo de texto con las librerías necesarias para correr el `main.py` y el `deployment_project.yaml` y sus versiones correspondientes
+ data $\Rightarrow$ Carpeta con los archivos .csv con los conjuntos de datos
  + `raw_data.csv` $\rightarrow$ Archivo separado por comas con los datos en bruto, obtenidos de [kaggle.com](https://www.kaggle.com/datasets/balakrishcodes/others?select=Movie_classification.csv)
  + `tidy_data.csv` $\rightarrow$ Archivo separado por comas con los datos limpios y listos para entrenar el modelo
+ images $\Rightarrow$ Carpeta con las imágenes para evidencias el proceso de conteneirizar del servicio, subir la imagen a la nube, despliegar el servicio en la nube (clúster de Kubernetes)
  + `Cloud_pred.jpeg` $\rightarrow$ Captura de pantalla de la predicción generada con la herramienta Postman accediendo de manera externa
  + `Docker_image.png` $\rightarrow$ Captura de pantalla de la imagen en la herramienta Docker
  + `Ejecucion_contenedor.png` $\rightarrow$ Captura de pantalla de la predicción generada con la herramienta Postman accediendo de manera local
  + `Imagen_nube.png` $\rightarrow$ Captura de pantalla de la imagen en la nube
  + `Pods_cloud.jpeg` $\rightarrow$ Captura de pantalla de los *pods* en la nube
  + `proceso_contenedor.png` $\rightarrow$ Captura de pantalla del contenedor ejecutado
+ `AndTheOscarGoesTo.ipynb` $\rightarrow$ Jupyter Notebook con el reporte final del proyecto
+ `Presentación_Final.pptx` $\rightarrow$ Presentación de PowerPoint con el resumen del reporte
+ `README.md` $\rightarrow$ Archivo actual
