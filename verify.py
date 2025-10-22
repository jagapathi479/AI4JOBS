#!/usr/bin/env python3
"""
Verification script to ensure chatbot is working correctly.
This script runs a comprehensive check of all components.
"""

import sys
from job_classifier import JobClassifier
from job_data import get_all_jobs, get_fake_jobs, get_real_jobs


def verify_installation():
    """Verify that all components are properly installed."""
    print("="*70)
    print("🔍 VERIFYING INSTALLATION")
    print("="*70)
    
    try:
        # Check imports
        print("\n✓ All modules imported successfully")
        
        # Check classifier
        classifier = JobClassifier()
        print("✓ Job classifier initialized")
        
        # Check data
        jobs = get_all_jobs()
        print(f"✓ Loaded {len(jobs)} job examples")
        
        fake_count = len(get_fake_jobs())
        real_count = len(get_real_jobs())
        print(f"  - {fake_count} fake job examples")
        print(f"  - {real_count} real job examples")
        
        # Test classification
        test_job = "Software Engineer. 3+ years experience. BS in Computer Science. Salary: $80,000-$120,000."
        result = classifier.analyze_job(test_job)
        print("✓ Classifier analysis working")
        
        print("\n" + "="*70)
        print("✅ ALL CHECKS PASSED!")
        print("="*70)
        print("\nThe chatbot is ready to use. Run: python chatbot.py")
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("\nPlease ensure all dependencies are installed:")
        print("  pip install -r requirements.txt")
        return False


if __name__ == "__main__":
    success = verify_installation()
    sys.exit(0 if success else 1)
