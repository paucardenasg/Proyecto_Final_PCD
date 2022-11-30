# Proyecto Final - Proyecto de Ciencia de Datos
Desde el 16 de mayo de 1929 la entrega del Premio de la Academia de Artes y Ciencias Cinematográficas, conocido popularmente como Premio Óscar, ha sido altamente conocido. Por ello, con este trabajo se creará un modelo de aprendizaje supervisado de clasificación para predecir si una película recibirá un Premio Óscar o no. Además, se realizará el *deployment* del modelo para crear todo el flujo de un sistema de ciencia de datos. Se trabajará con un conjunto de datos con información de distintas películas nominadas al Óscar con el objetivo de resolver el problema  mencionado, dicho conjunto de datos contiene $506$ registros (o filas) de películas y $19$ variables (o columnas) que explicarán más adelante. 

Una vez se hayan analizado, preprocesado y tratado los datos, se probarán distintos modelos para comparar su desempeño y elegir el más óptimo. El modelo seleccionado se utilizará dentro de la API para poder acceder a la predicción. Finalmente, se creará una imagen para subirla a *Docker* y se creará un contenedor en la plataforma *Azure* para poder acceder al servidor a través de la nube.

Este repositorio está estructurado de la siguiente manera:
+ EDA_MODEL $\Rightarrow$ Carpeta que contiene el Análisis Exploratorio de Datos y el
  + `Proyecto_Final.ipynb` $\rightarrow$ Jupyter Notebook que contiene el análisis exploratorio, preprocesamiento y tratamiento de datos, así como el entrenamiento, la prueba y selección del modelo
+ app
  + model
    + `rf_classifier.pkl`
  + `Dockerfile`
  + `deployment_project.yaml`
  + `main.py`
  + `requirements.txt`
+ data
  + `raw_data.csv`
  + `tidy_data.csv`
+ images
  + `Docker_image.png`
  + `Ejecucion_contenedor.png`
  + `Imagen_nube.png`
  + `proceso_contenedor.png`
+ `AndTheOscarGoesTo.ipynb`
+ `README.md`

se encuentra el reporte final del proyecto.
