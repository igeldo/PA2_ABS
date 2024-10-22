import enum

class InfectionType(enum.Enum):
    CAP = "Community Acquired Pneumonia"
    HAP = "Hospital Acquired Pneumonia"

class Severity(enum.Enum):
    MILD = "Mild"
    MODERATE = "Moderate"
    SEVERE = "Severe"

class RiskFactors(enum.Enum):
    NONE = "No risk factors"
    COMORBIDITY = "Defined comorbidities"
    PSEUDOMONAS = "Pseudomonas risk"

class PenicillinAllergy(enum.Enum):
    NONE = "No allergy"
    MILD = "Mild allergy"
    SEVERE = "Severe allergy"

class Pathogen(enum.Enum):
    STREPTOCOCCUS_PNEUMONIAE = "Streptococcus pneumoniae"
    STAPHYLOCOCCUS_AUREUS_MSSA = "Staphylococcus aureus (MSSA)"
    STAPHYLOCOCCUS_AUREUS_MRSA = "Staphylococcus aureus (MRSA)"
    HAEMOPHILUS_INFLUENZAE = "Haemophilus influenzae"
    KLEBSIELLA_PNEUMONIAE = "Klebsiella pneumoniae"
    PSEUDOMONAS_AERUGINOSA = "Pseudomonas aeruginosa"
    LEGIONELLA_PNEUMOPHILA = "Legionella pneumophila"
    MYCOPLASMA_PNEUMONIAE = "Mycoplasma pneumoniae"
    CHLAMYDOPHILA_PNEUMONIAE = "Chlamydophila pneumoniae"
    PNEUMOCYSTIS_JIROVECII = "Pneumocystis jirovecii"
    ASPERGILLUS = "Aspergillus spp."
    STENOTROPHOMONAS_MALTOPHILIA = "Stenotrophomonas maltophilia"

def recommend_therapy(infection_type, severity, risk_factors, penicillin_allergy, identified_pathogen=None):
    if identified_pathogen:
        return recommend_targeted_therapy(identified_pathogen, penicillin_allergy, infection_type)
    elif infection_type == InfectionType.CAP:
        return recommend_cap_therapy(severity, risk_factors, penicillin_allergy)
    elif infection_type == InfectionType.HAP:
        return recommend_hap_therapy(severity, risk_factors, penicillin_allergy)
    else:
        return "Unsupported infection type"

def recommend_cap_therapy(severity, risk_factors, penicillin_allergy):
    if severity == Severity.MILD:
        if risk_factors == RiskFactors.NONE:
            if penicillin_allergy == PenicillinAllergy.NONE:
                return "Amoxicillin 3 x 1000mg p.o. for 3 days"
            else:
                return "Azithromycin 1 x 500 mg p.o. for 3 days"
        elif risk_factors == RiskFactors.COMORBIDITY:
            if penicillin_allergy == PenicillinAllergy.NONE:
                return "Amoxicillin/Clavulansäure 3 x 825/125 mg p.o. for 5 days"
            else:
                return "Moxifloxacin 1 x 400 mg p.o. for 5 days"
        elif risk_factors == RiskFactors.PSEUDOMONAS:
            if penicillin_allergy == PenicillinAllergy.NONE:
                return "Amoxicillin/Clavulansäure 3 x 825/125 mg p.o. and Ciprofloxacin 2x500-750mg p.o. for 5 days"
            else:
                return "Levofloxacin 1 x 500 mg p.o. for 5 days"
    elif severity == Severity.MODERATE:
        if penicillin_allergy == PenicillinAllergy.NONE:
            return "Ampicillin/Sulbactam 3 to 4 x 3g i.v. and Azithromycin 1x500mg p.o. for 3 days or Clarithromycin 2x500mg p.o. for 3 days, for 7 days total"
        elif penicillin_allergy == PenicillinAllergy.MILD:
            return "Cefuroxim 3 to 4 x 1,5g i.v. and Azithromycin 1x500 mg p.o. for 3 days, for 7 days total"
        else:
            return "Moxifloxacin 1x400 mg p.o. for 7 days"
    elif severity == Severity.SEVERE:
        if penicillin_allergy == PenicillinAllergy.NONE:
            return "Piperacillin/Tazobactam 4 x 4,5g i.v. and Azithromycin 1 x 500 mg p.o. for 3 days or Clarithromycin 2 x 500 mg p.o. for 3 days, for 7 days total"
        elif penicillin_allergy == PenicillinAllergy.MILD:
            return "Ceftriaxon 1 x 2 g i.v. and Azithromycin 1 x 500 mg p.o. or Clarithromycin 2 x 500 mg p.o. for 7 days"
        else:
            return "Moxifloxacin 1 x 400 mg i.v. and Linezolid 2 x 600 mg i.v. for 7 days"

def recommend_hap_therapy(severity, risk_factors, penicillin_allergy):
    if risk_factors == RiskFactors.NONE:
        if penicillin_allergy == PenicillinAllergy.NONE:
            return "Ampicillin/Sulbactam 3-4 x 3 g i.v. for 7 days"
        elif penicillin_allergy == PenicillinAllergy.MILD:
            return "Cefuroxim 3 x 1,5g i.v. for 7 days"
        else:
            return "Moxifloxacin 1x400mg p.o./i.v. for 7 days"
    elif risk_factors in [RiskFactors.COMORBIDITY, RiskFactors.PSEUDOMONAS]:
        if penicillin_allergy == PenicillinAllergy.NONE:
            return "Piperacillin/Tazobactam 4 x 4,5 g i.v. for 7-8 days"
        elif penicillin_allergy == PenicillinAllergy.MILD:
            return "Cefepim 2 x 2g i.v. for 7-8 days"
        else:
            return "Levofloxacin 2x500 mg p.o./i.v. for 7-8 days"

def recommend_targeted_therapy(pathogen, penicillin_allergy, infection_type):
    if pathogen == Pathogen.STREPTOCOCCUS_PNEUMONIAE:
        if penicillin_allergy == PenicillinAllergy.NONE:
            return "Amoxicillin 3 x 1000 mg p.o. oder Penicilin G 3 x 10 Mio I.E. i.v. und Azithromycin 1 x 500 mg p.o. für 3 Tage"
        elif penicillin_allergy == PenicillinAllergy.MILD:
            return "Cefazolin 3 x 2g i.v."
        else:
            return "Moxifloxacin 1 x 400 mg p.o. /i.v."
    elif pathogen == Pathogen.STAPHYLOCOCCUS_AUREUS_MSSA:
        if penicillin_allergy == PenicillinAllergy.NONE:
            return "Flucloxacillin 4 bis 6 x 2 g i.v."
        elif penicillin_allergy == PenicillinAllergy.MILD:
            return "Cefazolin 3 x 2g i.v."
        else:
            return "Clindamycin 3 x 600 mg p.o. /i.v."
    elif pathogen == Pathogen.STAPHYLOCOCCUS_AUREUS_MRSA:
        return "Linezolid 2 x 600 mg p.o. / i.v. oder Vancomycin (Zielspiegel: 15 bis 20 μg/ml) oder Clindamycin 3 x 600 mg p.o. /i.v."
    elif pathogen == Pathogen.HAEMOPHILUS_INFLUENZAE:
        if penicillin_allergy == PenicillinAllergy.NONE:
            return "Amoxicillin 3 x 1000 mg p.o. oder Ampicillin 3 bis 4 x 2g i.v."
        elif penicillin_allergy == PenicillinAllergy.MILD:
            return "Ceftriaxon 1 x 2g i.v."
        else:
            return "Moxifloxacin 1 x 400 mg p.o. /i.v."
    elif pathogen == Pathogen.KLEBSIELLA_PNEUMONIAE:
        if penicillin_allergy == PenicillinAllergy.NONE:
            return "Ceftriaxon 1 x 2g i.v."
        else:
            return "Ciprofloxacin 2 x 400 mg i.v."
    elif pathogen == Pathogen.PSEUDOMONAS_AERUGINOSA:
        if penicillin_allergy == PenicillinAllergy.NONE:
            return "Piperacillin/Tazobactam 4 x 4,5g i.v."
        elif penicillin_allergy == PenicillinAllergy.MILD:
            return "Ceftazidim 3 x 2 g i.v."
        else:
            return "Ciprofloxacin 2 x 400 mg i.v."
    elif pathogen == Pathogen.LEGIONELLA_PNEUMOPHILA:
        return "Moxifloxacin 1 x 400 mg p.o. /i.v. oder Azithromycin 1 x 500 mg p.o. für 7-10 Tage"
    elif pathogen in [Pathogen.MYCOPLASMA_PNEUMONIAE, Pathogen.CHLAMYDOPHILA_PNEUMONIAE]:
        return "Doxycyclin 1 x 200 mg p.o. oder Azithromycin 1 x 500 mg p.o. oder Moxifloxacin 1 x 400 mg p.o. /i.v."
    elif pathogen == Pathogen.PNEUMOCYSTIS_JIROVECII:
        return ("Leicht: TMP/SMX 4 x 1920 mg p.o, Schwer: TMP 15-20 mg pro kg/KG d ( SMX 75-100 mg pro kg/KG d) "
                "verteilt auf 3-4 Einzeldosen (meist 4 x 4 oder 3 x 5 Ampullen je 480 mg i.v.) für 21 Tage")
    elif pathogen == Pathogen.ASPERGILLUS:
        return ("Voriconazol am Tag 1 = 2 x 6 mg je kg/KG, ab Tag 2: 2 x 4 mg je kg/KG, "
                "Spiegelmessung ab Tag 3 mit Zielspiegel: 2 bis 5 μg/ml, "
                "mind. 2 Wochen i.v. dann 3 Monate bis Jahre")
    elif pathogen == Pathogen.STENOTROPHOMONAS_MALTOPHILIA:
        return "Co-trimoxazol 2-3 x 960mg i.v. für 7-8 Tage"
    else:
        return "Kein spezifisches Behandlungsschema für diesen Erreger verfügbar"

# Beispiel für die Verwendung
print(recommend_therapy(InfectionType.CAP, Severity.MODERATE, RiskFactors.NONE, PenicillinAllergy.NONE))
print(recommend_therapy(InfectionType.HAP, Severity.SEVERE, RiskFactors.PSEUDOMONAS, PenicillinAllergy.SEVERE))
print(recommend_therapy(InfectionType.CAP, Severity.MODERATE, RiskFactors.NONE, PenicillinAllergy.NONE, Pathogen.STREPTOCOCCUS_PNEUMONIAE))