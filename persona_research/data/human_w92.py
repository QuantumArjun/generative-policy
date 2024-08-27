class HumanW92:
    def __init__(self,
                 POL1JB_W92,
                 LIFEFIFTY_W92,
                 BIGHOUSES_W92,
                 INSTN_CHR_W92,
                 INSTN_CLGS_W92,
                 INSTN_LGECRP_W92,
                 INSTN_MSCENT_W92,
                 INSTN_LBRUN_W92,
                 INSTN_K12_W92,
                 INSTN_BNKS_W92,
                 INSTN_TECHCMP_W92,
                 DIFFPARTY_W92,
                 GOVSIZE1_W92,
                 GOVSIZE2_W92,
                 GOVSIZE3_W92,
                 USEXCEPT_W92,
                 WOMENOBS_W92,
                 ECONFAIR_W92,
                 OPENIDEN_W92,
                 VTRGHTPRIV1_W92,
                 ALLIES_W92,
                 PEACESTR_W92,
                 GOVWASTE_W92,
                 COMPROMISEVAL_W92,
                 POORASSIST_W92,
                 PAR2CHILD_W92,
                 PAR2CHILDa_W92,
                 POLICY3MOD_W92,
                 WHADVANT_W92,
                 SUPERPWR_W92,
                 IL_IMM_PRI_W92,
                 BILLION_W92,
                 GLBLZE_W92,
                 FP_AUTH_W92,
                 GOVTHC_W92,
                 SNGLPYER_W92,
                 NOGOVTHC_W92,
                 FREECOLL_W92,
                 CRIM_SENT2_W92,
                 USMILSIZ_W92,
                 PROG_RRETRO_W92,
                 PROG_RNEED_W92,
                 PROG_RNEED2b_W92,
                 ELITEUNDMOD_W92,
                 POLINTOL2_a_W92,
                 POLINTOL2_b_W92,
                 CANQUALPOL_W92,
                 CANMTCHPOL_W92,
                 SOCIETY_TRANS_W92,
                 SOCIETY_RHIST_W92,
                 SOCIETY_JBCLL_W92,
                 SOCIETY_RELG_W92,
                 SOCIETY_WHT_W92,
                 SOCIETY_GUNS_W92,
                 SOCIETY_SSM_W92,
                 PROBOFF_a_W92,
                 PROBOFF_b_W92,
                 BUSPROFIT_W92,
                 CNTRYFAIR_W92,
                 GOVPROTCT_W92,
                 MARRFAM_W92,
                 GOVAID_W92,
                 RELIG_GOV_W92,
                 GOODEVIL_W92,
                 PPLRESP_W92,
                 RACESURV52MOD_W92,
                 ELECT_IMPT3_PRVFR_W92,
                 ELECT_IMPT3_PRVSUP_W92,
                 ELECT_CONF3_PRVFR_W92,
                 ELECT_CONF3_PRVSUP_W92,
                 CANDEXP_W92,
                 LEGALIMMIGAMT_W92,
                 UNIMMIGCOMM_W92,
                 GODMORALIMP_W92,
                 REPRSNTREP_W92,
                 REPRSNTDEM_W92,
                 VTRS_VALS_W92,
                 CREGION, 
                 AGE, 
                 SEX, 
                 EDUCATION, 
                 CITIZEN, 
                 MARITAL, 
                 RELIG, 
                 RELIGATTEND, 
                 POLPARTY, 
                 INCOME, 
                 POLIDEOLOGY,
                 RACE):
        self.POL1JB_W92 = POL1JB_W92
        self.LIFEFIFTY_W92 = LIFEFIFTY_W92
        self.BIGHOUSES_W92 = BIGHOUSES_W92
        self.INSTN_CHR_W92 = INSTN_CHR_W92
        self.INSTN_CLGS_W92 = INSTN_CLGS_W92
        self.INSTN_LGECRP_W92 = INSTN_LGECRP_W92
        self.INSTN_MSCENT_W92 = INSTN_MSCENT_W92
        self.INSTN_LBRUN_W92 = INSTN_LBRUN_W92
        self.INSTN_K12_W92 = INSTN_K12_W92
        self.INSTN_BNKS_W92 = INSTN_BNKS_W92
        self.INSTN_TECHCMP_W92 = INSTN_TECHCMP_W92
        self.DIFFPARTY_W92 = DIFFPARTY_W92
        self.GOVSIZE1_W92 = GOVSIZE1_W92
        self.GOVSIZE2_W92 = GOVSIZE2_W92
        self.GOVSIZE3_W92 = GOVSIZE3_W92
        self.USEXCEPT_W92 = USEXCEPT_W92
        self.WOMENOBS_W92 = WOMENOBS_W92
        self.ECONFAIR_W92 = ECONFAIR_W92
        self.OPENIDEN_W92 = OPENIDEN_W92
        self.VTRGHTPRIV1_W92 = VTRGHTPRIV1_W92
        self.ALLIES_W92 = ALLIES_W92
        self.PEACESTR_W92 = PEACESTR_W92
        self.GOVWASTE_W92 = GOVWASTE_W92
        self.COMPROMISEVAL_W92 = COMPROMISEVAL_W92
        self.POORASSIST_W92 = POORASSIST_W92
        self.PAR2CHILD_W92 = PAR2CHILD_W92
        self.PAR2CHILDa_W92 = PAR2CHILDa_W92
        self.POLICY3MOD_W92 = POLICY3MOD_W92
        self.WHADVANT_W92 = WHADVANT_W92
        self.SUPERPWR_W92 = SUPERPWR_W92
        self.IL_IMM_PRI_W92 = IL_IMM_PRI_W92
        self.BILLION_W92 = BILLION_W92
        self.GLBLZE_W92 = GLBLZE_W92
        self.FP_AUTH_W92 = FP_AUTH_W92
        self.GOVTHC_W92 = GOVTHC_W92
        self.SNGLPYER_W92 = SNGLPYER_W92
        self.NOGOVTHC_W92 = NOGOVTHC_W92
        self.FREECOLL_W92 = FREECOLL_W92
        self.CRIM_SENT2_W92 = CRIM_SENT2_W92
        self.USMILSIZ_W92 = USMILSIZ_W92
        self.PROG_RRETRO_W92 = PROG_RRETRO_W92
        self.PROG_RNEED_W92 = PROG_RNEED_W92
        self.PROG_RNEED2b_W92 = PROG_RNEED2b_W92
        self.ELITEUNDMOD_W92 = ELITEUNDMOD_W92
        self.POLINTOL2_a_W92 = POLINTOL2_a_W92
        self.POLINTOL2_b_W92 = POLINTOL2_b_W92
        self.CANQUALPOL_W92 = CANQUALPOL_W92
        self.CANMTCHPOL_W92 = CANMTCHPOL_W92
        self.SOCIETY_TRANS_W92 = SOCIETY_TRANS_W92
        self.SOCIETY_RHIST_W92 = SOCIETY_RHIST_W92
        self.SOCIETY_JBCLL_W92 = SOCIETY_JBCLL_W92
        self.SOCIETY_RELG_W92 = SOCIETY_RELG_W92
        self.SOCIETY_WHT_W92 = SOCIETY_WHT_W92
        self.SOCIETY_GUNS_W92 = SOCIETY_GUNS_W92
        self.SOCIETY_SSM_W92 = SOCIETY_SSM_W92
        self.PROBOFF_a_W92 = PROBOFF_a_W92
        self.PROBOFF_b_W92 = PROBOFF_b_W92
        self.BUSPROFIT_W92 = BUSPROFIT_W92
        self.CNTRYFAIR_W92 = CNTRYFAIR_W92
        self.GOVPROTCT_W92 = GOVPROTCT_W92
        self.MARRFAM_W92 = MARRFAM_W92
        self.GOVAID_W92 = GOVAID_W92
        self.RELIG_GOV_W92 = RELIG_GOV_W92
        self.GOODEVIL_W92 = GOODEVIL_W92
        self.PPLRESP_W92 = PPLRESP_W92
        self.RACESURV52MOD_W92 = RACESURV52MOD_W92
        self.ELECT_IMPT3_PRVFR_W92 = ELECT_IMPT3_PRVFR_W92
        self.ELECT_IMPT3_PRVSUP_W92 = ELECT_IMPT3_PRVSUP_W92
        self.ELECT_CONF3_PRVFR_W92 = ELECT_CONF3_PRVFR_W92
        self.ELECT_CONF3_PRVSUP_W92 = ELECT_CONF3_PRVSUP_W92
        self.CANDEXP_W92 = CANDEXP_W92
        self.LEGALIMMIGAMT_W92 = LEGALIMMIGAMT_W92
        self.UNIMMIGCOMM_W92 = UNIMMIGCOMM_W92
        self.GODMORALIMP_W92 = GODMORALIMP_W92
        self.REPRSNTREP_W92 = REPRSNTREP_W92
        self.REPRSNTDEM_W92 = REPRSNTDEM_W92
        self.VTRS_VALS_W92 = VTRS_VALS_W92
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
        self.all_fields = [POL1JB_W92,
                 LIFEFIFTY_W92,
                 BIGHOUSES_W92,
                 INSTN_CHR_W92,
                 INSTN_CLGS_W92,
                 INSTN_LGECRP_W92,
                 INSTN_MSCENT_W92,
                 INSTN_LBRUN_W92,
                 INSTN_K12_W92,
                 INSTN_BNKS_W92,
                 INSTN_TECHCMP_W92,
                 DIFFPARTY_W92,
                 GOVSIZE1_W92,
                 GOVSIZE2_W92,
                 GOVSIZE3_W92,
                 USEXCEPT_W92,
                 WOMENOBS_W92,
                 ECONFAIR_W92,
                 OPENIDEN_W92,
                 VTRGHTPRIV1_W92,
                 ALLIES_W92,
                 PEACESTR_W92,
                 GOVWASTE_W92,
                 COMPROMISEVAL_W92,
                 POORASSIST_W92,
                 PAR2CHILD_W92,
                 PAR2CHILDa_W92,
                 POLICY3MOD_W92,
                 WHADVANT_W92,
                 SUPERPWR_W92,
                 IL_IMM_PRI_W92,
                 BILLION_W92,
                 GLBLZE_W92,
                 FP_AUTH_W92,
                 GOVTHC_W92,
                 SNGLPYER_W92,
                 NOGOVTHC_W92,
                 FREECOLL_W92,
                 CRIM_SENT2_W92,
                 USMILSIZ_W92,
                 PROG_RRETRO_W92,
                 PROG_RNEED_W92,
                 PROG_RNEED2b_W92,
                 ELITEUNDMOD_W92,
                 POLINTOL2_a_W92,
                 POLINTOL2_b_W92,
                 CANQUALPOL_W92,
                 CANMTCHPOL_W92,
                 SOCIETY_TRANS_W92,
                 SOCIETY_RHIST_W92,
                 SOCIETY_JBCLL_W92,
                 SOCIETY_RELG_W92,
                 SOCIETY_WHT_W92,
                 SOCIETY_GUNS_W92,
                 SOCIETY_SSM_W92,
                 PROBOFF_a_W92,
                 PROBOFF_b_W92,
                 BUSPROFIT_W92,
                 CNTRYFAIR_W92,
                 GOVPROTCT_W92,
                 MARRFAM_W92,
                 GOVAID_W92,
                 RELIG_GOV_W92,
                 GOODEVIL_W92,
                 PPLRESP_W92,
                 RACESURV52MOD_W92,
                 ELECT_IMPT3_PRVFR_W92,
                 ELECT_IMPT3_PRVSUP_W92,
                 ELECT_CONF3_PRVFR_W92,
                 ELECT_CONF3_PRVSUP_W92,
                 CANDEXP_W92,
                 LEGALIMMIGAMT_W92,
                 UNIMMIGCOMM_W92,
                 GODMORALIMP_W92,
                 REPRSNTREP_W92,
                 REPRSNTDEM_W92,
                 VTRS_VALS_W92,
                 CREGION, 
                 AGE, 
                 SEX, 
                 EDUCATION, 
                 CITIZEN, 
                 MARITAL, 
                 RELIG, 
                 RELIGATTEND, 
                 POLPARTY, 
                 INCOME, 
                 POLIDEOLOGY,
                 RACE]

    def getAttributes(self):
        return self.__dict__
    
    def identityParagraph(self): 
        citizen = "a US citizen" if self.CITIZEN == "Yes" else "not a US citizen"
        identity_template = """I live in the {self.CREGION} region of the United States. I am {self.SEX}. In terms of my age, I am {self.AGE}. My level of education is: {self.EDUCATION}. I am {self.RACE} and I am {citizen}. My marital status is {self.MARITAL}. I go to church: {self.RELIGATTEND}. My religion is {self.RELIG}. Politically, I am a {self.POLPARTY}. I would describe my politics as {self.POLIDEOLOGY}. My total family income is {self.INCOME} every year.\n"""        
        identity_paragraph = identity_template.format(self=self, citizen=citizen)
        return identity_paragraph
