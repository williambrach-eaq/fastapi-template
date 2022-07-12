# Fast-API-template 🚀

###  **Introduction: Structuring of API**


- `api_template:`  Contains all the API related Code Base.
    - `manage.py:` Only entry point for API. Contains no logic. 
    - `.env:` Most important file for your api and contains global configs. Acoid using application/variable level configs here.
    - `application:`  It contains all your api related codes and test modules. I prefer keeping application folder at global.
    - `logs`: Logs is self-explanatory. FYI it will not contain any configuration information, just raw logs. Feel free to move according to your comfort but not inside the application folder.
    - `models:` As a part of Machine-Learning/ Deep-Learning app you might need to add model files here or if you have huge files on cloud add symlinks if possibles.
    - `resources:` To store any documentation, application related csv/txt/img files etc.
    - `settings:` Logger/DataBase/Model global settings files in yaml/json format.

- `application:` 
    - `main:` priority folder of all your application related code.
        - `🏗 infrastructure:` Data Base and ML/DL models related backbone code
        - `📮 routers:` API routers and they strictly do not contain any business logic
        - `📡 services:` All processing and business logic for routers here at service layer
        - `⚒ utility:`
            - `config_loader` Load all application related config files from settings directory 
            - `logger` Logging module for application
            - `manager` A manager utility for Data Related Task which can be common for different services
        - `🐍 config.py:` Main config of application, inherits all details from .env file
    - `test:` Write test cases for your application here.
    - `initializer.py:` Preload/Initialisation of Models and Module common across application. Preloading model improves inferencing.
    
### Running Locally ? 📍
    ```bash
    uvicorn manage:app --host 0.0.0.0 --port 8000
    ```

### Update requirements
    ```
    pip freeze > requirements.txt
    ```

### Docker Support 🐳

    docker build -t fastapi-image  .
    docker run -d --name fastapi-container -p 8000:8000 fastapi-image

