#!/usr/bin/python

import re
import os
import sys
debug = True

lines = sys.stdin.readlines()
lemma = sys.argv[1]

# INPUT:
# - lines contain a list of "%i:goal" where "%i" is the index of the goal
# - lemma contain the name of the lemma under scrutiny
# OUTPUT:
# - (on stdout) a list of ordered index separated by EOL


rank = []             # list of list of goals, main list is ordered by priority
maxPrio = 110
for i in range(0,maxPrio):
  rank.append([])

if lemma[0:7]=="Correct":
  print ("applying oracle to "+lemma)
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*KU\( ~sk_HN.*', line): rank[109].append(num)
    elif re.match('.*ST.*_.*', line): rank[109].append(num)
    elif re.match('.*St.*_.*', line): rank[109].append(num)
    elif re.match('.*KU\( ~k.*',line): rank[106].append(num)
    elif re.match('.*KU\( ~supi \)',line): rank[106].append(num)
    elif re.match('.*!UE.*',line): rank[100].append(num)
    elif re.match('.*!CN.*',line): rank[100].append(num)
    elif re.match('.*!Ltk.*',line): rank[100].append(num)
    elif re.match('.*!Pk.*',line): rank[100].append(num)
    elif re.match('.*!N2.*',line): rank[100].append(num)
    elif re.match('.*Sqn_HSS.*',line): rank[98].append(num)
    elif re.match('.*Sqn_UE.*',line): rank[97].append(num)
    elif re.match('.*KU\( aenc.*supi.*',line): rank[95].append(num)
    elif re.match('.*KU\( senc.*RAR.*',line): rank[94].append(num)
    elif re.match('.*KU\( f1\(~k.*',line): rank[92].append(num)
    elif re.match('.*KU\( f5\(~k.*',line): rank[90].append(num)
    elif re.match('.*RcvS.*', line): rank[80].append(num)


elif re.match('^GUTI_SRC_HO', lemma):
  print ("applying oracle to "+lemma)
  for line in lines:
    num = line.split(':')[0]

    if re.match('.*last.*', line): rank[100].append(num)
    elif re.match('.*\<\'MRU\',.*', line): rank[95].append(num)
    elif re.match('.*RcvS\(.*\<\'ho\_req\',.*', line): rank[90].append(num)
    else: rank[20].append(num)


elif lemma=='executability_HO_hkd':
  print ("applying oracle to "+lemma)
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*Init.*', line): rank[109].append(num)
    elif re.match('.*KU\( ~SUPI.*', line): rank[105].append(num)
    elif re.match('.*KU\( ~k.*', line): rank[105].append(num)
    elif re.match('.*KU\( ~sk_HN.*', line): rank[105].append(num)
    elif re.match('.*ST4_Reg.*', line): rank[100].append(num)
    elif re.match('.*St4_Reg.*', line): rank[100].append(num)
    elif re.match('.*St_3_UE.*', line): rank[100].append(num)
    elif re.match('.*PDU_Sess.*', line): rank[100].append(num)
    elif re.match('.*St_4.*', line): rank[90].append(num)
    elif re.match('.*!N2*', line): rank[80].append(num)
    elif re.match('.*!Xn*', line): rank[80].append(num)
    elif re.match('.*Sqn_HSS*', line): rank[80].append(num)
    elif re.match('.*Sqn_UE*', line): rank[79].append(num)
    elif re.match('.*RcvS*', line): rank[79].append(num)
    else: rank[20].append(num)


elif lemma=='executability_HO_hkd_vkd1':
  print ("applying oracle to "+lemma)
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*Init.*', line): rank[109].append(num)
    elif re.match('.*KU\( ~SUPI.*', line): rank[105].append(num)
    elif re.match('.*KU\( ~k.*', line): rank[105].append(num)
    elif re.match('.*KU\( ~sk_HN.*', line): rank[105].append(num)
    elif re.match('.*Horizontal.*', line): rank[100].append(num)
    elif re.match('.*Vertical.*', line): rank[100].append(num)
    elif re.match('.*Connect.*', line): rank[100].append(num)
    elif re.match('.*SessionHand.*', line): rank[100].append(num)
    elif re.match('.*Init\( .*', line): rank[100].append(num)
    elif re.match('.*=.*=.*', line): rank[95].append(num)
    elif re.match('.*<.*=.*', line): rank[95].append(num)
    elif re.match('.*St_5_SRAN.*', line): rank[93].append(num)
    elif re.match('.*ST4_Reg.*', line): rank[92].append(num)
    elif re.match('.*St4_Reg.*', line): rank[92].append(num)
    elif re.match('.*St_3_UE.*', line): rank[92].append(num)
    elif re.match('.*St_4.*', line): rank[90].append(num)
    elif re.match('.*St_1.*', line): rank[85].append(num)
    elif re.match('.*!N2*', line): rank[80].append(num)
    elif re.match('.*!Xn*', line): rank[80].append(num)
    elif re.match('.*Sqn_HSS*', line): rank[80].append(num)
    elif re.match('.*Sqn_UE*', line): rank[79].append(num)
    elif re.match('.*RcvS*', line): rank[78].append(num)
    elif re.match('.*PDU\_Session\( .*', line): rank[70].append(num)
    else: rank[20].append(num)



elif lemma=='executability_HO_hkd_vkd':
  print ("applying oracle to "+lemma)
  for line in lines:
    num = line.split(':')[0]

    if re.match('.*Handover.*Done\( .*', line): rank[100].append(num)
    elif re.match('.*Horizontal.*', line): rank[100].append(num)
    elif re.match('.*Vertical.*', line): rank[100].append(num)
    elif re.match('.*Connect.*', line): rank[100].append(num)
    elif re.match('.*Init\( .*', line): rank[100].append(num)
    elif re.match('.*=.*=.*', line): rank[95].append(num)
    elif re.match('.*<.*=.*', line): rank[95].append(num)
    elif re.match('.*St\_.*\_.*\( .*', line): rank[80].append(num)
    elif re.match('.*ST\_.*\_.*\( .*', line): rank[80].append(num)
    elif re.match('.*!UE\( .*', line): rank[95].append(num)
    elif re.match('.*!KU\( senc\(.*', line): rank[50].append(num)
    elif re.match('.*!KU\( KDF\(.*', line): rank[95].append(num)
    elif re.match('.*RcvS\( .*', line): rank[80].append(num)
    elif re.match('.*!KU\( \~TRAN.*', line): rank[50].append(num)
    elif re.match('.*!KU\( \~PDU\_SESSION\_ID.*', line): rank[50].append(num)
    elif re.match('.*!KU\( \~K\_AMF.*', line): rank[95].append(num)
    elif re.match('.*!KU\( \~SUPI.*', line): rank[95].append(num)
    elif re.match('.*!KU\( \~K\_SEAF.*', line): rank[95].append(num)
    elif re.match('.*PDU\_Session\( .*', line): rank[70].append(num)
    else: rank[20].append(num)




elif lemma == "executability_resync" or \
     lemma == "executability_desync":
  print ("applying oracle to "+lemma)
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*!KU\( ~k.*', line): rank[100].append(num)
    elif re.match('.*!HNet\(.*', line): rank[99].append(num)
    elif re.match('.*=.*=.*', line): rank[98].append(num)
    elif re.match('.*<.*=.*', line): rank[97].append(num)
    elif re.match('.*HSS_Resync_End\(.*', line): rank[96].append(num)
    elif re.match('.*!KU\( f5\(.*', line) or \
         re.match('.*!KU\( f5_star\(.*', line): rank[95].append(num)
    elif re.match('.*!KU\( ~sqn_root.*', line): rank[95].append(num)
    elif re.match('.*St_1_UE\(.*', line): rank[94].append(num)
    elif re.match('.*St_1_HSS\(.*', line): rank[94].append(num)
    elif re.match('.*St_2_SEAF\(.*', line): rank[94].append(num)
    elif re.match('.*St_3_SEAF\(.*', line): rank[94].append(num)
    elif re.match('.*Sqn_UE\(.*', line): rank[93].append(num)
    elif re.match('.*Sqn_HSS\(.*', line): rank[93].append(num)
    elif re.match('.*~~>.*', line): rank[92].append(num)
    elif re.match('.*!Ltk_Sym\(.*', line): rank[90].append(num)
    elif re.match('.*RcvS\(.*', line): rank[70].append(num)
    elif re.match('.*!KU\( KDF\(.*', line): rank[60].append(num)
    elif re.match('.*!KU\( f3\(.*', line): rank[50].append(num)
    elif re.match('.*!KU\( f1_star\(.*', line): rank[40].append(num)
    elif re.match('.*!KU\( f1\(.*', line): rank[30].append(num)
    elif re.match('.*!KU\( \(f5\(.*', line): rank[20].append(num)
    elif re.match('.*!KD\( \(f5\(.*', line): rank[20].append(num)
    elif re.match('.*!KU\( \(f5_star\(.*', line): rank[20].append(num)
    elif re.match('.*!KD\( \(f5_star\(.*', line): rank[20].append(num)



# SOURCES AND REUSE LEMMAS

elif lemma == "sqn_ue_invariance" or \
     lemma == "sqn_hss_invariance" or \
     lemma == "sqn_ue_src" or \
     lemma == "sqn_hss_src":
  print ("applying oracle to "+lemma)
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*Sqn_UE\(.*', line): rank[90].append(num)
    elif re.match('.*Sqn_HSS\(.*', line): rank[90].append(num)
    elif re.match('.*St_1_UE\(.*', line): rank[95].append(num)
    elif re.match('.*St_1_HSS\(.*', line): rank[95].append(num)


elif lemma == "sqn_ue_nodecrease":
  print ("applying oracle to "+lemma)
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*\(last\(#j.*', line): rank[100].append(num)
    elif re.match('.*Sqn_UE_Change\(.*', line): rank[90].append(num)
    elif re.match('.*\(#vr < #i\).*', line): rank[80].append(num)
    elif re.match('.*Sqn_UE\(.*count.1.*', line): rank[70].append(num)

elif lemma == "sqn_ue_unique":
  print ("applying oracle to "+lemma)
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*\(#vr < #i\).*', line): rank[95].append(num)



elif lemma == "anonymous_injectiveagreement_ue_seaf_kseaf_noKeyRev_noChanRev":
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*ST.*_.*', line): rank[109].append(num)
    elif re.match('.*St.*_.*', line): rank[109].append(num)
    elif re.match('.*KU\( ~k.*',line): rank[106].append(num)
    elif re.match('.*KU\( f1\(~k.*',line): rank[105].append(num)
    elif re.match('.*RcvS.*', line): rank[80].append(num)
    elif re.match('.*Commit.*', line): rank[70].append(num)





else:
    print ("not applying the rule")
    exit(0)

# Ordering all goals by ranking (higher first)
for listGoals in reversed(rank):
  for goal in listGoals:
    sys.stderr.write(goal)
    print (goal)
