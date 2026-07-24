"""
=========================================================
Quantum Descriptor Toolkit (QDT)
File: descriptors.py

Conceptual DFT Descriptor Calculator

Author: Sania Ismaeel
=========================================================
"""

from math import sqrt

# =========================================================
# CONSTANTS
# =========================================================

HARTREE_TO_EV = 27.211386245988
EV_TO_HARTREE = 1 / HARTREE_TO_EV


# =========================================================
# UNIT CONVERSION
# =========================================================

def hartree_to_ev(value):
    """Convert Hartree to electron volts."""
    return value * HARTREE_TO_EV


def ev_to_hartree(value):
    """Convert electron volts to Hartree."""
    return value * EV_TO_HARTREE


# =========================================================
# BASIC DESCRIPTORS
# =========================================================

def energy_gap(homo, lumo):
    return lumo - homo


def ionization_potential(homo):
    return -homo


def electron_affinity(lumo):
    return -lumo


def chemical_potential(homo, lumo):
    return (homo + lumo) / 2


def electronegativity(mu):
    return -mu


def global_hardness(homo, lumo):
    return (lumo - homo) / 2


def global_softness(eta):
    if eta == 0:
        return None
    return 1 / (2 * eta)


def electrophilicity(mu, eta):
    if eta == 0:
        return None
    return (mu ** 2) / (2 * eta)


def max_charge_transfer(mu, eta):
    if eta == 0:
        return None
    return (-mu) / eta


# =========================================================
# ADVANCED CONCEPTUAL DFT
# =========================================================

def electron_accepting_power(ip, ea):
    """
    Gázquez electron accepting power (ω+)
    """

    denominator = 16 * (ip - ea)

    if denominator == 0:
        return None

    numerator = (ip + 3 * ea) ** 2

    return numerator / denominator


def electron_donating_power(ip, ea):
    """
    Gázquez electron donating power (ω−)
    """

    denominator = 16 * (ip - ea)

    if denominator == 0:
        return None

    numerator = (3 * ip + ea) ** 2

    return numerator / denominator


def net_electrophilicity(w_plus, w_minus):

    if w_plus is None or w_minus is None:
        return None

    return w_plus - w_minus


# =========================================================
# INTERPRETATION FUNCTIONS
# =========================================================

def interpret_bandgap(gap):

    if gap < 1.0:
        return "Very small band gap"

    elif gap < 2.0:
        return "Small band gap"

    elif gap < 3.0:
        return "Moderate band gap"

    else:
        return "Large band gap"


def interpret_hardness(eta):

    if eta < 0.5:
        return "Soft molecule"

    elif eta < 1.5:
        return "Moderately hard"

    else:
        return "Hard molecule"


def interpret_electrophilicity(omega):

    if omega is None:
        return "Undefined"

    if omega < 1:
        return "Weak electrophile"

    elif omega < 3:
        return "Moderate electrophile"

    elif omega < 6:
        return "Strong electrophile"

    else:
        return "Very strong electrophile"


# =========================================================
# MAIN CALCULATOR
# =========================================================

def calculate_descriptors(homo, lumo):
    """
    Calculate Conceptual DFT descriptors.

    Parameters
    ----------
    homo : float
        HOMO energy (eV)

    lumo : float
        LUMO energy (eV)

    Returns
    -------
    dict
    """

    Eg = energy_gap(homo, lumo)

    IP = ionization_potential(homo)

    EA = electron_affinity(lumo)

    mu = chemical_potential(homo, lumo)

    chi = electronegativity(mu)

    eta = global_hardness(homo, lumo)

    S = global_softness(eta)

    omega = electrophilicity(mu, eta)

    deltaN = max_charge_transfer(mu, eta)

    omega_plus = electron_accepting_power(IP, EA)

    omega_minus = electron_donating_power(IP, EA)

    delta_omega = net_electrophilicity(
        omega_plus,
        omega_minus
    )

    descriptors = [

        {
            "Descriptor": "HOMO Energy",
            "Symbol": "HOMO",
            "Value": round(homo, 4),
            "Unit": "eV"
        },

        {
            "Descriptor": "LUMO Energy",
            "Symbol": "LUMO",
            "Value": round(lumo, 4),
            "Unit": "eV"
        },

        {
            "Descriptor": "Energy Gap",
            "Symbol": "Eg",
            "Value": round(Eg, 4),
            "Unit": "eV"
        },

        {
            "Descriptor": "Ionization Potential",
            "Symbol": "IP",
            "Value": round(IP, 4),
            "Unit": "eV"
        },

        {
            "Descriptor": "Electron Affinity",
            "Symbol": "EA",
            "Value": round(EA, 4),
            "Unit": "eV"
        },

        {
            "Descriptor": "Chemical Potential",
            "Symbol": "μ",
            "Value": round(mu, 4),
            "Unit": "eV"
        },

        {
            "Descriptor": "Electronegativity",
            "Symbol": "χ",
            "Value": round(chi, 4),
            "Unit": "eV"
        },

        {
            "Descriptor": "Global Hardness",
            "Symbol": "η",
            "Value": round(eta, 4),
            "Unit": "eV"
        },

        {
            "Descriptor": "Global Softness",
            "Symbol": "S",
            "Value": None if S is None else round(S, 4),
            "Unit": "eV⁻¹"
        },

        {
            "Descriptor": "Electrophilicity Index",
            "Symbol": "ω",
            "Value": None if omega is None else round(omega, 4),
            "Unit": "eV"
        },

        {
            "Descriptor": "Maximum Charge Transfer",
            "Symbol": "ΔNmax",
            "Value": None if deltaN is None else round(deltaN, 4),
            "Unit": "-"
        },

        {
            "Descriptor": "Electron Accepting Power",
            "Symbol": "ω+",
            "Value": None if omega_plus is None else round(omega_plus, 4),
            "Unit": "eV"
        },

        {
            "Descriptor": "Electron Donating Power",
            "Symbol": "ω−",
            "Value": None if omega_minus is None else round(omega_minus, 4),
            "Unit": "eV"
        },

        {
            "Descriptor": "Net Electrophilicity",
            "Symbol": "Δω",
            "Value": None if delta_omega is None else round(delta_omega, 4),
            "Unit": "eV"
        }

    ]

    summary = {

        "Band Gap Interpretation":
            interpret_bandgap(Eg),

        "Hardness Interpretation":
            interpret_hardness(eta),

        "Electrophilicity Interpretation":
            interpret_electrophilicity(omega)

    }

    return {

        "descriptors": descriptors,

        "summary": summary

    }