# Proyecto Final PCD
Desde el 16 de mayo de 1929 la entrega del Premio de la Academia de Artes y Ciencias Cinematográficas, conocido popularmente como Premio Óscar, ha sido altamente conocido. Se entrega dicho premio de manera anual para reconocer a la excelencia y activismo social de los profesionales en la industria cinematográfica, como actores, directores y guionistas. Se considera el máximo honor en el cine. Por ello, con este trabajo se creará un modelo de aprendizaje supervisado de clasificación para predecir si una película recibirá un Premio Óscar o no.


**`Antecedentes`**
Es bien sabido que cada película es diferente y lleva a cabo un proceso distinto; algunas pueden tener un presupuesto relativamente bajo (de algunos millones de dólares) mientras que otras pueden llegar a $379$ millones de dólares, como Piratas del Caribe: En Mareas Misteriosas que ha sido la película más costosa hasta el momento (Bedard, 2022). Sin embargo, según Investopedia, el presupuesto promedio para una película de Hollywood es de $65$ milliones de dólares sin incluir la inversión de pubilicidad. Esto último en promedio cuesta la mitad que la producción; $35$ milliones de dólares aproximadamente, dando un total de $100$ milliones de dólares en promedio. Considerando que ha habido $581$ películas nominadas para la estatuilla dorada por "Mejor Película" y únicamente han ganado $94$, se creará un modelo para predecir si una película ganará dicho premio basado en diferentes características, incluyendo su presupuesto.

**`Objetivos`**
+ Generar un modelo de aprendizaje supervisado para resolver un problema de clasificación
+ Crear un API con la librería FastAPI con los *endpoints* necesarios
+ Acceder al modelo a través de una API

**`Planteamiento del problema`**
Se trabajará con un conjunto de datos con información de distintas películas con el objetivo de resolver un problema de clasificación para predecir si una película va a ganar un premio Óscar o no. Dicho conjunto de datos contiene $506$ registros (o filas) de películas y $19$ variables (o columnas), que son las siguientes:
+ **Marketing expense** $\Rightarrow$ cuánto se gastó en mercadotecnia, en millones de dólares
+ **Production expense** $\Rightarrow$ cuánto se gastó en la producción de la película, en millones de dólares
+ **Multiplex coverage** $\Rightarrow$ qué tanta cobertura tuvo en los cines
+ **Budget** $\Rightarrow$ con cuánto dinero contaban para realizar la película
+ **Movie_lenght** $\Rightarrow$ duración de la película
+ **Lead_actor_rating** $\Rightarrow$ rating del actor principal
+ **Lead_Actrees_rating** $\Rightarrow$ rating de la actriz principal
+ **Director_rating** $\Rightarrow$ rating del director
+ **Producer_rating** $\Rightarrow$ rating del productor
+ **Critic_rating** $\Rightarrow$ rating de las críticas
+ **Trailer_views** $\Rightarrow$ cantidad de visitas en el trailer
+ **3D_available** $\Rightarrow$ si la película está disponible en 3D o no
+ **Time_taken** $\Rightarrow$ semanas que les tomó hacer la película
+ **Twitter_hastags** $\Rightarrow$ cantidad de hastags en twitter
+ **Genre** $\Rightarrow$ género de la película
+ **Avg_age_actors** $\Rightarrow$ promedio de la edad de los actores
+ **Num_multiplex** $\Rightarrow$ número de cines en los que fue transmitida la película
+ **Collection** $\Rightarrow$ ganancia monetaria
+ **Start_tech_Oscar** $\Rightarrow$ si ganó el premio Óscar o no (variable de respuesta)
