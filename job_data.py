"""
Sample job descriptions dataset with fake and real examples.
This module contains sample data for training and testing the fake job detector.
"""

SAMPLE_JOB_DESCRIPTIONS = [
    {
        "title": "Software Engineer",
        "company": "Tech Corp",
        "description": "We are looking for a talented Software Engineer to join our team. You will work on developing web applications using Python and JavaScript. Requirements: 3+ years of experience, BS in Computer Science or related field. Competitive salary and benefits package.",
        "requirements": "Python, JavaScript, 3+ years experience, BS degree",
        "salary_range": "$80,000 - $120,000",
        "location": "San Francisco, CA",
        "is_fake": False,
        "indicators": ["Clear requirements", "Specific salary range", "Professional description"]
    },
    {
        "title": "Data Entry Specialist",
        "company": "Global Solutions Inc",
        "description": "URGENT! Make $5000/week working from home! No experience needed! Just send $99 for training materials and start earning immediately! Limited spots available!",
        "requirements": "None - anyone can do this!",
        "salary_range": "$5000/week!!!",
        "location": "Work from anywhere!",
        "is_fake": True,
        "indicators": ["Too good to be true salary", "Upfront payment required", "Excessive exclamation marks", "Vague description", "Urgency tactics"]
    },
    {
        "title": "Marketing Manager",
        "company": "ABC Marketing Agency",
        "description": "Seeking experienced Marketing Manager to lead our digital marketing team. Responsibilities include developing marketing strategies, managing campaigns, and analyzing performance metrics. Must have 5+ years experience in digital marketing and proven track record of successful campaigns.",
        "requirements": "5+ years experience, Digital marketing expertise, Team leadership",
        "salary_range": "$70,000 - $95,000",
        "location": "New York, NY",
        "is_fake": False,
        "indicators": ["Specific role description", "Reasonable requirements", "Professional language"]
    },
    {
        "title": "Online Survey Taker",
        "company": "EZ Money Co",
        "description": "Earn $500 daily taking surveys! No skills needed! Work 2 hours a day! Send payment of $50 to receive your survey list! 100% guaranteed income!",
        "requirements": "Must pay $50 registration fee",
        "salary_range": "$500 per day guaranteed!",
        "location": "Remote",
        "is_fake": True,
        "indicators": ["Unrealistic earnings", "Registration fee required", "Too easy claims", "Guaranteed income promise"]
    },
    {
        "title": "Senior Data Scientist",
        "company": "DataTech Solutions",
        "description": "We're hiring a Senior Data Scientist to work on machine learning projects. You'll build predictive models, analyze large datasets, and collaborate with cross-functional teams. Requirements: PhD or MS in relevant field, 4+ years experience with Python, R, and ML frameworks.",
        "requirements": "MS/PhD, Python, R, ML experience, 4+ years",
        "salary_range": "$110,000 - $150,000",
        "location": "Boston, MA",
        "is_fake": False,
        "indicators": ["Specific technical requirements", "Realistic salary", "Detailed job description"]
    },
    {
        "title": "Executive Assistant",
        "company": "Premium Enterprises",
        "description": "MAKE MONEY FAST!!! Be your own boss! $10,000/month working part-time! No interviews! No experience! Just pay $200 for our exclusive business kit!",
        "requirements": "Pay $200 to get started",
        "salary_range": "$10,000/month GUARANTEED",
        "location": "Worldwide",
        "is_fake": True,
        "indicators": ["Excessive caps and exclamation marks", "Unrealistic income", "Upfront fee", "No real job duties", "No interview process"]
    },
    {
        "title": "Project Manager",
        "company": "Construction Dynamics",
        "description": "Experienced Project Manager needed for commercial construction projects. Manage project timelines, budgets, and coordinate with contractors. PMP certification preferred. 5+ years in construction management required.",
        "requirements": "5+ years construction management, PMP preferred, Budget management",
        "salary_range": "$85,000 - $110,000",
        "location": "Austin, TX",
        "is_fake": False,
        "indicators": ["Industry-specific requirements", "Professional credentials mentioned", "Clear responsibilities"]
    },
    {
        "title": "Customer Service Representative",
        "company": "Retail Plus",
        "description": "Join our customer service team! Handle customer inquiries, process orders, and resolve issues. Must have excellent communication skills and 1+ year customer service experience. We offer training, health insurance, and paid time off.",
        "requirements": "1+ year customer service, Good communication",
        "salary_range": "$35,000 - $45,000",
        "location": "Chicago, IL",
        "is_fake": False,
        "indicators": ["Clear job duties", "Reasonable experience requirement", "Benefits mentioned"]
    },
    {
        "title": "Crypto Investment Manager",
        "company": "Blockchain Wealth",
        "description": "SECRET OPPORTUNITY! Triple your income in 30 days! Invest just $1000 and we'll make you rich! Limited time offer! No experience needed! Join now before spots fill up!",
        "requirements": "Must invest $1000 minimum",
        "salary_range": "Unlimited earning potential!!!",
        "location": "Online",
        "is_fake": True,
        "indicators": ["Investment scam red flags", "Unrealistic promises", "Urgency and scarcity tactics", "No legitimate job duties"]
    },
    {
        "title": "Graphic Designer",
        "company": "Creative Studio X",
        "description": "Looking for creative Graphic Designer to work on branding and marketing materials. Proficiency in Adobe Creative Suite required. 2+ years of professional design experience. Portfolio review required.",
        "requirements": "2+ years experience, Adobe Creative Suite, Portfolio",
        "salary_range": "$50,000 - $70,000",
        "location": "Los Angeles, CA",
        "is_fake": False,
        "indicators": ["Specific software requirements", "Portfolio requirement (standard for design)", "Realistic experience level"]
    }
]

def get_fake_jobs():
    """Returns list of fake job descriptions."""
    return [job for job in SAMPLE_JOB_DESCRIPTIONS if job["is_fake"]]

def get_real_jobs():
    """Returns list of real job descriptions."""
    return [job for job in SAMPLE_JOB_DESCRIPTIONS if not job["is_fake"]]

def get_all_jobs():
    """Returns all job descriptions."""
    return SAMPLE_JOB_DESCRIPTIONS
