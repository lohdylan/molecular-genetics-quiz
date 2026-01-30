#!/usr/bin/env python3
"""
Molecular Genetics Quiz Tool

Interactive CLI quiz for active recall study.
Presents questions, accepts answers, provides immediate feedback.
"""

import json
import random
import os
import sys


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def load_questions(filepath='data/questions.json'):
    """Load quiz questions from JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find {filepath}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {filepath}")
        sys.exit(1)


def display_question(question, number, total):
    """Display a single question with its options."""
    print(f"\n{'='*80}")
    print(f"Question {number}/{total}")
    print(f"Topic: {question['topic']} | Source: {question['quiz']}")
    print(f"{'='*80}\n")
    print(question['question'])
    print()
    for option in question['options']:
        print(f"  {option}")
    print()


def get_answer():
    """Get and validate user's answer input."""
    while True:
        try:
            answer = input("Your answer (A/B/C/D/E or 'q' to quit): ").strip().upper()
            if answer == 'Q':
                return None
            if answer in ['A', 'B', 'C', 'D', 'E']:
                return answer
            print("Invalid input. Please enter A, B, C, D, E, or 'q' to quit.")
        except (EOFError, KeyboardInterrupt):
            print("\n\nQuiz interrupted.")
            return None


def display_feedback(user_answer, correct_answer, explanation):
    """Display whether answer was correct and show explanation."""
    print(f"\n{'-'*80}")
    if user_answer == correct_answer:
        print("✓ CORRECT!")
    else:
        print(f"✗ INCORRECT - The correct answer is {correct_answer}")
    print(f"{'-'*80}")
    print(f"\nExplanation: {explanation}")
    print(f"\n{'-'*80}")


def display_final_score(correct, total):
    """Display final quiz results."""
    percentage = (correct / total * 100) if total > 0 else 0
    print(f"\n{'='*80}")
    print("QUIZ COMPLETE!")
    print(f"{'='*80}")
    print(f"\nFinal Score: {correct}/{total} ({percentage:.1f}%)")
    print()

    if percentage >= 90:
        print("Outstanding! You have excellent mastery of this material.")
    elif percentage >= 80:
        print("Great job! You have a strong understanding.")
    elif percentage >= 70:
        print("Good work! Review the topics where you struggled.")
    elif percentage >= 60:
        print("Passing, but there's room for improvement.")
    else:
        print("Keep studying! Focus on understanding the explanations.")

    print(f"\n{'='*80}\n")


def run_quiz():
    """Main quiz execution function."""
    clear_screen()
    print("="*80)
    print("MOLECULAR GENETICS QUIZ")
    print("="*80)
    print("\nLoading questions...")

    # Load and shuffle questions
    questions = load_questions()
    random.shuffle(questions)
    total_questions = len(questions)

    print(f"\nLoaded {total_questions} questions from Quiz 1, Quiz 2, and Practice Problems.")
    print("\nInstructions:")
    print("  - Answer each question by entering the letter (A, B, C, D, or E)")
    print("  - You'll see immediate feedback and explanations")
    print("  - Enter 'q' at any time to quit")
    print()
    input("Press Enter to begin...")

    correct_count = 0

    # Quiz loop
    for i, question in enumerate(questions, 1):
        clear_screen()
        display_question(question, i, total_questions)

        user_answer = get_answer()
        if user_answer is None:  # User quit
            print("\n\nQuiz ended early.")
            display_final_score(correct_count, i - 1)
            return

        # Check answer
        is_correct = (user_answer == question['correct'])
        if is_correct:
            correct_count += 1

        display_feedback(user_answer, question['correct'], question['explanation'])

        # Pause before next question
        if i < total_questions:
            input("\nPress Enter for next question...")

    # Display final results
    clear_screen()
    display_final_score(correct_count, total_questions)


def main():
    """Entry point for the quiz application."""
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\n\nQuiz interrupted. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
