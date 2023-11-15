Subindo as paradas:

    docker-compose build
    docker-compose up -d

No vscode, com extensão docker, clicar em attach shell, depois subir o Ambiente virtual:

    cd fastapi
    python -m venv ./venv
    source venv/bin/activate
    pip install fastapi uvicorn

Criou-se um arquivo app.py e um model chamado person. Subindo a aplicação:

    uvicorn app:app --host 0.0.0.0 --port 7001 --reload
    
Interessante, documentação automática da api:
    
    http://0.0.0.0:7001/docs



