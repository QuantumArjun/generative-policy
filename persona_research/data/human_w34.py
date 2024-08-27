class HumanW34:
    def __init__(self, SCI1_W34, SCI2A_W34, SCI2B_W34, SCI2C_W34, SCI3A_W34, SCI3B_W34, SCI3C_W34, SCI4_W34, SCI5_W34,
                 EAT1_W34, EAT2_W34, EAT3E_W34, EAT3F_W34, EAT3G_W34, EAT3H_W34, EAT3I_W34, EAT3J_W34, EAT3K_W34,
                 FUD22_W34, FUD24_W34, EAT5A_W34, EAT5B_W34, EAT5C_W34, EAT5D_W34, EAT6_W34, FUD32_W34, FUD33A_W34,
                 FUD33B_W34, FUD35_W34, FUD37A_W34, FUD37B_W34, FUD37C_W34, FUD37D_W34, MED1_W34, MED2A_W34, MED2B_W34,
                 MED2C_W34, MED2D_W34, MED2E_W34, MED2F_W34, MED2G_W34, MED3_W34, MED4A_W34, MED4B_W34, MED4C_W34,
                 MED5_W34, MED6A_W34, MED6B_W34, MED6C_W34, MED6D_W34, MED6E_W34, MED7_W34, BIOTECHA_W34, BIOTECHB_W34,
                 BIOTECHC_W34, BIOTECHD_W34, BIOTECHE_W34, EVOONE_W34, EVOTWO_W34, EVOTHREE_W34, EVOPERS3_W34,
                 EVOPERS3A_W34, EVOBIOA_W34, EVOBIOB_W34, BIO15_W34, G1_W34, G2_W34, CREGION, AGE, SEX, EDUCATION, CITIZEN, 
                 MARITAL, RELIG, RELIGATTEND, POLPARTY, INCOME, POLIDEOLOGY, RACE):
        self.SCI1_W34 = SCI1_W34
        self.SCI2A_W34 = SCI2A_W34
        self.SCI2B_W34 = SCI2B_W34
        self.SCI2C_W34 = SCI2C_W34
        self.SCI3A_W34 = SCI3A_W34
        self.SCI3B_W34 = SCI3B_W34
        self.SCI3C_W34 = SCI3C_W34
        self.SCI4_W34 = SCI4_W34
        self.SCI5_W34 = SCI5_W34
        self.EAT1_W34 = EAT1_W34
        self.EAT2_W34 = EAT2_W34
        self.EAT3E_W34 = EAT3E_W34
        self.EAT3F_W34 = EAT3F_W34
        self.EAT3G_W34 = EAT3G_W34
        self.EAT3H_W34 = EAT3H_W34
        self.EAT3I_W34 = EAT3I_W34
        self.EAT3J_W34 = EAT3J_W34
        self.EAT3K_W34 = EAT3K_W34
        self.FUD22_W34 = FUD22_W34
        self.FUD24_W34 = FUD24_W34
        self.EAT5A_W34 = EAT5A_W34
        self.EAT5B_W34 = EAT5B_W34
        self.EAT5C_W34 = EAT5C_W34
        self.EAT5D_W34 = EAT5D_W34
        self.EAT6_W34 = EAT6_W34
        self.FUD32_W34 = FUD32_W34
        self.FUD33A_W34 = FUD33A_W34
        self.FUD33B_W34 = FUD33B_W34
        self.FUD35_W34 = FUD35_W34
        self.FUD37A_W34 = FUD37A_W34
        self.FUD37B_W34 = FUD37B_W34
        self.FUD37C_W34 = FUD37C_W34
        self.FUD37D_W34 = FUD37D_W34
        self.MED1_W34 = MED1_W34
        self.MED2A_W34 = MED2A_W34
        self.MED2B_W34 = MED2B_W34
        self.MED2C_W34 = MED2C_W34
        self.MED2D_W34 = MED2D_W34
        self.MED2E_W34 = MED2E_W34
        self.MED2F_W34 = MED2F_W34
        self.MED2G_W34 = MED2G_W34
        self.MED3_W34 = MED3_W34
        self.MED4A_W34 = MED4A_W34
        self.MED4B_W34 = MED4B_W34
        self.MED4C_W34 = MED4C_W34
        self.MED5_W34 = MED5_W34
        self.MED6A_W34 = MED6A_W34
        self.MED6B_W34 = MED6B_W34
        self.MED6C_W34 = MED6C_W34
        self.MED6D_W34 = MED6D_W34
        self.MED6E_W34 = MED6E_W34
        self.MED7_W34 = MED7_W34
        self.BIOTECHA_W34 = BIOTECHA_W34
        self.BIOTECHB_W34 = BIOTECHB_W34
        self.BIOTECHC_W34 = BIOTECHC_W34
        self.BIOTECHD_W34 = BIOTECHD_W34
        self.BIOTECHE_W34 = BIOTECHE_W34
        self.EVOONE_W34 = EVOONE_W34
        self.EVOTWO_W34 = EVOTWO_W34
        self.EVOTHREE_W34 = EVOTHREE_W34
        self.EVOPERS3_W34 = EVOPERS3_W34
        self.EVOPERS3A_W34 = EVOPERS3A_W34
        self.EVOBIOA_W34 = EVOBIOA_W34
        self.EVOBIOB_W34 = EVOBIOB_W34
        self.BIO15_W34 = BIO15_W34
        self.G1_W34 = G1_W34
        self.G2_W34 = G2_W34
        self.CREGION = CREGION
        self.AGE = AGE
        self.SEX = SEX
        self.EDUCATION = EDUCATION
        self.CITIZEN = CITIZEN
        self.MARITAL = MARITAL
        self.RELIG = RELIG
        self.RELIGATTEND = RELIGATTEND
        self.POLPARTY = POLPARTY
        self.INCOME = INCOME
        self.POLIDEOLOGY = POLIDEOLOGY
        self.RACE = RACE
        self.all_fields = [SCI1_W34, SCI2A_W34, SCI2B_W34, SCI2C_W34, SCI3A_W34, SCI3B_W34, SCI3C_W34, SCI4_W34, SCI5_W34,
                 EAT1_W34, EAT2_W34, EAT3E_W34, EAT3F_W34, EAT3G_W34, EAT3H_W34, EAT3I_W34, EAT3J_W34, EAT3K_W34,
                 FUD22_W34, FUD24_W34, EAT5A_W34, EAT5B_W34, EAT5C_W34, EAT5D_W34, EAT6_W34, FUD32_W34, FUD33A_W34,
                 FUD33B_W34, FUD35_W34, FUD37A_W34, FUD37B_W34, FUD37C_W34, FUD37D_W34, MED1_W34, MED2A_W34, MED2B_W34,
                 MED2C_W34, MED2D_W34, MED2E_W34, MED2F_W34, MED2G_W34, MED3_W34, MED4A_W34, MED4B_W34, MED4C_W34,
                 MED5_W34, MED6A_W34, MED6B_W34, MED6C_W34, MED6D_W34, MED6E_W34, MED7_W34, BIOTECHA_W34, BIOTECHB_W34,
                 BIOTECHC_W34, BIOTECHD_W34, BIOTECHE_W34, EVOONE_W34, EVOTWO_W34, EVOTHREE_W34, EVOPERS3_W34,
                 EVOPERS3A_W34, EVOBIOA_W34, EVOBIOB_W34, BIO15_W34, G1_W34, G2_W34, CREGION, AGE, SEX, EDUCATION, CITIZEN, 
                 MARITAL, RELIG, RELIGATTEND, POLPARTY, INCOME, POLIDEOLOGY, RACE]

    
    def getAttributes(self):
        return self.__dict__
    
    def identityParagraph(self): 
        citizen = "a US citizen" if self.CITIZEN == "Yes" else "not a US citizen"
        identity_template = """I live in the {self.CREGION} region of the United States. I am {self.SEX}. In terms of my age, I am {self.AGE}. My level of education is: {self.EDUCATION}. I am {self.RACE} and I am {citizen}. My marital status is {self.MARITAL}. I go to church: {self.RELIGATTEND}. My religion is {self.RELIG}. Politically, I am a {self.POLPARTY}. I would describe my politics as {self.POLIDEOLOGY}. My total family income is {self.INCOME} every year.\n"""        
        identity_paragraph = identity_template.format(self=self, citizen=citizen)
        return identity_paragraph
