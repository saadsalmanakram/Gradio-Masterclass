# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:48:16 2024

@author: saads
"""

# In this example, we combine global and session states. A global scoreboard keeps track of the top scores across all users, while each user has their own session-based personal best score.

import gradio as gr

global_scores = []

def submit_score(score, personal_best):
    global global_scores
    
    global_scores.append(score)
    top_scores = sorted(global_scores, reverse=True)[:5]  # Top 5 global scores
    
    if score > personal_best:
        personal_best = score  # Update user's personal best if they beat it
    
    return {
        "Global Top Scores": top_scores,
        "Your Personal Best": personal_best
    }, personal_best

demo = gr.Interface(
    fn=submit_score,
    inputs=[gr.Number(label="Your Score"), gr.State(value=0)],  # Personal best as session state
    outputs=[gr.JSON(), gr.State()]
)

demo.launch()
