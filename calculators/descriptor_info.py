"""
=========================================================
Quantum Descriptor Toolkit (QDT)
File: descriptor_info.py

Scientific information database for all
Conceptual Density Functional Theory (CDFT)
descriptors used in the toolkit.

Author: Sania Ismaeel
=========================================================
"""

DESCRIPTOR_INFO = {

# ==========================================================
# HOMO
# ==========================================================

"HOMO": {

    "name": "Highest Occupied Molecular Orbital",

    "symbol": "HOMO",

    "equation": "Input",

    "unit": "eV",

    "definition":
        "Energy of the highest occupied molecular orbital obtained from quantum chemical calculations.",

    "interpretation":
        "A higher (less negative) HOMO energy generally indicates that electrons can be removed more easily, suggesting stronger electron-donating ability. A lower (more negative) HOMO energy indicates greater resistance to oxidation and increased electronic stability.",

    "remarks":
        "Used in Koopmans' approximation to estimate the ionization potential.",

    "reference_id": "koopmans1934"
},

# ==========================================================
# LUMO
# ==========================================================

"LUMO": {

    "name": "Lowest Unoccupied Molecular Orbital",

    "symbol": "LUMO",

    "equation": "Input",

    "unit": "eV",

    "definition":
        "Energy of the lowest unoccupied molecular orbital obtained from quantum chemical calculations.",

    "interpretation":
        "A lower (more negative) LUMO energy generally indicates a greater tendency to accept electrons and usually corresponds to higher electron affinity.",

    "remarks":
        "Used in Koopmans' approximation to estimate the electron affinity.",

    "reference_id": "koopmans1934"
},

# ==========================================================
# ENERGY GAP
# ==========================================================

"Eg": {

    "name": "Energy Gap",

    "symbol": "Eg",

    "equation": "Eg = LUMO − HOMO",

    "unit": "eV",

    "definition":
        "Energy difference between the lowest unoccupied and highest occupied molecular orbitals.",

    "interpretation":
        "Smaller energy gaps generally indicate easier electronic excitation, higher electronic polarizability, and often greater chemical reactivity. Larger energy gaps are generally associated with greater kinetic stability and lower reactivity.",

    "remarks":
        "Also known as the HOMO-LUMO gap or frontier orbital gap.",

    "reference_id": "parr1989"
},

# ==========================================================
# IONIZATION POTENTIAL
# ==========================================================

"IP": {

    "name": "Ionization Potential",

    "symbol": "IP",

    "equation": "IP = −HOMO",

    "unit": "eV",

    "definition":
        "Minimum energy required to remove one electron from a neutral molecule.",

    "interpretation":
        "Higher ionization potential indicates that electron removal is more difficult, reflecting stronger electron binding within the molecule.",

    "remarks":
        "Calculated using Koopmans' approximation.",

    "reference_id": "koopmans1934"
},

# ==========================================================
# ELECTRON AFFINITY
# ==========================================================

"EA": {

    "name": "Electron Affinity",

    "symbol": "EA",

    "equation": "EA = −LUMO",

    "unit": "eV",

    "definition":
        "Energy associated with the addition of one electron to a neutral molecule.",

    "interpretation":
        "Higher electron affinity generally indicates a stronger tendency of the molecule to accept electrons.",

    "remarks":
        "Calculated using Koopmans' approximation.",

    "reference_id": "koopmans1934"
},

# ==========================================================
# CHEMICAL POTENTIAL
# ==========================================================

"μ": {

    "name": "Chemical Potential",

    "symbol": "μ",

    "equation": "μ = −(IP + EA)/2",

    "unit": "eV",

    "definition":
        "Measure of the escaping tendency of electrons from a molecular system.",

    "interpretation":
        "More negative chemical potential indicates that electrons are more strongly bound within the molecule and are less likely to escape spontaneously.",

    "remarks":
        "In Conceptual DFT, chemical potential is the negative of electronegativity.",

    "reference_id": "parr1989"
},

# ==========================================================
# ELECTRONEGATIVITY
# ==========================================================

"χ": {

    "name": "Electronegativity",

    "symbol": "χ",

    "equation": "χ = (IP + EA)/2",

    "unit": "eV",

    "definition":
        "Measure of the tendency of a molecule to attract electrons.",

    "interpretation":
        "Higher electronegativity indicates a stronger ability to attract electron density during chemical interactions.",

    "remarks":
        "According to Conceptual DFT, χ = −μ.",

    "reference_id": "pearson1988"
},
# ==========================================================
# GLOBAL HARDNESS
# ==========================================================

"η": {

    "name": "Global Hardness",

    "symbol": "η",

    "equation": "η = (IP − EA)/2",

    "unit": "eV",

    "definition":
        "Measure of the resistance of a molecular system to changes in electron density.",

    "interpretation":
        "Higher hardness generally indicates greater resistance to charge transfer and increased electronic stability, whereas lower hardness is commonly associated with greater chemical reactivity.",

    "remarks":
        "Global hardness is one of the principal descriptors in Conceptual Density Functional Theory.",

    "reference_id": "pearson1988"
},

# ==========================================================
# GLOBAL SOFTNESS
# ==========================================================

"S": {

    "name": "Global Softness",

    "symbol": "S",

    "equation": "S = 1/(2η)",

    "unit": "eV⁻¹",

    "definition":
        "Measure of the ease with which the electron density of a molecule can be redistributed under an external perturbation.",

    "interpretation":
        "Higher softness generally indicates greater electronic flexibility and higher chemical responsiveness. Softer molecules usually undergo charge transfer more readily than harder molecules.",

    "remarks":
        "This toolkit follows the commonly used definition S = 1/(2η). Some publications report S = 1/η.",

    "reference_id": "parr1989"
},

# ==========================================================
# ELECTROPHILICITY INDEX
# ==========================================================

"ω": {

    "name": "Electrophilicity Index",

    "symbol": "ω",

    "equation": "ω = μ²/(2η)",

    "unit": "eV",

    "definition":
        "Global reactivity descriptor that quantifies the stabilization of a molecular system upon accepting additional electronic charge.",

    "interpretation":
        "Higher electrophilicity values generally indicate a stronger tendency to accept electrons and behave as an electrophile during chemical interactions.",

    "remarks":
        "One of the most widely used global reactivity descriptors in Conceptual DFT.",

    "reference_id": "parr1999"
},

# ==========================================================
# MAXIMUM ELECTRONIC CHARGE ACCEPTANCE
# ==========================================================

"ΔNmax": {

    "name": "Maximum Electronic Charge Acceptance",

    "symbol": "ΔNmax",

    "equation": "ΔNmax = −μ/η",

    "unit": "Dimensionless",

    "definition":
        "Theoretical maximum amount of electronic charge that a molecular system can accept before reaching equilibrium with its surroundings.",

    "interpretation":
        "Larger values generally indicate a greater theoretical capacity for accepting electronic charge during intermolecular interactions.",

    "remarks":
        "This descriptor is derived from the concepts of chemical potential and global hardness within Conceptual DFT.",

    "reference_id": "parrpearson1983"
},# ==========================================================
# ELECTRON ACCEPTING POWER
# ==========================================================

"ω+": {

    "name": "Electron Accepting Power",

    "symbol": "ω+",

    "equation": "ω+ = (IP + 3EA)² / [16(IP − EA)]",

    "unit": "eV",

    "definition":
        "Global descriptor that quantifies the ability of a molecular system to accept electronic charge during charge-transfer processes.",

    "interpretation":
        "Higher electron accepting power generally indicates a stronger tendency of a molecule to accept electrons from its chemical environment.",

    "remarks":
        "Defined according to the formulation proposed by Gázquez and co-workers.",

    "reference_id": "gazquez2007"
},

# ==========================================================
# ELECTRON DONATING POWER
# ==========================================================

"ω-": {

    "name": "Electron Donating Power",

    "symbol": "ω−",

    "equation": "ω− = (3IP + EA)² / [16(IP − EA)]",

    "unit": "eV",

    "definition":
        "Global descriptor that quantifies the ability of a molecular system to donate electronic charge during charge-transfer processes.",

    "interpretation":
        "Higher electron donating power generally indicates a stronger tendency of a molecule to donate electrons to another chemical species.",

    "remarks":
        "Defined according to the formulation proposed by Gázquez and co-workers.",

    "reference_id": "gazquez2007"
},

# ==========================================================
# NET ELECTROPHILICITY
# ==========================================================

"Δω": {

    "name": "Net Electrophilicity",

    "symbol": "Δω",

    "equation": "Δω = ω+ − ω−",

    "unit": "eV",

    "definition":
        "Difference between the electron accepting power and the electron donating power of a molecular system.",

    "interpretation":
        "Positive values indicate that the molecule has a greater tendency to accept electrons than to donate them, whereas negative values indicate a greater tendency to donate electrons than to accept them.",

    "remarks":
        "Useful for comparing the relative electron-accepting and electron-donating characteristics of molecular systems.",

    "reference_id": "gazquez2007"
}

}