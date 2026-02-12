# Hierarchical Stitcher API

A FastAPI application for managing educational prompts with hierarchical context stitching.

## Features
- Multi-layer prompt construction (Core Rules, Project State, Local Context, Recent Dialogue)
- Persistent student state management
- Geospatial context injection
- Automatic conversation summarization

## Installation

```bash
pip install -r requirements.txt
```

## Running Locally

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoint

### POST /chat
Send a message and get the stitched prompt.

**Parameters:**
- `student_id` (str): Unique identifier for the student
- `message` (str): The student's message/query

**Example Request:**
```bash
curl -X POST "http://localhost:8000/chat?student_id=student123&message=How%20do%20I%20select%20a%20sensor?" \
  -H "Content-Type: application/json"
```

**Response:**
```json
{
  "prompt_to_send_to_llm": "... stitched prompt ..."
}
```

## Deployment

### Option 1: Deploy to Render
1. Push to GitHub
2. Connect your GitHub repo to Render
3. Select "Web Service"
4. Build command: `pip install -r requirements.txt`
5. Start command: `uvicorn app:app --host 0.0.0.0 --port $PORT`

### Option 2: Deploy to Railway
1. Push to GitHub
2. Connect repo to Railway
3. Railway will auto-detect FastAPI and deploy

### Option 3: Deploy to Heroku
1. Add `Procfile` (see below)
2. Push to GitHub
3. Connect to Heroku

## File Structure
```
.
├── app.py              # FastAPI application
├── stitcher.py         # HierarchicalStitcher class
├── requirements.txt    # Python dependencies
└── README.md          # This file
```
