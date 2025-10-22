#!/usr/bin/env python3
"""
Test script to demonstrate the chatbot functionality.
"""

from job_classifier import JobClassifier
from job_data import get_all_jobs, get_fake_jobs, get_real_jobs


def test_classifier():
    """Test the job classifier with various examples."""
    print("="*70)
    print("TESTING JOB CLASSIFIER")
    print("="*70)
    
    classifier = JobClassifier()
    
    # Test cases
    test_cases = [
        {
            "name": "Fake Job - Upfront Fee Scam",
            "description": "Make $5000 per week! Pay $99 for training materials! No experience needed!"
        },
        {
            "name": "Real Job - Software Engineer",
            "description": "Software Engineer needed. 3+ years Python experience. BS in CS required. Salary: $80,000-$120,000. Develop web applications and collaborate with team."
        },
        {
            "name": "Fake Job - Too Good to Be True",
            "description": "WORK FROM HOME!!! $10,000 monthly GUARANTEED!!! No interviews! Anyone can do this!"
        },
        {
            "name": "Real Job - Marketing Manager",
            "description": "Marketing Manager position available. 5+ years experience in digital marketing. Lead team and manage campaigns. Competitive salary with benefits package."
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*70}")
        print(f"TEST {i}: {test_case['name']}")
        print('='*70)
        print(f"\nJob Description:\n{test_case['description']}\n")
        
        result = classifier.analyze_job(test_case['description'])
        explanation = classifier.get_explanation(result)
        print(explanation)
    
    print("="*70)
    print("CLASSIFIER TESTING COMPLETE")
    print("="*70)


def test_data_loading():
    """Test loading of job data."""
    print("\n" + "="*70)
    print("TESTING DATA LOADING")
    print("="*70)
    
    all_jobs = get_all_jobs()
    fake_jobs = get_fake_jobs()
    real_jobs = get_real_jobs()
    
    print(f"\nTotal job examples: {len(all_jobs)}")
    print(f"Fake job examples: {len(fake_jobs)}")
    print(f"Real job examples: {len(real_jobs)}")
    
    print("\n📋 Sample Fake Job:")
    if fake_jobs:
        job = fake_jobs[0]
        print(f"  Title: {job['title']}")
        print(f"  Company: {job['company']}")
        print(f"  Red Flags: {', '.join(job['indicators'][:3])}")
    
    print("\n📋 Sample Real Job:")
    if real_jobs:
        job = real_jobs[0]
        print(f"  Title: {job['title']}")
        print(f"  Company: {job['company']}")
        print(f"  Indicators: {', '.join(job['indicators'][:3])}")
    
    print("\n" + "="*70)
    print("DATA LOADING COMPLETE")
    print("="*70)


def test_accuracy():
    """Test classifier accuracy on sample data."""
    print("\n" + "="*70)
    print("TESTING CLASSIFIER ACCURACY")
    print("="*70)
    
    classifier = JobClassifier()
    all_jobs = get_all_jobs()
    
    correct = 0
    total = len(all_jobs)
    
    print(f"\nTesting on {total} job examples...\n")
    
    for job in all_jobs:
        result = classifier.analyze_job(job['description'])
        expected_fake = job['is_fake']
        predicted_fake = result['is_fake']
        
        is_correct = (expected_fake == predicted_fake)
        if is_correct:
            correct += 1
        
        status = "✓" if is_correct else "✗"
        expected_label = "FAKE" if expected_fake else "REAL"
        predicted_label = "FAKE" if predicted_fake else "REAL" if predicted_fake is not None else "UNCERTAIN"
        
        print(f"{status} {job['title'][:40]:<40} Expected: {expected_label:<10} Got: {predicted_label}")
    
    accuracy = (correct / total) * 100
    print(f"\n{'='*70}")
    print(f"Accuracy: {correct}/{total} = {accuracy:.1f}%")
    print(f"{'='*70}")


def main():
    """Run all tests."""
    print("\n🤖 AI4JOBS - Job Description Analyzer Test Suite\n")
    
    # Run tests
    test_data_loading()
    test_classifier()
    test_accuracy()
    
    print("\n✅ All tests completed!\n")
    print("To run the interactive chatbot, use: python chatbot.py\n")


if __name__ == "__main__":
    main()
