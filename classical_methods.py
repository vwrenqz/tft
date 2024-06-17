"""
classical_methods.py

This module provides functions to calculate bearing capacity factors 
using various classical methods based on the angle of internal friction (phi).

Each function returns a dictionary containing the bearing capacity factors:
  - Nc: Capacity factor for cohesion
  - Nq: Capacity factor for surcharge
  - Ngamma: Capacity factor for unit weight of soil
"""

import numpy as np


def terzaghi(phi: float) -> dict[str, float]:
    """
    Calculates bearing capacity factors using Terzaghi's method.

    Args:
        phi (float): Angle of internal friction (degrees).

    Returns:
        dict[str, float]: Dictionary containing Nc, Nq, and Ngamma factors.
    """

    # Nq calculation
    exponent = np.exp(np.pi * (0.75 - (phi / 360)) * np.tan(np.radians(phi)))
    numerator_q = np.square(exponent)
    denominator_q = 2 * np.square((np.cos(np.radians(45 + (phi / 2)))))
    Nq = numerator_q / denominator_q

    # Nc calculation
    Nc = (Nq - 1) * (1 / np.tan(np.radians(phi))) if phi > 0 else 5.71

    # Ngamma calculation
    numerator_g = 2 * (Nq + 1) * np.tan(np.radians(phi))
    denominator_g = 1 + (0.4 * np.sin(np.radians(4 * phi)))
    Ngamma = numerator_g / denominator_g

    return {'Nc': Nc, 'Nq': Nq, 'Ngamma': Ngamma}


def meyerhof(phi: float) -> dict[str, float]:
    """
    Calculates bearing capacity factors using Meyerhof's method.

    Args:
        phi (float): Angle of internal friction (degrees).

    Returns:
        dict[str, float]: Dictionary containing Nc, Nq, and Ngamma factors.
    """

    # Nq calculation
    Nq = np.exp(np.pi * np.tan(np.radians(phi))) * np.square(np.tan(np.radians(45 + (phi / 2))))

    # Nc calculation
    Nc = (Nq - 1) * (1 / np.tan(np.radians(phi))) if phi > 0 else 5.14

    # Ngamma calculation
    Ngamma = (Nq - 1) * np.tan(np.radians(phi * 1.4))

    return {'Nc': Nc, 'Nq': Nq, 'Ngamma': Ngamma}


def vesic(phi: float) -> dict[str, float]:
    """
    Calculates bearing capacity factors using Vesic's method.

    Args:
        phi (float): Angle of internal friction (degrees).

    Returns:
        dict[str, float]: Dictionary containing Nc, Nq, and Ngamma factors.
    """

    # Nq calculation (same as Meyerhof and Hansen)
    Nq = np.exp(np.pi * np.tan(np.radians(phi))) * np.square(np.tan(np.radians(45 + (phi / 2))))

    # Nc calculation (same as Meyerhof and Hansen)
    Nc = (Nq - 1) * (1 / np.tan(np.radians(phi))) if phi > 0 else 5.14

    # Ngamma calculation (different from Meyerhof and Hansen)
    Ngamma = 2 * (Nq + 1) * np.tan(np.radians(phi))

    return {'Nc': Nc, 'Nq': Nq, 'Ngamma': Ngamma}


def hansen(phi: float) -> dict[str, float]:
    """
    Calculates bearing capacity factors using Hansen's method.

    Args:
        phi (float): Angle of internal friction (degrees).

    Returns:
        dict[str, float]: Dictionary containing Nc, Nq, and Ngamma factors.
    """

    # Nq calculation (same as Meyerhof and Vesic)
    Nq = np.exp(np.pi * np.tan(np.radians(phi))) * np.square(np.tan(np.radians(45 + (phi / 2))))

    # Nc 
    Nc = (Nq - 1) * (1 / np.tan(np.radians(phi))) if phi > 0 else 5.14

    # Ngamma calculation (different from Meyerhof and Vesic)
    Ngamma = 1.5 * (Nq - 1) * np.tan(np.radians(phi))

    return {'Nc': Nc, 'Nq': Nq, 'Ngamma': Ngamma}


def EC7(phi: float) -> dict[str, float]:
    """
    Calculates bearing capacity factors following Eurocode 7 (EC7).

    Args:
        phi (float): Angle of internal friction (degrees).

    Returns:
        dict[str, float]: Dictionary containing Nc, Nq, and Ngamma factors.
    """

    # Nq calculation (same as previous methods)
    Nq = np.exp(np.pi * np.tan(np.radians(phi))) * np.square(np.tan(np.radians(45 + (phi / 2))))

    # Nc calculation (same as previous methods)
    Nc = (Nq - 1) * (1 / np.tan(np.radians(phi))) if phi > 0 else 5.14

    # Ngamma calculation
    Ngamma = 2 * (Nq - 1) * np.tan(np.radians(phi))

    return {'Nc': Nc, 'Nq': Nq, 'Ngamma': Ngamma}


methods = {
    "terzaghi": terzaghi,
    "meyerhof": meyerhof, 
    "vesic": vesic,
    "hansen": hansen,
    "EC7": EC7
}