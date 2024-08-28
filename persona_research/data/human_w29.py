class HumanW29:
    def __init__(self, PERSDISCR_W29, NOWSMK_NHIS_W29, BLOODPR_W29, DIFF1A_W29, DIFF1B_W29, DIFF1C_W29, 
                 DIFF1D_W29, DIFF1E_W29, MASC2_W29, FEM2_W29, MASC1F1_W29, MASC2AF1_W29, MASC2BF1_W29, 
                 FEM1F2_W29, FEM2AF2_W29, FEM2BF2_W29, GOODJOBS_W29, HELPHURTA_W29, HELPHURTB_W29, 
                 HELPHURTC_W29, HELPHURTD_W29, HELPHURTE_W29, HELPHURTF_W29, HELPHURTG_W29, TRANSGEND1_W29, 
                 SEENMASC_W29, SEENFEM_W29, MAN1A_W29, MAN1B_W29, MAN1C_W29, MAN1D_W29, MAN1E_W29, 
                 MESUM1_FA_W29, MESUM1_FB_W29, MESUM1_FC_W29, MESUM1_FD_W29, MESUM1_FE_W29, MESUM1_FF_W29, 
                 MESUM2_FA_W29, MESUM2_FB_W29, MESUM2_FC_W29, MESUM2_FD_W29, MESUM2_FE_W29, MESUM2_FF_W29, 
                 TRANSGEND2_W29, TRANSGEND3_W29, TRAITSA_W29, TRAITSB_W29, TRAITSC_W29, TRAITSD_W29, 
                 TRAITSE_W29, TRAITSF_W29, BOYSF1A_W29, BOYSF1B_W29, BOYSF1C_W29, BOYSF1D_W29, GIRLSF2A_W29, 
                 GIRLSF2B_W29, GIRLSF2C_W29, GIRLSF2D_W29, SPOUSESEX_W29, HOOD_NHISA_W29, HOOD_NHISB_W29, 
                 HOOD_NHISC_W29, LOCALELECT_W29, PARTICIPATEA_W29, PARTICIPATEB_W29, PARTICIPATEC_W29, 
                 S7_W29, S12_W29, S13_W29, TALK_CPS_W29, FAVORS_CPS_W29, WORRYRET_W29, WORRYBILL_W29, 
                 GOPDIRCT_W29, DEMDIRCT_W29, CREGION, AGE, SEX, EDUCATION, CITIZEN, 
                 MARITAL, RELIG, RELIGATTEND, POLPARTY, INCOME, POLIDEOLOGY, RACE):
        self.PERSDISCR_W29 = PERSDISCR_W29
        self.NOWSMK_NHIS_W29 = NOWSMK_NHIS_W29
        self.BLOODPR_W29 = BLOODPR_W29
        self.DIFF1A_W29 = DIFF1A_W29
        self.DIFF1B_W29 = DIFF1B_W29
        self.DIFF1C_W29 = DIFF1C_W29
        self.DIFF1D_W29 = DIFF1D_W29
        self.DIFF1E_W29 = DIFF1E_W29
        self.MASC2_W29 = MASC2_W29
        self.FEM2_W29 = FEM2_W29
        self.MASC1F1_W29 = MASC1F1_W29
        self.MASC2AF1_W29 = MASC2AF1_W29
        self.MASC2BF1_W29 = MASC2BF1_W29
        self.FEM1F2_W29 = FEM1F2_W29
        self.FEM2AF2_W29 = FEM2AF2_W29
        self.FEM2BF2_W29 = FEM2BF2_W29
        self.GOODJOBS_W29 = GOODJOBS_W29
        self.HELPHURTA_W29 = HELPHURTA_W29
        self.HELPHURTB_W29 = HELPHURTB_W29
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
        self.HELPHURTC_W29 = HELPHURTC_W29
        self.HELPHURTD_W29 = HELPHURTD_W29
        self.HELPHURTE_W29 = HELPHURTE_W29
        self.HELPHURTF_W29 = HELPHURTF_W29
        self.HELPHURTG_W29 = HELPHURTG_W29
        self.TRANSGEND1_W29 = TRANSGEND1_W29
        self.SEENMASC_W29 = SEENMASC_W29
        self.SEENFEM_W29 = SEENFEM_W29
        self.MAN1A_W29 = MAN1A_W29
        self.MAN1B_W29 = MAN1B_W29
        self.MAN1C_W29 = MAN1C_W29
        self.MAN1D_W29 = MAN1D_W29
        self.MAN1E_W29 = MAN1E_W29
        self.MESUM1_FA_W29 = MESUM1_FA_W29
        self.MESUM1_FB_W29 = MESUM1_FB_W29
        self.MESUM1_FC_W29 = MESUM1_FC_W29
        self.MESUM1_FD_W29 = MESUM1_FD_W29
        self.MESUM1_FE_W29 = MESUM1_FE_W29
        self.MESUM1_FF_W29 = MESUM1_FF_W29
        self.MESUM2_FA_W29 = MESUM2_FA_W29
        self.MESUM2_FB_W29 = MESUM2_FB_W29
        self.MESUM2_FC_W29 = MESUM2_FC_W29
        self.MESUM2_FD_W29 = MESUM2_FD_W29
        self.MESUM2_FE_W29 = MESUM2_FE_W29
        self.MESUM2_FF_W29 = MESUM2_FF_W29
        self.TRANSGEND2_W29 = TRANSGEND2_W29
        self.TRANSGEND3_W29 = TRANSGEND3_W29
        self.TRAITSA_W29 = TRAITSA_W29
        self.TRAITSB_W29 = TRAITSB_W29
        self.TRAITSC_W29 = TRAITSC_W29
        self.TRAITSD_W29 = TRAITSD_W29
        self.TRAITSE_W29 = TRAITSE_W29
        self.TRAITSF_W29 = TRAITSF_W29
        self.BOYSF1A_W29 = BOYSF1A_W29
        self.BOYSF1B_W29 = BOYSF1B_W29
        self.BOYSF1C_W29 = BOYSF1C_W29
        self.BOYSF1D_W29 = BOYSF1D_W29
        self.GIRLSF2A_W29 = GIRLSF2A_W29
        self.GIRLSF2B_W29 = GIRLSF2B_W29
        self.GIRLSF2C_W29 = GIRLSF2C_W29
        self.GIRLSF2D_W29 = GIRLSF2D_W29
        self.SPOUSESEX_W29 = SPOUSESEX_W29
        self.HOOD_NHISA_W29 = HOOD_NHISA_W29
        self.HOOD_NHISB_W29 = HOOD_NHISB_W29
        self.HOOD_NHISC_W29 = HOOD_NHISC_W29
        self.LOCALELECT_W29 = LOCALELECT_W29
        self.PARTICIPATEA_W29 = PARTICIPATEA_W29
        self.PARTICIPATEB_W29 = PARTICIPATEB_W29
        self.PARTICIPATEC_W29 = PARTICIPATEC_W29
        self.S7_W29 = S7_W29
        self.S12_W29 = S12_W29
        self.S13_W29 = S13_W29
        self.TALK_CPS_W29 = TALK_CPS_W29
        self.FAVORS_CPS_W29 = FAVORS_CPS_W29
        self.WORRYRET_W29 = WORRYRET_W29
        self.WORRYBILL_W29 = WORRYBILL_W29
        self.GOPDIRCT_W29 = GOPDIRCT_W29
        self.DEMDIRCT_W29 = DEMDIRCT_W29
        self.all_fields = [PERSDISCR_W29, NOWSMK_NHIS_W29, BLOODPR_W29, DIFF1A_W29, DIFF1B_W29, DIFF1C_W29, 
                 DIFF1D_W29, DIFF1E_W29, MASC2_W29, FEM2_W29, MASC1F1_W29, MASC2AF1_W29, MASC2BF1_W29, 
                 FEM1F2_W29, FEM2AF2_W29, FEM2BF2_W29, GOODJOBS_W29, HELPHURTA_W29, HELPHURTB_W29, 
                 HELPHURTC_W29, HELPHURTD_W29, HELPHURTE_W29, HELPHURTF_W29, HELPHURTG_W29, TRANSGEND1_W29, 
                 SEENMASC_W29, SEENFEM_W29, MAN1A_W29, MAN1B_W29, MAN1C_W29, MAN1D_W29, MAN1E_W29, 
                 MESUM1_FA_W29, MESUM1_FB_W29, MESUM1_FC_W29, MESUM1_FD_W29, MESUM1_FE_W29, MESUM1_FF_W29, 
                 MESUM2_FA_W29, MESUM2_FB_W29, MESUM2_FC_W29, MESUM2_FD_W29, MESUM2_FE_W29, MESUM2_FF_W29, 
                 TRANSGEND2_W29, TRANSGEND3_W29, TRAITSA_W29, TRAITSB_W29, TRAITSC_W29, TRAITSD_W29, 
                 TRAITSE_W29, TRAITSF_W29, BOYSF1A_W29, BOYSF1B_W29, BOYSF1C_W29, BOYSF1D_W29, GIRLSF2A_W29, 
                 GIRLSF2B_W29, GIRLSF2C_W29, GIRLSF2D_W29, SPOUSESEX_W29, HOOD_NHISA_W29, HOOD_NHISB_W29, 
                 HOOD_NHISC_W29, LOCALELECT_W29, PARTICIPATEA_W29, PARTICIPATEB_W29, PARTICIPATEC_W29, 
                 S7_W29, S12_W29, S13_W29, TALK_CPS_W29, FAVORS_CPS_W29, WORRYRET_W29, WORRYBILL_W29, 
                 GOPDIRCT_W29, DEMDIRCT_W29, CREGION, AGE, SEX, EDUCATION, CITIZEN, 
                 MARITAL, RELIG, RELIGATTEND, POLPARTY, INCOME, POLIDEOLOGY, RACE]

    
    def getAttributes(self):
        return self.__dict__
    
    def identityParagraph(self): 
        citizen = "a US citizen" if self.CITIZEN == "Yes" else "not a US citizen"
        identity_template = """I live in the {self.CREGION} region of the United States. I am {self.SEX}. In terms of my age, I am {self.AGE}. My level of education is: {self.EDUCATION}. I am {self.RACE} and I am {citizen}. My marital status is {self.MARITAL}. I go to church: {self.RELIGATTEND}. My religion is {self.RELIG}. Politically, I am a {self.POLPARTY}. I would describe my politics as {self.POLIDEOLOGY}. My total family income is {self.INCOME} every year.\n"""        
        identity_paragraph = identity_template.format(self=self, citizen=citizen)
        return identity_paragraph