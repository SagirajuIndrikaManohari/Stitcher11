from fastapi import FastAPI
from stitcher import HierarchicalStitcher

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(student_id: str, message: str):
    # 1. Attempt to load existing state from the JSON file
    stitcher = HierarchicalStitcher.load_state(student_id)
    
    # 2. If it's a new student (no file found), create a new instance
    if not stitcher:
        stitcher = HierarchicalStitcher(student_id, "Erode", 14)
    
    # 3. Stitch the multi-layered prompt
    final_prompt = stitcher.stitch(message)
    
    # 4. Save the updated state (updates decisions and counts)
    stitcher.save_state()
    
    return {"prompt_to_send_to_llm": final_prompt}
