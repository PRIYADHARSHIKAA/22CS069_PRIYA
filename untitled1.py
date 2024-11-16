# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h_4vBGhOh4cZZVQrtXFCTDoYziL1_T_P
"""

!pip install gradio

import gradio as gr
questions = [
    {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": 3},
    {"question": "Which programming language is used for web development?", "options": ["Python", "HTML", "Java", "C++"], "answer": 2},
    {"question": "What is (6*7)/3?", "options": ["42", "14", "21", "17"], "answer": 2},
    {"question": "Where were fortune cookies invented?", "options": ["China", "Italy", "Japan", "USA"], "answer": 4},
    {"question": "What is the fear of fun called?", "options": ["Phobophobia", "Cherophobia", "Hilarophobia", "Funophobia"], "answer": 2},
    {"question": "Which country invented ice cream?", "options": ["USA", "Italy", "France", "China"], "answer": 4},
    {"question": "Which ancient people invented the toothbrush?", "options": ["Romans", "Egyptians", "Greeks", "Africans"], "answer": 3},
    {"question": "What vegetable was originally purple?", "options": ["Potato", "Carrot", "Onion", "Cabbage"], "answer": 2},
    {"question": "How do you say “The Pizza” in French?", "options": ["La Pizza", "Le Pizza", "L’Pizza", "Li Pizza"], "answer": 1},
]
current_index = 0
score = 0

def start_quiz():
    """Starts the quiz and returns the first question."""
    global current_index, score
    current_index = 0
    score = 0
    question = questions[current_index]
    return (
        question["question"],
        gr.update(choices=question["options"]),
        "Good luck!",
        f"Score: 0/{len(questions)}"
    )

def next_question(user_answer):
    """Handles the transition to the next question and feedback."""
    global current_index, score
    if current_index < len(questions):
        correct_answer = questions[current_index]["answer"]
        feedback = "Correct!" if user_answer == questions[current_index]["options"][correct_answer - 1] else f"Wrong! The correct answer was: {questions[current_index]['options'][correct_answer - 1]}"

        if user_answer == questions[current_index]["options"][correct_answer - 1]:
            score += 1

        current_index += 1
        if current_index < len(questions):
            next_q = questions[current_index]
            return (
                next_q["question"],
                gr.update(choices=next_q["options"]),
                feedback,
                f"Score: {score}/{len(questions)}"
            )
        else:
            return (
                "Quiz Completed!",
                gr.update(choices=[]),
                feedback,
                f"Final Score: {score}/{len(questions)}"
            )
    else:
        return (
            "Quiz Completed!",
            gr.update(choices=[]),
            "Thank you for playing!",
            f"Final Score: {score}/{len(questions)}"
        )
with gr.Blocks() as quiz_app:
    gr.Markdown("# 📝 Quiz Bot")

    question_display = gr.Label()
    options_display = gr.Radio(choices=[], label="Options", interactive=True)
    feedback_display = gr.Label()
    score_display = gr.Label()

    start_btn = gr.Button("Start Quiz")
    submit_btn = gr.Button("Submit Answer")
    start_btn.click(
        start_quiz,
        inputs=[],
        outputs=[question_display, options_display, feedback_display, score_display],
    )
        submit_btn.click(
        next_question,
        inputs=[options_display],
        outputs=[question_display, options_display, feedback_display, score_display],
    )

quiz_app.launch()