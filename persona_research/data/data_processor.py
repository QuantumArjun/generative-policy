import csv
import ast
from .human import Human
from .humanGlobal import HumanGlobal
from .human_w26 import HumanW26
from .human_w27 import HumanW27
from .human_w29 import HumanW29
from .human_w32 import HumanW32
from .human_w34 import HumanW34
from .human_w36 import HumanW36
from .human_w41 import HumanW41
from .human_w42 import HumanW42
from .human_w43 import HumanW43
from .human_w45 import HumanW45
from .human_w49 import HumanW49
from .human_w50 import HumanW50
from .human_w54 import HumanW54
from .human_w82 import HumanW82
from .human_w92 import HumanW92

import os

from enum import Enum

anes_key_question = {}
anes_key_fields = ["vote", "race", "year", "predicted_vote", "gender", "age", "view", "party", "interest", "church", "discuss_disc", "flag", "state", "number"]

w26_key_question = {}
w26_key_fields = ["SAFECRIME_W26", "WORLDDANGER_W26", "WORRYA_W26", "WORRYB_W26", "WORRYC_W26", "WORRYD_W26", "WORRYE_W26", "WORRYF_W26", "WORRYG_W26", "GUN_W26", "GUN1_W26", "EVEROWN_W26", "NEVEROWN_W26", "GUNTYPEOWNC_W26", "EVERSHOT_W26", "REASONGUNA_W26", "REASONGUNB_W26", "REASONGUNC_W26", "REASONGUND_W26", "REASONGUNE_W26", "IMPREASONGUN_W26", "GUNIDENTITY_W26", "GUNFRIEND_W26", "GUNSOCIETY_W26", "GUNCOMMUNITY_W26", "SHOOTFREQ_W26", "GUNSAFE_W26", "GUNSAFE2_W26", "GUNCOURSES_W26", "GUNACCESS_W26", "GUNLOCKED1_W26", "GUNLOADED1_W26", "GUNLOCKED2_W26", "GUNLOADED2_W26", "GUNCONTRIBA_W26", "GUNCONTRIBB_W26", "GUNCONTRIBC_W26", "GUNCONTRIBD_W26", "GUNCONTRIBE_W26", "GUNCONTRIBF_W26", "GROWUPVIOL_W26", "GROWUPGUN1_W26", "GROWUPGUN2A_W26", "GROWUPGUN2B_W26", "GROWUPGUN2C_W26", "GROWUPGUN4_W26", "GROWUPGUN6_W26", "GROWUPGUN7_W26", "GUNRESPNOKIDSA_W26", "GUNRESPNOKIDSB_W26", "GUNRESPNOKIDSC_W26", "GUNRESPNOKIDSD_W26", "GUNRESPNOKIDSE_W26", "GUNRESPNOKIDSF_W26", "GUNRESPNOKIDSG_W26", "GUNRESPKIDSA_W26", "GUNRESPKIDSB_W26", "GUNRESPKIDSC_W26", "GUNRESPKIDSD_W26", "GUNRESPKIDSE_W26", "GUNRESPKIDSF_W26", "GUNRESPKIDSG_W26", "GUNRESPKIDSH_W26", "GUNSAFETYKIDS_W26", "CARRYGUN_W26", "NOCARRYGUN_W26", "GUNKILLF1_W26", "GUNKILLF2_W26", "DEFENDGUN_W26", "GUNTHREAT_W26", "CRIMEVICTIM_W26", "MARGUN_W26", "GUNASSOCIATIONA_W26", "GUNACTIVITYA_W26", "GUNACTIVITYB_W26", "GUNACTIVITYC_W26", "GUNACTIVITYD_W26", "GUNACTIVITYE_W26"]

w27_key_question = {}
w27_key_fields = ["CAREREL_W27", "INDUSTRY_W27", "PREDICTA_W27", "PREDICTB_W27", "PREDICTC_W27", "PREDICTD_W27", 
                 "CARS1_W27", "CARS2_W27", "CARS3A_W27", "CARS3B_W27", "CARS4_W27", "CARS5_W27", "CARS7A_W27", "CARS7B_W27", 
                 "CARS8_W27", "CARS9A_W27", "CARS9B_W27", "CARS9C_W27", "CARS10A_W27", "CARS10B_W27", "CARS10C_W27", 
                 "CARS10D_W27", "CARS10E_W27", "WORK2_W27", "WORK3A_W27", "WORK3B_W27", "WORK3C_W27", "WORK3D_W27", 
                 "WORK3E_W27", "WORK3F_W27", "WORK4A_W27", "WORK4B_W27", "WORK4C_W27", "ROBJOB1_W27", "ROBJOB2_W27", 
                 "ROBJOB3A_W27", "ROBJOB3B_W27", "ROBJOB4A_W27", "ROBJOB4B_W27", "ROBJOB4C_W27", "ROBJOB4D_W27", 
                 "ROBJOB4E_W27", "ROBJOB4F_W27", "ROBJOB5B_W27", "ROBJOB5C_W27", "ROBJOB5D_W27", "ROBJOB6_W27", 
                 "ROBJOB7_W27", "ROBJOB8A_W27", "ROBJOB8B_W27", "ROBJOB8C_W27", "ROBJOB8D_W27", "ROBJOB8E_W27", 
                 "ROBJOB8F_W27", "ROBJOB8G_W27", "ROBJOB9_W27", "WORK5A_W27", "WORK6_W27", "WORK7_W27", "CAREGIV1_W27", 
                 "CAREGIV2_W27", "CAREGIV3A_W27", "CAREGIV3B_W27", "CAREGIV4_W27", "CAREGIV6A_W27", "CAREGIV6B_W27", 
                 "CAREGIV6C_W27", "CAREGIV6D_W27", "CAREGIV6E_W27", "CAREGIV6F_W27", "CAREGIV7_W27", "HIRING1_W27", 
                 "HIRING2_W27", "HIRING3A_W27", "HIRING3B_W27", "HIRING4_W27", "HIRING6A_W27", "HIRING6B_W27", 
                 "HIRING6C_W27", "HIRING6D_W27", "HIRING7A_W27", "HIRING7B_W27", "VOICE1_W27", "VOICE3_W27", "VOICE4_W27", 
                 "VOICE5A_W27", "VOICE5B_W27", "VOICE5C_W27", "VOICE5D_W27", "DRONE1_W27", "DRONE2_W27", "DRONE4A_W27", 
                 "DRONE4B_W27", "DRONE4C_W27", "DRONE4D_W27", "DRONE4E_W27"]

w29_key_question = {}
w29_key_fields = ["PERSDISCR_W29", "NOWSMK_NHIS_W29", "BLOODPR_W29", "DIFF1A_W29", "DIFF1B_W29", "DIFF1C_W29", 
 "DIFF1D_W29", "DIFF1E_W29", "MASC2_W29", "FEM2_W29", "MASC1F1_W29", "MASC2AF1_W29", "MASC2BF1_W29", 
 "FEM1F2_W29", "FEM2AF2_W29", "FEM2BF2_W29", "GOODJOBS_W29", "HELPHURTA_W29", "HELPHURTB_W29", 
 "HELPHURTC_W29", "HELPHURTD_W29", "HELPHURTE_W29", "HELPHURTF_W29", "HELPHURTG_W29", "TRANSGEND1_W29", 
 "SEENMASC_W29", "SEENFEM_W29", "MAN1A_W29", "MAN1B_W29", "MAN1C_W29", "MAN1D_W29", "MAN1E_W29", 
 "MESUM1_FA_W29", "MESUM1_FB_W29", "MESUM1_FC_W29", "MESUM1_FD_W29", "MESUM1_FE_W29", "MESUM1_FF_W29", 
 "MESUM2_FA_W29", "MESUM2_FB_W29", "MESUM2_FC_W29", "MESUM2_FD_W29", "MESUM2_FE_W29", "MESUM2_FF_W29", 
 "TRANSGEND2_W29", "TRANSGEND3_W29", "TRAITSA_W29", "TRAITSB_W29", "TRAITSC_W29", "TRAITSD_W29", 
 "TRAITSE_W29", "TRAITSF_W29", "BOYSF1A_W29", "BOYSF1B_W29", "BOYSF1C_W29", "BOYSF1D_W29", "GIRLSF2A_W29", 
 "GIRLSF2B_W29", "GIRLSF2C_W29", "GIRLSF2D_W29", "SPOUSESEX_W29", "HOOD_NHISA_W29", "HOOD_NHISB_W29", 
 "HOOD_NHISC_W29", "LOCALELECT_W29", "PARTICIPATEA_W29", "PARTICIPATEB_W29", "PARTICIPATEC_W29", 
 "S7_W29", "S12_W29", "S13_W29", "TALK_CPS_W29", "FAVORS_CPS_W29", "WORRYRET_W29", "WORRYBILL_W29", 
 "GOPDIRCT_W29", "DEMDIRCT_W29"]


w32_key_question = {}
w32_key_fields = ["SATLIFEA_W32", "SATLIFEB_W32", "SATLIFEC_W32", "SATLIFED_W32", "SATLIFEE_W32", "SOCTRUST_W32",
 "SOCTRUST2_W32", "SOCTRUST4_W32", "SOCTRUST5_W32", "COMMYRS_W32", "COMATTACH_W32", "FEELA_W32",
 "FEELB_W32", "FEELC_W32", "FEELD_W32", "INC_W32", "INCFUTURE_W32", "COMMIMPA_W32", "COMMIMPB_W32",
 "COMMIMPC_W32", "COMMIMPD_W32", "COMMIMPE_W32", "COMMIMPF_W32", "COMMIMPG_W32", "COMMIMPH_W32",
 "FAMNEAR_W32", "SUCCESSIMPA_W32", "SUCCESSIMPB_W32", "SUCCESSIMPC_W32", "SUCCESSIMPD_W32",
 "FEDSHAREA_W32", "FEDSHAREB_W32", "FEDSHAREC_W32", "LOCALPROBA_W32", "LOCALPROBB_W32",
 "LOCALPROBC_W32", "LOCALPROBD_W32", "LOCALPROBE_W32", "LOCALPROBF_W32", "LOCALPROBG_W32",
 "LOCALPROBH_W32", "LOCALPROBI_W32", "LOCALPROBJ_W32", "LOCALPROBK_W32", "LOCALPROBL_F1_W32",
 "LOCALPROBM_F2_W32", "JOBSFUTURE_W32", "HARASS1A_W32", "HARASS1B_W32", "HARASS1C_W32",
 "HARASS1D_W32", "HARASS2F1_W32", "HARASS3F2_W32", "HARASS4_W32", "HARASS5_W32", "GROWUPNEAR_W32",
 "LIFELOC_W32", "VALUEURBAN_W32", "VALUESUBURB_W32", "VALUERURAL_W32", "NEIGHKNOW_W32",
 "NEIGHINTERA_W32", "NEIGHINTERB_W32", "NEIGHINTERC_W32", "NEIGHINTERD_W32", "NEIGHKEYS_W32",
 "NEIGHKIDS_W32", "NEIGHSAMEA_W32", "NEIGHSAMEB_W32", "NEIGHSAMEC_W32", "IMMCOMM_W32",
 "IMMIMPACT_W32", "GROWUPUSR_W32", "COMTYPE2_W32", "CITYSIZE_W32", "SUBURBNEAR_W32", "PROBURBAN_W32",
 "PROBSUBURB_W32", "PROBRURAL_W32", "WANTMOVE_W32", "WILLMOVE_W32", "MOVEURBAN_W32", "MOVESUBURB_W32",
 "MOVERURAL_W32", "ETHNCMAJ_W32", "IMMCULT2_W32", "MARRFAM2_W32", "ECONFAIR2_W32", "WOMENOPPS_W32",
 "GOVT_ROLE_W32", "WHADVANT_W32", "GAYMARR2_W32", "ABORTION_W32", "ABORTIONRESTR_W32",
 "ABORTIONALLOW_W32", "CLASS_W32", "MISINFG_W32", "MISINFT_W32", "CREGION", "AGE", "SEX", "EDUCATION", "CITIZEN",
 "MARITAL", "RELIG", "RELIGATTEND", "POLPARTY", "INCOME", "POLIDEOLOGY", "RACE"]

w34_key_question = {}
w34_key_fields = ["SCI1_W34", "SCI2A_W34", "SCI2B_W34", "SCI2C_W34", "SCI3A_W34", "SCI3B_W34", "SCI3C_W34", "SCI4_W34", "SCI5_W34",
 "EAT1_W34", "EAT2_W34", "EAT3E_W34", "EAT3F_W34", "EAT3G_W34", "EAT3H_W34", "EAT3I_W34", "EAT3J_W34", "EAT3K_W34",
 "FUD22_W34", "FUD24_W34", "EAT5A_W34", "EAT5B_W34", "EAT5C_W34", "EAT5D_W34", "EAT6_W34", "FUD32_W34", "FUD33A_W34",
 "FUD33B_W34", "FUD35_W34", "FUD37A_W34", "FUD37B_W34", "FUD37C_W34", "FUD37D_W34", "MED1_W34", "MED2A_W34", "MED2B_W34",
 "MED2C_W34", "MED2D_W34", "MED2E_W34", "MED2F_W34", "MED2G_W34", "MED3_W34", "MED4A_W34", "MED4B_W34", "MED4C_W34",
 "MED5_W34", "MED6A_W34", "MED6B_W34", "MED6C_W34", "MED6D_W34", "MED6E_W34", "MED7_W34", "BIOTECHA_W34", "BIOTECHB_W34",
 "BIOTECHC_W34", "BIOTECHD_W34", "BIOTECHE_W34", "EVOONE_W34", "EVOTWO_W34", "EVOTHREE_W34", "EVOPERS3_W34",
 "EVOPERS3A_W34", "EVOBIOA_W34", "EVOBIOB_W34", "BIO15_W34", "G1_W34", "G2_W34", "CREGION", "AGE", "SEX", "EDUCATION", "CITIZEN", 
 "MARITAL", "RELIG", "RELIGATTEND", "POLPARTY", "INCOME", "POLIDEOLOGY", "RACE"]

w36_key_question = {}
w36_key_fields = ["HAPPYLIFE_W36", "ESSENPOLF1A_W36", "ESSENPOLF1B_W36", "ESSENPOLF1C_W36", "ESSENPOLF1D_W36","ESSENPOLF1E_W36", "ESSENPOLF1F_W36", "ESSENPOLF1G_W36", "ESSENPOLF1H_W36", "ESSENPOLF1I_W36", "ESSENBIZF2A_W36", "ESSENBIZF2B_W36", "ESSENBIZF2C_W36", "ESSENBIZF2D_W36", "ESSENBIZF2E_W36","ESSENBIZF2F_W36", "ESSENBIZF2G_W36", "ESSENBIZF2H_W36", "ESSENBIZF2I_W36", "ESSENBIZF2J_W36", "ESSENBIZF2K_W36", "ESSENBIZF2L_W36", "STYLE1_W36", "STYLE2_W36", "AMNTWMNPF1_W36", "AMNTWMNP2F1_W36",
 "AMNTWMNBF1_W36", "AMNTWMNB2F1_W36", "EASIERBIZF2_W36", "EASIERPOLF2_W36","EQUALPOLF2_W36", "EQUALBIZF2_W36", "IMPROVE1_W36", "IMPROVE2_W36", "IMPROVE3_W36", "WHYNOTPOLF1A_W36", "WHYNOTPOLF1B_W36",
 "WHYNOTPOLF1C_W36", "WHYNOTPOLF1D_W36", "WHYNOTPOLF1E_W36", "WHYNOTPOLF1F_W36", "WHYNOTPOLF1G_W36",
 "WHYNOTPOLF1H_W36", "WHYNOTPOLF1I_W36", "WHYNOTPOLF1J_W36", "WHYNOTPOLF1K_W36", "WHYNOTPOLF1L_W36",
 "WHYNOTBIZF2A_W36", "WHYNOTBIZF2B_W36", "WHYNOTBIZF2C_W36", "WHYNOTBIZF2D_W36", "WHYNOTBIZF2F_W36",
 "WHYNOTBIZF2G_W36", "WHYNOTBIZF2H_W36", "WHYNOTBIZF2I_W36", "WHYNOTBIZF2J_W36", "WHYNOTBIZF2K_W36",
 "WHYNOTBIZF2L_W36", "WHYNOTBIZF2M_W36", "WHYNOTBIZF2N_W36", "WHYNOTBIZF2O_W36", "HIGHED_W36",
 "HIGHEDWRNGA_W36", "HIGHEDWRNGB_W36", "HIGHEDWRNGC_W36", "HIGHEDWRNGD_W36", "HIGHEDWRNGS_W36",
 "BETTERPOL1F1A_W36", "BETTERPOL1F1B_W36", "BETTERPOL1F1C_W36", "BETTERPOL1F1D_W36", "BETTERPOL1F1E_W36",
 "BETTERPOL1F1F_W36", "BETTERPOL1F1G_W36", "BETTERPOL1F1H_W36", "BETTERPOL1F1I_W36", "BETTERPOL2F1A_W36",
 "BETTERPOL2F1B_W36", "BETTERPOL2F1C_W36", "BETTERPOL2F1D_W36", "BETTERPOL2F1E_W36", "BETTERPOL2F1F_W36",
 "BETTERBIZ1F2A_W36", "BETTERBIZ1F2B_W36", "BETTERBIZ1F2C_W36", "BETTERBIZ1F2D_W36", "BETTERBIZ1F2E_W36",
 "BETTERBIZ1F2F_W36", "BETTERBIZ1F2G_W36", "BETTERBIZ1F2H_W36", "BETTERBIZ1F"]

w41_key_question = {}
w41_key_fields = ["OPTIMIST_W41", "AVGFAM_W41", "HAPPENa_W41", "HAPPENb_W41", "HAPPENc_W41", "HAPPENd_W41",
 "HAPPENe_W41", "HAPPENf_W41", "HAPPENg_W41", "HAPPENhF1_W41", "HAPPENiF2_W41", "HAPPENj_W41",
 "HAPPEN2a_W41", "HAPPEN2b_W41", "HAPPEN2c_W41", "HAPPEN2d_W41", "HAPPEN2e_W41", "HAPPEN2f_W41",
 "HAPPEN2g_W41", "HAPPEN2h_W41", "NATDEBT_W41", "ENVC_W41", "POPPROB_W41", "FTRWORRYa_W41",
 "FTRWORRYb_W41", "FTRWORRYc_W41", "FTRWORRYd_W41", "FTRWORRYe_W41", "FTRWORRYf_W41", "ELDCARE_W41",
 "ELDFINANCEF1_W41", "ELDFINANCEF2_W41", "GOVPRIOa_W41", "GOVPRIOb_W41", "GOVPRIOc_W41", "GOVPRIOd_W41",
 "GOVPRIOe_W41", "GOVPRIOfF1_W41", "GOVPRIOgF1_W41", "GOVPRIOhF1_W41", "GOVPRIOiF1_W41", "GOVPRIOjF1_W41",
 "GOVPRIOkF2_W41", "GOVPRIOlF2_W41", "GOVPRIOmF2_W41", "GOVPRIOnF2_W41", "GOVPRIOoF2_W41", "WRKTRN1F1_W41",
 "WRKTRN1F2_W41", "JOBSECURITY_W41", "JOBBENEFITS_W41", "AUTOWKPLC_W41", "ROBWRK_W41", "ROBWRK2_W41",
 "AUTOLKLY_W41", "ROBIMPACTa_W41", "ROBIMPACTb_W41", "LEGALIMG_W41", "FUTRCLASSa_W41", "FUTRCLASSb_W41",
 "FUTRCLASSc_W41", "HARASS1F1a_W41", "HARASS1F1b_W41", "HARASS1F1c_W41", "HARASS1F1d_W41",
 "HARASS1NOWRKF2a_W41", "HARASS1NOWRKF2c_W41", "HARASS1NOWRKF2d_W41", "HARASS3F1_W41",
 "HARASS3NOWRKF2_W41", "HARASS4_W41", "HARASS5_W41", "ETHNCMAJMOD_W41", "AGEMAJ_W41", "INTRMAR_W41",
 "SSMONEY_W41", "SSCUT_W41", "FUTR_ABR_W41", "FUTR_DIV_W41", "FUTR_M_W41", "FUTR_K_W41", "SOLVPROBa_W41",
 "SOLVPROBb_W41", "SOLVPROBc_W41", "SOLVPROBdF1_W41", "SOLVPROBeF2_W41", "SOLVPROBf_W41", "SOLVPROBg_W41",
 "SOLVPROBh_W41", "SOLVPROBi_W41"]

w42_key_question = {}
w42_key_fields = ["PAST_W42", "FUTURE_W42", "SC1_W42", "CONFa_W42", "CONFb_W42", "CONFc_W42", "CONFd_F1_W42", "CONFd_F2_W42",
 "CONFe_W42", "CONFf_W42", "CONFg_W42", "POLICY1_W42", "POLICY2_W42", "POLICY3_W42", "RQ1_F1A_W42", "RQ2_F1A_W42",
 "RQ3_F1Aa_W42", "RQ3_F1Ab_W42", "RQ3_F1Ac_W42", "RQ3_F1Ad_W42", "RQ4_F1Aa_W42", "RQ4_F1Ab_W42", "RQ4_F1Ac_W42",
 "RQ4_F1Ad_W42", "RQ4_F1Ae_W42", "RQ5_F1A_W42", "RQ6_F1A_W42", "RQ7_F1A_W42", "RQ8_F1A_W42", "RQ1_F1B_W42",
 "RQ2_F1B_W42", "RQ3_F1Ba_W42", "RQ3_F1Bb_W42", "RQ3_F1Bc_W42", "RQ3_F1Bd_W42", "RQ4_F1Ba_W42", "RQ4_F1Bb_W42",
 "RQ4_F1Bc_W42", "RQ4_F1Bd_W42", "RQ4_F1Be_W42", "RQ5_F1B_W42", "RQ6_F1B_W42", "RQ7_F1B_W42", "RQ8_F1B_W42",
 "RQ1_F1C_W42", "RQ2_F1C_W42", "RQ3_F1Ca_W42", "RQ3_F1Cb_W42", "RQ3_F1Cc_W42", "RQ3_F1Cd_W42", "RQ4_F1Ca_W42",
 "RQ4_F1Cb_W42", "RQ4_F1Cc_W42", "RQ4_F1Cd_W42", "RQ4_F1Ce_W42", "RQ5_F1C_W42", "RQ6_F1C_W42", "RQ7_F1C_W42",
 "RQ8_F1C_W42", "PQ1_F2A_W42", "PQ2_F2A_W42", "PQ3_F2Aa_W42", "PQ3_F2Ab_W42", "PQ3_F2Ac_W42", "PQ3_F2Ad_W42",
 "PQ4_F2Aa_W42", "PQ4_F2Ab_W42", "PQ4_F2Ac_W42", "PQ4_F2Ad_W42", "PQ4_F2Ae_W42", "PQ5_F2A_W42", "PQ6_F2A_W42",
 "PQ7_F2A_W42", "PQ8_F2A_W42", "PQ1_F2B_W42", "PQ2_F2B_W42", "PQ3_F2Ba_W42", "PQ3_F2Bb_W42", "PQ3_F2Bc_W42",
 "PQ3_F2Bd_W42", "PQ4_F2Ba_W42", "PQ4_F2Bb_W42", "PQ4_F2Bc_W42", "PQ4_F2Bd_W42", "PQ4_F2Be_W42", "PQ5_F2B_W42",
 "PQ6_F2B_W42", "PQ7_F2B_W42", "PQ8_F2B_W42", "PQ1_F2C_W42", "PQ2_F2C_W42", "PQ3_F2Ca_W42", "PQ3_F2Cb_W42",
 "PQ3_F2Cc_W42", "PQ3_F2Cd_W42", "PQ4_F2Ca_W42", "PQ4_F2Cb_W42", "PQ4_F2Cc_W42", "PQ4_F2Cd_W42", "PQ4_F2Ce_W42",
 "PQ5_F2C_W42", "PQ6_F2C_W42", "PQ7_F2C_W42", "PQ8_F2C_W42", "SCM4a_W42", "SCM4b_W42", "Q6F1_W42", "Q7F1_W42",
 "Q8F1_W42", "Q9F1_W42", "Q6F2_W42", "Q7F2_W42", "Q8F2_W42", "Q9F2_W42", "SCM5a_W42", "SCM5b_W42", "SCM5c_W42",
 "SCM5d_W42", "SCM5e_W42", "SCM5f_W42", "SCM5g_W42", "SCM5h_W42", "SCM5i_W42", "SCM5j_W42", "SCM2_W42", "SCM3_W42",
 "POP1_W42", "POP2_W42", "POP3_W42", "CREGION", "AGE", "SEX", "EDUCATION", "CITIZEN", "MARITAL", "RELIG", "RELIGATTEND", "POLPARTY", "INCOME", "POLIDEOLOGY", "RACE"]

w43_key_question = {}
w43_key_fields = ["RACESURV1a_W43", "RACESURV1b_W43", "RACESURV1c_W43", "RACESURV1d_W43", "ADMISSIONa_W43", "ADMISSIONb_W43", "ADMISSIONc_W43", "ADMISSIONd_W43", "ADMISSIONe_W43", "ADMISSIONf_W43", "ADMISSIONg_W43", "ADMISSIONh_W43", "RACESURV2_W43", "RACESURV3_W43", "RACESURV4_W43", "RACESURV5a_W43", "RACESURV5b_W43", "RACESURV5c_W43", "RACESURV5d_W43", "RACESURV5e_W43", "RACESURV5f_W43", "RACESURV5g_W43", "RACESURV5h_W43", "RACESURV5i_W43", "RACESURV5j_W43", "RACESURV5k_W43", "RACESURV5l_W43", "RACESURV6_W43", "RACESURV7_W43", "RACESURV8_W43", "RACESURV9_W43", "RACESURV10_W43", "RACESURV11_W43", "RACESURV12_W43", "RACESURV13_W43", "RACATTN_W43", "RACESURV14_W43", "RACESURV15a_W43", "RACESURV15b_W43", "RACESURV16_W43", "RACESURV17_W43", "RACESURV18a_W43", "RACESURV18b_W43", "RACESURV18c_W43", "RACESURV18d_W43", "RACESURV18e_W43", "RACESURV18f_W43", "RACESURV19a_W43", "RACESURV19b_W43", "RACESURV19c_W43", "RACESURV19d_W43", "RACESURV19e_W43", "RACESURV19f_W43", "RACESURV20_W43", "RACESURV21_W43", "RACESURV22_W43", "RACESURV24_W43", "RACESURV25_W43", "RACESURV26_W43", "RACESURV27_W43", "IDIMPORT_W43", "RACESURV28a_W43", "RACESURV28b_W43", "RACESURV28c_W43", "RACESURV28d_W43", "RACESURV28e_W43", "RACESURV28f_W43", "RACESURV28g_W43", "RACESURV29a_W43", "RACESURV29b_W43", "RACESURV29c_W43", "RACESURV29d_W43", "RACESURV34a_W43", "RACESURV34b_W43", "RACESURV34c_W43", "RACESURV34d_W43", "RACESURV34e_W43", "RACESURV36_W43", "RACESURV37_W43", "RACESURV38_W43", "RACESURV40_W43", "RACESURV41_W43", "RACESURV44_W43", "RACESURV45_W43", "RACESURV47a_W43", "RACESURV47b_W43", "RACESURV47c_W43", "RACESURV47d_W43", "RACESURV47e_W43", "RACESURV47f_W43", "RACESURV48_W43", "RACESURV49_W43", "RACESURV50_W43", "RACESURV51_W43", "RACESURV52_W43", "RACESURV53a_W43", "RACESURV53b_W43", "RACESURV53c_W43", "RACESURV53d_W43", "RACESURV53e_W43", "RACESURV53f_W43", "RACESURV53g_W43"]

w45_key_question = {}
w45_key_fields = ["NEWS_PLATFORMg_W45", "NEWS_PLATFORMh_W45", "NEWSPREFV2_W45", "SOURCESKEPa_W45", "SOURCESKEPb_W45", "SOURCESKEPc_W45", "SOURCESKEPd_W45", "SOURCESKEPe_W45", "INFOCONFUSEa_W45", "INFOCONFUSEb_W45", "INFOCONFUSEc_W45", "INFOCONFUSEd_W45", "INFOCONFUSEe_W45", "INFOKNOWa_W45", "INFOKNOWb_W45", "INFOKNOWc_W45", "INFOKNOWd_W45", "INFOKNOWe_W45", "INFOOWNa_W45", "INFOOWNb_W45", "INFOOWNc_W45", "INFOOWNd_W45", "INFOOWNe_W45", "MEDIALOYAL3_W45", "LEAD_W45", "SEEK_W45", "INFORESTRICTa_W45", "INFORESTRICTb_W45", "INFORESTRICTc_W45", "INFORESTRICTd_W45", "INFORESTRICTe_W45", "INFOWHYa_W45", "INFOWHYb_W45", "INFOWHYc_W45", "INFOWHYd_W45", "INFOCREATEa_W45", "INFOCREATEb_W45", "INFOCREATEc_W45", "INFOCREATEd_W45", "INFOCREATEe_W45", "MADEUPOFT_W45", "MADEUPSHARE1_W45", "MADEUPSHARE2_W45", "MADEUPSHAREWHY_W45", "MADEUPTOPICa_W45", "MADEUPTOPICb_W45", "MADEUPTOPICc_W45", "MADEUPTOPICd_W45", "MADEUPTOPICe_W45", "MADEUPTOPICf_W45", "MADEUPLEVELa_W45", "MADEUPLEVELb_W45", "MADEUPRESa_W45", "MADEUPRESb_W45", "MADEUPRESc_W45", "MADEUPRESd_W45", "MADEUPRESe_W45", "MADEUPIMPa_W45", "MADEUPIMPb_W45", "MADEUPIMPc_W45", "MADEUPIMPd_W45", "MADEUPIMPe_W45", "MADEUPDIS_W45", "DISAVOID_W45", "SMSHARER_W45", "SMLIKESa_W45", "SMLIKESb_W45", "SMLIKESc_W45", "SMLIKESd_W45", "SMLIKESe_W45", "SMLIKESf_W45", "SMSHARE_W45", "MADEUPSMCLICK_W45", "MADEUPSMFOL1_W45", "MADEUPSMFOL2_W45", "ONLINESOURCE_W45", "DIGWDOG_3_W45", "NEWSPROBa_W45", "NEWSPROBb_W45", "NEWSPROBc_W45", "NEWSPROBd_W45", "NEWSPROBe_W45", "VIDOFT_W45", "MADEUPSOLVE_W45", "INFOCHALa_W45", "INFOCHALb_W45", "INFOCHALc_W45", "INFOCHALd_W45", "INFOCHALe_W45", "RESTRICTWHO_W45", "ACCCHECK_W45", "FCFAIR_W45", "WATCHDOG_1_W45", "WATCHDOG_3_W45", "SNSUSE_W45"]

w49_key_question = {}
w49_key_fields = ["SOCMEDIAUSEa_W49", "SOCMEDIAUSEb_W49", "SOCMEDIAUSEc_W49", "SOCMEDIAUSEd_W49",
 "ELECTFTGSNSINT_W49", "TALKDISASNSINT_W49", "TALKCMNSNSINT_W49", "SECUR1_W49",
 "PRIVACYNEWS1_W49", "HOMEASSIST1_W49", "HOMEASSIST2_W49", "HOMEASSIST3_W49",
 "HOMEASSIST4_W49", "HOMEASSIST5a_W49", "HOMEASSIST5b_W49", "HOMEIOT_W49",
 "FITTRACK_W49", "LOYALTY_W49", "DNATEST_W49", "TRACKCO1a_W49", "TRACKCO1b_W49",
 "CONCERNCO_W49", "BENEFITCO_W49", "CONTROLCO_W49", "UNDERSTANDCO_W49",
 "POSNEGCO_W49", "ANONYMOUS1CO_W49", "TRACKGOV1a_W49", "TRACKGOV1b_W49",
 "CONCERNGOV_W49", "BENEFITGOV_W49", "CONTROLGOV_W49", "UNDERSTANDGOV_W49",
 "POSNEGGOV_W49", "ANONYMOUS1GOV_W49", "CONCERNGRPa_W49", "CONCERNGRPb_W49",
 "CONCERNGRPc_W49", "CONCERNGRPd_W49", "CONCERNGRPe_W49", "CONCERNGRPf_W49",
 "CONTROLGRPa_W49", "CONTROLGRPb_W49", "CONTROLGRPc_W49", "CONTROLGRPd_W49",
 "CONTROLGRPe_W49", "CONTROLGRPf_W49", "PP1_W49", "PP2_W49", "PP3_W49", "PP4_W49",
 "PP5a_W49", "PP5b_W49", "PP5c_W49", "PP5d_W49", "PP5e_W49", "PP6a_W49", "PP6b_W49",
 "PP6c_W49", "PRIVACYREG_W49", "GOVREGV1_W49", "GOVREGV2_W49", "SHARE1_W49",
 "PWMAN_W49", "PWMAN2_W49", "SMARTPHONE_W49", "SMARTAPP_W49", "PUBLICDATA_W49",
 "RTBFa_W49", "RTBFb_W49", "RTBFc_W49", "RTBFd_W49", "RTDa_W49", "RTDb_W49",
 "RTDc_W49", "RTDd_W49", "PROFILE3_W49", "PROFILE5_W49", "DATAUSEa_W49",
 "DATAUSEb_W49", "DATAUSEc_W49", "DATAUSEd_W49", "DATAUSEe_W49", "DATAUSEf_W49",
 "FACE1_W49", "FACE2a_W49", "FACE2b_W49", "FACE2c_W49", "FACE3a_W49", "FACE3b_W49",
 "FACE3c_W49", "FACE4a_W49", "FACE4b_W49", "FACE4c_W49", "FACE4d_W49", "DB1a_W49",
 "DB1b_W49", "DB1c_W49"]

w50_key_question = {}
w50_key_fields = ["SATLIFEa_W50", "SATLIFEb_W50", "SATLIFEc_W50", "SATLIFEd_W50", "FAMSURV1_W50", 
 "FAMSURV2Ma_W50", "FAMSURV2Mb_W50", "FAMSURV2Mc_W50", "FAMSURV2Md_W50", "FAMSURV2Me_W50", 
 "FAMSURV2Wa_W50", "FAMSURV2Wb_W50", "FAMSURV2Wc_W50", "FAMSURV2Wd_W50", "FAMSURV2We_W50", 
 "FAMSURV3_W50", "FAMSURV4_W50", "FAMSURV5a_W50", "FAMSURV5b_W50", "FAMSURV5c_W50", 
 "FAMSURV5d_W50", "FAMSURV6_W50", "FAMSURV7_W50", "FAMSURV8_W50", "FAMSURV9a_W50", 
 "FAMSURV9b_W50", "FAMSURV9c_W50", "FAMSURV9e_W50", "FAMSURV10a_W50", "FAMSURV10b_W50", 
 "FAMSURV10c_W50", "FAMSURV10e_W50", "FAMSURV11W_W50", "FAMSURV11M_W50", "FAMSURV12_W50", 
 "MOTHER_W50", "FATHER_W50", "SIB_W50", "REMARR_W50", "ENG_W50", "LWPT_W50", "MAR2_W50", 
 "FAMSURV16_W50", "FAMSURV17_W50", "ADKIDS_W50", "PAR1_W50", "PAR2_W50", "ROMRELDUR_W50", 
 "MARRDUR_W50", "COHABDUR_W50", "LWPSP_W50", "FAMSURV18A_W50", "FAMSURV18B_W50", 
 "ROMRELSER_W50", "FAMSURV19_W50", "FAMSURV20_W50", "FAMSURV21_W50", "FAMSURV22a_W50", 
 "FAMSURV22b_W50", "FAMSURV22c_W50", "FAMSURV22d_W50", "FAMSURV22e_W50", "FAMSURV22f_W50", 
 "FAMSURV22g_W50", "FAMSURV23a_W50", "FAMSURV23b_W50", "FAMSURV23c_W50", "FAMSURV23d_W50", 
 "FAMSURV23e_W50", "FAMSURV23f_W50", "FAMSURV23g_W50", "MARRYPREF1_W50", "MARRYPREF2_W50", 
 "FAMSURV25_W50", "FAMSURV26a_W50", "FAMSURV26b_W50", "FAMSURV26c_W50", "FAMSURV26d_W50", 
 "FAMSURV27a_W50", "FAMSURV27b_W50", "FAMSURV27c_W50", "FAMSURV27d_W50", "FAMSURV28_W50", 
 "FAMSURV29_W50", "FAMSURV30a_W50", "FAMSURV30b_W50", "FAMSURV30c_W50", "FAMSURV30d_W50", 
 "FAMSURV30e_W50", "FAMSURV30f_W50", "E5MOD_W50", "FAMSURV32a_W50", "FAMSURV32b_W50", 
 "FAMSURV32c_W50", "FAMSURV32d_W50", "FAMSURV32e_W50", "FAMSURV33a_W50", "FAMSURV33b_W50", 
 "FAMSURV33c_W50", "FAMSURV33d_W50", "FAMSURV34A_W50", "FAMSURV34B_W50", "FAMSURV35a_W50", 
 "FAMSURV35b_W50", "FAMSURV35c_W50", "FAMSURV36a_W50", "FAMSURV36b_W50", "FAMSURV36c_W50", 
 "HAVEKIDS1_W50", "FAMSURV37_W50", "FAMSURV38a_W50", "FAMSURV38b_W50", "FAMSURV38c_W50", 
 "FAMSURV39_W50", "FAMSURV40_W50", "FAMSURV43_W50", "FAMSURV44_W50", "DNATEST_W50", 
 "DNA2a_W50", "DNA2b_W50", "DNA2c_W50", "DNA3a_W50", "DNA3b_W50", "DNA3c_W50", "DNA4_W50", 
 "DNA5_W50", "SPOUSESEX_W50", "ORIENTATIONMOD_W50"]

w54_key_question = {}
w54_key_fields = ["FIN_SIT_W54", "FIN_SITFUT_W54", "FIN_SITMOST_W54", "FIN_SITCOMM_W54", "FIN_SITGROWUP_W54", "JOBTRAIN_W54", "GOVPRIORITYa_W54", "GOVPRIORITYb_W54", "GOVPRIORITYc_W54", "GOVPRIORITYd_W54", "GOVPRIORITYe_W54", "GOVPRIORITYf_W54", "GOVRESP_a_W54", "GOVRESP_b_W54", "GOVRESP_c_W54", "GOVRESP_d_W54", "GOVRESP_e_W54", "GOVRESP_f_W54", "GOVRESP_g_W54", "GOVRESP_h_W54", "ECON1_W54", "ECON1B_W54", "ECON3_a_W54", "ECON3_b_W54", "ECON3_c_W54", "ECON3_d_W54", "ECON3_e_W54", "ECON3_f_W54", "ECON3_g_W54", "ECON3_h_W54", "ECON3_i_W54", "ECON4_a_W54", "ECON4_b_W54", "ECON4_c_W54", "ECON4_d_W54", "ECON4_e_W54", "ECON4_f_W54", "ECON4_g_W54", "ECON4_h_W54", "ECON4_i_W54", "INEQ1_W54", "INEQ2_W54", "INEQ3_W54", "INEQ4_a_W54", "INEQ4_b_W54", "INEQ4_c_W54", "INEQ4_d_W54", "INEQ4_e_W54", "INEQ5_a_W54", "INEQ5_b_W54", "INEQ5_c_W54", "INEQ5_d_W54", "INEQ5_e_W54", "INEQ5_f_W54", "INEQ5_g_W54", "INEQ5_h_W54", "INEQ5_i_W54", "INEQ5_j_W54", "INEQ5_k_W54", "INEQ5_l_W54", "INEQ5_m_W54", "INEQ6_W54", "INEQ7_W54", "INEQ8_a_W54", "INEQ8_b_W54", "INEQ8_c_W54", "INEQ8_d_W54", "INEQ8_e_W54", "INEQ8_f_W54", "INEQ8_g_W54", "INEQ8_h_W54", "INEQ8_i_W54", "INEQ8_j_W54", "INEQ9_W54", "INEQ10_W54", "INEQ11_W54", "ECON5_a_W54", "ECON5_b_W54", "ECON5_c_W54", "ECON5_d_W54", "ECON5_e_W54", "ECON5_f_W54", "ECON5_g_W54", "ECON5_h_W54", "ECON5_i_W54", "ECON5_j_W54", "ECON5_k_W54", "ECIMPa_W54", "ECIMPb_W54", "ECIMPc_W54", "ECIMPd_W54", "ECIMPe_W54", "ECIMPf_W54", "ECIMPg_W54", "ECIMPh_W54", "ECIMPi_W54", "ECIMPj_W54", "WORRY2a_W54", "WORRY2b_W54", "WORRY2c_W54", "WORRY2d_W54", "WORRY2e_W54", "FINANCEa_W54", "FINANCEb_W54", "FINANCEc_W54", "DEBTa_W54", "DEBTb_W54", "DEBTc_W54", "DEBTd_W54", "DEBTe_W54", "BENEFITSa_W54", "BENEFITSb_W54", "BENEFITSc_W54", "WORKHARD_W53", "POOREASY_W53", "ECONFAIR_W53"]

w82_key_question = {}
w82_key_fields = ["GAP21Q1_W82", "GAP21Q2_W82", "GAP21Q3_W82", "GAP21Q4_a_W82", "GAP21Q4_b_W82", 
"GAP21Q4_c_W82", "GAP21Q4_d_W82", "GAP21Q4_e_W82", "GAP21Q4_f_W82", "GAP21Q5_a_W82", 
"GAP21Q5_b_W82", "GAP21Q6_W82", "GAP21Q7_a_W82", "GAP21Q7_b_W82", "GAP21Q7_c_W82", 
"GAP21Q7_d_W82", "GAP21Q7_e_W82", "GAP21Q8_W82", "GAP21Q9_W82", "GAP21Q10_W82", 
"GAP21Q11_W82", "GAP21Q12_W82", "GAP21Q13_a_W82", "GAP21Q13_b_W82", "GAP21Q13_c_W82", 
"GAP21Q14_W82", "GAP21Q15_a_W82", "GAP21Q15_b_W82", "GAP21Q15_c_W82", "GAP21Q15_d_W82", 
"GAP21Q15_e_W82", "GAP21Q15_f_W82", "GAP21Q17_W82", "GAP21Q18_W82", "GAP21Q19_a_W82", 
"GAP21Q19_b_W82", "GAP21Q19_c_W82", "GAP21Q19_d_W82", "GAP21Q19_e_W82", "GAP21Q20_W82", 
"GAP21Q21_a_W82", "GAP21Q21_b_W82", "GAP21Q21_c_W82", "GAP21Q21_d_W82", "GAP21Q21_e_W82", 
"GAP21Q22_W82", "GAP21Q23_W82", "GAP21Q24_W82", "GAP21Q25_W82", "GAP21Q26_a_W82", 
"GAP21Q26_b_W82", "GAP21Q26_c_W82", "GAP21Q26_d_W82", "GAP21Q27_W82", "GAP21Q28_W82", 
"GAP21Q29_W82", "GAP21Q30_W82", "GAP21Q31_W82", "GAP21Q32_W82", "GAP21Q33_a_W82", 
"GAP21Q33_b_W82", "GAP21Q33_c_W82", "GAP21Q33_d_W82", "GAP21Q33_e_W82", "GAP21Q33_f_W82", 
"GAP21Q33_g_W82", "GAP21Q33_h_W82", "GAP21Q33_i_W82", "GAP21Q33_j_W82", "GAP21Q33_k_W82", 
"GAP21Q33_l_W82", "GAP21Q33_m_W82", "GAP21Q33_n_W82", "GAP21Q33_o_W82", "GAP21Q33_p_W82", 
"GAP21Q33_q_W82", "GAP21Q33_r_W82", "GAP21Q33_s_W82", "GAP21Q33_t_W82", "GAP21Q34_a_W82", 
"GAP21Q34_b_W82", "GAP21Q34_c_W82", "GAP21Q34_d_W82", "GAP21Q34_e_W82", "GAP21Q34_f_W82", 
"GAP21Q35_W82", "GAP21Q36_W82", "GAP21Q37_W82", "GAP21Q38_a_W82", "GAP21Q38_b_W82", 
"GAP21Q38_c_W82", "GAP21Q40_W82", "GAP21Q41_W82", "GAP21Q42_W82", "GAP21Q43_a_W82", 
"GAP21Q43_b_W82", "GAP21Q43_c_W82", "GAP21Q43_d_W82", "GAP21Q43_e_W82", "GAP21Q43_f_W82", 
"GAP21Q43_g_W82", "GAP21Q43_h_W82", "GAP21Q46_W82", "GAP21Q47_W82"]

w92_key_question = {}
w92_key_fields = ["POL1JB_W92", "LIFEFIFTY_W92", "BIGHOUSES_W92", "INSTN_CHR_W92", "INSTN_CLGS_W92", 
"INSTN_LGECRP_W92", "INSTN_MSCENT_W92", "INSTN_LBRUN_W92", "INSTN_K12_W92", "INSTN_BNKS_W92", 
"INSTN_TECHCMP_W92", "DIFFPARTY_W92", "GOVSIZE1_W92", "GOVSIZE2_W92", "GOVSIZE3_W92", 
"USEXCEPT_W92", "WOMENOBS_W92", "ECONFAIR_W92", "OPENIDEN_W92", "VTRGHTPRIV1_W92", 
"ALLIES_W92", "PEACESTR_W92", "GOVWASTE_W92", "COMPROMISEVAL_W92", "POORASSIST_W92", 
"PAR2CHILD_W92", "PAR2CHILDa_W92", "POLICY3MOD_W92", "WHADVANT_W92", "SUPERPWR_W92", 
"IL_IMM_PRI_W92", "BILLION_W92", "GLBLZE_W92", "FP_AUTH_W92", "GOVTHC_W92", 
"SNGLPYER_W92", "NOGOVTHC_W92", "FREECOLL_W92", "CRIM_SENT2_W92", "USMILSIZ_W92", 
"PROG_RRETRO_W92", "PROG_RNEED_W92", "PROG_RNEED2b_W92", "ELITEUNDMOD_W92", "POLINTOL2_a_W92", 
"POLINTOL2_b_W92", "CANQUALPOL_W92", "CANMTCHPOL_W92", "SOCIETY_TRANS_W92", "SOCIETY_RHIST_W92", 
"SOCIETY_JBCLL_W92", "SOCIETY_RELG_W92", "SOCIETY_WHT_W92", "SOCIETY_GUNS_W92", "SOCIETY_SSM_W92", 
"PROBOFF_a_W92", "PROBOFF_b_W92", "BUSPROFIT_W92", "CNTRYFAIR_W92", "GOVPROTCT_W92", 
"MARRFAM_W92", "GOVAID_W92", "RELIG_GOV_W92", "GOODEVIL_W92", "PPLRESP_W92", 
"RACESURV52MOD_W92", "ELECT_IMPT3_PRVFR_W92", "ELECT_IMPT3_PRVSUP_W92", "ELECT_CONF3_PRVFR_W92", 
"ELECT_CONF3_PRVSUP_W92", "CANDEXP_W92", "LEGALIMMIGAMT_W92", "UNIMMIGCOMM_W92", "GODMORALIMP_W92", 
"REPRSNTREP_W92", "REPRSNTDEM_W92", "VTRS_VALS_W92"]

opinion_qa_questions = {}
# Variable mappings for each year. 
mapping_2012 = {
    "dem_raceeth_x": "Race/Ethnicity",
    "gender_respondent_x": "Gender",
    "dem_age_r_x": "Age",
    "libcpre_self": "Liberal/Conservative",
    "pid_x": "Party",
    "paprofile_interestpolit": "Interest in Politics",
    "relig_church": "Church",
    "discuss_disc": "Political Discussion",
    "patriot_flag": "Flag-Patriotism",
    "sample_stfips": "State",}
mapping_2016 = {
    "V161310x": "Race/Ethnicity",
    "V161342": "Gender",
    "V161267": "Age",
    "V161126": "Liberal/Conservative",
    "V161158x": "Party",
    "V162256": "Interest in Politics",
    "V161244": "Church",
    "V162174": "Political Discussion",
    "V162125x": "Flag-Patriotism",
    "V161010d": "State",}
mapping_2020 = {
    "V201549x": "Race/Ethnicity",
    "V201600": "Gender",
    "V201507x": "Age",
    "V201200": "Liberal/Conservative",
    "V201231x": "Party",
    "V202406": "Interest in Politics",
    "V201452": "Church",
    "V202023": "Political Discussion",}

c_2012 = {
    "dem_raceeth_x": {
        1: "White, non-Hispanic",
        2: "Black, non-Hispanic",
        3: "Asian, native Hawaiian or other Pacific Islr,non-Hispanic",
        4: "Native American or Alaska Native, non-Hispanic",
        5: "Hispanic",
        6: "Other non-Hispanic incl multiple races",
        -9: "Missing"
    },
    "gender_respondent_x": {
        1: "Male",
        2: "Female",
    },
    "libcpre_self": {
        1: "Extremely liberal",
        2: "Liberal",
        3: "Slightly liberal",
        4: "Moderate, middle of the road",
        5: "Slightly conservative",
        6: "Conservative",
        7: "Extremely conservative",
        -2: "Haven’t thought much about this",
        -8: "Don’t know",
        -9: "Refused"
    },
    "pid_x": {
        1: "Strong Democrat",
        2: "Not very strong Democrat",
        3: "Independent-Democrat",
        4: "Independent",
        5: "Independent-Republican",
        6: "Not very strong Republican",
        7: "Strong Republican",
        -2: "Missing"
    },
    "paprofile_interestpolit": {
        1: "Very interested",
        2: "Somewhat interested",
        3: "Slightly interested",
        4: "Not at all interested",
        -1: "Inapplicable",
        -9: "Refused"
    },
    "relig_church": {
        1: "Yes",
        2: "No",
        -8: "Don’t know",
        -9: "Refused"
    },
    "discuss_disc": {
        1: "Yes",
        2: "No",
        -6: "No post-election interview",
        -7: "No post data, deleted due to incomplete IW",
        -8: "Don’t Know",
        -9: "Refused"
    },
    "patriot_flag": {
        1: "Extremely good",
        2: "Very good",
        3: "Moderately good",
        4: "Slightly good",
        5: "Not good at all",
        -6: "No post-election interview",
        -7: "Deleted due to partial (post-election) interview",
        -8: "Don't know",
        -9: "Refused"
    },
    "sample_stfips": {
        1: 'Alabama',
        2: 'Alaska',
        4: 'Arizona',
        5: 'Arkansas',
        6: 'California',
        8: 'Colorado',
        9: 'Connecticut',
        10: 'Delaware',
        11: 'District of Columbia',
        12: 'Florida',
        13: 'Georgia',
        15: 'Hawaii',
        16: 'Idaho',
        17: 'Illinois',
        18: 'Indiana',
        19: 'Iowa',
        20: 'Kansas',
        21: 'Kentucky',
        22: 'Louisiana',
        23: 'Maine',
        24: 'Maryland',
        25: 'Massachusetts',
        26: 'Michigan',
        27: 'Minnesota',
        28: 'Mississippi',
        29: 'Missouri',
        30: 'Montana',
        31: 'Nebraska',
        32: 'Nevada',
        33: 'New Hampshire',
        34: 'New Jersey',
        35: 'New Mexico',
        36: 'New York',
        37: 'North Carolina',
        38: 'North Dakota',
        39: 'Ohio',
        40: 'Oklahoma',
        41: 'Oregon',
        42: 'Pennsylvania',
        44: 'Rhode Island',
        45: 'South Carolina',
        46: 'South Dakota',
        47: 'Tennessee',
        48: 'Texas',
        49: 'Utah',
        50: 'Vermont',
        51: 'Virginia',
        53: 'Washington',
        54: 'West Virginia',
        55: 'Wisconsin',
        56: 'Wyoming',
    },
    'presvote2012_x': {
        1: 'Obama',
        2: 'Romney',
        5: 'Other candidate',
        -1: 'Inapplicable',
        -2: 'Missing',
        -6: 'Not asked, unit nonresponse (no post-election interview',
        -7: 'Deleted due to partial (post-election) interview',
        -9: 'Refused'
    }
}

c_2016 = {
    'V161310x': {
        1: "White, non-Hispanic",
        2: "Black, non-Hispanic",
        3: "Asian, native Hawaiian or other Pacific Islr,non-Hispanic",
        4: "Native American or Alaska Native, non-Hispanic",
        5: "Hispanic",
        6: "Other non-Hispanic incl multiple races",
        -2: "Missing"
    },
    'V161342': {
        1: "Male",
        2: "Female",
        3: "Other",
        -9: "Refused"
    },
    'V161126': {
        1: "Extremely liberal",
        2: "Liberal",
        3: "Slightly liberal",
        4: "Moderate, middle of the road",
        5: "Slightly conservative",
        6: "Conservative",
        7: "Extremely conservative",
        99: "Haven’t thought much about this",
        -8: "Don’t know",
        -9: "Refused"
    },
    'V161158x': {
        1: "Strong Democrat",
        2: "Not very strong Democrat",
        3: "Independent-Democrat",
        4: "Independent",
        5: "Independent-Republican",
        6: "Not very strong Republican",
        7: "Strong Republican",
        -8: "Don’t Know",
        -9: "Refused"
    },
    'V162256': {
        1: "Very interested",
        2: "Somewhat interested",
        3: "Not very interested",
        4: "Not at all interested",
        -6: "No post-election interview",
        -7: "No post data, deleted due to incomplete IW",
        -8: "Don’t know",
        -9: "Refused"
    },
    'V161244': {
        1: "Yes",
        2: "No",
        -8: "Don’t know",
        -9: "Refused"
    },
    'V162174': {
        1: "Yes",
        2: "No",
        -6: "No post-election interview",
        -7: "No post data, deleted due to incomplete IW",
        -9: "Refused"
    },
    'V162125x': {
        1: "Extremely good",
        2: "Moderately good",
        3: "A little good",
        4: "Neither good nor bad",
        5: "A little bad",
        6: "Moderately bad",
        7: "Extremely bad",
        -6: "No post-election interview",
        -7: "No post data, deleted due to incomplete IW",
        -9: "Refused"
    },
    'V161010d': {
        1: 'Alabama',
        2: 'Alaska',
        4: 'Arizona',
        5: 'Arkansas',
        6: 'California',
        8: 'Colorado',
        9: 'Connecticut',
        10: 'Delaware',
        11: 'District of Columbia',
        12: 'Florida',
        13: 'Georgia',
        15: 'Hawaii',
        16: 'Idaho',
        17: 'Illinois',
        18: 'Indiana',
        19: 'Iowa',
        20: 'Kansas',
        21: 'Kentucky',
        22: 'Louisiana',
        23: 'Maine',
        24: 'Maryland',
        25: 'Massachusetts',
        26: 'Michigan',
        27: 'Minnesota',
        28: 'Mississippi',
        29: 'Missouri',
        30: 'Montana',
        31: 'Nebraska',
        32: 'Nevada',
        33: 'New Hampshire',
        34: 'New Jersey',
        35: 'New Mexico',
        36: 'New York',
        37: 'North Carolina',
        38: 'North Dakota',
        39: 'Ohio',
        40: 'Oklahoma',
        41: 'Oregon',
        42: 'Pennsylvania',
        44: 'Rhode Island',
        45: 'South Carolina',
        46: 'South Dakota',
        47: 'Tennessee',
        48: 'Texas',
        49: 'Utah',
        50: 'Vermont',
        51: 'Virginia',
        53: 'Washington',
        54: 'West Virginia',
        55: 'Wisconsin',
        56: 'Wyoming',
    },
    'V162062x': {
        -9: 'Refused',
        -8: 'Don’t know',
        -2: 'Missing, no vote for Pres in Post/no Post and no vote for Pres in pre',
        5: 'Other candidates',
        1: 'Hillary Clinton',
        2: "Donald Trump",
        3: "Gary Johnson",
        4: "Jill Stein",
    }
}

c_2020 = {
    'V201549x': {
        -9: 'Refused',
        -8: 'Don’t know',
        1: 'White, non-Hispanic',
        2: 'Black, non-Hispanic',
        3: 'Hispanic',
        4: 'Asian or Native Hawaiian/other Pacific Islander, non-Hispanic',
        5: 'Native American/Alaska Native or other race, non-Hispanic',
        6: 'Multiple races, non-Hispanic'
    },
    'V201600': {
        -9: 'Refused',
        1: 'Male',
        2: 'Female'
    },
    'V201507x': {  
        -9: 'Refused',
        80: 'Age 80 or older'
    },
    'V201200': {
        -9: 'Refused',
        -8: 'Don’t know',
        1: 'Extremely liberal',
        2: 'Liberal',
        3: 'Slightly liberal',
        4: 'Moderate; middle of the road',
        5: 'Slightly conservative',
        6: 'Conservative',
        7: 'Extremely conservative',
        99: 'Haven’t thought much about this'
    },
    'V201231x': {
        -9: 'Refused',
        -8: 'Don’t know',
        1: 'Strong Democrat',
        2: 'Not very strong Democrat',
        3: 'Independent-Democrat',
        4: 'Independent',
        5: 'Independent-Republican',
        6: 'Not very strong Republican',
        7: 'Strong Republican'
    },
    'V202406': {
        -9: 'Refused',
        -8: 'Don’t know',
        -7: 'No post-election data, deleted due to incomplete interview',
        -6: 'No post-election interview',
        -5: 'Interview breakoff (sufficient partial IW)',
        1: 'Very interested',
        2: 'Somewhat interested',
        3: 'Not very interested',
        4: 'Not at all interested'
    },
    'V201452': {
        -9: 'Refused',
        -8: 'Don’t know',
        1: 'Yes',
        2: 'No'
    },
    'V202023': {
        -9: 'Refused',
        -7: 'No post-election data, deleted due to incomplete interview',
        -6: 'No post-election interview',
        -1: 'Inapplicable',
        0: 'Zero days',
        1: 'One day',
        2: 'Two days',
        3: 'Three days',
        4: 'Four days',
        5: 'Five days',
        6: 'Six days',
        7: 'Seven days'
    },
    'V202110x' : {
        -9: 'Refused',
        -8: 'Don’t know',
        -1: 'Inapplicable',
        1: 'Joe Biden',
        2: 'Donald Trump',
        3: "Jo Jorgensen",
        4: "Howie Hawkins",
        5: "Other candidate",
    }
}

# the outer list
participants_anes = []
participants_qa = []
participants_w26 = []
participants_w27 = []
participants_w29 = []
participants_w32 = []
participants_w34 = []
participants_w36 = []
participants_w41 = []
participants_w42 = []
participants_w43 = []
participants_w45 = []
participants_w49 = []
participants_w50 = []
participants_w54 = []
participants_w82 = []
participants_w92 = []
participants_global = []

# Get the directory of the current file (data_processor.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Go up two levels to the project root
project_root = os.path.dirname(os.path.dirname(current_dir))

# Construct the full path to the data file
file_path = os.path.join(project_root, 'persona_research/data', 'anes_timeseries_2012_rawdata.txt')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter='|')

    for row in reader:
        # participant_entry = {"Participant_" + str(reader.line_num - 1): []}
        # demographics dict
        # data_dict = {}
        h = Human (
            vote = c_2012["presvote2012_x"][int(row["presvote2012_x"].replace(" ", ""))],
            race = c_2012["dem_raceeth_x"][int(row["dem_raceeth_x"].replace(" ", ""))],
            year = 2012,
            gender = c_2012["gender_respondent_x"][int(row["gender_respondent_x"].replace(" ", ""))],
            age = row["dem_age_r_x"],
            view = c_2012["libcpre_self"][int(row["libcpre_self"].replace(" ", ""))],
            party = c_2012["pid_x"][int(row["pid_x"].replace(" ", ""))],
            interest = c_2012["paprofile_interestpolit"][int(row["paprofile_interestpolit"].replace(" ", ""))],
            church = c_2012["relig_church"][int(row["relig_church"].replace(" ", ""))],
            discuss_disc = c_2012["discuss_disc"][int(row["discuss_disc"].replace(" ", ""))],
            flag = c_2012["patriot_flag"][int(row["patriot_flag"].replace(" ", ""))],
            state = c_2012["sample_stfips"][int(row["sample_stfips"].replace(" ", ""))],
            number = reader.line_num - 1 
        )
        # for var in mapping_2012:
            # if var in row and var != "presvote2012_x" and var != "dem_age_r_x":
            #     data_dict[mapping_2012[var]] = c_2012[var][int(row[var].replace(" ", ""))]
        # data_dict[mapping_2012["dem_age_r_x"]] = row["dem_age_r_x"]
        # data_dict['year'] = '2012'
        # "Who did you vote for"
        # vote_dict = {"Who did you vote for": c_2012['presvote2012_x'][int(row.get("presvote2012_x").replace(" ", ""))]} 

        # Add dictionaries into a list for that participant in a dictionary
        # participant_entry["Participant_" + str(reader.line_num - 1)].extend([data_dict, vote_dict])

        # Add participant dict to outer list
        participants_anes.append(h)
        
# Get the directory of the current file (data_processor.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Go up two levels to the project root
project_root = os.path.dirname(os.path.dirname(current_dir))

# Construct the full path to the data file
file_path = os.path.join(project_root, 'persona_research/data', 'anes_timeseries_2016_rawdata.txt')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter='|')        

    for row in reader:
        # participant_entry = {"Participant_" + str(reader.line_num - 1): []}
        h = Human (
            vote = c_2016["V162062x"][int(row["V162062x"].replace(" ", ""))],
            race = c_2016["V161310x"][int(row["V161310x"].replace(" ", ""))],
            year = 2016,
            gender = c_2016["V161342"][int(row["V161342"].replace(" ", ""))],
            age = row["V161267"],
            view = c_2016["V161126"][int(row["V161126"].replace(" ", ""))],
            party = c_2016["V161158x"][int(row["V161158x"].replace(" ", ""))],
            interest = c_2016["V162256"][int(row["V162256"].replace(" ", ""))],
            church = c_2016["V161244"][int(row["V161244"].replace(" ", ""))],
            discuss_disc = c_2016["V162174"][int(row["V162174"].replace(" ", ""))],
            flag = c_2016["V162125x"][int(row["V162125x"].replace(" ", ""))],
            state = c_2016["V161010d"][int(row["V161010d"].replace(" ", ""))],
            number = reader.line_num - 1 
        )
        # demographics dict
        # data_dict = {}
        # for var in mapping_2016:
        #     if var in row and var != "V162062x" and var != "V161267":
        #         data_dict[mapping_2016[var]] = c_2016[var][int(row[var].replace(" ", ""))]
        # data_dict[mapping_2016["V161267"]] = row["V161267"]
        # data_dict['year'] = '2016'
        # # "Who did you vote for"
        # vote_dict = {"Who did you vote for": c_2016['V162062x'][int(row.get("V162062x").replace(" ", ""))]} 

        # # Add dictionaries into a list for that participant in a dictionary
        # participant_entry["Participant_" + str(reader.line_num - 1)].extend([data_dict, vote_dict])

        # # Add participant dict to outer list
        participants_anes.append(h)
# Get the directory of the current file (data_processor.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Go up two levels to the project root
project_root = os.path.dirname(os.path.dirname(current_dir))

# Construct the full path to the data file
file_path = os.path.join(project_root, 'persona_research/data', 'anes_timeseries_2020_csv_20220210.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')  
    
    for row in reader:
        # participant_entry = {"Participant_" + str(reader.line_num - 1): []}
        h = Human (
            vote = c_2020["V202110x"][int(row["V202110x"].replace(" ", ""))],
            race = c_2020["V201549x"][int(row["V201549x"].replace(" ", ""))],
            year = 2020,
            gender = c_2020["V201600"][int(row["V201600"].replace(" ", ""))],
            age = row["V201507x"],
            view = c_2020["V201200"][int(row["V201200"].replace(" ", ""))],
            party = c_2020["V201231x"][int(row["V201231x"].replace(" ", ""))],
            interest = c_2020["V202406"][int(row["V202406"].replace(" ", ""))],
            church = c_2020["V201452"][int(row["V201452"].replace(" ", ""))],
            discuss_disc = c_2020["V202023"][int(row["V202023"].replace(" ", ""))],
            number = reader.line_num - 1 
        )        
        # demographics dict
        # data_dict = {}
        # for var in mapping_2020:
        #     if var in row and var != "V202110x" and var != "V201507x":
        #         data_dict[mapping_2020[var]] = c_2020[var][int(row[var].replace(" ", ""))]
        # data_dict[mapping_2020["V201507x"]] = row["V201507x"]
        # data_dict['year'] = '2020'
        # # "Who did you vote for"
        # vote_dict = {"Who did you vote for": c_2020['V202110x'][int(row.get("V202110x").replace(" ", ""))]} 

        # # Add dictionaries into a list for that participant in a dictionary
        # participant_entry["Participant_" + str(reader.line_num - 1)].extend([data_dict, vote_dict])

        # Add participant dict to outer list
        participants_anes.append(h)
        
# Get the directory of the current file (data_processor.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'questions_w26.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        #create key-question dict
        w26_key_question[row["key"]] = [row["question"], row["options"]]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'responses_w26.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    question_keys = list(w26_key_question.keys())
    question_keys.extend([
        "RACE",
        "POLIDEOLOGY",
        "INCOME",
        "POLPARTY",
        "RELIGATTEND",
        "RELIG",
        "MARITAL",
        "CITIZEN",
        "EDUCATION",
        "SEX",
        "AGE",
        "CREGION"
    ])
    for row in reader:
        kwargs = {key: row[key] for key in question_keys if key in row}
        if len(kwargs) == len(question_keys):
            human = HumanW26(**kwargs)
            participants_w26.append(human)
        # else:
        #     print(f"Row is missing data.")
        

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'questions_w27.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        #create key-question dict
        w27_key_question[row["key"]] = [row["question"], row["options"]]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'responses_w27.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    question_keys = list(w27_key_question.keys())
    question_keys.extend([
        "RACE",
        "POLIDEOLOGY",
        "INCOME",
        "POLPARTY",
        "RELIGATTEND",
        "RELIG",
        "MARITAL",
        "CITIZEN",
        "EDUCATION",
        "SEX",
        "AGE",
        "CREGION"
    ])
    for row in reader:
        kwargs = {key: row[key] for key in question_keys if key in row}
        if len(kwargs) == len(question_keys):
            human = HumanW27(**kwargs)
            participants_w27.append(human)  
        # else:
        #     print(f"Row is missing data.")


current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'questions_w29.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        #create key-question dict
        w29_key_question[row["key"]] = [row["question"], row["options"]]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'responses_w29.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    question_keys = list(w29_key_question.keys())
    question_keys.extend([
        "RACE",
        "POLIDEOLOGY",
        "INCOME",
        "POLPARTY",
        "RELIGATTEND",
        "RELIG",
        "MARITAL",
        "CITIZEN",
        "EDUCATION",
        "SEX",
        "AGE",
        "CREGION"
    ])
    for row in reader:
        kwargs = {key: row[key] for key in question_keys if key in row}
        if len(kwargs) == len(question_keys):
            human = HumanW29(**kwargs)
            participants_w29.append(human)  
        # else:
        #     print(f"Row is missing data.")

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'questions_w32.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        #create key-question dict
        w32_key_question[row["key"]] = [row["question"], row["options"]]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'responses_w32.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    question_keys = list(w32_key_question.keys())
    question_keys.extend([
        "RACE",
        "POLIDEOLOGY",
        "INCOME",
        "POLPARTY",
        "RELIGATTEND",
        "RELIG",
        "MARITAL",
        "CITIZEN",
        "EDUCATION",
        "SEX",
        "AGE",
        "CREGION"
    ])
    for row in reader:
        kwargs = {key: row[key] for key in question_keys if key in row}
        if len(kwargs) == len(question_keys):
            human = HumanW32(**kwargs)
            participants_w32.append(human)  
        # else:
        #     print(f"Row is missing data.")

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'questions_w34.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        #create key-question dict
        w34_key_question[row["key"]] = [row["question"], row["options"]]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'responses_w34.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    question_keys = list(w34_key_question.keys())
    question_keys.extend([
        "RACE",
        "POLIDEOLOGY",
        "INCOME",
        "POLPARTY",
        "RELIGATTEND",
        "RELIG",
        "MARITAL",
        "CITIZEN",
        "EDUCATION",
        "SEX",
        "AGE",
        "CREGION"
    ])
    for row in reader:
        kwargs = {key: row[key] for key in question_keys if key in row}
        if len(kwargs) == len(question_keys):
            human = HumanW34(**kwargs)
            participants_w34.append(human)  
        # else:
        #     print(f"Row is missing data.")

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'questions_w36.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        #create key-question dict
        w36_key_question[row["key"]] = [row["question"], row["options"]]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'responses_w36.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    question_keys = list(w36_key_question.keys())
    question_keys.extend([
        "RACE",
        "POLIDEOLOGY",
        "INCOME",
        "POLPARTY",
        "RELIGATTEND",
        "RELIG",
        "MARITAL",
        "CITIZEN",
        "EDUCATION",
        "SEX",
        "AGE",
        "CREGION"
    ])
    for row in reader:
        kwargs = {key: row[key] for key in question_keys if key in row}
        if len(kwargs) == len(question_keys):
            human = HumanW36(**kwargs)
            participants_w36.append(human)  
        # else:
        #     print(f"Row is missing data.")               

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'questions_w41.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        #create key-question dict
        w41_key_question[row["key"]] = [row["question"], row["options"]]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'responses_w41.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    question_keys = list(w41_key_question.keys())
    question_keys.extend([
        "RACE",
        "POLIDEOLOGY",
        "INCOME",
        "POLPARTY",
        "RELIGATTEND",
        "RELIG",
        "MARITAL",
        "CITIZEN",
        "EDUCATION",
        "SEX",
        "AGE",
        "CREGION"
    ])
    for row in reader:
        kwargs = {key: row[key] for key in question_keys if key in row}
        if len(kwargs) == len(question_keys):
            human = HumanW41(**kwargs)
            participants_w41.append(human)  
        # else:
        #     print(f"Row is missing data.")

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'questions_w42.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        #create key-question dict
        w42_key_question[row["key"]] = [row["question"], row["options"]]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'responses_w42.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    question_keys = list(w42_key_question.keys())
    question_keys.extend([
        "RACE",
        "POLIDEOLOGY",
        "INCOME",
        "POLPARTY",
        "RELIGATTEND",
        "RELIG",
        "MARITAL",
        "CITIZEN",
        "EDUCATION",
        "SEX",
        "AGE",
        "CREGION"
    ])
    for row in reader:
        kwargs = {key: row[key] for key in question_keys if key in row}
        if len(kwargs) == len(question_keys):
            human = HumanW42(**kwargs)
            participants_w42.append(human)  
        # else:
        #     print(f"Row is missing data.")

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'questions_w43.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        #create key-question dict
        w43_key_question[row["key"]] = [row["question"], row["options"]]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'responses_w43.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    question_keys = list(w43_key_question.keys())
    question_keys.extend([
        "RACE",
        "POLIDEOLOGY",
        "INCOME",
        "POLPARTY",
        "RELIGATTEND",
        "RELIG",
        "MARITAL",
        "CITIZEN",
        "EDUCATION",
        "SEX",
        "AGE",
        "CREGION"
    ])
    for row in reader:
        kwargs = {key: row[key] for key in question_keys if key in row}
        if len(kwargs) == len(question_keys):
            human = HumanW43(**kwargs)
            participants_w43.append(human)  
        # else:
        #     print(f"Row is missing data.")

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'questions_w45.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        #create key-question dict
        w45_key_question[row["key"]] = [row["question"], row["options"]]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'responses_w45.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    question_keys = list(w45_key_question.keys())
    question_keys.extend([
        "RACE",
        "POLIDEOLOGY",
        "INCOME",
        "POLPARTY",
        "RELIGATTEND",
        "RELIG",
        "MARITAL",
        "CITIZEN",
        "EDUCATION",
        "SEX",
        "AGE",
        "CREGION"
    ])
    for row in reader:
        kwargs = {key: row[key] for key in question_keys if key in row}
        if len(kwargs) == len(question_keys):
            human = HumanW45(**kwargs)
            participants_w45.append(human)  
        # else:
        #     print(f"Row is missing data.")

# with open('data/questions_w49.csv', mode='r', errors='ignore') as file:
#     reader = csv.DictReader(file, delimiter=',')
#     for row in reader:
#         #create key-question dict
#         w49_key_question[row["key"]] = [row["question"], row["options"]]

# with open('data/responses_w49.csv', mode='r', errors='ignore') as file:
#     reader = csv.DictReader(file, delimiter=',')
#     question_keys = list(w49_key_question.keys())
#     question_keys.extend([
#         "RACE",
#         "POLIDEOLOGY",
#         "INCOME",
#         "POLPARTY",
#         "RELIGATTEND",
#         "RELIG",
#         "MARITAL",
#         "CITIZEN",
#         "EDUCATION",
#         "SEX",
#         "AGE",
#         "CREGION"
#     ])
#     for row in reader:
#         kwargs = {key: row[key] for key in question_keys if key in row}
#         if len(kwargs) == len(question_keys):
#             human = HumanW49(**kwargs)
#             participants_w49.append(human)  
#         else:
#             print(f"Row is missing data.")

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'questions_w50.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        #create key-question dict
        w50_key_question[row["key"]] = [row["question"], row["options"]]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'responses_w50.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    question_keys = list(w50_key_question.keys())
    question_keys.extend([
        "RACE",
        "POLIDEOLOGY",
        "INCOME",
        "POLPARTY",
        "RELIGATTEND",
        "RELIG",
        "MARITAL",
        "CITIZEN",
        "EDUCATION",
        "SEX",
        "AGE",
        "CREGION"
    ])
    for row in reader:
        kwargs = {key: row[key] for key in question_keys if key in row}
        if len(kwargs) == len(question_keys):
            human = HumanW50(**kwargs)
            participants_w50.append(human)  
        # else:
        #     print(f"Row is missing data.")

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'questions_w54.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        #create key-question dict
        w54_key_question[row["key"]] = [row["question"], row["options"]]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'responses_w54.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    question_keys = list(w54_key_question.keys())
    question_keys.extend([
        "RACE",
        "POLIDEOLOGY",
        "INCOME",
        "POLPARTY",
        "RELIGATTEND",
        "RELIG",
        "MARITAL",
        "CITIZEN",
        "EDUCATION",
        "SEX",
        "AGE",
        "CREGION"
    ])
    for row in reader:
        kwargs = {key: row[key] for key in question_keys if key in row}
        if len(kwargs) == len(question_keys):
            human = HumanW54(**kwargs)
            participants_w54.append(human)  
        # else:
        #     print(f"Row is missing data.")

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'global_opinions.csv')

with open(file_path, mode='r', errors='ignore') as file:            
        reader = csv.DictReader(file, delimiter=',') 
        for row in reader:
            country_dict = ast.literal_eval(row['selections'][28:][:-1])
            option_list = ast.literal_eval(row['options'])
            
            for key in country_dict.keys():
                h = HumanGlobal (
                    question = row['question'],
                    country = key,
                    option = option_list,
                    selection = country_dict[key]
                )
                participants_global.append(h)

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'questions_w82.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        #create key-question dict
        w82_key_question[row["key"]] = [row["question"], row["options"]]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'responses_w82.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    question_keys = list(w82_key_question.keys())
    question_keys.extend([
        "RACE",
        "POLIDEOLOGY",
        "INCOME",
        "POLPARTY",
        "RELIGATTEND",
        "RELIG",
        "MARITAL",
        "CITIZEN",
        "EDUCATION",
        "SEX",
        "AGE",
        "CREGION"
    ])
    for row in reader:
        kwargs = {key: row[key] for key in question_keys if key in row}
        if len(kwargs) == len(question_keys):
            human = HumanW82(**kwargs)
            participants_w82.append(human)  
        # else:
        #     print(f"Row is missing data.")

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'questions_w92.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        #create key-question dict
        w92_key_question[row["key"]] = [row["question"], row["options"]]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
file_path = os.path.join(project_root, 'persona_research/data', 'responses_w92.csv')

with open(file_path, mode='r', errors='ignore') as file:
    reader = csv.DictReader(file, delimiter=',')
    question_keys = list(w92_key_question.keys())
    question_keys.extend([
        "RACE",
        "POLIDEOLOGY",
        "INCOME",
        "POLPARTY",
        "RELIGATTEND",
        "RELIG",
        "MARITAL",
        "CITIZEN",
        "EDUCATION",
        "SEX",
        "AGE",
        "CREGION"
    ])
    for row in reader:
        kwargs = {key: row[key] for key in question_keys if key in row}
        if len(kwargs) == len(question_keys):
            human = HumanW92(**kwargs)
            participants_w92.append(human)  
        # else:
        #     print(f"Row is missing data.")

# A helper function that returns all the different questions that a country has answered
def globalHelperCountry(datas, country, key_question= "hello"):
    Result = []
    for data in datas:
        if key_question == data.question:
            continue 
        if data.country == country:
            Result.append(data)
    return Result

# A helper function that returns all the country that answered a specific question
def globalHelperQuestion(datas, question):
    Result = []
    for data in datas:
        if data.question == question:
            Result.append(data)
    return Result

# A helper function that returns all the questions of the data set
def globalQuestions(datas):
    Result = [] 
    for data in datas:
        if data.question not in Result:
            Result.append(data)
    return Result


