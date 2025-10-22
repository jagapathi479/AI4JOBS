# AI4JOBS - Job Description Analyzer Chatbot

An intelligent chatbot that helps identify fake and real job descriptions, protecting job seekers from employment scams.

## 🎯 Features

- **Interactive Chatbot Interface**: Easy-to-use conversational interface
- **Job Description Analysis**: Analyze any job posting to identify red flags
- **Fake vs Real Classification**: Automatically classify job postings
- **Example Database**: Learn from real examples of fake and legitimate jobs
- **Educational Tips**: Get tips on spotting employment scams
- **Detailed Explanations**: Understand why a job might be fake or real

## 🚀 Quick Start

### Installation

1. Clone the repository:
```bash
git clone https://github.com/jagapathi479/AI4JOBS.git
cd AI4JOBS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

Run the chatbot:
```bash
python chatbot.py
```

## 💡 How to Use

Once you start the chatbot, you can use these commands:

- `analyze` - Analyze a custom job description
- `fake` - See examples of fake job postings
- `real` - See examples of real job postings
- `examples` - See all example job postings
- `tips` - Get tips on spotting fake jobs
- `help` - Show available commands
- `quit` or `exit` - Exit the chatbot

### Example Session

```
💬 You: tips

🎯 TIPS FOR SPOTTING FAKE JOB POSTINGS:

🚩 RED FLAGS:
  • Requests for upfront payment
  • Unrealistic salary promises
  • Excessive exclamation marks
  ...

💬 You: analyze
📝 Enter the job description to analyze.
(Type 'END' on a new line when finished):

Make $5000 per week from home! No experience needed!
END

🔍 ANALYSIS RESULTS
Classification: Likely Fake (Confidence: 85.0%)
...
```

## 🔍 What the Chatbot Analyzes

The classifier looks for multiple indicators:

### Fake Job Red Flags:
- 💰 Upfront payment requirements
- 📈 Unrealistic salary promises
- ⚡ Urgency and scarcity tactics
- 🎯 "Too good to be true" claims
- ❗ Excessive punctuation and caps
- 🏢 Vague company information
- 💵 Guaranteed income promises

### Legitimate Job Indicators:
- ✓ Specific job requirements
- ✓ Realistic salary ranges
- ✓ Professional language
- ✓ Benefits packages
- ✓ Clear responsibilities
- ✓ Standard qualifications

## 📁 Project Structure

```
AI4JOBS/
├── chatbot.py           # Main chatbot interface
├── job_classifier.py    # Job description classifier
├── job_data.py         # Sample job descriptions dataset
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🛡️ Safety Tips

**Never pay money to get a job!** Legitimate employers will never ask you to:
- Pay upfront fees for training or materials
- Send money for background checks
- Invest in the company
- Purchase products or starter kits

**Always verify:**
- Research the company thoroughly
- Check reviews on Glassdoor or Indeed
- Verify contact information
- Look for official company websites
- Be skeptical of generic email addresses

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add more example job descriptions
- Improve the classification rules
- Enhance the chatbot interface
- Add new features

## 📄 License

This project is open source and available for educational purposes.

## ⚠️ Disclaimer

This tool is designed to help identify potential job scams but should not be the only method used to evaluate job opportunities. Always do your own research and use common sense when applying for jobs.