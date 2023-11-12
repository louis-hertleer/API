# API

In mijn vrije tijd doe ik graag landbouw activiteiten, daarom heb ik voor mijn api iets in dit thema gekozen.
De database bestaat uit 2 tabellen waarbij een worker een tractor kan bezitten.
Een worker heeft een id, een naam, een email en een list van tractors.
Een tractor heeft een id,een type, een year en een worker.


In dit screenshot is te zien dat alle workers door een GET request worden opgevraagd.
![image](https://github.com/louis-hertleer/API/assets/114073936/0fdd50f7-40d8-4e00-8792-a6b6ec694c82)

In dit screenshot is te zien dat een worker met id 1 door een GET request wordt opgevraagd.
![image](https://github.com/louis-hertleer/API/assets/114073936/fd6962ad-8fc4-4771-afa9-8f7c5d31e5b0)

In dit screenshot is te zien dat een worker wordt aangemaakt door een POST request.
![image](https://github.com/louis-hertleer/API/assets/114073936/5c61d568-1423-439e-89fb-cf2418de655c)

In dit screenshot is te zien dat een worker met id 1 verwijderd wordt door een DELETE request.
![image](https://github.com/louis-hertleer/API/assets/114073936/5c92ab77-3135-4b99-83f8-493816b99b57)


Hosted API:https://system-service-louis-hertleer.cloud.okteto.net/
