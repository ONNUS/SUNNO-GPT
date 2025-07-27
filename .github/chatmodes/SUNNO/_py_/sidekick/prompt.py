"""
SUNNO Sidekick Prompt Utility
Structured like hooks.py; logs saved in sidekick/logs/YYYYMMDD.md
"""

import datetime
import os

SIDEKICK_DIR = os.path.abspath(os.path.dirname(__file__))
LOG_DIR = os.path.join(SIDEKICK_DIR, 'logs')
LOG_FILE = os.path.join(LOG_DIR, datetime.datetime.now().strftime('%y%m%d') + '.md')

PROMPT_TEMPLATE = '''
```
Sidekick, please review the following decision point:

Context:
{context}

Decision/Action:
{decision}

Questions:
{questions}
```
'''

def generate_sidekick_prompt(context, decision, questions):
    """
    Generate a markdown code block prompt for sidekick review.
    Args:
        context (str): Context of the decision point.
        decision (str): The decision or action taken.
        questions (str): Questions for the sidekick.
    Returns:
        str: Markdown code block prompt.
    """
    return PROMPT_TEMPLATE.format(context=context, decision=decision, questions=questions)

def log_sidekick_event(agent, event_type, prompt, response):
    """
    Log a sidekick event to the markdown log file.
    Args:
        agent (str): Agent name or ID.
        event_type (str): Event type (e.g., 'Review', 'Feedback').
        prompt (str): The prompt sent to sidekick.
        response (str): The response received from sidekick.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [{agent}] [{event_type}]\nPROMPT:\n{prompt}\nRESPONSE:\n{response}\n"
    os.makedirs(LOG_DIR, exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(entry + '\n')

# Example usage:
if __name__ == "__main__":
    context = "Audit found ambiguous objective."
    decision = "Escalate to sidekick for review."
    questions = "Is the objective clear? What improvements do you suggest?"
    prompt = generate_sidekick_prompt(context, decision, questions)
    print(prompt)
    # Simulate sidekick response
    response = "Objective needs clarification. Suggest adding more details."
    log_sidekick_event("SUNNO-Agent", "Review", prompt, response)
