# Contributing to SUNNO-GPT

Thank you for your interest in contributing to SUNNO-GPT! This guide will help you get started.

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

## Architecture Guidelines

### Modular Design
- New Features: Create separate `.md` files in the `SUNNO/` folder
- Don't Modify: Avoid changing `instructions.md` for new features
- Reference System: Update chatmode files to reference new modules

### File Organization
```
SUNNO/
├── [feature].md         # Feature-specific instructions
├── prompts/
│   └── [feature].md     # Starter prompts for testing
└── _py_/
    └── [feature]/       # Python utilities (if needed)
```

## Contributing Process

### 1. Planning
- Check existing issues and discussions
- Create an issue for new features or major changes
- Use SUNNO sidekick mode for design review

### 2. Development
- Follow the modular architecture
- Add starter prompts for testing your changes
- Include security considerations per `security.md`
- Add comprehensive logging hooks

### 3. Testing
- Use starter prompts in `prompts/` folder
- Test with both SUNNO-4 and SUNNO-4o models
- Run security audits
- Validate workflow integration

### 4. Documentation
- Update relevant instruction files
- Add usage examples
- Document any new tools or capabilities
- Include version history in modified files

## Code Standards

### Python Code
- Follow PEP 8 style guidelines
- Include docstrings for all functions
- Use type hints where appropriate
- Add logging hooks for transparency

### Markdown Documentation
- Use consistent formatting
- Include file path comments
- Add version history sections
- Reference related files appropriately

### Security
- Follow OWASP LLM guidelines
- Include input validation
- Add sanitization for risky operations
- Document security implications

## Testing Guidelines

### Automated Testing
```python
# Example test structure
from SUNNO._py_.hooks import log_event

def test_feature():
    log_event("Test", "Feature", "Testing new functionality")
    # Test implementation
    assert result == expected
```

### Manual Testing
- Use starter prompts for validation
- Test edge cases and error conditions
- Verify sidekick integration
- Check audit trail completeness

## Sidekick Collaboration

When developing complex features:

```
Activate sidekick mode. Sidekick, please review my proposed changes to [feature]. 
Audit for security, efficiency, and integration with existing SUNNO modules.
```

## Submission Guidelines

### Pull Request Process
1. Create a descriptive PR title
2. Fill out the PR template
3. Include test results
4. Document any breaking changes
5. Add screenshots for UI changes

### PR Template
```markdown
## Description
Brief description of changes

## Changes Made
- [ ] Added new feature
- [ ] Updated documentation
- [ ] Fixed bug
- [ ] Added tests

## Testing
- [ ] Tested with SUNNO-4
- [ ] Tested with SUNNO-4o
- [ ] Ran security audit
- [ ] Validated workflow integration

## Security Review
- [ ] Follows OWASP guidelines
- [ ] Includes input validation
- [ ] No privilege escalation risks
- [ ] Audit trail maintained
```

## Community Guidelines

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Follow the code of conduct

## Getting Help

- Documentation: Check the `SUNNO/` folder
- Issues: Search existing issues first
- Discussions: Use GitHub Discussions for questions
- Sidekick Mode: Use SUNNO's collaborative features

Thank you for contributing to SUNNO-GPT! 🚀
