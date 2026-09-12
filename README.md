# studyrats-api

.venv\Scripts\activate

uvicorn app.main:app --reload

pip freeze > requirements.txt

Adicionar no readme infos da api externa

docker build -t studyrats-api .


ZENQUOTES
   ↓
[1] Cache
   ↓
[2] Tratamento de erros
   ↓
[3] Configurações (.env)
   ↓
[4] Revisão/testes
   ↓
[5] Dockerfile
   ↓
[6] README
   ↓
BACKEND FINALIZADO ✅