"""
Job Description Classifier
This module provides functionality to classify job descriptions as fake or real.
"""

import re
from typing import Dict, List, Tuple


class JobClassifier:
    """
    Classifier to identify fake vs real job descriptions using rule-based analysis.
    """
    
    def __init__(self):
        """Initialize the classifier with detection rules."""
        self.fake_indicators = {
            'upfront_payment': [
                r'\$\d+.*(?:registration|fee|training|materials|kit|startup)',
                r'(?:send|pay|invest).*\$\d+',
                r'(?:registration|startup).*(?:fee|cost|payment)'
            ],
            'unrealistic_salary': [
                r'\$\d{4,}.*(?:per day|daily|/day)',
                r'\$\d{4,}.*(?:per week|weekly|/week)',
                r'(?:unlimited|guaranteed).*(?:earning|income)',
                r'\$\d+k.*(?:per week|weekly)',
            ],
            'excessive_punctuation': [
                r'!{3,}',
                r'[A-Z\s]{20,}',
            ],
            'urgency_tactics': [
                r'(?:urgent|hurry|limited|act now|don\'t wait)',
                r'(?:limited spots|filling fast|last chance)',
            ],
            'vague_company': [
                r'(?:global|international|premium).*(?:solutions|enterprises|inc)',
            ],
            'too_easy': [
                r'no (?:experience|skills|interview).*(?:needed|required)',
                r'anyone can do',
                r'(?:easy money|fast cash|quick money)',
            ],
            'work_from_home_scam': [
                r'work from (?:home|anywhere).*\$\d{3,}',
                r'be your own boss.*\$\d{3,}',
            ],
            'guaranteed_income': [
                r'(?:100%|guaranteed).*(?:income|earnings|profit)',
                r'(?:guaranteed|sure).*\$\d+',
            ]
        }
        
        self.real_indicators = {
            'specific_requirements': [
                r'\d+\+?\s*years?.*experience',
                r'(?:BS|BA|MS|MA|PhD).*(?:degree|in)',
                r'(?:certification|certified)',
            ],
            'realistic_salary': [
                r'\$\d{2},\d{3}\s*-\s*\$\d{2,3},\d{3}',
            ],
            'professional_language': [
                r'(?:responsibilities include|seeking|looking for)',
                r'(?:collaborate|develop|manage|analyze|coordinate)',
            ],
            'benefits_mentioned': [
                r'(?:benefits|insurance|401k|pto|paid time off|health)',
            ]
        }
    
    def count_indicators(self, text: str, patterns: List[str]) -> int:
        """Count how many indicators match in the text."""
        count = 0
        text_lower = text.lower()
        for pattern in patterns:
            if re.search(pattern, text_lower, re.IGNORECASE):
                count += 1
        return count
    
    def analyze_job(self, job_description: str) -> Dict:
        """
        Analyze a job description and return classification results.
        
        Args:
            job_description: The job description text to analyze
            
        Returns:
            Dictionary with classification results and detected indicators
        """
        fake_score = 0
        real_score = 0
        detected_fake_flags = []
        detected_real_flags = []
        
        # Check for fake indicators
        for indicator_type, patterns in self.fake_indicators.items():
            matches = self.count_indicators(job_description, patterns)
            if matches > 0:
                fake_score += matches
                detected_fake_flags.append(indicator_type.replace('_', ' ').title())
        
        # Check for real indicators
        for indicator_type, patterns in self.real_indicators.items():
            matches = self.count_indicators(job_description, patterns)
            if matches > 0:
                real_score += matches
                detected_real_flags.append(indicator_type.replace('_', ' ').title())
        
        # Determine classification
        total_score = fake_score + real_score
        if total_score == 0:
            confidence = 0.5
            is_fake = None
            classification = "Uncertain"
        elif fake_score > real_score * 1.5:
            is_fake = True
            confidence = min(0.95, 0.5 + (fake_score / (total_score + 1)) * 0.5)
            classification = "Likely Fake"
        elif real_score > fake_score * 1.5:
            is_fake = False
            confidence = min(0.95, 0.5 + (real_score / (total_score + 1)) * 0.5)
            classification = "Likely Real"
        else:
            confidence = 0.5
            is_fake = None
            classification = "Uncertain"
        
        return {
            'classification': classification,
            'is_fake': is_fake,
            'confidence': confidence,
            'fake_score': fake_score,
            'real_score': real_score,
            'fake_indicators': detected_fake_flags,
            'real_indicators': detected_real_flags
        }
    
    def get_explanation(self, analysis: Dict) -> str:
        """
        Generate a human-readable explanation of the analysis.
        
        Args:
            analysis: The analysis dictionary from analyze_job()
            
        Returns:
            String explanation of the classification
        """
        classification = analysis['classification']
        confidence = analysis['confidence']
        
        explanation = f"Classification: {classification} (Confidence: {confidence:.1%})\n\n"
        
        if analysis['fake_indicators']:
            explanation += "🚩 Warning Signs Detected:\n"
            for indicator in analysis['fake_indicators']:
                explanation += f"  • {indicator}\n"
            explanation += "\n"
        
        if analysis['real_indicators']:
            explanation += "✓ Legitimate Job Indicators:\n"
            for indicator in analysis['real_indicators']:
                explanation += f"  • {indicator}\n"
            explanation += "\n"
        
        # Add recommendations
        if analysis['is_fake']:
            explanation += "⚠️ RECOMMENDATION: This job posting shows multiple red flags commonly "
            explanation += "associated with scams. Exercise extreme caution. Never pay money upfront "
            explanation += "for a job opportunity.\n"
        elif analysis['is_fake'] is False:
            explanation += "✓ RECOMMENDATION: This job posting appears legitimate based on common "
            explanation += "characteristics of real job postings. However, always research the company "
            explanation += "and verify the posting through official channels.\n"
        else:
            explanation += "⚠️ RECOMMENDATION: Unable to determine with confidence. Research the company "
            explanation += "carefully and watch for red flags like upfront fees or unrealistic promises.\n"
        
        return explanation
