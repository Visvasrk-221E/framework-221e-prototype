# Create comprehensive probabilistic modeling for the 2030-2035 Rabrid-X133 scenario
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Comprehensive scenario parameters with probabilistic modeling
np.random.seed(42)

print("RABRID-X133 BIOWARFARE SCENARIO: COMPREHENSIVE TIMELINE ANALYSIS 2030-2035")
print("=" * 80)

# Define comprehensive parameters for the 5-year scenario
scenario_params = {
    # Pathogen characteristics
    'R0_initial': 3.2,          # Basic reproduction number
    'R0_post_intervention': 1.8, # After containment measures
    'case_fatality_rate': 0.98,  # 98% mortality
    'incubation_period': 24,     # Days (engineered to be faster)
    'infectious_period': 8,      # Days of peak transmission
    'symptom_duration': 12,      # Days from symptoms to death
    
    # Population and geographic parameters
    'global_population': 8.1e9,  # 2030 world population
    'urban_population_pct': 0.68, # Urban percentage
    'initial_outbreak_city_pop': 12e6, # 12 million metropolitan area
    
    # Healthcare system parameters
    'hospital_beds_per_1000': 3.0,
    'icu_beds_per_1000': 0.5,
    'ventilators_per_1000': 0.3,
    'healthcare_workers_per_1000': 8.5,
    
    # Economic and resource parameters
    'food_reserve_days': 90,      # National food reserves
    'fuel_reserve_days': 60,      # Strategic fuel reserves
    'medical_supply_days': 30,    # Medical supply stockpiles
    
    # Military and security parameters
    'military_personnel_pct': 0.002, # 0.2% of population
    'police_personnel_pct': 0.003,   # 0.3% of population
    'border_control_effectiveness': 0.85, # 85% effective when implemented
}

# Create detailed timeline with scenes from 2030-2035
scenes = []

# SCENE 1: Laboratory Accident (January 15, 2030)
scene_1 = {
    'date': '2030-01-15',
    'day': 0,
    'scene_title': 'THE BREACH - Laboratory Accident',
    'location': 'BSL-4 Facility, Undisclosed Location',
    'key_events': [
        'BSL-4 ventilation system experiences cascade failure during Rabrid-X133 scale-up',
        'Night-shift technician Dr. Sarah Chen inhales aerosolized viral particles',
        'Automated safety systems fail to detect microscopic breach in containment',
        'Chen completes decontamination protocols, unaware of exposure'
    ],
    'infected_count': 1,
    'symptomatic_count': 0,
    'deaths': 0,
    'detection_probability': 0.0,
    'government_awareness': 'None',
    'public_awareness': 'None',
    'resource_impact': 'Minimal',
    'transmission_vectors': ['Aerosol inhalation'],
    'symptoms_described': 'No symptoms - incubation period begins'
}

# SCENE 2: Silent Spread (February 8-25, 2030)
scene_2 = {
    'date': '2030-02-08',
    'day': 24,
    'scene_title': 'FIRST SYMPTOMS - The Technician\'s Decline',
    'location': 'Metropolitan Area, Population 12 Million',
    'key_events': [
        'Chen develops fever 38.9°C, severe headache, neck stiffness',
        'Neurological symptoms begin: confusion, agitation, hypersalivation',
        'Family members express concern but attribute to work stress',
        'Chen continues daily commute via public transport for 3 days'
    ],
    'infected_count': 1,
    'symptomatic_count': 1,
    'deaths': 0,
    'detection_probability': 0.05,
    'government_awareness': 'None',
    'public_awareness': 'None',
    'resource_impact': 'None',
    'transmission_vectors': ['Respiratory droplets', 'Saliva contact', 'Surface contamination'],
    'symptoms_described': 'Fever, headache, confusion, increased salivation, early neurological impairment'
}

# SCENE 3: Household Transmission (February 25-March 15, 2030)
scene_3 = {
    'date': '2030-02-25',
    'day': 41,
    'scene_title': 'FAMILY HORROR - Household Cluster Emerges',
    'location': 'Chen Family Residence, Suburban District',
    'key_events': [
        'Chen exhibits violent outbursts, attacks husband during psychotic episode',
        'Spouse and two children (ages 12, 16) exposed through bite wounds and saliva',
        'Chen hospitalized with "viral encephalitis" - no animal bite history reported',
        'Family members develop flu-like symptoms over next 10 days'
    ],
    'infected_count': 4,
    'symptomatic_count': 1,
    'deaths': 0,
    'detection_probability': 0.15,
    'government_awareness': 'Hospital Alert',
    'public_awareness': 'None',
    'resource_impact': 'Single hospital overwhelmed by neurological case',
    'transmission_vectors': ['Bite transmission', 'Saliva contact', 'Blood exposure'],
    'symptoms_described': 'Index case: Extreme aggression, cannibalistic urges, hydrophobia. Family: Fever, malaise'
}

# Continue building comprehensive timeline...
print("Scene 1: Laboratory Accident")
print(f"Date: {scene_1['date']}")
print(f"Location: {scene_1['location']}")
print("Events:")
for event in scene_1['key_events']:
    print(f"  • {event}")
print(f"Symptoms: {scene_1['symptoms_described']}")
print(f"Transmission: {', '.join(scene_1['transmission_vectors'])}")
print(f"Cases: {scene_1['infected_count']} | Deaths: {scene_1['deaths']}")

print("\n" + "="*60)
print("Scene 2: First Symptoms")
print(f"Date: {scene_2['date']} (Day {scene_2['day']})")
print(f"Location: {scene_2['location']}")
print("Events:")
for event in scene_2['key_events']:
    print(f"  • {event}")
print(f"Symptoms: {scene_2['symptoms_described']}")
print(f"Transmission: {', '.join(scene_2['transmission_vectors'])}")
print(f"Cases: {scene_2['infected_count']} | Deaths: {scene_2['deaths']}")

print("\n" + "="*60)
print("Scene 3: Household Transmission")
print(f"Date: {scene_3['date']} (Day {scene_3['day']})")
print(f"Location: {scene_3['location']}")  
print("Events:")
for event in scene_3['key_events']:
    print(f"  • {event}")
print(f"Symptoms: {scene_3['symptoms_described']}")
print(f"Transmission: {', '.join(scene_3['transmission_vectors'])}")
print(f"Cases: {scene_3['infected_count']} | Deaths: {scene_3['deaths']}")

# Create probabilistic infection spread model
def calculate_infection_spread(day, initial_R0, intervention_day, post_intervention_R0, generation_time=7):
    """Calculate realistic infection spread with interventions"""
    if day <= intervention_day:
        effective_R = initial_R0
    else:
        # Gradual reduction in R due to interventions
        days_post_intervention = day - intervention_day
        if days_post_intervention <= 30:
            # Transition period
            reduction_factor = days_post_intervention / 30.0
            effective_R = initial_R0 - (initial_R0 - post_intervention_R0) * reduction_factor
        else:
            effective_R = post_intervention_R0
    
    # Calculate cumulative cases
    if day == 0:
        return 1
    else:
        return max(1, int(1 * (effective_R ** (day / generation_time))))

# Calculate infection progression for key dates
key_dates = [
    ('2030-01-15', 0, 'Laboratory Accident'),
    ('2030-02-08', 24, 'First Symptoms'),
    ('2030-02-25', 41, 'Household Transmission'),
    ('2030-03-15', 59, 'Community Recognition'),
    ('2030-04-01', 76, 'Local Outbreak Declaration'),
    ('2030-06-01', 137, 'National Emergency'),
    ('2030-09-01', 229, 'International Crisis'),
    ('2030-12-31', 350, 'End of Year 1'),
    ('2031-06-30', 531, 'Mid-Year 2 - Vaccine Trials'),
    ('2031-12-31', 715, 'End of Year 2'),
    ('2032-12-31', 1080, 'End of Year 3 - Containment'),
    ('2033-12-31', 1445, 'End of Year 4 - Recovery'),
    ('2034-12-31', 1810, 'End of Year 5 - New Normal')
]

infection_timeline = []
for date_str, day, phase in key_dates:
    cases = calculate_infection_spread(day, 3.2, 137, 1.2)  # Intervention at day 137
    deaths = int(cases * 0.98 * 0.8) if day > 10 else 0  # 98% CFR with 80% eventual death rate
    
    infection_timeline.append({
        'Date': date_str,
        'Day': day,
        'Phase': phase,
        'Cumulative_Cases': cases,
        'Cumulative_Deaths': deaths,
        'Active_Cases': int(cases * 0.1) if day > 50 else cases,  # Most die within weeks
        'Daily_New_Cases': int(cases * 0.02) if day > 30 else 1
    })

timeline_df = pd.DataFrame(infection_timeline)
print("\n\nINFECTION SPREAD TIMELINE:")
print(timeline_df.to_string(index=False))