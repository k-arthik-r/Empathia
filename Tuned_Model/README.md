<div align="center">
<image src="https://github.com/user-attachments/assets/d297baee-64a5-4b89-bf90-d005aaac6847"/>
</div>

-----------------------------

<div align="center">
  <a><img src="https://custom-icon-badges.demolab.com/badge/Streamlit-000000?style=for-the-badge&logo=streamlit"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Gemini-FFFFFF?style=for-the-badge&logo=gemini"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/google colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white"></a> &nbsp;
  <br><br>
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

## Requirements
- google account
- google cloud account
- gcp CLI SDK

---------------------------

## Steps to Use the Model

- Get the client_secret.json file by contacting the developers at empathia.dev@gmail.com
- Paste the content of the client_secret.json as a secret within the colab Environment with the name 'CLIENT_SECRET'.
- Ask the developers to add you as a tester by providing your gmail ID.
- Open [MCG.ipynb](MCG.ipynb) in a google colab Environment.
- Upload the [app.py](app.py), [chatbot.py](chatbot.py), [db.py](db.py), [config.ini](config.ini) into the google colab environment.
- In [config.ini](config.ini), provide your mongo db connection string.
- Run the Cells in the Colab Environment.

- After Executing the Second Cell in the colab, you will be asked to Enter the output of the above comand. Copy the above command as shown in the snapshot:
    
   ![Screenshot 2024-07-30 202750](https://github.com/user-attachments/assets/c9533674-d8ec-4e7b-aa9b-5327096b58a1)

- Paste the copied command into the CMD of your system (its Important that GOOGLE CLI SDK Had to be Installed), click on Enter, type 'y' and click enter:
   
   ![Screenshot 2024-07-30 203036](https://github.com/user-attachments/assets/81d72644-f25a-465c-96f5-4d283ffe1b08)
   
- You will be redirected to a google sign in page, click on continue, give all the permissions required and click on continue, you should be asle to see this Interface:
   
    ![Screenshot 2024-07-30 203002](https://github.com/user-attachments/assets/de8df443-3cbd-46d5-b0c8-027cb9a531a5)

- After that, visit to your CMD, you should have got this Interface shown in the snapshot, copy the output shown in the snapshot.

   ![Screenshot 2024-07-30 203118](https://github.com/user-attachments/assets/895ae487-c853-467d-9ac6-4bd750c8d60f)

- Paste the copied link in the colab environment:
   
   ![Screenshot 2024-07-30 203141](https://github.com/user-attachments/assets/79fa0438-7964-415e-9a89-4710a7fa3c14)
   
- After this, the authentication will be successfull and you will get a confirmation:

    ![Screenshot 2024-07-30 203203](https://github.com/user-attachments/assets/73fa232e-7105-42ae-baf3-02d01df48c3d)

- Run the streamlit app in the local tunnel, paste the external URL IP  as Tunnel Password in the Tunnel Interface, you should be able to access the Application.

-------------------------------

## Application Usage

- Create a New Account by providing appropriate details.
  
  ![Screenshot 2024-07-30 204722](https://github.com/user-attachments/assets/852bc1c6-90ff-4cb1-a0cb-df0a3f332f02)


- Login to the using the credentials.
  
  ![Screenshot 2024-07-30 204800](https://github.com/user-attachments/assets/53333689-bb40-4d13-b29b-f1ebcc46db92)


- Use the Chatbot Interface to share your feelings.
  
  ![Screenshot 2024-07-30 204945](https://github.com/user-attachments/assets/9138f634-2ef2-4474-be63-d7cb35da9720)


- Review your Previously asked query and the corresponding Response.
  
  ![Screenshot 2024-07-30 205101](https://github.com/user-attachments/assets/6c7eb697-06e9-4662-93d7-7fce35a48938)


- Delete your Account.
  
  ![Screenshot 2024-07-30 205138](https://github.com/user-attachments/assets/766c97ca-98e1-462b-ba30-9c7b17fd040f)


-----------------------

## Training Details

![Screenshot 2024-07-29 002435](https://github.com/user-attachments/assets/02534868-4779-45ea-9da4-275ee5602629)

--------------------------

## Dataset

The Dataset Used to Tune the Model can be accessd [here](https://docs.google.com/spreadsheets/d/1Elf0wP54e-p8rb2gVWGdPU8-c83IIXZcT8o7TPrylJ8/edit?usp=sharing )

The Data is Originally Sourced from here: [Amod/mental_health_counseling_conversations](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations)


----------------------------


## License

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
