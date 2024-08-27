class HumanW42:
    def __init__(self, PAST_W42, FUTURE_W42, SC1_W42, CONFa_W42, CONFb_W42, CONFc_W42, CONFd_F1_W42, CONFd_F2_W42, 
                 CONFe_W42, CONFf_W42, CONFg_W42, POLICY1_W42, POLICY2_W42, POLICY3_W42, RQ1_F1A_W42, RQ2_F1A_W42, 
                 RQ3_F1Aa_W42, RQ3_F1Ab_W42, RQ3_F1Ac_W42, RQ3_F1Ad_W42, RQ4_F1Aa_W42, RQ4_F1Ab_W42, RQ4_F1Ac_W42, 
                 RQ4_F1Ad_W42, RQ4_F1Ae_W42, RQ5_F1A_W42, RQ6_F1A_W42, RQ7_F1A_W42, RQ8_F1A_W42, RQ1_F1B_W42, 
                 RQ2_F1B_W42, RQ3_F1Ba_W42, RQ3_F1Bb_W42, RQ3_F1Bc_W42, RQ3_F1Bd_W42, RQ4_F1Ba_W42, RQ4_F1Bb_W42, 
                 RQ4_F1Bc_W42, RQ4_F1Bd_W42, RQ4_F1Be_W42, RQ5_F1B_W42, RQ6_F1B_W42, RQ7_F1B_W42, RQ8_F1B_W42, 
                 RQ1_F1C_W42, RQ2_F1C_W42, RQ3_F1Ca_W42, RQ3_F1Cb_W42, RQ3_F1Cc_W42, RQ3_F1Cd_W42, RQ4_F1Ca_W42, 
                 RQ4_F1Cb_W42, RQ4_F1Cc_W42, RQ4_F1Cd_W42, RQ4_F1Ce_W42, RQ5_F1C_W42, RQ6_F1C_W42, RQ7_F1C_W42, 
                 RQ8_F1C_W42, PQ1_F2A_W42, PQ2_F2A_W42, PQ3_F2Aa_W42, PQ3_F2Ab_W42, PQ3_F2Ac_W42, PQ3_F2Ad_W42, 
                 PQ4_F2Aa_W42, PQ4_F2Ab_W42, PQ4_F2Ac_W42, PQ4_F2Ad_W42, PQ4_F2Ae_W42, PQ5_F2A_W42, PQ6_F2A_W42, 
                 PQ7_F2A_W42, PQ8_F2A_W42, PQ1_F2B_W42, PQ2_F2B_W42, PQ3_F2Ba_W42, PQ3_F2Bb_W42, PQ3_F2Bc_W42, 
                 PQ3_F2Bd_W42, PQ4_F2Ba_W42, PQ4_F2Bb_W42, PQ4_F2Bc_W42, PQ4_F2Bd_W42, PQ4_F2Be_W42, PQ5_F2B_W42, 
                 PQ6_F2B_W42, PQ7_F2B_W42, PQ8_F2B_W42, PQ1_F2C_W42, PQ2_F2C_W42, PQ3_F2Ca_W42, PQ3_F2Cb_W42, 
                 PQ3_F2Cc_W42, PQ3_F2Cd_W42, PQ4_F2Ca_W42, PQ4_F2Cb_W42, PQ4_F2Cc_W42, PQ4_F2Cd_W42, PQ4_F2Ce_W42, 
                 PQ5_F2C_W42, PQ6_F2C_W42, PQ7_F2C_W42, PQ8_F2C_W42, SCM4a_W42, SCM4b_W42, Q6F1_W42, Q7F1_W42, 
                 Q8F1_W42, Q9F1_W42, Q6F2_W42, Q7F2_W42, Q8F2_W42, Q9F2_W42, SCM5a_W42, SCM5b_W42, SCM5c_W42, 
                 SCM5d_W42, SCM5e_W42, SCM5f_W42, SCM5g_W42, SCM5h_W42, SCM5i_W42, SCM5j_W42, SCM2_W42, SCM3_W42, 
                 POP1_W42, POP2_W42, POP3_W42,
                 CREGION, AGE, SEX, EDUCATION, CITIZEN, MARITAL, RELIG, RELIGATTEND, POLPARTY, INCOME, POLIDEOLOGY, RACE):
        
        self.PAST_W42 = PAST_W42
        self.FUTURE_W42 = FUTURE_W42
        self.SC1_W42 = SC1_W42
        self.CONFa_W42 = CONFa_W42
        self.CONFb_W42 = CONFb_W42
        self.CONFc_W42 = CONFc_W42
        self.CONFd_F1_W42 = CONFd_F1_W42
        self.CONFd_F2_W42 = CONFd_F2_W42
        self.CONFe_W42 = CONFe_W42
        self.CONFf_W42 = CONFf_W42
        self.CONFg_W42 = CONFg_W42
        self.POLICY1_W42 = POLICY1_W42
        self.POLICY2_W42 = POLICY2_W42
        self.POLICY3_W42 = POLICY3_W42
        self.RQ1_F1A_W42 = RQ1_F1A_W42
        self.RQ2_F1A_W42 = RQ2_F1A_W42
        self.RQ3_F1Aa_W42 = RQ3_F1Aa_W42
        self.RQ3_F1Ab_W42 = RQ3_F1Ab_W42
        self.RQ3_F1Ac_W42 = RQ3_F1Ac_W42
        self.RQ3_F1Ad_W42 = RQ3_F1Ad_W42
        self.RQ4_F1Aa_W42 = RQ4_F1Aa_W42
        self.RQ4_F1Ab_W42 = RQ4_F1Ab_W42
        self.RQ4_F1Ac_W42 = RQ4_F1Ac_W42
        self.RQ4_F1Ad_W42 = RQ4_F1Ad_W42
        self.RQ4_F1Ae_W42 = RQ4_F1Ae_W42
        self.RQ5_F1A_W42 = RQ5_F1A_W42
        self.RQ6_F1A_W42 = RQ6_F1A_W42
        self.RQ7_F1A_W42 = RQ7_F1A_W42
        self.RQ8_F1A_W42 = RQ8_F1A_W42
        self.RQ1_F1B_W42 = RQ1_F1B_W42
        self.RQ2_F1B_W42 = RQ2_F1B_W42
        self.RQ3_F1Ba_W42 = RQ3_F1Ba_W42
        self.RQ3_F1Bb_W42 = RQ3_F1Bb_W42
        self.RQ3_F1Bc_W42 = RQ3_F1Bc_W42
        self.RQ3_F1Bd_W42 = RQ3_F1Bd_W42
        self.RQ4_F1Ba_W42 = RQ4_F1Ba_W42
        self.RQ4_F1Bb_W42 = RQ4_F1Bb_W42
        self.RQ4_F1Bc_W42 = RQ4_F1Bc_W42
        self.RQ4_F1Bd_W42 = RQ4_F1Bd_W42
        self.RQ4_F1Be_W42 = RQ4_F1Be_W42
        self.RQ5_F1B_W42 = RQ5_F1B_W42
        self.RQ6_F1B_W42 = RQ6_F1B_W42
        self.RQ7_F1B_W42 = RQ7_F1B_W42
        self.RQ8_F1B_W42 = RQ8_F1B_W42
        self.RQ1_F1C_W42 = RQ1_F1C_W42
        self.RQ2_F1C_W42 = RQ2_F1C_W42
        self.RQ3_F1Ca_W42 = RQ3_F1Ca_W42
        self.RQ3_F1Cb_W42 = RQ3_F1Cb_W42
        self.RQ3_F1Cc_W42 = RQ3_F1Cc_W42
        self.RQ3_F1Cd_W42 = RQ3_F1Cd_W42
        self.RQ4_F1Ca_W42 = RQ4_F1Ca_W42
        self.RQ4_F1Cb_W42 = RQ4_F1Cb_W42
        self.RQ4_F1Cc_W42 = RQ4_F1Cc_W42
        self.RQ4_F1Cd_W42 = RQ4_F1Cd_W42
        self.RQ4_F1Ce_W42 = RQ4_F1Ce_W42
        self.RQ5_F1C_W42 = RQ5_F1C_W42
        self.RQ6_F1C_W42 = RQ6_F1C_W42
        self.RQ7_F1C_W42 = RQ7_F1C_W42
        self.RQ8_F1C_W42 = RQ8_F1C_W42
        self.PQ1_F2A_W42 = PQ1_F2A_W42
        self.PQ2_F2A_W42 = PQ2_F2A_W42
        self.PQ3_F2Aa_W42 = PQ3_F2Aa_W42
        self.PQ3_F2Ab_W42 = PQ3_F2Ab_W42
        self.PQ3_F2Ac_W42 = PQ3_F2Ac_W42
        self.PQ3_F2Ad_W42 = PQ3_F2Ad_W42
        self.PQ4_F2Aa_W42 = PQ4_F2Aa_W42
        self.PQ4_F2Ab_W42 = PQ4_F2Ab_W42
        self.PQ4_F2Ac_W42 = PQ4_F2Ac_W42
        self.PQ4_F2Ad_W42 = PQ4_F2Ad_W42
        self.PQ4_F2Ae_W42 = PQ4_F2Ae_W42
        self.PQ5_F2A_W42 = PQ5_F2A_W42
        self.PQ6_F2A_W42 = PQ6_F2A_W42
        self.PQ7_F2A_W42 = PQ7_F2A_W42
        self.PQ8_F2A_W42 = PQ8_F2A_W42
        self.PQ1_F2B_W42 = PQ1_F2B_W42
        self.PQ2_F2B_W42 = PQ2_F2B_W42
        self.PQ3_F2Ba_W42 = PQ3_F2Ba_W42
        self.PQ3_F2Bb_W42 = PQ3_F2Bb_W42
        self.PQ3_F2Bc_W42 = PQ3_F2Bc_W42
        self.PQ3_F2Bd_W42 = PQ3_F2Bd_W42
        self.PQ4_F2Ba_W42 = PQ4_F2Ba_W42
        self.PQ4_F2Bb_W42 = PQ4_F2Bb_W42
        self.PQ4_F2Bc_W42 = PQ4_F2Bc_W42
        self.PQ4_F2Bd_W42 = PQ4_F2Bd_W42
        self.PQ4_F2Be_W42 = PQ4_F2Be_W42
        self.PQ5_F2B_W42 = PQ5_F2B_W42
        self.PQ6_F2B_W42 = PQ6_F2B_W42
        self.PQ7_F2B_W42 = PQ7_F2B_W42
        self.PQ8_F2B_W42 = PQ8_F2B_W42
        self.PQ1_F2C_W42 = PQ1_F2C_W42
        self.PQ2_F2C_W42 = PQ2_F2C_W42
        self.PQ3_F2Ca_W42 = PQ3_F2Ca_W42
        self.PQ3_F2Cb_W42 = PQ3_F2Cb_W42
        self.PQ3_F2Cc_W42 = PQ3_F2Cc_W42
        self.PQ3_F2Cd_W42 = PQ3_F2Cd_W42
        self.PQ4_F2Ca_W42 = PQ4_F2Ca_W42
        self.PQ4_F2Cb_W42 = PQ4_F2Cb_W42
        self.PQ4_F2Cc_W42 = PQ4_F2Cc_W42
        self.PQ4_F2Cd_W42 = PQ4_F2Cd_W42
        self.PQ4_F2Ce_W42 = PQ4_F2Ce_W42
        self.PQ5_F2C_W42 = PQ5_F2C_W42
        self.PQ6_F2C_W42 = PQ6_F2C_W42
        self.PQ7_F2C_W42 = PQ7_F2C_W42
        self.PQ8_F2C_W42 = PQ8_F2C_W42
        self.SCM4a_W42 = SCM4a_W42
        self.SCM4b_W42 = SCM4b_W42
        self.SCM5a_W42 = SCM5a_W42
        self.SCM5b_W42 = SCM5b_W42
        self.SCM5c_W42 = SCM5c_W42
        self.SCM5d_W42 = SCM5d_W42
        self.SCM5e_W42 = SCM5e_W42
        self.SCM5f_W42 = SCM5f_W42
        self.SCM5g_W42 = SCM5g_W42
        self.SCM5h_W42 = SCM5h_W42
        self.SCM5i_W42 = SCM5i_W42
        self.SCM5j_W42 = SCM5j_W42
        self.SCM2_W42 = SCM2_W42
        self.SCM3_W42 = SCM3_W42
        self.POP1_W42 = POP1_W42
        self.POP2_W42 = POP2_W42
        self.POP3_W42 = POP3_W42
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
        self.all_fields = [PAST_W42, FUTURE_W42, SC1_W42, CONFa_W42, CONFb_W42, CONFc_W42, CONFd_F1_W42, CONFd_F2_W42, 
                 CONFe_W42, CONFf_W42, CONFg_W42, POLICY1_W42, POLICY2_W42, POLICY3_W42, RQ1_F1A_W42, RQ2_F1A_W42, 
                 RQ3_F1Aa_W42, RQ3_F1Ab_W42, RQ3_F1Ac_W42, RQ3_F1Ad_W42, RQ4_F1Aa_W42, RQ4_F1Ab_W42, RQ4_F1Ac_W42, 
                 RQ4_F1Ad_W42, RQ4_F1Ae_W42, RQ5_F1A_W42, RQ6_F1A_W42, RQ7_F1A_W42, RQ8_F1A_W42, RQ1_F1B_W42, 
                 RQ2_F1B_W42, RQ3_F1Ba_W42, RQ3_F1Bb_W42, RQ3_F1Bc_W42, RQ3_F1Bd_W42, RQ4_F1Ba_W42, RQ4_F1Bb_W42, 
                 RQ4_F1Bc_W42, RQ4_F1Bd_W42, RQ4_F1Be_W42, RQ5_F1B_W42, RQ6_F1B_W42, RQ7_F1B_W42, RQ8_F1B_W42, 
                 RQ1_F1C_W42, RQ2_F1C_W42, RQ3_F1Ca_W42, RQ3_F1Cb_W42, RQ3_F1Cc_W42, RQ3_F1Cd_W42, RQ4_F1Ca_W42, 
                 RQ4_F1Cb_W42, RQ4_F1Cc_W42, RQ4_F1Cd_W42, RQ4_F1Ce_W42, RQ5_F1C_W42, RQ6_F1C_W42, RQ7_F1C_W42, 
                 RQ8_F1C_W42, PQ1_F2A_W42, PQ2_F2A_W42, PQ3_F2Aa_W42, PQ3_F2Ab_W42, PQ3_F2Ac_W42, PQ3_F2Ad_W42, 
                 PQ4_F2Aa_W42, PQ4_F2Ab_W42, PQ4_F2Ac_W42, PQ4_F2Ad_W42, PQ4_F2Ae_W42, PQ5_F2A_W42, PQ6_F2A_W42, 
                 PQ7_F2A_W42, PQ8_F2A_W42, PQ1_F2B_W42, PQ2_F2B_W42, PQ3_F2Ba_W42, PQ3_F2Bb_W42, PQ3_F2Bc_W42, 
                 PQ3_F2Bd_W42, PQ4_F2Ba_W42, PQ4_F2Bb_W42, PQ4_F2Bc_W42, PQ4_F2Bd_W42, PQ4_F2Be_W42, PQ5_F2B_W42, 
                 PQ6_F2B_W42, PQ7_F2B_W42, PQ8_F2B_W42, PQ1_F2C_W42, PQ2_F2C_W42, PQ3_F2Ca_W42, PQ3_F2Cb_W42, 
                 PQ3_F2Cc_W42, PQ3_F2Cd_W42, PQ4_F2Ca_W42, PQ4_F2Cb_W42, PQ4_F2Cc_W42, PQ4_F2Cd_W42, PQ4_F2Ce_W42, 
                 PQ5_F2C_W42, PQ6_F2C_W42, PQ7_F2C_W42, PQ8_F2C_W42, SCM4a_W42, SCM4b_W42, Q6F1_W42, Q7F1_W42, 
                 Q8F1_W42, Q9F1_W42, Q6F2_W42, Q7F2_W42, Q8F2_W42, Q9F2_W42, SCM5a_W42, SCM5b_W42, SCM5c_W42, 
                 SCM5d_W42, SCM5e_W42, SCM5f_W42, SCM5g_W42, SCM5h_W42, SCM5i_W42, SCM5j_W42, SCM2_W42, SCM3_W42, 
                 POP1_W42, POP2_W42, POP3_W42,
                 CREGION, AGE, SEX, EDUCATION, CITIZEN, MARITAL, RELIG, RELIGATTEND, POLPARTY, INCOME, POLIDEOLOGY, RACE]


    def getAttributes(self):
        return self.__dict__
    
    def identityParagraph(self): 
        citizen = "a US citizen" if self.CITIZEN == "Yes" else "not a US citizen"
        identity_template = """I live in the {self.CREGION} region of the United States. I am {self.SEX}. In terms of my age, I am {self.AGE}. My level of education is: {self.EDUCATION}. I am {self.RACE} and I am {citizen}. My marital status is {self.MARITAL}. I go to church: {self.RELIGATTEND}. My religion is {self.RELIG}. Politically, I am a {self.POLPARTY}. I would describe my politics as {self.POLIDEOLOGY}. My total family income is {self.INCOME} every year.\n"""        
        identity_paragraph = identity_template.format(self=self, citizen=citizen)
        return identity_paragraph
