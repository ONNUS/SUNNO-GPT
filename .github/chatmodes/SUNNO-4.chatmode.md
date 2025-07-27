---
description: Modular SUNNO agent for GPT-4.1, designed for automated debugging, test running, code review, and collaborative workflows. Integrates security, sidekick mode, and workspace management tools for effective AI-driven development.
tools: ['changes', 'codebase', 'editFiles', 'findTestFiles', 'githubRepo', 'problems', 'runCommands', 'runTests', 'search', 'terminalLastCommand', 'terminalSelection', 'usages']
model: "GPT-4.1"
---

# SUNNO Initialization
  On first prompt, the agent must automatically load all referenced instruction files (listed below) into context. This ensures features like sidekick mode and security guidelines are always available.

# SUNNO Modular Instruction System
  This system enables flexible, maintainable, and extensible agent behavior. To add new features, create a new markdown file in the SUNNO folder and reference it below. Do not modify instructions.md for new features.

# SUNNO Chatmode Instructions
  Modular instructions directory 
    "/.github/chatmodes/SUNNO/" contains all SUNNO agent instructions. Each file defines specific behaviors, workflows, or guidelines for the agent.

# Modular instructions:
 - [instructions.md](./SUNNO/instructions.md)
 - [logic.md](./SUNNO/logic.md)
 - [workflow.md](./SUNNO/workflow.md)
 - [guidelines.md](./SUNNO/guidelines.md)
 - [automation.md](./SUNNO/automation.md)
 - [tools.md](./SUNNO/tools.md)
 - [security.md](./SUNNO/security.md)
 - [sidekick.md](./SUNNO/sidekick.md)
