"""
Job Description Chatbot
Interactive chatbot to analyze job descriptions and identify fake vs real postings.
"""

import sys
from job_classifier import JobClassifier
from job_data import get_fake_jobs, get_real_jobs, get_all_jobs


class JobDescriptionChatbot:
    """
    Interactive chatbot for analyzing job descriptions.
    """
    
    def __init__(self):
        """Initialize the chatbot with classifier and sample data."""
        self.classifier = JobClassifier()
        self.fake_jobs = get_fake_jobs()
        self.real_jobs = get_real_jobs()
        self.all_jobs = get_all_jobs()
        
    def display_welcome(self):
        """Display welcome message."""
        print("\n" + "="*70)
        print("🤖 JOB DESCRIPTION ANALYZER CHATBOT")
        print("="*70)
        print("\nWelcome! I can help you identify fake and real job descriptions.")
        print("\nWhat I can do:")
        print("  1. Analyze custom job descriptions")
        print("  2. Show examples of fake job postings")
        print("  3. Show examples of real job postings")
        print("  4. Explain red flags in job scams")
        print("\nType 'help' for commands or 'quit' to exit.")
        print("="*70 + "\n")
    
    def display_help(self):
        """Display help information."""
        print("\n📋 AVAILABLE COMMANDS:")
        print("  analyze     - Analyze a custom job description")
        print("  fake        - See examples of fake job postings")
        print("  real        - See examples of real job postings")
        print("  examples    - See all example job postings")
        print("  tips        - Get tips on spotting fake jobs")
        print("  help        - Show this help message")
        print("  quit/exit   - Exit the chatbot\n")
    
    def display_tips(self):
        """Display tips for identifying fake jobs."""
        print("\n🎯 TIPS FOR SPOTTING FAKE JOB POSTINGS:\n")
        print("🚩 RED FLAGS:")
        print("  • Requests for upfront payment (training fees, materials, etc.)")
        print("  • Unrealistic salary promises ($500+/day for simple tasks)")
        print("  • Excessive exclamation marks and ALL CAPS text")
        print("  • Vague or generic company names")
        print("  • 'Too good to be true' claims (no experience needed, guaranteed income)")
        print("  • Urgency tactics (limited spots, act now)")
        print("  • No interview process mentioned")
        print("  • Poor grammar and unprofessional language")
        print("\n✓ SIGNS OF LEGITIMATE JOBS:")
        print("  • Specific job requirements and qualifications")
        print("  • Realistic salary ranges")
        print("  • Professional, detailed job descriptions")
        print("  • Clear company information")
        print("  • Standard application process")
        print("  • Benefits package mentioned")
        print("  • No upfront fees required\n")
    
    def show_examples(self, job_type='all'):
        """Show example job postings."""
        if job_type == 'fake':
            jobs = self.fake_jobs
            title = "FAKE JOB EXAMPLES"
        elif job_type == 'real':
            jobs = self.real_jobs
            title = "REAL JOB EXAMPLES"
        else:
            jobs = self.all_jobs
            title = "ALL JOB EXAMPLES"
        
        print(f"\n{'='*70}")
        print(f"📑 {title}")
        print('='*70)
        
        for i, job in enumerate(jobs, 1):
            print(f"\n{i}. {job['title']} at {job['company']}")
            print(f"   Type: {'❌ FAKE' if job['is_fake'] else '✓ REAL'}")
            print(f"   Location: {job['location']}")
            print(f"   Salary: {job['salary_range']}")
            print(f"   Description: {job['description'][:100]}...")
            if job['indicators']:
                print(f"   Key Indicators: {', '.join(job['indicators'][:3])}")
        print()
    
    def analyze_custom_job(self):
        """Analyze a custom job description provided by user."""
        print("\n📝 Enter the job description to analyze.")
        print("(Type 'END' on a new line when finished):\n")
        
        lines = []
        while True:
            try:
                line = input()
                if line.strip().upper() == 'END':
                    break
                lines.append(line)
            except EOFError:
                break
        
        job_description = '\n'.join(lines)
        
        if not job_description.strip():
            print("❌ No description provided. Please try again.")
            return
        
        print("\n" + "="*70)
        print("🔍 ANALYSIS RESULTS")
        print("="*70 + "\n")
        
        # Analyze the job
        analysis = self.classifier.analyze_job(job_description)
        explanation = self.classifier.get_explanation(analysis)
        
        print(explanation)
    
    def process_command(self, command):
        """Process user command."""
        command = command.strip().lower()
        
        if command in ['quit', 'exit', 'q']:
            return False
        elif command == 'help':
            self.display_help()
        elif command == 'analyze':
            self.analyze_custom_job()
        elif command == 'fake':
            self.show_examples('fake')
        elif command == 'real':
            self.show_examples('real')
        elif command in ['examples', 'all']:
            self.show_examples('all')
        elif command == 'tips':
            self.display_tips()
        else:
            print(f"❌ Unknown command: '{command}'. Type 'help' for available commands.")
        
        return True
    
    def run(self):
        """Run the chatbot main loop."""
        self.display_welcome()
        
        while True:
            try:
                user_input = input("💬 You: ").strip()
                
                if not user_input:
                    continue
                
                if not self.process_command(user_input):
                    print("\n👋 Thank you for using Job Description Analyzer! Stay safe!")
                    break
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except EOFError:
                print("\n👋 Goodbye!")
                break


def main():
    """Main entry point for the chatbot."""
    chatbot = JobDescriptionChatbot()
    chatbot.run()


if __name__ == "__main__":
    main()
