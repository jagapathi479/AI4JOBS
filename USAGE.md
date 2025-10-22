# Usage Guide - AI4JOBS Chatbot

## Quick Start

1. **Installation**
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify Installation**
   ```bash
   python verify.py
   ```

3. **Run the Chatbot**
   ```bash
   python chatbot.py
   ```

## Features Overview

### 1. Interactive Commands

- `analyze` - Analyze your own job description
- `fake` - View examples of fake job postings
- `real` - View examples of legitimate job postings  
- `examples` - View all example job postings
- `tips` - Get tips for spotting fake jobs
- `help` - Display available commands
- `quit` or `exit` - Exit the chatbot

### 2. Analyzing Job Descriptions

When you use the `analyze` command, you can paste any job description and the chatbot will:
- Classify it as Likely Fake, Likely Real, or Uncertain
- Show confidence level
- List detected red flags
- List legitimate indicators
- Provide recommendations

Example:
```
💬 You: analyze
📝 Enter the job description to analyze.
(Type 'END' on a new line when finished):

Make $5000 per week! No experience needed!
Just pay $99 for training materials!
END

🔍 ANALYSIS RESULTS
Classification: Likely Fake (Confidence: 85.0%)

🚩 Warning Signs Detected:
  • Upfront Payment
  • Unrealistic Salary
  • Too Easy

⚠️ RECOMMENDATION: This job posting shows multiple red flags...
```

### 3. Learning from Examples

Use `fake`, `real`, or `examples` commands to see sample job postings and learn what to look for.

### 4. Getting Safety Tips

Use the `tips` command to see a comprehensive list of:
- Red flags to watch for
- Signs of legitimate jobs
- Safety recommendations

## Running Demos

### Test Suite
```bash
python test_chatbot.py
```
This runs comprehensive tests and shows the classifier accuracy.

### Demo Mode
```bash
python demo.py
```
This shows detailed examples of job analysis with explanations.

## What the Classifier Detects

### Fake Job Red Flags

1. **Upfront Payment Requests**
   - Training fees
   - Material costs
   - Registration fees
   - Investment requirements

2. **Unrealistic Promises**
   - $500+ per day for simple tasks
   - Guaranteed income
   - No experience needed for high-paying jobs

3. **Pressure Tactics**
   - Urgency (limited time, act now)
   - Scarcity (limited spots)
   - Excessive punctuation (!!!)

4. **Vague Information**
   - Generic company names
   - No clear job duties
   - Missing requirements

### Legitimate Job Indicators

1. **Clear Requirements**
   - Specific years of experience
   - Educational qualifications
   - Technical skills needed

2. **Professional Details**
   - Realistic salary ranges
   - Benefits packages
   - Clear responsibilities

3. **Standard Practices**
   - Interview process
   - Application procedures
   - Company information

## Safety Guidelines

### ⚠️ NEVER

- Pay money to get a job
- Provide financial information upfront
- Accept jobs that seem too good to be true
- Skip background research on the company

### ✓ ALWAYS

- Research the company thoroughly
- Verify job postings through official channels
- Check company reviews on Glassdoor/Indeed
- Look for official company websites and contact info
- Trust your instincts

## Tips for Best Results

1. **Provide Complete Descriptions**
   - Include job title, salary, requirements
   - More text = better analysis

2. **Look for Patterns**
   - Use the examples to understand common patterns
   - Learn to recognize red flags

3. **Use Multiple Sources**
   - Don't rely solely on this tool
   - Cross-reference with other verification methods

4. **Stay Updated**
   - Scam tactics evolve over time
   - Stay informed about new fraud patterns

## Troubleshooting

### Issue: Module not found
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: Chatbot doesn't start
**Solution:** Run verification
```bash
python verify.py
```

### Issue: Unexpected classification
**Solution:** The classifier uses rules-based detection. Some edge cases may be misclassified. Always use your judgment and additional research.

## Contributing

To improve the chatbot:
1. Add more example job descriptions to `job_data.py`
2. Enhance classification rules in `job_classifier.py`
3. Add new features to `chatbot.py`

## Support

For issues or questions:
- Check the README.md
- Review the examples with `python demo.py`
- Run tests with `python test_chatbot.py`

## Disclaimer

This tool is designed to help identify potential scams but should not be your only method of verification. Always research companies and job postings thoroughly before applying or providing any information.
