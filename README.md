<div align="center">
<image src="https://github.com/user-attachments/assets/99bdd6b4-57f9-42a8-a1c5-75e51fdabe49"/>
</div>


-----------------------------

<div align="center">
  <a><img src="https://custom-icon-badges.demolab.com/badge/Streamlit-000000?style=for-the-badge&logo=streamlit"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Gemini-FFFFFF?style=for-the-badge&logo=gemini"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/MongoDB_Atlas-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/google colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Huggingface-FF9D00?style=for-the-badge&logo=huggingface-logo"></a> &nbsp;

</div>

---------------------

Empathia is your compassionate companion in mental well-being. Designed to provide emotional support and guidance, Empathia offers a safe space for you to explore your thoughts and feelings. Whether you need someone to talk to, seek advice on managing stress, or simply need a moment of calm, Empathia is here to listen and help.

 -------------------
## Key Features:
- Empathetic Conversations: Engage in meaningful dialogues with a chatbot designed to understand and empathize with your concerns.
- 24/7 Availability: Access support anytime, anywhere, without the need for appointments or waiting times.
- Confidentiality: Your privacy is paramount. Conversations with Empathia are confidential and secure.
- Personalized Guidance: Receive tailored suggestions and resources based on your unique needs and preferences.
- Holistic Support: Whether you're dealing with everyday stress or seeking deeper emotional insights, Empathia provides a range of supportive responses.

## Mission:
Our mission with Empathia is to make mental health support accessible and approachable. We aim to provide a reliable and empathetic digital companion that empowers you to take charge of your well-being and fosters a supportive environment for personal growth.

Empathia is here to support you every step of the way. Embrace the journey towards a more balanced and mindful life with us.

--------------------------
## Requirments
Python 3.9.8 (Recommended) 

<a href="https://www.python.org/downloads/release/python-398/" alt="python">
        <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" /></a>

<br>
<br>

Mongo DB Atlas Account(To Save data in cloud) or Mongo DB Compass(To Save the Data Locally)

<a href="https://www.mongodb.com/" alt="mongo">
      <img src="https://img.shields.io/badge/MongoDB_Atlas-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white"></a>
        
<br>
<br>

Gemini API Key

<a href="https://ai.google.dev/gemini-api/docs/api-key" alt="Gemini API key">
      <img src="https://custom-icon-badges.demolab.com/badge/Gemini-FFFFFF?style=for-the-badge&logo=gemini"></a> &nbsp;

--------------------
## Modules/Libraries Used

All The Modules/Libraries Used in the Project can be installed using [requirements.txt](requirements.txt)

- Streamlit
- Pymongo
- google.generativeai
- configparser 
- datetime 
- random
- time

--------------------
## Setup

### Database
Use the below configurations for MongoDB
<br>
- Database Name: Chatbot
- Total Number of Collections: 2
    - users
    - queries

<br>

Add your Mongo DB Connection String [Here](config.ini)

<br>

### Gemini API key
Get your Gemini API key [Here](https://ai.google.dev/gemini-api/docs/api-key)
<br>

Add your API key [Here](config.ini)

<br>

### Fine Tuned Model

To access the Fine Tuned Model please follow the steps provided in [Tuned_Model](Tuned_Model)


--------------------------
## How to Run?

- Intialize a Git Repository.

  
``` bash
  git init
```

- Clone the Current Git Repository.
  
```bash
  git clone https://github.com/k-arthik-r/Empathia.git
```

- Navigate to the root Directory of the project and Create a python virtual environment.
  
```bash
  python -m venv venv

```
- Activate the Environment:

  - for Powershell

  ```bash
    .\venv\Scripts\Activate.ps1
  ```
  - for CommandPrompt

  ```bash
    .\venv\Scripts\activate.bat
  ```

- Install all the Modules Present in [requirements](requirements.txt)
  
```bash
  pip install -r requirements.txt
```

- paste your Mongo DB Connection String and Gemini API Key inside config.ini file in the root directory. [Here](config.ini)

```bash
  CONNECTIONSTRING = <mongo-db-connection-string>
  APIKEY = <gemini-api-key>
```

- run your application using,
  
```bash
  streamlit run app.py
```


-------------------------
## Architecture

![architecture (4)](https://github.com/user-attachments/assets/be7920ec-b882-4958-9ac6-6c2d80fc6b7c)

-------------------------

## Application Overview

- Create a New Account by providing appropriate details.
  
  ![Screenshot 2024-07-30 204722](https://github.com/user-attachments/assets/852bc1c6-90ff-4cb1-a0cb-df0a3f332f02)

<br>


- Login to the using the credentials.
  
  ![Screenshot 2024-07-30 204800](https://github.com/user-attachments/assets/53333689-bb40-4d13-b29b-f1ebcc46db92)

<br>

- Use the Chatbot Interface to share your feelings.
  
  ![Screenshot 2024-07-30 204945](https://github.com/user-attachments/assets/9138f634-2ef2-4474-be63-d7cb35da9720)

<br>

- Review your Previously asked query and the corresponding Response.
  
  ![Screenshot 2024-07-30 205101](https://github.com/user-attachments/assets/6c7eb697-06e9-4662-93d7-7fce35a48938)

<br>

- Delete your Account.
  
  ![Screenshot 2024-07-30 205138](https://github.com/user-attachments/assets/766c97ca-98e1-462b-ba30-9c7b17fd040f)

  <br>
  
----------------------------



## License

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

----------------------------


## Feedback

If you have any feedback, please reach out to us at empathia.dev@gmail.com .
You are also welcomed to add new features by creating Pull Requests.
