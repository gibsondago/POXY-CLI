<div align="center">

# 🚀 Contributing to Poxy CLI

[![Contributions](https://img.shields.io/badge/Contributions-Welcome-blue)](#)
[![Open Source](https://img.shields.io/badge/Open%20Source-Community-green)](#)
[![PRs](https://img.shields.io/badge/PRs-Encouraged-yellow)](#)

</div>

<div align="center">

**🌟 Join Our Open Source Journey** - Help us build the most advanced proxy management tool together. Every contribution, big or small, makes a difference!

**[📋 Getting Started](#-getting-started) • [🐛 Report Issues](#-report-issues) • [💡 Feature Requests](#-feature-requests) • [🔧 Development](#-development-setup) • [📝 Guidelines](#-contribution-guidelines)**

</div>

<br/>

## 🎯 Why Contribute?

Your contributions help make **Poxy CLI** better for everyone! Whether you're:
- 🐛 **Fixing bugs** to improve stability
- ✨ **Adding features** to enhance functionality
- 📚 **Improving documentation** to help other users
- 🎨 **Enhancing UI/UX** for better user experience
- 🔒 **Strengthening security** to protect users

**Every contribution counts!** 🚀

## 📋 Getting Started

### 🌟 **First Steps**
1. **📖 Read our [Code of Conduct](CODE_OF_CONDUCT.md)** - Understand our community values
2. **🔍 Explore the [README.md](README.md)** - Learn about the project
3. **🔒 Check our [Security Policy](SECURITY.md)** - Know how we handle vulnerabilities
4. **⭐ Star the repository** - Show your support for the project!

### 🛠️ **Development Environment**
```bash
# Clone the repository
git clone https://github.com/rezaulwork/POXY-CLI.git
cd POXY-CLI

# Set up virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

## 🐛 Report Issues

### 🚨 **Bug Reports**
Help us identify and fix problems! Here's how to create an effective bug report:

#### ✅ **Good Bug Report Template**
```markdown
**🐛 Bug Description**
[Clear, concise description of the issue]

**🔄 Steps to Reproduce**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**💻 Environment**
- **OS**: [Windows/Linux/macOS]
- **Python Version**: [e.g., 3.9.0]
- **Poxy CLI Version**: [e.g., v1.0.0]

**⚡ Expected Behavior**
[What should happen]

**❌ Actual Behavior**
[What actually happens]

**📸 Screenshots/Logs**
[Include relevant screenshots or error logs]
```

#### 🔍 **Before Reporting**
- ✅ **Search existing issues** - Someone might have reported it already
- ✅ **Check the latest version** - The bug might be fixed
- ✅ **Include reproduction steps** - Help us reproduce the issue
- ✅ **Add environment details** - Context helps with debugging

## 💡 Feature Requests

### ✨ **Suggesting New Features**
Have an idea that would make Poxy CLI even better? We'd love to hear it!

#### ✅ **Effective Feature Request Template**
```markdown
**🎯 Feature Description**
[What feature do you want and why?]

**🔍 Problem Statement**
[What problem does this solve?]

**💡 Proposed Solution**
[How would you implement this feature?]

**🎨 User Experience**
[How would users interact with this feature?]

**📋 Additional Context**
[Any other relevant information, mockups, or examples]
```

## 🔧 Development Workflow

### 🚀 **Pull Request Process**

#### 1. 🍴 **Fork & Clone**
```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/POXY-CLI.git
cd POXY-CLI
```

#### 2. 🌿 **Create Feature Branch**
```bash
# Create a descriptive branch name
git checkout -b feature/amazing-new-feature
# or
git checkout -b fix/bug-description
# or
git checkout -b docs/update-readme
```

#### 3. 💻 **Make Your Changes**
- Write clean, readable code
- Add tests for new functionality
- Update documentation as needed
- Follow our coding standards

#### 4. 🧪 **Test Your Changes**
```bash
# Run existing tests
python -m pytest

# Test your specific changes
python main.py --help

# Manual testing
python main.py list  # Test proxy listing
python main.py add test --type http --host example.com --port 8080
```

#### 5. 📝 **Commit Your Changes**
```bash
# Stage your changes
git add .

# Write a clear commit message
git commit -m "Add: amazing new feature that solves X problem

- Detailed description of changes
- Why this change was made
- Any breaking changes or migration notes"
```

#### 6. 🚀 **Push & Create PR**
```bash
# Push to your fork
git push origin feature/amazing-new-feature

# Create Pull Request on GitHub
# Fill out the PR template completely
```

### 📋 **Pull Request Template**
```markdown
## 📋 Description
[Brief description of changes]

## 🔍 Type of Change
- [ ] 🐛 Bug fix
- [ ] ✨ New feature
- [ ] 📚 Documentation update
- [ ] 🎨 UI/UX improvement
- [ ] 🔒 Security enhancement
- [ ] ⚡ Performance improvement

## ✅ Checklist
- [ ] 🔍 I have read the [Contributing Guide](CONTRIBUTING.md)
- [ ] 🤝 I agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md)
- [ ] 🧪 I have tested my changes thoroughly
- [ ] 📚 I have updated documentation (if needed)
- [ ] 🔒 Security impact assessed (if relevant)

## 🎯 Related Issues
Closes #[issue_number]

## 🔄 Testing
[How you tested these changes]

## 📸 Screenshots
[Before/after screenshots if UI changes]
```

## 📝 Contribution Guidelines

### 💻 **Code Standards**

| Aspect | Standard | Tool/Enforcement |
|--------|----------|------------------|
| **Python Style** | PEP 8 | `flake8`, `black` |
| **Type Hints** | ✅ Required for new code | `mypy` |
| **Documentation** | Google/Sphinx style | `sphinx` |
| **Testing** | pytest framework | `pytest-cov` |
| **Imports** | `isort` organized | `isort` |

### 🧪 **Testing Requirements**
- ✅ **Unit tests** for new functions
- ✅ **Integration tests** for new features
- ✅ **Minimum 80% coverage** for new code
- ✅ **Test both success and failure cases**

### 📚 **Documentation Standards**
- ✅ **Docstrings** for all public functions
- ✅ **README updates** for new features
- ✅ **Usage examples** in documentation
- ✅ **Clear parameter descriptions**

### 🔒 **Security Considerations**
- ✅ **Input validation** for all user inputs
- ✅ **No hardcoded credentials** in code
- ✅ **Safe proxy handling** practices
- ✅ **Error messages** don't leak sensitive info

## 🌟 Recognition & Rewards

### 🏆 **Contributors Hall of Fame**
We love recognizing our amazing contributors:

- ⭐ **GitHub Stars** and social media shoutouts
- 📝 **Release notes** featuring your contributions
- 🎯 **Priority support** for active contributors
- 🚀 **Early access** to new features and betas

### 💝 **Special Acknowledgments**
- **🐛 Bug Hunters**: Special mention for security researchers
- **📚 Documentation Heroes**: Recognition for documentation improvements
- **🎨 UX Champions**: Shoutouts for UI/UX enhancements
- **🔧 Code Wizards**: Technical excellence acknowledgments

## 🛠️ Development Tools

### 🔧 **Recommended Setup**
```bash
# Code formatting
pip install black isort flake8

# Type checking
pip install mypy

# Testing tools
pip install pytest pytest-cov

# Documentation
pip install sphinx

# Development helpers
pip install pre-commit
```

### ⚙️ **Pre-commit Hooks**
```bash
# Install pre-commit hooks
pre-commit install

# Available hooks:
# - Code formatting (black, isort)
# - Linting (flake8)
# - Type checking (mypy)
# - Trailing whitespace removal
```

## 📞 Getting Help

### 🌐 **Community Channels**
- **🐛 Issues**: [GitHub Issues](https://github.com/rezaulwork/POXY-CLI/issues) - Bug reports and feature requests
- **💬 Discussions**: [GitHub Discussions](https://github.com/rezaulwork/POXY-CLI/discussions) - Q&A and community chat
- **📧 Email**: work.rezaul@outlook.com - Direct contact with maintainers

### ❓ **Common Questions**
**Q: How do I start contributing?**
A: Start with documentation improvements or bug fixes - they're great entry points!

**Q: I found a bug but don't know how to fix it**
A: No worries! Just report it clearly and we'll help figure out the solution.

**Q: Can I contribute even if I'm new to Python?**
A: Absolutely! We welcome contributors of all skill levels.

## 🎯 Quick Start Checklist

- [ ] ⭐ **Star the repository**
- [ ] 📖 **Read the documentation**
- [ ] 🐛 **Look for open issues** you can help with
- [ ] 🍴 **Fork the repository**
- [ ] 🌟 **Make your first contribution**
- [ ] 🚀 **Submit a pull request**

---

<div align="center">

**🏠 [Home](README.md) • 🤝 [Code of Conduct](CODE_OF_CONDUCT.md) • 🔒 [Security](SECURITY.md) • 📋 [Usage](USAGE.md)**

**🚀 Built with ❤️ by the Open Source Community & [REZ LAB](https://github.com/rezaulwork)**

</div>
