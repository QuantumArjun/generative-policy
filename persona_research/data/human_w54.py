class HumanW54:
    def __init__(self,FIN_SIT_W54,FIN_SITFUT_W54,FIN_SITMOST_W54,FIN_SITCOMM_W54,FIN_SITGROWUP_W54,JOBTRAIN_W54,GOVPRIORITYa_W54,GOVPRIORITYb_W54,GOVPRIORITYc_W54,GOVPRIORITYd_W54,GOVPRIORITYe_W54,GOVPRIORITYf_W54,GOVRESP_a_W54, GOVRESP_b_W54,GOVRESP_c_W54,GOVRESP_d_W54,GOVRESP_e_W54,GOVRESP_f_W54,GOVRESP_g_W54,GOVRESP_h_W54,ECON1_W54, ECON1B_W54,ECON3_a_W54,ECON3_b_W54,ECON3_c_W54, ECON3_d_W54,ECON3_e_W54, ECON3_f_W54,ECON3_g_W54,ECON3_h_W54,ECON3_i_W54,ECON4_a_W54,ECON4_b_W54,ECON4_c_W54,ECON4_d_W54,ECON4_e_W54, ECON4_f_W54, ECON4_g_W54,ECON4_h_W54,ECON4_i_W54,INEQ1_W54,INEQ2_W54,INEQ3_W54, INEQ4_a_W54,INEQ4_b_W54,INEQ4_c_W54,INEQ4_d_W54,INEQ4_e_W54,INEQ5_a_W54,INEQ5_b_W54,INEQ5_c_W54,INEQ5_d_W54,INEQ5_e_W54,INEQ5_f_W54,INEQ5_g_W54,INEQ5_h_W54,INEQ5_i_W54,INEQ5_j_W54,INEQ5_k_W54,INEQ5_l_W54,INEQ5_m_W54,INEQ6_W54,INEQ7_W54,INEQ8_a_W54,INEQ8_b_W54,INEQ8_c_W54,INEQ8_d_W54,INEQ8_e_W54,INEQ8_f_W54,INEQ8_g_W54,INEQ8_h_W54, INEQ8_i_W54,INEQ8_j_W54, INEQ9_W54,INEQ10_W54,INEQ11_W54,ECON5_a_W54,ECON5_b_W54,ECON5_c_W54, ECON5_d_W54,ECON5_e_W54,ECON5_f_W54,ECON5_g_W54,ECON5_h_W54,ECON5_i_W54,ECON5_j_W54,ECON5_k_W54,ECIMPa_W54,ECIMPb_W54,ECIMPc_W54,ECIMPd_W54,ECIMPe_W54,
                ECIMPf_W54,
                ECIMPg_W54,
                ECIMPh_W54,
                ECIMPi_W54,
                ECIMPj_W54,
                WORRY2a_W54,
                WORRY2b_W54,
                WORRY2c_W54,
                WORRY2d_W54,
                WORRY2e_W54,
                FINANCEa_W54,
                FINANCEb_W54,
                FINANCEc_W54,
                DEBTa_W54,
                DEBTb_W54,
                DEBTc_W54,
                DEBTd_W54,
                DEBTe_W54,
                BENEFITSa_W54,
                BENEFITSb_W54,
                BENEFITSc_W54,
                WORKHARD_W53,
                POOREASY_W53,
                ECONFAIR_W53,
                CREGION, AGE, SEX, EDUCATION, 
                 CITIZEN, MARITAL, RELIG, RELIGATTEND, POLPARTY, INCOME, POLIDEOLOGY, RACE):

        self.FIN_SIT_W54 = FIN_SIT_W54
        self.FIN_SITFUT_W54 = FIN_SITFUT_W54
        self.FIN_SITMOST_W54 = FIN_SITMOST_W54
        self.FIN_SITCOMM_W54 = FIN_SITCOMM_W54
        self.FIN_SITGROWUP_W54 = FIN_SITGROWUP_W54
        self.JOBTRAIN_W54 = JOBTRAIN_W54
        self.GOVPRIORITYa_W54 = GOVPRIORITYa_W54
        self.GOVPRIORITYb_W54 = GOVPRIORITYb_W54
        self.GOVPRIORITYc_W54 = GOVPRIORITYc_W54
        self.GOVPRIORITYd_W54 = GOVPRIORITYd_W54
        self.GOVPRIORITYe_W54 = GOVPRIORITYe_W54
        self.GOVPRIORITYf_W54 = GOVPRIORITYf_W54
        self.GOVRESP_a_W54 = GOVRESP_a_W54
        self.GOVRESP_b_W54 = GOVRESP_b_W54
        self.GOVRESP_c_W54 = GOVRESP_c_W54
        self.GOVRESP_d_W54 = GOVRESP_d_W54
        self.GOVRESP_e_W54 = GOVRESP_e_W54
        self.GOVRESP_f_W54 = GOVRESP_f_W54
        self.GOVRESP_g_W54 = GOVRESP_g_W54
        self.GOVRESP_h_W54 = GOVRESP_h_W54
        self.ECON1_W54 = ECON1_W54
        self.ECON1B_W54 = ECON1B_W54
        self.ECON3_a_W54 = ECON3_a_W54
        self.ECON3_b_W54 = ECON3_b_W54
        self.ECON3_c_W54 = ECON3_c_W54
        self.ECON3_d_W54 = ECON3_d_W54
        self.ECON3_e_W54 = ECON3_e_W54
        self.ECON3_f_W54 = ECON3_f_W54
        self.ECON3_g_W54 = ECON3_g_W54
        self.ECON3_h_W54 = ECON3_h_W54
        self.ECON3_i_W54 = ECON3_i_W54
        self.ECON4_a_W54 = ECON4_a_W54
        self.ECON4_b_W54 = ECON4_b_W54
        self.ECON4_c_W54 = ECON4_c_W54
        self.ECON4_d_W54 = ECON4_d_W54
        self.ECON4_e_W54 = ECON4_e_W54
        self.ECON4_f_W54 = ECON4_f_W54
        self.ECON4_g_W54 = ECON4_g_W54
        self.ECON4_h_W54 = ECON4_h_W54
        self.ECON4_i_W54 = ECON4_i_W54
        self.INEQ1_W54 = INEQ1_W54
        self.INEQ2_W54 = INEQ2_W54
        self.INEQ3_W54 = INEQ3_W54
        self.INEQ4_a_W54 = INEQ4_a_W54
        self.INEQ4_b_W54 = INEQ4_b_W54
        self.INEQ4_c_W54 = INEQ4_c_W54
        self.INEQ4_d_W54 = INEQ4_d_W54
        self.INEQ4_e_W54 = INEQ4_e_W54
        self.INEQ5_a_W54 = INEQ5_a_W54
        self.INEQ5_b_W54 = INEQ5_b_W54
        self.INEQ5_c_W54 = INEQ5_c_W54
        self.INEQ5_d_W54 = INEQ5_d_W54
        self.INEQ5_e_W54 = INEQ5_e_W54
        self.INEQ5_f_W54 = INEQ5_f_W54
        self.INEQ5_g_W54 = INEQ5_g_W54
        self.INEQ5_h_W54 = INEQ5_h_W54
        self.INEQ5_i_W54 = INEQ5_i_W54
        self.INEQ5_j_W54 = INEQ5_j_W54
        self.INEQ5_k_W54 = INEQ5_k_W54
        self.INEQ5_l_W54 = INEQ5_l_W54
        self.INEQ5_m_W54 = INEQ5_m_W54
        self.INEQ6_W54 = INEQ6_W54
        self.INEQ7_W54 = INEQ7_W54
        self.INEQ8_a_W54 = INEQ8_a_W54
        self.INEQ8_b_W54 = INEQ8_b_W54
        self.INEQ8_c_W54 = INEQ8_c_W54
        self.INEQ8_d_W54 = INEQ8_d_W54
        self.INEQ8_e_W54 = INEQ8_e_W54
        self.INEQ8_f_W54 = INEQ8_f_W54
        self.INEQ8_g_W54 = INEQ8_g_W54
        self.INEQ8_h_W54 = INEQ8_h_W54
        self.INEQ8_i_W54 = INEQ8_i_W54
        self.INEQ8_j_W54 = INEQ8_j_W54
        self.INEQ9_W54 = INEQ9_W54
        self.INEQ10_W54 = INEQ10_W54
        self.INEQ11_W54 = INEQ11_W54
        self.ECON5_a_W54 = ECON5_a_W54
        self.ECON5_b_W54 = ECON5_b_W54
        self.ECON5_c_W54 = ECON5_c_W54
        self.ECON5_d_W54 = ECON5_d_W54
        self.ECON5_e_W54 = ECON5_e_W54
        self.ECON5_f_W54 = ECON5_f_W54
        self.ECON5_g_W54 = ECON5_g_W54
        self.ECON5_h_W54 = ECON5_h_W54
        self.ECON5_i_W54 = ECON5_i_W54
        self.ECON5_j_W54 = ECON5_j_W54
        self.ECON5_k_W54 = ECON5_k_W54
        self.ECIMPa_W54 = ECIMPa_W54
        self.ECIMPb_W54 = ECIMPb_W54
        self.ECIMPc_W54 = ECIMPc_W54
        self.ECIMPd_W54 = ECIMPd_W54
        self.ECIMPe_W54 = ECIMPe_W54
        self.ECIMPf_W54 = ECIMPf_W54
        self.ECIMPg_W54 = ECIMPg_W54
        self.ECIMPh_W54 = ECIMPh_W54
        self.ECIMPi_W54 = ECIMPi_W54
        self.ECIMPj_W54 = ECIMPj_W54
        self.WORRY2a_W54 = WORRY2a_W54
        self.WORRY2b_W54 = WORRY2b_W54
        self.WORRY2c_W54 = WORRY2c_W54
        self.WORRY2d_W54 = WORRY2d_W54
        self.WORRY2e_W54 = WORRY2e_W54
        self.FINANCEa_W54 = FINANCEa_W54
        self.FINANCEb_W54 = FINANCEb_W54
        self.FINANCEc_W54 = FINANCEc_W54
        self.DEBTa_W54 = DEBTa_W54
        self.DEBTb_W54 = DEBTb_W54
        self.DEBTc_W54 = DEBTc_W54
        self.DEBTd_W54 = DEBTd_W54
        self.DEBTe_W54 = DEBTe_W54
        self.BENEFITSa_W54 = BENEFITSa_W54
        self.BENEFITSb_W54 = BENEFITSb_W54
        self.BENEFITSc_W54 = BENEFITSc_W54
        self.WORKHARD_W53 = WORKHARD_W53
        self.POOREASY_W53 = POOREASY_W53
        self.ECONFAIR_W53 = ECONFAIR_W53     
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
        self.all_fields = [FIN_SIT_W54,FIN_SITFUT_W54,FIN_SITMOST_W54,FIN_SITCOMM_W54,FIN_SITGROWUP_W54,JOBTRAIN_W54,GOVPRIORITYa_W54,GOVPRIORITYb_W54,GOVPRIORITYc_W54,GOVPRIORITYd_W54,GOVPRIORITYe_W54,GOVPRIORITYf_W54,GOVRESP_a_W54, GOVRESP_b_W54,GOVRESP_c_W54,GOVRESP_d_W54,GOVRESP_e_W54,GOVRESP_f_W54,GOVRESP_g_W54,GOVRESP_h_W54,ECON1_W54, ECON1B_W54,ECON3_a_W54,ECON3_b_W54,ECON3_c_W54, ECON3_d_W54,ECON3_e_W54, ECON3_f_W54,ECON3_g_W54,ECON3_h_W54,ECON3_i_W54,ECON4_a_W54,ECON4_b_W54,ECON4_c_W54,ECON4_d_W54,ECON4_e_W54, ECON4_f_W54, ECON4_g_W54,ECON4_h_W54,ECON4_i_W54,INEQ1_W54,INEQ2_W54,INEQ3_W54, INEQ4_a_W54,INEQ4_b_W54,INEQ4_c_W54,INEQ4_d_W54,INEQ4_e_W54,INEQ5_a_W54,INEQ5_b_W54,INEQ5_c_W54,INEQ5_d_W54,INEQ5_e_W54,INEQ5_f_W54,INEQ5_g_W54,INEQ5_h_W54,INEQ5_i_W54,INEQ5_j_W54,INEQ5_k_W54,INEQ5_l_W54,INEQ5_m_W54,INEQ6_W54,INEQ7_W54,INEQ8_a_W54,INEQ8_b_W54,INEQ8_c_W54,INEQ8_d_W54,INEQ8_e_W54,INEQ8_f_W54,INEQ8_g_W54,INEQ8_h_W54, INEQ8_i_W54,INEQ8_j_W54, INEQ9_W54,INEQ10_W54,INEQ11_W54,ECON5_a_W54,ECON5_b_W54,ECON5_c_W54, ECON5_d_W54,ECON5_e_W54,ECON5_f_W54,ECON5_g_W54,ECON5_h_W54,ECON5_i_W54,ECON5_j_W54,ECON5_k_W54,ECIMPa_W54,ECIMPb_W54,ECIMPc_W54,ECIMPd_W54,ECIMPe_W54,
                ECIMPf_W54,
                ECIMPg_W54,
                ECIMPh_W54,
                ECIMPi_W54,
                ECIMPj_W54,
                WORRY2a_W54,
                WORRY2b_W54,
                WORRY2c_W54,
                WORRY2d_W54,
                WORRY2e_W54,
                FINANCEa_W54,
                FINANCEb_W54,
                FINANCEc_W54,
                DEBTa_W54,
                DEBTb_W54,
                DEBTc_W54,
                DEBTd_W54,
                DEBTe_W54,
                BENEFITSa_W54,
                BENEFITSb_W54,
                BENEFITSc_W54,
                WORKHARD_W53,
                POOREASY_W53,
                ECONFAIR_W53,
                CREGION, AGE, SEX, EDUCATION, 
                 CITIZEN, MARITAL, RELIG, RELIGATTEND, POLPARTY, INCOME, POLIDEOLOGY, RACE]

    def getAttributes(self):
        return self.__dict__
    
    def identityParagraph(self): 
        citizen = "a US citizen" if self.CITIZEN == "Yes" else "not a US citizen"
        identity_template = """I live in the {self.CREGION} region of the United States. I am {self.SEX}. In terms of my age, I am {self.AGE}. My level of education is: {self.EDUCATION}. I am {self.RACE} and I am {citizen}. My marital status is {self.MARITAL}. I go to church: {self.RELIGATTEND}. My religion is {self.RELIG}. Politically, I am a {self.POLPARTY}. I would describe my politics as {self.POLIDEOLOGY}. My total family income is {self.INCOME} every year.\n"""        
        identity_paragraph = identity_template.format(self=self, citizen=citizen)
        return identity_paragraph
