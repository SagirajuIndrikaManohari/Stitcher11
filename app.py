from google import genai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from stitcher import AgribotStitcher

# 1. Setup Gemini (Use your actual key)
GEMINI_API_KEY = "YOUR_API_KEY_HERE"
client = genai.Client(api_key=GEMINI_API_KEY)

app = FastAPI(title="Agribot Stitcher API", docs_url="/agri-docs")

# 2. Add the "Bridge" (CORS) so your website can connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows your GitHub page to send data here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def health_check():
    return {"status": "Online", "message": "Stitcher is ready for input!"}

@app.post("/agri-chat")
async def handle_farm_query(uid: str, location: str, query: str):
    # Resume or create the bot instance
    bot = AgribotStitcher.recover_from_disk(uid)
    if not bot:
        bot = AgribotStitcher(uid, "Turmeric", "Small-hold")
    
    # --- THE STITCHING PROCESS ---
    # This prepares the prompt with Engineering rules + Regional Alerts
    final_context = bot.construct_payload(location, query)
    
    # 3. Call Gemini with the STITCHED prompt
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=final_context
        )
        ai_reply = response.text
    except Exception as e:
        ai_reply = f"AI Error: {str(e)}"
    
    # Save the session to disk
    bot.persist_to_disk()
    
    return {
        "uid": uid,
        "location": location,
        "ai_response": ai_reply,
        "stitched_prompt": final_context # This lets you SEE what the stitcher did
    }
