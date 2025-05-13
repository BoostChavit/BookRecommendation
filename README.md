# Book Recommendation website

- Develop by using vue.js, fastapi and postgresql.

- Recommendation using content-based filtering by using TF-IDF and Cosine Similarity

- Data from https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset


## Frontend 
### .env example
add in frontend directory
```
VITE_API_URL="http://localhost:8000"
```

### how to start up
```
cd frontend
npm install
npm run dev
```


## Backend
### .env example
add in backend/backend directory
```
DATABASE_URL=postgresql://postgres:postgres@database:5432/books
FRONTEND_URL=http://localhost:5173
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=books
```

### how to start up
```
cd backend/backend
docker-compose up --build
```