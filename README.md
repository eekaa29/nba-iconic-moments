# 🏀 NBA Iconic Project

La idea principal del proyecto es reunir los momentos más icónicos y memorables de la historia de la NBA. Cada historia, momento o suceso consiste en un post específico, ordenados por franquicia y por la conferencia en la que cada franquicia se encuentra(Por el momento sólo hay posts sobre las franquicias de Lakers, Bulls, Warriors, Spurs y Cavaliers. Con el tiempo habrá más). Además, la web tiene una API integrada en la seccion **Articles** la cual permite consultar las noticias más recientes del mundo NBA publicadas por los medios más grandes de EEUU(Slam, ESPN, Bleacher Report, NBA.com y Yahoo) 

## Tecnologías utilizadas

### Backend

El objetico de este proyecto es prácticar con el framework Django, por lo que el backend al completo está creado sobre esta herramienta.

### Frontend

Para el fontend he usado django-tailwind.css y JavaScript.
En la app **theme** se encuentra **settings.json**, el script donde hay que añadir los templates que contengan clases de tailwind



## ⚙️ Funcionalidades

- Posts de momentos que se recordarám siempre en la NBA(solo de unas pocas franquicias, en el futuro se irán añadiendo más).
- Operaciones CRUD para los posts
- Integración de una API para colsultar las noticias más recientes publicadas por los periódicos(ESPN, Slam, Yahoo y Bleacher Report)
- Filtar las noticias por equipo 
- SignUp
- Login
- Logout
- Cambio de contraseña
- Cambio de email
- Perfil para cada usuario


## 🧱 Estructura del Proyecto
<img href="readme\img\NBA-ICONIC-PROJECT.png" rel="Estructura del proyecto">

## Estética del Proyecto

### Home
<img href="readme\img\home.PNG" rel="Home">

### Franchises
<img href="readme\img\franchise_list.PNG" rel="Franchise_list">

### Posts
<img href="readme\img\lebron_post.PNG" rel="Post-Cavaliers">
<img href="readme\img\post_jordan.PNG" rel="Jordan-Post">

### Profile
<img href="readme\img\profile.PNG" rel="Profile">

## ¿Cómo ejecutar el proyecto?

- Clonar el repo
    - **https://github.com/eekaa29/nba-iconic-moments.git**

- Intalar requirements.txt dentro de un entorno virtual
    -  pip install -r requirements.txt

## Autor 

Ekaitz Martin - Proyecto de práctica para Django y Tailwind.css