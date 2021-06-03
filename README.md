# TFM: Aplicación de métodos semisupervisados para el reconocimiento de voces patológicas con afasia
Este repositorio contiene tres scripst de python para el preprocesamiento y limpieza de los datos obtenidos en [AphasiaBank](https://talkbank.org/share/data.html). 

- preprocessing_clean_data.ipynb.ipynb: script para la lectura, limpieza y creación del dataframe usado posteriormente para generar los cortes de audio donde el paciente habla. 
- convert_mp4_wav.py: script que convierte los videos de las conversaciones entre investigador y paiciente de mp4 a wav. 
- aduio_chunks.py: script que genera los cortes de audios donde el paciente habla. 

Además de dos códigos bash para la creación del docker y ejecutar el experimento. 

- 0_BuildDocker.sh: script para la creación del docker 
- 1_RunExperiment0_GPU0.sh: script para ejecución del modelo wav2vec2.0

# Autora
Mónica Romero Ferrón

# Acerca de este software
- Master de Data Science.
- Universitat Oberta of Catalunya.

# Licencia
Esta obra está sujeta a una licencia de Reconocimiento -  NoComercial - SinObraDerivada
[3.0 España de CreativeCommons](https://creativecommons.org/licenses/by-nc-nd/3.0/es/)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# TFM: Application of semi-supervised methods for the recognition of pathological voices in aphasia
This repository contains three python scripst for preprocessing and cleaning the data obtained from [AphasiaBank](https://talkbank.org/share/data.html). 

- preprocessing_clean_data.ipynb.ipynb: script for reading, cleaning and creating the dataframe used later to generate the audio slices where the patient speaks. 
- convert_mp4_wav.py: script that converts the videos of the conversations between researcher and patient from mp4 to wav. 
- aduio_chunks.py: script that generates the audio cuts where the patient speaks. 

In addition to two bash codes for creating the docker and running the experiment. 

- 0_BuildDocker.sh: script for the creation of the docker. 
- 1_RunExperiment0_GPU0.sh: script for running the wav2vec2.0 model.

# Author
Mónica Romero Ferrón

# About this software
- Master in Data Science.
- Universitat Oberta de Catalunya.

# License
This work is licensed under a CreativeCommons Attribution - NonCommercial - NoDerivs License
[3.0 España de CreativeCommons](https://creativecommons.org/licenses/by-nc-nd/3.0/es/)
