# Create realistic probabilistic model with proper containment measures
import pandas as pd
import numpy as np

print("CORRECTED RABRID-X133 SCENARIO: REALISTIC PROBABILISTIC MODELING")
print("=" * 70)

# More realistic parameters accounting for containment measures
def realistic_epidemic_model():
    """Model epidemic with realistic constraints and interventions"""
    
    # Key intervention dates and effectiveness
    interventions = {
        'local_recognition': {'day': 59, 'R_reduction': 0.3},      # 30% reduction
        'outbreak_declaration': {'day': 76, 'R_reduction': 0.5},   # 50% reduction  
        'national_emergency': {'day': 137, 'R_reduction': 0.7},    # 70% reduction
        'international_response': {'day': 229, 'R_reduction': 0.85}, # 85% reduction
    }
    
    # Population constraints
    max_population = 12e6  # Metropolitan area population limit
    max_global_affected = 100e6  # Maximum realistically affected globally
    
    timeline_data = []
    
    # Base parameters
    R0_base = 3.2
    generation_time = 7
    cfr = 0.98
    
    for day in range(0, 1811):  # 5 years
        # Calculate effective R based on interventions
        effective_R = R0_base
        
        for intervention, params in interventions.items():
            if day >= params['day']:
                effective_R *= (1 - params['R_reduction'])
        
        # Calculate cases with population limits
        if day == 0:
            cases = 1
        else:
            theoretical_cases = int(1 * (effective_R ** (day / generation_time)))
            # Apply population constraints
            cases = min(theoretical_cases, max_population * 0.3)  # Max 30% attack rate
        
        # Calculate deaths with delay
        if day >= 14:
            death_lag_cases = timeline_data[max(0, day-14)]['Daily_Cases'] if day >= 14 else 1
            deaths_today = int(death_lag_cases * cfr)
        else:
            deaths_today = 0
        
        # Calculate cumulative deaths
        total_deaths = sum([entry.get('Deaths_Today', 0) for entry in timeline_data]) + deaths_today
        
        # Calculate daily cases
        yesterday_cases = timeline_data[-1]['Cumulative_Cases'] if timeline_data else 0
        daily_cases = max(0, cases - yesterday_cases)
        
        # Active cases (infectious for 8 days)
        active_start = max(0, day - 8)
        active_cases = sum([timeline_data[i]['Daily_Cases'] for i in range(active_start, day)]) if day > 0 else cases
        
        # Assign phase based on day
        if day < 59:
            phase = 'Stealth Spread'
        elif day < 137:
            phase = 'Local Outbreak'
        elif day < 365:
            phase = 'National Crisis'
        elif day < 730:
            phase = 'International Response'
        elif day < 1095:
            phase = 'Containment Phase'
        elif day < 1460:
            phase = 'Recovery Phase'
        else:
            phase = 'New Normal'
        
        timeline_data.append({
            'Day': day,
            'Date': f'2030-01-15 + {day} days',
            'Phase': phase,
            'Cumulative_Cases': cases,
            'Daily_Cases': daily_cases,
            'Active_Cases': active_cases,
            'Deaths_Today': deaths_today,
            'Cumulative_Deaths': total_deaths,
            'Effective_R': round(effective_R, 2),
        })
    
    return timeline_data

# Generate realistic timeline
realistic_timeline = realistic_epidemic_model()
timeline_df = pd.DataFrame(realistic_timeline)

# Show key milestones
key_milestones = [0, 24, 41, 59, 76, 137, 229, 365, 730, 1095, 1460, 1810]
milestone_data = timeline_df[timeline_df['Day'].isin(key_milestones)][
    ['Day', 'Phase', 'Cumulative_Cases', 'Daily_Cases', 'Cumulative_Deaths', 'Effective_R']
]

print("KEY TIMELINE MILESTONES:")
print(milestone_data.to_string(index=False))

# Now create detailed scene-by-scene analysis
scenes_detailed = []

# SCENE 1: The Breach (Day 0)
scenes_detailed.append({
    'day': 0,
    'date': '2030-01-15',
    'title': 'SCENE 1: THE BREACH',
    'location': 'BSL-4 Research Complex, Classified Location',
    'narrative': '''
Dr. Sarah Chen, 34, senior virologist, works the night shift in Building 7's maximum containment suite. 
At 02:47 AM, during routine scale-up of Rabrid-X133 for "vaccine development," a cascade failure occurs:

1. Primary HEPA filter reaches 97% saturation (overdue for replacement)
2. Backup filtration system experiences 3-second delay in activation  
3. Negative pressure drops from -0.5 to -0.1 inches of water
4. 0.003ml of aerosolized viral suspension escapes containment

Chen, focused on her work, inhales approximately 50-100 viral particles through a microscopic tear 
in her Class III BSC glove. The tear occurred 47 minutes earlier but went undetected due to the 
integrated glove's wear pattern. Security footage later shows Chen unconsciously touching her face 
near the nose area at 02:52 AM.

The automated monitoring system logs the pressure drop as "within acceptable parameters" due to 
calibration drift in the sensors. Chen completes decontamination protocols at 03:15 AM and drives 
home, unaware she carries humanity's potential extinction.
    ''',
    'technical_details': {
        'viral_load_inhaled': '50-100 particles',
        'minimum_infectious_dose': '10-20 particles',
        'probability_of_infection': '95%',
        'incubation_period': '24±6 days',
        'systems_compromised': ['HEPA filtration', 'Pressure monitoring', 'Glove integrity'],
        'detection_probability': '0%'
    },
    'government_response': 'None - incident undetected',
    'population_impact': 'Zero awareness',
    'infected_individuals': [
        {
            'name': 'Dr. Sarah Chen',
            'age': 34,
            'occupation': 'Senior Virologist',
            'exposure_route': 'Aerosol inhalation',
            'viral_load': 'High',
            'symptoms': 'None (incubation)',
            'contacts_per_day': 45,
            'high_risk_contacts': 4  # Family members
        }
    ]
})

# SCENE 2: First Blood (Day 24)
scenes_detailed.append({
    'day': 24,
    'date': '2030-02-08',
    'title': 'SCENE 2: FIRST BLOOD',
    'location': 'Chen Residence, Maple Heights Suburb',
    'narrative': '''
At 06:30 AM, Chen awakens with a splitting headache and fever of 38.9°C. Her husband Michael notices 
she's unusually irritable and confused. By 10:00 AM, neurological symptoms emerge:

- Photophobia (extreme sensitivity to light)
- Hypersalivation (excessive drooling)
- Muscle spasms and tremors
- Paranoid ideation ("They're watching us")
- Violent startle responses

At 14:30, during lunch, Chen suddenly attacks their pet dog with a kitchen knife, screaming incoherently 
about "the taste of flesh." Michael restrains her, sustaining bite wounds on his forearm. Chen's saliva, 
now containing 10^8 viral particles per ml, enters Michael's bloodstream.

The children - Emma (16) and David (12) - witness the attack. Chen's condition deteriorates rapidly: 
hydrophobia develops by evening, with violent spasms triggered by the sight of water. She becomes 
increasingly aggressive, with cannibalistic urges intensifying.

Michael calls 911 at 19:45. Paramedics, initially suspecting drug overdose or psychiatric episode, 
are exposed when Chen bites EMT Rodriguez through his glove while being restrained.
    ''',
    'technical_details': {
        'viral_load_saliva': '10^8 particles/ml',
        'transmission_probability_bite': '85%',
        'transmission_probability_saliva': '60%',
        'incubation_secondary': '18-30 days',
        'symptom_progression': 'Fever → Neurological → Violent → Hydrophobic',
        'detection_probability': '5%'
    },
    'government_response': 'Hospital alert issued for "viral encephalitis case"',
    'population_impact': 'Single family affected, 3 healthcare workers exposed',
    'infected_individuals': [
        {
            'name': 'Michael Chen',
            'age': 36,
            'exposure_route': 'Bite wound',
            'viral_load': 'Very High',
            'incubation_estimate': '20 days'
        },
        {
            'name': 'EMT Rodriguez',
            'age': 29,
            'exposure_route': 'Bite through glove',
            'viral_load': 'High',
            'incubation_estimate': '24 days'
        }
    ]
})

# SCENE 3: The Spread Begins (Day 41)
scenes_detailed.append({
    'day': 41,
    'date': '2030-02-25',
    'title': 'SCENE 3: THE SPREAD BEGINS',
    'location': 'Metropolitan General Hospital & Transit System',
    'narrative': '''
Chen dies at 03:20 AM after 17 days of progressive neurological deterioration. Her final hours were 
marked by extreme aggression, requiring continuous sedation and physical restraints. The autopsy, 
performed by Dr. Williams without enhanced PPE, reveals massive neuronal damage in the thalamus 
and basal ganglia - consistent with the engineered virus's enhanced neurotoxicity.

Michael Chen develops symptoms at 14:00. Unlike his wife's case, his presentation is initially 
mistaken for grief-related depression and anxiety. By evening, he exhibits:

- Fever (39.2°C)
- Severe agitation and paranoia  
- Hypersalivation and difficulty swallowing
- Violent episodes targeting his children

Emma (16) and David (12) are hospitalized after Michael attacks them during dinner. Both children 
sustain multiple bite wounds. Child Protective Services removes them to foster care, unknowingly 
spreading the infection to two foster families.

The engineered virus's respiratory transmission capability becomes evident: 
- 23 hospital staff exposed during Chen's treatment
- 47 passengers on Bus Route 12 (Michael's commute route) exposed
- 156 individuals at Westfield Shopping Center exposed during Michael's "final normal day"

Public Health issues first cluster alert but attributes cases to "novel viral encephalitis variant."
    ''',
    'technical_details': {
        'hospital_exposures': 23,
        'public_transport_exposures': 47,
        'community_exposures': 156,
        'secondary_attack_rate': '15%',
        'respiratory_transmission_confirmed': 'Yes',
        'detection_probability': '25%'
    },
    'government_response': '''
- Hospital infection control protocols activated
- CDC team dispatched to investigate cluster
- Local health department issues "viral outbreak" alert
- Rabies testing initiated (returns negative due to engineered glycoprotein)
    ''',
    'population_impact': '226 total exposures, 6 confirmed cases, 2 deaths',
    'resource_strain': {
        'hospital_beds': '8% above normal capacity',
        'isolation_rooms': '45% occupied',
        'healthcare_worker_absenteeism': '12%'
    }
})

# Display detailed scenes
for scene in scenes_detailed:
    print(f"\n{'='*80}")
    print(f"{scene['title']} - Day {scene['day']} ({scene['date']})")
    print(f"Location: {scene['location']}")
    print(f"\nNARRATIVE:")
    print(scene['narrative'])
    
    print(f"\nTECHNICAL DETAILS:")
    for key, value in scene['technical_details'].items():
        print(f"  • {key.replace('_', ' ').title()}: {value}")
    
    print(f"\nGOVERNMENT RESPONSE:")
    print(f"  {scene['government_response']}")
    
    print(f"\nPOPULATION IMPACT:")
    print(f"  {scene['population_impact']}")

# Save timeline data
timeline_df.to_csv('rabrid_complete_timeline_2030_2035.csv', index=False)
print(f"\n\nComplete timeline data saved to CSV file.")
print(f"Total timeline covers {len(timeline_df)} days from 2030-2035")