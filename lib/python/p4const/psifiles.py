#
#@BEGIN LICENSE
#
# PSI4: an ab initio quantum chemistry software package
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#@END LICENSE
#

# Do not modify this file! It is auto-generated by the document_psifiles
# script, from psi4topdir/include/psifiles.h
PSIF_OPTKING                =    1  # 
PSIF_GRAD                   =   11  # geometry optimization, geometry, and gradient; currently is an ASCII file like output.grad
PSIF_INTCO                  =   12  # internal coordinates file, currently is ASCII file like output.intco
PSIF_3INDEX                 =   16  # 
PSIF_DSCF                   =   31  # 
PSIF_CHKPT                  =   32  # new libpsio checkpoint file number
PSIF_SO_TEI                 =   33  # 
PSIF_SO_PK                  =   34  # 
PSIF_OEI                    =   35  # 
PSIF_SO_ERF_TEI             =   36  # 
PSIF_SO_ERFC_TEI            =   37  # 
PSIF_SO_R12                 =   38  # 
PSIF_SO_R12T1               =   39  # 
PSIF_DERINFO                =   40  # 
PSIF_SO_PRESORT             =   41  # 
PSIF_OLD_CHKPT              =   42  # Until we have flexible PSIF_CHKPT this will store previous calculation info
PSIF_CIVECT                 =   43  # CI vector from DETCI along with string and determinant info
PSIF_AO_DGDBX               =   44  # B-field derivative AO integrals over GIAO Gaussians -- only bra-ket permutational symmetry holds
PSIF_AO_DGDBY               =   45  # 
PSIF_AO_DGDBZ               =   46  # 
PSIF_PSIMRCC_INTEGRALS      =   50  # 
PSIF_PSIMRCC_RESTART        =   51  # 
PSIF_MCSCF                  =   52  # 
PSIF_TPDM_HALFTRANS         =   53  # 
PSIF_DETCAS                 =   60  # 
PSIF_LIBTRANS_DPD           =   61  # libtrans: All transformed integrals in DPD format are sent here by default
PSIF_LIBTRANS_A_HT          =   62  # libtrans: Alpha half-transformed integrals in DPD format
PSIF_LIBTRANS_B_HT          =   63  # libtrans: Beta half-tranformed integrals in DPD format
PSIF_LIBDIIS                =   64  # Storage for libdiis
PSIF_DFT_GRID               =   65  # Storage for DFT/pseudospectral grid
PSIF_DF_TENSOR              =   66  # 
PSIF_PS_TENSOR              =   67  # 
PSIF_TPDM_PRESORT           =   71  # 
PSIF_MO_TEI                 =   72  # 
PSIF_MO_OPDM                =   73  # 
PSIF_MO_TPDM                =   74  # 
PSIF_MO_LAG                 =   75  # 
PSIF_AO_OPDM                =   76  # PSIF_AO_OPDM also contains AO Lagrangian
PSIF_AO_TPDM                =   77  # 
PSIF_DBOC                   =   78  # dboc:
PSIF_MO_R12                 =   79  # 
PSIF_MO_R12T2               =   80  # 
PSIF_MO_AA_TEI              =   81  # 
PSIF_MO_BB_TEI              =   82  # 
PSIF_MO_AB_TEI              =   83  # 
PSIF_MO_AA_TPDM             =   84  # 
PSIF_MO_BB_TPDM             =   85  # 
PSIF_MO_AB_TPDM             =   86  # 
PSIF_AA_PRESORT             =   87  # AA UHF twopdm presort file
PSIF_BB_PRESORT             =   88  # BB UHF twopdm presort file
PSIF_AB_PRESORT             =   89  # AB UHF twopdm presort file
PSIF_MO_HESS                =   90  # 
PSIF_CPHF                   =   91  # 
PSIF_SO_PKSUPER1            =   92  # 
PSIF_SO_PKSUPER2            =   93  # 
PSIF_HALFT0                 =   94  # 
PSIF_HALFT1                 =   95  # 
PSIF_DFSCF_A                =   96  # B Matrix containing 3-index tensor in AOs for use with DF-SCF
PSIF_DFSCF_BJ               =   97  # B Matrix containing 3-index tensor in AOs with J^-1/2 for use with DF-SCF
PSIF_DFSCF_K                =   98  # Exchange tensor for DF-SCF
PSIF_DFSCF_BJI              =   99  # The three-center integrals for DF-SCF
PSIF_CC_INFO                =  100  # 
PSIF_CC_OEI                 =  101  # 
PSIF_CC_AINTS               =  102  # 
PSIF_CC_BINTS               =  103  # 
PSIF_CC_CINTS               =  104  # 
PSIF_CC_DINTS               =  105  # 
PSIF_CC_EINTS               =  106  # 
PSIF_CC_FINTS               =  107  # 
PSIF_CC_DENOM               =  108  # 
PSIF_CC_TAMPS               =  109  # 
PSIF_CC_GAMMA               =  110  # 
PSIF_CC_MISC                =  111  # 
PSIF_CC_HBAR                =  112  # 
PSIF_CC_OEI_NEW             =  113  # 
PSIF_CC_GAMMA_NEW           =  114  # 
PSIF_CC_AINTS_NEW           =  115  # 
PSIF_CC_BINTS_NEW           =  116  # 
PSIF_CC_CINTS_NEW           =  117  # 
PSIF_CC_DINTS_NEW           =  118  # 
PSIF_CC_EINTS_NEW           =  119  # 
PSIF_CC_FINTS_NEW           =  120  # 
PSIF_CC_LAMBDA              =  121  # 
PSIF_CC_RAMPS               =  122  # 
PSIF_CC_LAMPS               =  123  # 
PSIF_CC_LR                  =  124  # 
PSIF_CC_DIIS_ERR            =  125  # 
PSIF_CC_DIIS_AMP            =  126  # 
PSIF_CC_TMP                 =  127  # 
PSIF_CC_TMP0                =  128  # 
PSIF_CC_TMP1                =  129  # 
PSIF_CC_TMP2                =  130  # 
PSIF_CC_TMP3                =  131  # 
PSIF_CC_TMP4                =  132  # 
PSIF_CC_TMP5                =  133  # 
PSIF_CC_TMP6                =  134  # 
PSIF_CC_TMP7                =  135  # 
PSIF_CC_TMP8                =  135  # 
PSIF_CC_TMP9                =  137  # 
PSIF_CC_TMP10               =  138  # 
PSIF_CC_TMP11               =  139  # 
PSIF_EOM_D                  =  140  # 
PSIF_EOM_CME                =  141  # 
PSIF_EOM_Cme                =  142  # 
PSIF_EOM_CMNEF              =  143  # 
PSIF_EOM_Cmnef              =  144  # 
PSIF_EOM_CMnEf              =  145  # 
PSIF_EOM_SIA                =  146  # 
PSIF_EOM_Sia                =  147  # 
PSIF_EOM_SIJAB              =  148  # 
PSIF_EOM_Sijab              =  149  # 
PSIF_EOM_SIjAb              =  150  # 
PSIF_EOM_R                  =  151  # holds residual
PSIF_CC_GLG                 =  152  # left-hand psi for g.s. parts of cc-density
PSIF_CC_GL                  =  153  # left-hand psi for e.s. parts of cc-density
PSIF_CC_GR                  =  154  # right-hand eigenvector for cc-density
PSIF_EOM_TMP1               =  155  # intermediates just for single contractions
PSIF_EOM_TMP0               =  156  # temporary copies of density
PSIF_EOM_TMP_XI             =  157  # intermediates for xi computation
PSIF_EOM_XI                 =  158  # xi = dE/dt amplitudes
PSIF_EOM_TMP                =  159  # intermediates used more than once
PSIF_CC3_HET1               =  160  # [H,e^T1]
PSIF_CC3_HC1                =  161  # [H,C1]
PSIF_CC3_HC1ET1             =  162  # [[H,e^T1],C1]
PSIF_CC3_MISC               =  163  # various intermediates needed in CC3 codes
PSIF_CC2_HET1               =  164  # [H,e^T1]
PSIF_SCF_MOS                =  180  # Save SCF orbitals for re-use later as guess, etc.
PSIF_DFMP2_AIA              =  181  # Unfitted three-index MO ints for DFMP2
PSIF_DFMP2_QIA              =  182  # Fitted-three index MO ints for DFMP2
PSIF_ADC                    =  183  # ADC
PSIF_ADC_SEM                =  184  # ADC
PSIF_SAPT_DIMER             =  190  # SAPT Two-Body Dimer
PSIF_SAPT_MONOMERA          =  191  # SAPT Two-Body Mon A
PSIF_SAPT_MONOMERB          =  192  # SAPT Two-Body Mon B
PSIF_SAPT_AA_DF_INTS        =  193  # SAPT AA DF Ints
PSIF_SAPT_AB_DF_INTS        =  194  # SAPT AB DF Ints
PSIF_SAPT_BB_DF_INTS        =  195  # SAPT BB DF Ints
PSIF_SAPT_AMPS              =  196  # SAPT Amplitudes
PSIF_SAPT_TEMP              =  197  # SAPT Temporary worlds fastest code file
PSIF_SAPT_LRINTS            =  198  # SAPT0 2-Body linear response LDA integrals
PSIF_SO_D1OEI               =  199  # Derivative OEIs are stored in file 199
PSIF_SO_D1ERI               =  200  # Derivative ERIs are stored in files 200, 201, 202, etc. File 200
PSIF_3B_SAPT_TRIMER         =  220  # SAPT Three-Body Trimer
PSIF_3B_SAPT_DIMER_AB       =  221  # SAPT Three-Body Dimer AB
PSIF_3B_SAPT_DIMER_AC       =  222  # SAPT Three-Body Dimer AC
PSIF_3B_SAPT_DIMER_BC       =  223  # SAPT Three-Body Dimer BC
PSIF_3B_SAPT_MONOMER_A      =  224  # SAPT Three-Body Mon A
PSIF_3B_SAPT_MONOMER_B      =  225  # SAPT Three-Body Mon B
PSIF_3B_SAPT_MONOMER_C      =  226  # SAPT Three-Body Mon C
PSIF_3B_SAPT_AA_DF_INTS     =  227  # 
PSIF_3B_SAPT_BB_DF_INTS     =  228  # 
PSIF_3B_SAPT_CC_DF_INTS     =  229  # 
PSIF_3B_SAPT_AMPS           =  230  # 
PSIF_DCC_IJAK               =  250  # CEPA/CC (ij|ak)
PSIF_DCC_IJAK2              =  251  # CEPA/CC (ij|ak)
PSIF_DCC_ABCI               =  252  # CEPA/CC (ia|bc)
PSIF_DCC_ABCI2              =  253  # CEPA/CC (ia|bc)
PSIF_DCC_ABCI3              =  254  # CEPA/CC (ia|bc)
PSIF_DCC_ABCI4              =  255  # CEPA/CC (ia|bc)
PSIF_DCC_ABCI5              =  256  # CEPA/CC (ia|bc)
PSIF_DCC_ABCD1              =  257  # CEPA/CC (ab|cd)+
PSIF_DCC_ABCD2              =  258  # CEPA/CC (ab|cd)-
PSIF_DCC_IJAB               =  259  # CEPA/CC (ij|ab)
PSIF_DCC_IAJB               =  260  # CEPA/CC (ia|jb)
PSIF_DCC_IJKL               =  261  # CEPA/CC (ij|kl)
PSIF_DCC_OVEC               =  262  # CEPA/CC old vectors for diis
PSIF_DCC_EVEC               =  263  # CEPA/CC error vectors for diis
PSIF_DCC_R2                 =  264  # CEPA/CC residual
PSIF_DCC_TEMP               =  265  # CEPA/CC temporary storage
PSIF_DCC_T2                 =  266  # CEPA/CC t2 amplitudes
PSIF_DCC_QSO                =  267  # DFCC 3-index integrals
PSIF_DCC_SORT_START         =  270  # CEPA/CC integral sort starting file number
PSIF_SAPT_CCD               =  271  # SAPT2+ CCD Utility File
PSIF_HESS                   =  272  # Hessian Utility File
PSIF_OCC_DPD                =  273  # OCC DPD
PSIF_OCC_DENSITY            =  274  # OCC Density
PSIF_OCC_IABC               =  275  # OCC out-of-core <IA|BC>
PSIF_DFOCC_INTS             =  276  # DFOCC Integrals
PSIF_DFOCC_AMPS             =  277  # DFOCC Amplitudes
PSIF_DFOCC_DENS             =  278  # DFOCC PDMs

