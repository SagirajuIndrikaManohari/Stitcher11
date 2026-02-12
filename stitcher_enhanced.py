import json
import os

class HierarchicalStitcher:
    def __init__(self, student_id, location, current_stage):
        self.student_id = student_id
        self.location = location
        self.current_stage = current_stage
        
        # LAYER 1: Permanent Rules
        self.core_context = (
            "1. Adhere to the 36-stage engineering lifecycle.\n"
            "2. Prioritize UN Sustainability Goal 14 (Life Below Water).\n"
            "3. Safety First: Include waterproofing warnings."
        )
        
        # LAYER 2: Persistent Memory
        self.major_decisions = "No hardware selected yet."
        
        # LAYER 3: Episodic Buffer
        self.episodic_buffer = [] 
        self.interaction_count = 0
        
        # DUAL THRESHOLD TRIGGERS (as per requirement)
        self.interaction_trigger_limit = 5
        self.token_trigger_limit = 500  # NEW: Token-based trigger
        
        # Geospatial Database
        self.geo_db = {
            "Erode": "High textile dye concentration in local water sources (Cauvery basin).",
            "Tuticorin": "High salinity and heavy coral reef protection zones.",
            "Chennai": "High groundwater salinity and seasonal flooding risks."
        }
        
        # Stage progression tracking
        self.completed_milestones = []

    def _get_geospatial_injection(self):
        return self.geo_db.get(self.location, "Standard environmental guidelines.")

    def _estimate_tokens(self, text):
        """Rough token estimation (1 token ≈ 4 characters)"""
        return len(text) // 4

    def _get_buffer_tokens(self):
        """Calculate total tokens in episodic buffer"""
        total_text = "\n".join(self.episodic_buffer)
        return self._estimate_tokens(total_text)

    def _semantic_summarization(self):
        """
        Enhanced summarization with structured extraction
        (Requirement: Generate structured output)
        """
        if not self.episodic_buffer:
            return "Initial phase."
        
        # Extract key information patterns
        summary_points = []
        
        # Analyze buffer for key topics
        buffer_text = " ".join(self.episodic_buffer).lower()
        
        # Topic detection
        if "sensor" in buffer_text or "hardware" in buffer_text:
            summary_points.append("Discussed sensor/hardware selection")
        if "data" in buffer_text or "collect" in buffer_text:
            summary_points.append("Explored data collection methods")
        if "cost" in buffer_text or "budget" in buffer_text:
            summary_points.append("Considered budget constraints")
        if "pollution" in buffer_text or "water quality" in buffer_text:
            summary_points.append("Analyzed water quality parameters")
        if "filter" in buffer_text or "treatment" in buffer_text:
            summary_points.append("Evaluated filtration/treatment systems")
        
        # Decision extraction (look for decisive keywords)
        if "select" in buffer_text or "choose" in buffer_text or "decided" in buffer_text:
            # Try to extract what was selected
            for entry in self.episodic_buffer[-3:]:
                if any(word in entry.lower() for word in ["select", "choose", "decided"]):
                    summary_points.append(f"Decision: {entry[:60]}...")
                    break
        
        # Generate structured summary
        if summary_points:
            return " | ".join(summary_points)
        else:
            return f"Recent focus: {self.episodic_buffer[-1][:80]}..." if self.episodic_buffer else "Initial phase"

    def _trigger_summarization(self):
        """
        DUAL THRESHOLD SUMMARIZATION
        Triggered by: interaction count >= 5 OR token volume >= 500
        """
        print("\n" + "="*60)
        print("SYSTEM: Summarization Triggered")
        print(f"  - Interaction Count: {self.interaction_count}")
        print(f"  - Buffer Token Count: {self._get_buffer_tokens()}")
        print("  - Running semantic compression...")
        
        # Generate semantic summary
        self.major_decisions = self._semantic_summarization()
        
        # Clear episodic buffer
        old_buffer_size = len(self.episodic_buffer)
        self.episodic_buffer = []
        
        print(f"  - Compressed {old_buffer_size} messages into summary")
        print(f"  - Summary: {self.major_decisions}")
        print("="*60 + "\n")

    def advance_stage(self, milestone_description):
        """
        Track progression through 36-stage lifecycle
        """
        self.current_stage += 1
        self.completed_milestones.append({
            "stage": self.current_stage - 1,
            "milestone": milestone_description,
            "timestamp": None  # Could add datetime if needed
        })
        print(f"✓ Advanced to Stage {self.current_stage}: {milestone_description}")

    def stitch(self, user_query):
        """
        Main stitching function with DUAL THRESHOLD LOGIC
        """
        self.interaction_count += 1
        
        # Add user query to episodic buffer
        self.episodic_buffer.append(f"Student: {user_query}")
        
        # DUAL THRESHOLD CHECK (Requirement: interaction count >= 5 OR tokens >= 500)
        should_summarize = (
            self.interaction_count >= self.interaction_trigger_limit or
            self._get_buffer_tokens() >= self.token_trigger_limit
        )
        
        if should_summarize:
            self._trigger_summarization()
            self.interaction_count = 0  # Reset counter after summarization

        # Assemble final prompt using all layers
        template = f"""
### [CORE RULES]
{self.core_context}

### [PROJECT STATE]
Stage: {self.current_stage}/36 | Decisions: {self.major_decisions}
Completed Milestones: {len(self.completed_milestones)}

### [LOCAL CONTEXT]
Location: {self.location} | Alert: {self._get_geospatial_injection()}

### [RECENT DIALOGUE]
{"\n".join(self.episodic_buffer)}

### [QUERY]
{user_query}
"""
        return template

    def save_state(self):
        """Saves memory to a JSON file."""
        file_name = f"{self.student_id}_state.json"
        data = {
            "student_id": self.student_id,
            "location": self.location,
            "current_stage": self.current_stage,
            "major_decisions": self.major_decisions,
            "interaction_count": self.interaction_count,
            "completed_milestones": self.completed_milestones,
            "episodic_buffer": self.episodic_buffer  # Save buffer too
        }
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_state(cls, student_id):
        """Restores memory from a JSON file."""
        file_name = f"{student_id}_state.json"
        if not os.path.exists(file_name):
            return None
        
        with open(file_name, 'r') as f:
            data = json.load(f)
            
        instance = cls(data['student_id'], data['location'], data['current_stage'])
        instance.major_decisions = data.get('major_decisions', "Initial phase.")
        instance.interaction_count = data.get('interaction_count', 0)
        instance.completed_milestones = data.get('completed_milestones', [])
        instance.episodic_buffer = data.get('episodic_buffer', [])
        return instance
