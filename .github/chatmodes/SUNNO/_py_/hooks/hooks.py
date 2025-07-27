"""
SUNNO Code Hooks for Centralized Logging and Module Integration
"""

import datetime
import os



# Always resolve logs relative to the location of this hooks.py file
HOOKS_DIR = os.path.abspath(os.path.dirname(__file__))
LOG_DIR = os.path.join(HOOKS_DIR, 'logs')
LOG_FILE = os.path.join(LOG_DIR, datetime.datetime.now().strftime('%y%m%d') + '.md')


def log_event(agent, event_type, details):
    """Log an event to the centralized markdown log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [{agent}] [{event_type}] {details}  "
    # Ensure log directory exists
    os.makedirs(LOG_DIR, exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(entry + '\n')

# Example hooks for each module

def audit_hook(agent, details):
    log_event(agent, "Audit", details)

def error_hook(agent, details):
    log_event(agent, "Error", details)

def security_hook(agent, details):
    log_event(agent, "Security", details)

def sidekick_hook(agent, details):
    log_event(agent, "Sidekick", details)

def objective_hook(agent, details):
    log_event(agent, "Objective", details)

def question_hook(agent, details):
    log_event(agent, "Question", details)

def option_hook(agent, details):
    log_event(agent, "Option", details)

def score_option(agent, option, score, rationale):
    """Log option scoring and rationale for auditability."""
    details = f"Option: {option} | Score: {score} | Rationale: {rationale}"
    log_event(agent, "OptionScore", details)

def file_approval_hook(agent, details):
    log_event(agent, "FileApproval", details)

def test_hook(agent, details):
    log_event(agent, "Test", details)

def sanitization_hook(agent, details):
    log_event(agent, "Sanitization", details)
