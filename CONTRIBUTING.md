# Contributing to SUNNO-GPT

Thank you for your interest in contributing to SUNNO-GPT! This simplified guide will help you get started.

## Development Setup

1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/[your-username]/SUNNO-GPT.git
   cd SUNNO-GPT
   ```

3. **Set up the development environment**:
   - Ensure you have GitHub Copilot access
   - Place the chatmode files in your `.github/chatmodes/` directory

## Simplified Architecture

### Core Files
```
SUNNO/
├── instructions.md         # Core behavior and capabilities
├── tools.md               # Tool usage guide
├── logic.md              # Self-diagnosis and error handling
└── prompts.md              # Self-improvement prompts
```

### Contributing Process

#### 1. Testing Your Changes
1. Test with the starter prompts in `prompts.md`
- Run system diagnostics to ensure core functionality works
- Test tool usage with the workflows in `tools.md`
- Verify self-diagnosis capabilities from `logic.md`

#### 2. Making Improvements
- **For Core Behavior**: Update `instructions.md`
- **For Tool Usage**: Update `tools.md`  
- **For Self-Diagnosis**: Update `logic.md`
- **For Testing**: Add new prompts to `prompts.md`

#### 3. Validation
- Test with both SUNNO-4 and SUNNO-4o chatmodes
- Ensure changes improve effectiveness without adding complexity
- Verify that self-diagnosis still works after changes

## Guidelines

### Keep It Simple
- Focus on making SUNNO more effective, not adding features
- Prefer clear, direct instructions over complex workflows
- Ensure any changes improve actual results in VS Code

### Test Thoroughly
- Use real development scenarios to test changes
- Run the diagnostic prompts after making modifications  
- Ensure both chatmodes work identically

### Documentation
- Update relevant files when making changes
- Keep instructions clear and focused
- Add examples when helpful

## Submission Guidelines

### Pull Request Process
1. Create a descriptive PR title
2. Explain what problem your change solves
3. Include test results using starter prompts
4. Show before/after effectiveness if possible

### PR Template
```markdown
## Problem Solved
Brief description of what wasn't working well

## Changes Made
- [ ] Updated instructions.md
- [ ] Updated tools.md  
- [ ] Updated logic.md
- [ ] Added/updated starter prompts

## Testing
- [ ] Tested with SUNNO-4
- [ ] Tested with SUNNO-4o
- [ ] Ran diagnostic prompts
- [ ] Verified in real development scenario

## Results
Describe how this makes SUNNO more effective
```

## Testing with Starter Prompts

Before submitting changes, run these key tests:

1. **System Health Check**: Verify all core functionality works
2. **Tool Functionality Test**: Ensure all tools work as expected
3. **Self-Improvement Loop**: Test that SUNNO can improve itself
4. **Real Development Scenario**: Use SUNNO for actual coding tasks

## Getting Help

- **Documentation**: Check the simplified files in `SUNNO/`
- **Issues**: Search existing issues first
- **Testing**: Use the starter prompts for validation

## Focus Areas

We're particularly interested in contributions that:
- Make SUNNO more effective at debugging and development tasks
- Improve self-diagnosis and automatic improvement capabilities
- Simplify and clarify instructions without losing functionality
- Add useful starter prompts for common scenarios

Thank you for helping make SUNNO more effective! 🚀
