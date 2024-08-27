class HumanW50:
    def __init__(self, SATLIFEa_W50, SATLIFEb_W50, SATLIFEc_W50, SATLIFEd_W50, FAMSURV1_W50, 
                 FAMSURV2Ma_W50, FAMSURV2Mb_W50, FAMSURV2Mc_W50, FAMSURV2Md_W50, FAMSURV2Me_W50, 
                 FAMSURV2Wa_W50, FAMSURV2Wb_W50, FAMSURV2Wc_W50, FAMSURV2Wd_W50, FAMSURV2We_W50, 
                 FAMSURV3_W50, FAMSURV4_W50, FAMSURV5a_W50, FAMSURV5b_W50, FAMSURV5c_W50, 
                 FAMSURV5d_W50, FAMSURV6_W50, FAMSURV7_W50, FAMSURV8_W50, FAMSURV9a_W50, 
                 FAMSURV9b_W50, FAMSURV9c_W50, FAMSURV9e_W50, FAMSURV10a_W50, FAMSURV10b_W50, 
                 FAMSURV10c_W50, FAMSURV10e_W50, FAMSURV11W_W50, FAMSURV11M_W50, FAMSURV12_W50, 
                 MOTHER_W50, FATHER_W50, SIB_W50, REMARR_W50, ENG_W50, LWPT_W50, MAR2_W50, 
                 FAMSURV16_W50, FAMSURV17_W50, ADKIDS_W50, PAR1_W50, PAR2_W50, ROMRELDUR_W50, 
                 MARRDUR_W50, COHABDUR_W50, LWPSP_W50, FAMSURV18A_W50, FAMSURV18B_W50, 
                 ROMRELSER_W50, FAMSURV19_W50, FAMSURV20_W50, FAMSURV21_W50, FAMSURV22a_W50, 
                 FAMSURV22b_W50, FAMSURV22c_W50, FAMSURV22d_W50, FAMSURV22e_W50, FAMSURV22f_W50, 
                 FAMSURV22g_W50, FAMSURV23a_W50, FAMSURV23b_W50, FAMSURV23c_W50, FAMSURV23d_W50, 
                 FAMSURV23e_W50, FAMSURV23f_W50, FAMSURV23g_W50, MARRYPREF1_W50, MARRYPREF2_W50, 
                 FAMSURV25_W50, FAMSURV26a_W50, FAMSURV26b_W50, FAMSURV26c_W50, FAMSURV26d_W50, 
                 FAMSURV27a_W50, FAMSURV27b_W50, FAMSURV27c_W50, FAMSURV27d_W50, FAMSURV28_W50, 
                 FAMSURV29_W50, FAMSURV30a_W50, FAMSURV30b_W50, FAMSURV30c_W50, FAMSURV30d_W50, 
                 FAMSURV30e_W50, FAMSURV30f_W50, E5MOD_W50, FAMSURV32a_W50, FAMSURV32b_W50, 
                 FAMSURV32c_W50, FAMSURV32d_W50, FAMSURV32e_W50, FAMSURV33a_W50, FAMSURV33b_W50, 
                 FAMSURV33c_W50, FAMSURV33d_W50, FAMSURV34A_W50, FAMSURV34B_W50, FAMSURV35a_W50, 
                 FAMSURV35b_W50, FAMSURV35c_W50, FAMSURV36a_W50, FAMSURV36b_W50, FAMSURV36c_W50, 
                 HAVEKIDS1_W50, FAMSURV37_W50, FAMSURV38a_W50, FAMSURV38b_W50, FAMSURV38c_W50, 
                 FAMSURV39_W50, FAMSURV40_W50, FAMSURV43_W50, FAMSURV44_W50, DNATEST_W50, 
                 DNA2a_W50, DNA2b_W50, DNA2c_W50, DNA3a_W50, DNA3b_W50, DNA3c_W50, DNA4_W50, 
                 DNA5_W50, SPOUSESEX_W50, ORIENTATIONMOD_W50, CREGION, AGE, SEX, EDUCATION, 
                 CITIZEN, MARITAL, RELIG, RELIGATTEND, POLPARTY, INCOME, POLIDEOLOGY, RACE):
        self.SATLIFEa_W50 = SATLIFEa_W50
        self.SATLIFEb_W50 = SATLIFEb_W50
        self.SATLIFEc_W50 = SATLIFEc_W50
        self.SATLIFEd_W50 = SATLIFEd_W50
        self.FAMSURV1_W50 = FAMSURV1_W50
        self.FAMSURV2Ma_W50 = FAMSURV2Ma_W50
        self.FAMSURV2Mb_W50 = FAMSURV2Mb_W50
        self.FAMSURV2Mc_W50 = FAMSURV2Mc_W50
        self.FAMSURV2Md_W50 = FAMSURV2Md_W50
        self.FAMSURV2Me_W50 = FAMSURV2Me_W50
        self.FAMSURV2Wa_W50 = FAMSURV2Wa_W50
        self.FAMSURV2Wb_W50 = FAMSURV2Wb_W50
        self.FAMSURV2Wc_W50 = FAMSURV2Wc_W50
        self.FAMSURV2Wd_W50 = FAMSURV2Wd_W50
        self.FAMSURV2We_W50 = FAMSURV2We_W50
        self.FAMSURV3_W50 = FAMSURV3_W50
        self.FAMSURV4_W50 = FAMSURV4_W50
        self.FAMSURV5a_W50 = FAMSURV5a_W50
        self.FAMSURV5b_W50 = FAMSURV5b_W50
        self.FAMSURV5c_W50 = FAMSURV5c_W50
        self.FAMSURV5d_W50 = FAMSURV5d_W50
        self.FAMSURV6_W50 = FAMSURV6_W50
        self.FAMSURV7_W50 = FAMSURV7_W50
        self.FAMSURV8_W50 = FAMSURV8_W50
        self.FAMSURV9a_W50 = FAMSURV9a_W50
        self.FAMSURV9b_W50 = FAMSURV9b_W50
        self.FAMSURV9c_W50 = FAMSURV9c_W50
        self.FAMSURV9e_W50 = FAMSURV9e_W50
        self.FAMSURV10a_W50 = FAMSURV10a_W50
        self.FAMSURV10b_W50 = FAMSURV10b_W50
        self.FAMSURV10c_W50 = FAMSURV10c_W50
        self.FAMSURV10e_W50 = FAMSURV10e_W50
        self.FAMSURV11W_W50 = FAMSURV11W_W50
        self.FAMSURV11M_W50 = FAMSURV11M_W50
        self.FAMSURV12_W50 = FAMSURV12_W50
        self.MOTHER_W50 = MOTHER_W50
        self.FATHER_W50 = FATHER_W50
        self.SIB_W50 = SIB_W50
        self.REMARR_W50 = REMARR_W50
        self.ENG_W50 = ENG_W50
        self.LWPT_W50 = LWPT_W50
        self.MAR2_W50 = MAR2_W50
        self.FAMSURV16_W50 = FAMSURV16_W50
        self.FAMSURV17_W50 = FAMSURV17_W50
        self.ADKIDS_W50 = ADKIDS_W50
        self.PAR1_W50 = PAR1_W50
        self.PAR2_W50 = PAR2_W50
        self.ROMRELDUR_W50 = ROMRELDUR_W50
        self.MARRDUR_W50 = MARRDUR_W50
        self.COHABDUR_W50 = COHABDUR_W50
        self.LWPSP_W50 = LWPSP_W50
        self.FAMSURV18A_W50 = FAMSURV18A_W50
        self.FAMSURV18B_W50 = FAMSURV18B_W50
        self.ROMRELSER_W50 = ROMRELSER_W50
        self.FAMSURV19_W50 = FAMSURV19_W50
        self.FAMSURV20_W50 = FAMSURV20_W50
        self.FAMSURV21_W50 = FAMSURV21_W50
        self.FAMSURV22a_W50 = FAMSURV22a_W50
        self.FAMSURV22b_W50 = FAMSURV22b_W50
        self.FAMSURV22c_W50 = FAMSURV22c_W50
        self.FAMSURV22d_W50 = FAMSURV22d_W50
        self.FAMSURV22e_W50 = FAMSURV22e_W50
        self.FAMSURV22f_W50 = FAMSURV22f_W50
        self.FAMSURV22g_W50 = FAMSURV22g_W50
        self.FAMSURV23a_W50 = FAMSURV23a_W50
        self.FAMSURV23b_W50 = FAMSURV23b_W50
        self.FAMSURV23c_W50 = FAMSURV23c_W50
        self.FAMSURV23d_W50 = FAMSURV23d_W50
        self.FAMSURV23e_W50 = FAMSURV23e_W50
        self.FAMSURV23f_W50 = FAMSURV23f_W50
        self.FAMSURV23g_W50 = FAMSURV23g_W50
        self.MARRYPREF1_W50 = MARRYPREF1_W50
        self.MARRYPREF2_W50 = MARRYPREF2_W50
        self.FAMSURV25_W50 = FAMSURV25_W50
        self.FAMSURV26a_W50 = FAMSURV26a_W50
        self.FAMSURV26b_W50 = FAMSURV26b_W50
        self.FAMSURV26c_W50 = FAMSURV26c_W50
        self.FAMSURV26d_W50 = FAMSURV26d_W50
        self.FAMSURV27a_W50 = FAMSURV27a_W50
        self.FAMSURV27b_W50 = FAMSURV27b_W50
        self.FAMSURV27c_W50 = FAMSURV27c_W50
        self.FAMSURV27d_W50 = FAMSURV27d_W50
        self.FAMSURV28_W50 = FAMSURV28_W50
        self.FAMSURV29_W50 = FAMSURV29_W50
        self.FAMSURV30a_W50 = FAMSURV30a_W50
        self.FAMSURV30b_W50 = FAMSURV30b_W50
        self.FAMSURV30c_W50 = FAMSURV30c_W50
        self.FAMSURV30d_W50 = FAMSURV30d_W50
        self.FAMSURV30e_W50 = FAMSURV30e_W50
        self.FAMSURV30f_W50 = FAMSURV30f_W50
        self.E5MOD_W50 = E5MOD_W50
        self.FAMSURV32a_W50 = FAMSURV32a_W50
        self.FAMSURV32b_W50 = FAMSURV32b_W50
        self.FAMSURV32c_W50 = FAMSURV32c_W50
        self.FAMSURV32d_W50 = FAMSURV32d_W50
        self.FAMSURV32e_W50 = FAMSURV32e_W50
        self.FAMSURV33a_W50 = FAMSURV33a_W50
        self.FAMSURV33b_W50 = FAMSURV33b_W50
        self.FAMSURV33c_W50 = FAMSURV33c_W50
        self.FAMSURV33d_W50 = FAMSURV33d_W50
        self.FAMSURV34A_W50 = FAMSURV34A_W50
        self.FAMSURV34B_W50 = FAMSURV34B_W50
        self.FAMSURV35a_W50 = FAMSURV35a_W50
        self.FAMSURV35b_W50 = FAMSURV35b_W50
        self.FAMSURV35c_W50 = FAMSURV35c_W50
        self.FAMSURV36a_W50 = FAMSURV36a_W50
        self.FAMSURV36b_W50 = FAMSURV36b_W50
        self.FAMSURV36c_W50 = FAMSURV36c_W50
        self.HAVEKIDS1_W50 = HAVEKIDS1_W50
        self.FAMSURV37_W50 = FAMSURV37_W50
        self.FAMSURV38a_W50 = FAMSURV38a_W50
        self.FAMSURV38b_W50 = FAMSURV38b_W50
        self.FAMSURV38c_W50 = FAMSURV38c_W50
        self.FAMSURV39_W50 = FAMSURV39_W50
        self.FAMSURV40_W50 = FAMSURV40_W50
        self.FAMSURV43_W50 = FAMSURV43_W50
        self.FAMSURV44_W50 = FAMSURV44_W50
        self.DNATEST_W50 = DNATEST_W50
        self.DNA2a_W50 = DNA2a_W50
        self.DNA2b_W50 = DNA2b_W50
        self.DNA2c_W50 = DNA2c_W50
        self.DNA3a_W50 = DNA3a_W50
        self.DNA3b_W50 = DNA3b_W50
        self.DNA3c_W50 = DNA3c_W50
        self.DNA4_W50 = DNA4_W50
        self.DNA5_W50 = DNA5_W50
        self.SPOUSESEX_W50 = SPOUSESEX_W50
        self.ORIENTATIONMOD_W50 = ORIENTATIONMOD_W50
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
        self.all_fields = [SATLIFEa_W50, SATLIFEb_W50, SATLIFEc_W50, SATLIFEd_W50, FAMSURV1_W50, 
                 FAMSURV2Ma_W50, FAMSURV2Mb_W50, FAMSURV2Mc_W50, FAMSURV2Md_W50, FAMSURV2Me_W50, 
                 FAMSURV2Wa_W50, FAMSURV2Wb_W50, FAMSURV2Wc_W50, FAMSURV2Wd_W50, FAMSURV2We_W50, 
                 FAMSURV3_W50, FAMSURV4_W50, FAMSURV5a_W50, FAMSURV5b_W50, FAMSURV5c_W50, 
                 FAMSURV5d_W50, FAMSURV6_W50, FAMSURV7_W50, FAMSURV8_W50, FAMSURV9a_W50, 
                 FAMSURV9b_W50, FAMSURV9c_W50, FAMSURV9e_W50, FAMSURV10a_W50, FAMSURV10b_W50, 
                 FAMSURV10c_W50, FAMSURV10e_W50, FAMSURV11W_W50, FAMSURV11M_W50, FAMSURV12_W50, 
                 MOTHER_W50, FATHER_W50, SIB_W50, REMARR_W50, ENG_W50, LWPT_W50, MAR2_W50, 
                 FAMSURV16_W50, FAMSURV17_W50, ADKIDS_W50, PAR1_W50, PAR2_W50, ROMRELDUR_W50, 
                 MARRDUR_W50, COHABDUR_W50, LWPSP_W50, FAMSURV18A_W50, FAMSURV18B_W50, 
                 ROMRELSER_W50, FAMSURV19_W50, FAMSURV20_W50, FAMSURV21_W50, FAMSURV22a_W50, 
                 FAMSURV22b_W50, FAMSURV22c_W50, FAMSURV22d_W50, FAMSURV22e_W50, FAMSURV22f_W50, 
                 FAMSURV22g_W50, FAMSURV23a_W50, FAMSURV23b_W50, FAMSURV23c_W50, FAMSURV23d_W50, 
                 FAMSURV23e_W50, FAMSURV23f_W50, FAMSURV23g_W50, MARRYPREF1_W50, MARRYPREF2_W50, 
                 FAMSURV25_W50, FAMSURV26a_W50, FAMSURV26b_W50, FAMSURV26c_W50, FAMSURV26d_W50, 
                 FAMSURV27a_W50, FAMSURV27b_W50, FAMSURV27c_W50, FAMSURV27d_W50, FAMSURV28_W50, 
                 FAMSURV29_W50, FAMSURV30a_W50, FAMSURV30b_W50, FAMSURV30c_W50, FAMSURV30d_W50, 
                 FAMSURV30e_W50, FAMSURV30f_W50, E5MOD_W50, FAMSURV32a_W50, FAMSURV32b_W50, 
                 FAMSURV32c_W50, FAMSURV32d_W50, FAMSURV32e_W50, FAMSURV33a_W50, FAMSURV33b_W50, 
                 FAMSURV33c_W50, FAMSURV33d_W50, FAMSURV34A_W50, FAMSURV34B_W50, FAMSURV35a_W50, 
                 FAMSURV35b_W50, FAMSURV35c_W50, FAMSURV36a_W50, FAMSURV36b_W50, FAMSURV36c_W50, 
                 HAVEKIDS1_W50, FAMSURV37_W50, FAMSURV38a_W50, FAMSURV38b_W50, FAMSURV38c_W50, 
                 FAMSURV39_W50, FAMSURV40_W50, FAMSURV43_W50, FAMSURV44_W50, DNATEST_W50, 
                 DNA2a_W50, DNA2b_W50, DNA2c_W50, DNA3a_W50, DNA3b_W50, DNA3c_W50, DNA4_W50, 
                 DNA5_W50, SPOUSESEX_W50, ORIENTATIONMOD_W50, CREGION, AGE, SEX, EDUCATION, 
                 CITIZEN, MARITAL, RELIG, RELIGATTEND, POLPARTY, INCOME, POLIDEOLOGY, RACE]

    def getAttributes(self):
        return self.__dict__
    
    def identityParagraph(self): 
        citizen = "a US citizen" if self.CITIZEN == "Yes" else "not a US citizen"
        identity_template = """I live in the {self.CREGION} region of the United States. I am {self.SEX}. In terms of my age, I am {self.AGE}. My level of education is: {self.EDUCATION}. I am {self.RACE} and I am {citizen}. My marital status is {self.MARITAL}. I go to church: {self.RELIGATTEND}. My religion is {self.RELIG}. Politically, I am a {self.POLPARTY}. I would describe my politics as {self.POLIDEOLOGY}. My total family income is {self.INCOME} every year.\n"""        
        identity_paragraph = identity_template.format(self=self, citizen=citizen)
        return identity_paragraph
