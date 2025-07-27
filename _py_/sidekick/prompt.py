def generate_sidekick_prompt(context, decision, questions):
    return f"""Sidekick, please review: {context}\nDecision: {decision}\nQuestions: {questions}"""

def log_sidekick_event(agent, event_type, prompt, response):
    with open(f"./_py_/sidekick/logs/20250727.md", "a") as log:
        log.write(f"\n- {agent}: {event_type}\n- Prompt: {prompt}\n- Response: {response}\n")
