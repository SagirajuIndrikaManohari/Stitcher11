#!/usr/bin/env python3
"""
Simple test to see the actual prompt that gets sent to the LLM
"""

from stitcher_enhanced import HierarchicalStitcher

print("=" * 70)
print("EXAMPLE: What the LLM actually receives")
print("=" * 70)

# Create a student session
stitcher = HierarchicalStitcher("student_018", "Erode", 14)

# Ask a question
user_question = "What sensors should I use for monitoring marine pollution?"

# Get the stitched prompt
final_prompt = stitcher.stitch(user_question)

print("\n📝 USER QUESTION:")
print(f"   {user_question}")

print("\n" + "=" * 70)
print("📤 COMPLETE PROMPT SENT TO LLM:")
print("=" * 70)
print(final_prompt)
print("=" * 70)

# Show another example with more context
print("\n\n" + "=" * 70)
print("EXAMPLE 2: After multiple interactions")
print("=" * 70)

stitcher2 = HierarchicalStitcher("student_019", "Chennai", 20)
stitcher2.stitch("I need pH sensors")
stitcher2.stitch("What about turbidity sensors?")
stitcher2.stitch("How much does Atlas Scientific cost?")

final_prompt2 = stitcher2.stitch("Should I collect data weekly or daily?")

print("\n📝 USER QUESTION:")
print("   Should I collect data weekly or daily?")

print("\n" + "=" * 70)
print("📤 COMPLETE PROMPT SENT TO LLM (with conversation history):")
print("=" * 70)
print(final_prompt2)
print("=" * 70)
