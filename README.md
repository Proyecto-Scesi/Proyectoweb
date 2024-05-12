# DISEÑO DE UNA PAGINA WEB

## GRUPO DEEP WEB

**El grupo usamos como flujo de trabajo el gitFlow ya que resulta mas facil de desarrollar como grupo basandonos en el uso de muchas ramas**

## Bitacora del proyecto
 **Dia 1**

  recien se armo por falta de tiempo la base del proyecto por el momento solo se añadio las ramas necesarias para usar el gitflow y se avanzo el proyectoweb

 **Sabado 11/05/24** 
 
 Siguiendo la forma de trabajo de git flow las ramas features a una develop y luego a una rama release que se elimino y creo con los comandos:  `git flow release, git flow publish y git flow finish` pero ocurrio que en el GitHub no se notaba que hubieramos usado una rama release, se probo de nuevo con los mismos comandos, hubo el mismo caso. A causa de conflictos no se podia hacer hacer un `git push origin main` luego de combinar la rama develops con la main, finalmente sin los comandos `git flow` se termino haciendo manualmente todos las combinaciones y subiendo finalmente al respositorio remoto. La rama features/TrabajoHTML no se descargaba con el comando `git pull --all`, al hacer el comando `git pull origin features/TrabajoHTML` se combino con la rama features/EstiloPagina.
 
 Se opto por no usar los comandos `git flow` y crear directamente las ramas de manera manual para evitar errores.

 Se creo la rama hotfix para arreglar problemas relacionados y actualizar rapidamente el README.md

 ## Analisis del equipo

 * Marcelo

    -Hizo correctamente el procedimiento de la rama features/TrabajoHTML, pero sucedio el problema explicada en la bitacora.
 * Pablo
   Buen manejo del workflow gitflow logro corregir problemas que existian en el gitflow con los comandos, solo le faltaria mejorar los commits y su forma de redactar
 * Saul

## Herramientas utilizadas en el proyecto

El grupo no opto por el uso de hooks ya que no logramos comprender el uso en completo solo usamos los hooks que vienen por defecto con el git.
camino - Equivalente a git status. "Camino" en español significa "status" en inglés.
ramificar - Equivalente a git branch. "Ramificar" en español se refiere a "branch" en inglés.
traer - Equivalente a git pull. "Traer" en español implica "pull" en inglés, que es para traer cambios remotos.
empujar - Equivalente a git push. "Empujar" en español es lo mismo que "push" en inglés, para enviar cambios locales a un repositorio remoto.
fijar - Equivalente a git commit. "Fijar" en español se refiere a "commit" en inglés, que es para guardar los cambios en el repositorio.