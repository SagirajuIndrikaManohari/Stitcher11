#!/usr/bin/env python3
"""
Demonstration of Enhanced Hierarchical Stitcher
Shows all features required by INTERNSHIP_DAY_012
"""

from stitcher_enhanced import HierarchicalStitcher

def demo_dual_threshold():
    """Demonstrates dual threshold summarization"""
    print("=" * 70)
    print("DEMO: Dual Threshold Summarization")
    print("=" * 70)
    
    stitcher = HierarchicalStitcher("demo_student", "Erode", 14)
    
    # Test 1: Interaction count trigger
    print("\n### Test 1: Interaction Count Trigger (>= 5)")
    for i in range(1, 7):
        query = f"Question {i}: What sensors should I use?"
        print(f"\nMessage {i}:")
        stitcher.stitch(query)
    
    # Test 2: Token volume trigger
    print("\n\n### Test 2: Token Volume Trigger (>= 500 tokens)")
    stitcher2 = HierarchicalStitcher("demo_student_2", "Chennai", 10)
    
    long_query = """
    I am working on reducing marine pollution in Tuticorin. I need to select 
    appropriate sensors for water quality monitoring. The parameters I want to 
    measure include pH, turbidity, dissolved oxygen, and heavy metal concentration.
    I'm also considering the cost constraints and the harsh marine environment.
    What would be the best sensor selection strategy? Should I use commercial 
    sensors or build custom ones? How do I ensure waterproofing? What about 
    calibration and maintenance schedules?
    """ * 3  # Repeat to exceed token limit
    
    stitcher2.stitch(long_query)

def demo_semantic_summarization():
    """Demonstrates semantic summarization quality"""
    print("\n\n" + "=" * 70)
    print("DEMO: Semantic Summarization")
    print("=" * 70)
    
    stitcher = HierarchicalStitcher("semantic_demo", "Tuticorin", 15)
    
    # Simulate a conversation
    queries = [
        "I need to select sensors for water quality monitoring",
        "What is the best pH sensor for marine environments?",
        "I decided to use Atlas Scientific pH sensor",
        "How much does it cost?",
        "Let's also look at turbidity sensors",
        "I want to collect data weekly"  # This should trigger summarization
    ]
    
    for i, query in enumerate(queries, 1):
        print(f"\n--- Message {i} ---")
        result = stitcher.stitch(query)
    
    print("\n### Final Summary Generated:")
    print(f"  {stitcher.major_decisions}")

def demo_stage_progression():
    """Demonstrates 36-stage lifecycle tracking"""
    print("\n\n" + "=" * 70)
    print("DEMO: Stage Progression Tracking")
    print("=" * 70)
    
    stitcher = HierarchicalStitcher("progression_demo", "Erode", 1)
    
    # Simulate project progression
    milestones = [
        "Problem identification completed",
        "Literature review finished",
        "Hardware selection finalized",
        "Prototype design approved",
        "Component procurement done"
    ]
    
    for milestone in milestones:
        stitcher.advance_stage(milestone)
    
    print(f"\nCurrent Stage: {stitcher.current_stage}/36")
    print(f"Completed Milestones: {stitcher.completed_milestones}")

def demo_geographic_intelligence():
    """Demonstrates dynamic injection mechanism"""
    print("\n\n" + "=" * 70)
    print("DEMO: Geographic Intelligence Injection")
    print("=" * 70)
    
    locations = ["Erode", "Tuticorin", "Chennai"]
    
    for location in locations:
        print(f"\n### Student Location: {location}")
        stitcher = HierarchicalStitcher("geo_demo", location, 10)
        prompt = stitcher.stitch("What environmental factors should I consider?")
        
        # Extract and show the LOCAL CONTEXT section
        for line in prompt.split('\n'):
            if 'LOCAL CONTEXT' in line or 'Alert:' in line:
                print(f"  {line}")

def demo_persistence():
    """Demonstrates state saving and loading"""
    print("\n\n" + "=" * 70)
    print("DEMO: State Persistence")
    print("=" * 70)
    
    # Create and save state
    print("\n### Creating new student session...")
    stitcher1 = HierarchicalStitcher("persist_demo", "Chennai", 20)
    stitcher1.stitch("First question about sensors")
    stitcher1.stitch("Second question about data collection")
    stitcher1.advance_stage("Completed sensor selection")
    stitcher1.save_state()
    print("  State saved to persist_demo_state.json")
    
    # Load state
    print("\n### Loading student session...")
    stitcher2 = HierarchicalStitcher.load_state("persist_demo")
    
    if stitcher2:
        print(f"  ✓ Loaded successfully!")
        print(f"  - Student ID: {stitcher2.student_id}")
        print(f"  - Location: {stitcher2.location}")
        print(f"  - Current Stage: {stitcher2.current_stage}")
        print(f"  - Interaction Count: {stitcher2.interaction_count}")
        print(f"  - Episodic Buffer Size: {len(stitcher2.episodic_buffer)}")
        print(f"  - Major Decisions: {stitcher2.major_decisions}")

def demo_complete_workflow():
    """Demonstrates complete workflow matching the document requirements"""
    print("\n\n" + "=" * 70)
    print("DEMO: Complete Workflow (Document Requirements)")
    print("=" * 70)
    
    # Initialize for student in Erode working on Tuticorin project
    stitcher = HierarchicalStitcher("student_018", "Erode", 14)
    
    print("\n### Initial Setup:")
    print(f"  Student ID: student_018")
    print(f"  Location: Erode")
    print(f"  Project: Reducing Marine Pollution in Tuticorin")
    print(f"  Current Stage: 14/36")
    
    # Simulate conversation
    print("\n### Conversation Flow:")
    queries = [
        "What sensors should I use for marine pollution monitoring?",
        "How do I account for Erode's textile pollution?",
        "Can you recommend cost-effective sensors?",
        "What data collection frequency is best?",
        "Should I use surveys or satellite data?",
        "I've decided to use both surveys and secondary data"
    ]
    
    for i, query in enumerate(queries, 1):
        print(f"\n[Message {i}] Student: {query}")
        prompt = stitcher.stitch(query)
        # Show that context is being assembled
        print(f"  → Context assembled ({stitcher._get_buffer_tokens()} tokens in buffer)")
    
    print("\n### Final State:")
    print(f"  Interaction Count: {stitcher.interaction_count}")
    print(f"  Summary: {stitcher.major_decisions}")
    print(f"  Buffer Size: {len(stitcher.episodic_buffer)} messages")

if __name__ == "__main__":
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 68 + "║")
    print("║" + "  HIERARCHICAL CONTEXT MANAGEMENT DEMONSTRATION".center(68) + "║")
    print("║" + "  (INTERNSHIP_DAY_012 Requirements)".center(68) + "║")
    print("║" + " " * 68 + "║")
    print("╚" + "=" * 68 + "╝")
    
    # Run all demos
    demo_dual_threshold()
    demo_semantic_summarization()
    demo_stage_progression()
    demo_geographic_intelligence()
    demo_persistence()
    demo_complete_workflow()
    
    print("\n\n" + "=" * 70)
    print("All demonstrations completed successfully!")
    print("=" * 70 + "\n")
