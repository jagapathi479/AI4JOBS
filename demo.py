#!/usr/bin/env python3
"""
Demo script showing how the chatbot analyzes job descriptions.
"""

from job_classifier import JobClassifier
from job_data import get_fake_jobs, get_real_jobs


def demo_analysis():
    """Demonstrate the analysis capabilities."""
    classifier = JobClassifier()
    
    print("="*70)
    print("🤖 JOB DESCRIPTION ANALYZER - DEMO")
    print("="*70)
    print("\nThis demo shows how the chatbot analyzes job descriptions.\n")
    
    # Demo 1: Analyze a fake job
    print("="*70)
    print("EXAMPLE 1: Analyzing a Suspicious Job Posting")
    print("="*70)
    
    fake_example = """
    URGENT OPPORTUNITY! Make $5,000 per week working from home!
    No experience needed! No interviews!
    Just send $99 for our exclusive training kit and start earning TODAY!
    Limited spots available! Act now!!!
    """
    
    print(f"\nJob Description:\n{fake_example}")
    print("\n🔍 Running Analysis...\n")
    
    result = classifier.analyze_job(fake_example)
    explanation = classifier.get_explanation(result)
    print(explanation)
    
    # Demo 2: Analyze a real job
    print("="*70)
    print("EXAMPLE 2: Analyzing a Legitimate Job Posting")
    print("="*70)
    
    real_example = """
    Senior Software Engineer - Python/Django
    
    We are seeking an experienced Software Engineer to join our growing team.
    
    Requirements:
    - 5+ years of experience in software development
    - Strong proficiency in Python and Django framework
    - BS in Computer Science or related field
    - Experience with cloud platforms (AWS/Azure)
    
    Responsibilities:
    - Develop and maintain web applications
    - Collaborate with cross-functional teams
    - Participate in code reviews
    - Mentor junior developers
    
    We offer:
    - Competitive salary: $100,000 - $140,000
    - Health insurance and 401k
    - Flexible work arrangements
    - Professional development opportunities
    """
    
    print(f"\nJob Description:\n{real_example}")
    print("\n🔍 Running Analysis...\n")
    
    result = classifier.analyze_job(real_example)
    explanation = classifier.get_explanation(result)
    print(explanation)
    
    # Demo 3: Show example comparisons
    print("="*70)
    print("EXAMPLE 3: Comparing Multiple Job Postings")
    print("="*70)
    
    fake_jobs = get_fake_jobs()[:2]
    real_jobs = get_real_jobs()[:2]
    
    print("\n🚩 FAKE JOB EXAMPLES:")
    for i, job in enumerate(fake_jobs, 1):
        print(f"\n{i}. {job['title']} at {job['company']}")
        print(f"   Key Red Flags: {', '.join(job['indicators'][:3])}")
    
    print("\n\n✓ REAL JOB EXAMPLES:")
    for i, job in enumerate(real_jobs, 1):
        print(f"\n{i}. {job['title']} at {job['company']}")
        print(f"   Legitimate Indicators: {', '.join(job['indicators'][:3])}")
    
    print("\n" + "="*70)
    print("📚 SAFETY REMINDERS:")
    print("="*70)
    print("""
✓ Never pay money to get a job
✓ Research companies thoroughly
✓ Be skeptical of unrealistic promises
✓ Verify job postings through official channels
✓ Trust your instincts - if it seems too good to be true, it probably is
    """)
    
    print("="*70)
    print("Demo Complete! Run 'python chatbot.py' for interactive mode.")
    print("="*70)


if __name__ == "__main__":
    demo_analysis()
