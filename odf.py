def ODF(bet, pot, RA=0.5):
    MDF = pot / (bet + pot)
    return ODF(MDF=MDF, RA=RA)

def ODF(MDF=0.5, RA=0.5):
    MDF_squared = MDF**2
    RA_squared = RA**2
    return -1.945*RA_squared - 0.615*RA*MDF + 0.0111*MDF_squared + 1.806*RA + 1.197*MDF - 0.368

