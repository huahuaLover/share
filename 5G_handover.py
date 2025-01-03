#!/usr/bin/python

import sys
import re

lines = sys.stdin.readlines()
lemma = sys.argv[1]

maxPriority = 101  # Maximum priority is 100

# List of ranks
rank = []
for i in range(0, maxPriority):
  rank.append([])

## SOURCES LEMMAS
if re.match('^GUTI', lemma):
  for line in lines:
    num = line.split(':')[0]

    if re.match('.*last.*', line): rank[100].append(num)
    elif re.match('.*\<\'MRU\',.*', line): rank[95].append(num)
    elif re.match('.*RcvS\(.*\<\'ho\_req\',.*', line): rank[90].append(num)
    else: rank[20].append(num)

## HELPER LEMMAS
elif re.match('^PDU', lemma):

  # PDU origin
  if (lemma == 'PDUorigin'):
    for line in lines:
      num = line.split(':')[0]

      if re.match('.*last.*', line): rank[100].append(num)
      elif re.match('.*PDU\_Session.*', line): rank[95].append(num)
      else: rank[20].append(num)

  # PDU arguments constant
  if (lemma == 'PDUargsconstant'):
    for line in lines:
      num = line.split(':')[0]

      if re.match('.*CreatePDUSession.*', line): rank[95].append(num)
      else: rank[20].append(num)

  # PDU identifier unique
  if (lemma == 'PDUidunique'):
    for line in lines:
      num = line.split(':')[0]

      if re.match('.*CreatePDUSession.*', line): rank[95].append(num)
      else: rank[20].append(num)

elif re.match('^Value', lemma):

  # Value origin
  if (lemma == 'ValueOrigin'):
    for line in lines:
      num = line.split(':')[0]

      if re.match('.*last.*', line): rank[100].append(num)
      elif re.match('.*St\_.\_UE\(.*', line): rank[95].append(num)
      else: rank[20].append(num)

  # Value reset
  if (lemma == 'ValueReset'):
    for line in lines:
      num = line.split(':')[0]

      if re.match('.*last.*', line): rank[100].append(num)
      elif re.match('.*St\_.\_UE\(.*', line): rank[95].append(num)
      else: rank[20].append(num)


## EXECUTABILITY LEMMAS
elif re.match('^executability\_', lemma):
  for line in lines:
    num = line.split(':')[0]

    if re.match('.*Handover.*Done\( .*', line): rank[100].append(num)
    elif re.match('.*SessionHandover.*', line): rank[100].append(num)
    elif re.match('.*bad.*', line): rank[100].append(num)
    elif re.match('.*good.*', line): rank[100].append(num)
    elif re.match('.*St\_1\_CN.*', line): rank[100].append(num)
    elif re.match('.*Horizontal.*', line): rank[100].append(num)
    elif re.match('.*Vertical.*', line): rank[100].append(num)
    elif re.match('.*Connect.*', line): rank[100].append(num)
    elif re.match('.*Init\( .*', line): rank[100].append(num)
    elif re.match('.*=.*=.*', line): rank[95].append(num)
    elif re.match('.*<.*=.*', line): rank[95].append(num)
    elif re.match('.*St\_.*\_.*\( .*', line): rank[80].append(num)
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

## AGREEMENT LEMMAS
elif re.match('^injectiveagreement\_', lemma):

  # Injective agreement of K_gNB (UE -> T-RAN)
  if (lemma == 'injectiveagreement_ue_tran_k_gnb'):
    for line in lines:
      num = line.split(':')[0]

      if re.match('.*RcvS\(.*\<\'ho\_req\_ack\.*', line): rank[100].append(num)
      elif re.match('.*!KU\( senc\(\<\'MRU\', \~K\_SEAF\>,.*K.*', line): rank[99].append(num)
      elif re.match('.*!KU\( senc\(\<\'ho\_init\', \~TRAN\_ID..*', line): rank[98].append(num)
      elif re.match('.*RcvS\(.*\<\'ho\_req\', \~TRAN\_ID.*', line): rank[99].append(num)
      elif re.match('.*Intermediate.*\<\'NH\', NH.*', line): rank[0].append(num)
      elif re.match('.*Intermediate.*', line): rank[98].append(num)
      elif re.match('.*!KU\( KDF\(KDF\(\~K\_SEAF.*', line): rank[98].append(num)
      elif re.match('.*!KU\( KDF\(\~K\_SEAF.*', line): rank[98].append(num)
      elif re.match('.*Commit', line): rank[100].append(num)
      elif re.match('.*St\_.\_UE\(.*MAX.*', line): rank[100].append(num)
      elif re.match('.*St\_.\_UE\( .*', line): rank[97].append(num)
      elif re.match('.*!KU\( \~K\_SEAF.*', line): rank[98].append(num)
      elif re.match('.*!KU\( \~SUPI.*', line): rank[98].append(num)
      else: rank[20].append(num)

  # Injective agreement of K_gNB (TRAN -> UE)
  elif (lemma == 'injectiveagreement_tran_ue_k_gnb'):
    for line in lines:
      num = line.split(':')[0]

      if re.match('.*!KU\( senc\(\'RRCReconfigurationComplete\',.*K.*', line): rank[85].append(num)
      elif re.match('.*!KU\( senc\(\<\'MRU\', \~K\_SEAF\>,.*K.*', line): rank[99].append(num)
      elif re.match('.*!KU\( senc\(\<\'ho\_init\', \~TRAN.*', line): rank[88].append(num)
      elif re.match('.*St\_.\_TRAN\( .*', line): rank[95].append(num)
      elif re.match('.*St\_.\_UE\( .*KDF\(.*', line): rank[89].append(num)
      elif re.match('.*Intermediate.*\<\'NH\', NH.*', line): rank[0].append(num)
      elif re.match('.*Intermediate.*', line): rank[96].append(num)
      elif re.match('.*RcvS\(.*\'sn\_status\_transfer.*', line): rank[84].append(num)
      elif re.match('.*Commit', line): rank[100].append(num)
      elif re.match('.*RcvS\(.*\<\'ho\_req\_ack\.*', line): rank[90].append(num)
      elif re.match('.*RcvS\(.*\<\'ho\_req\', \~TRAN\_ID.*', line): rank[90].append(num)
      elif re.match('.*!KU\( .*\~K\_SEAF\..*', line): rank[0].append(num)
      elif re.match('.*!KU\( KDF\(KDF\(KDF\(\~K\_SEAF.*', line): rank[95].append(num)
      elif re.match('.*!KU\( KDF\(KDF\(\~K\_SEAF.*', line): rank[95].append(num)
      elif re.match('.*!KU\( KDF\(\~K\_SEAF.*', line): rank[95].append(num)
      elif re.match('.*!KU\( \~K\_SEAF.*', line): rank[95].append(num)
      else: rank[20].append(num)

## SECRECY LEMMAS
elif re.match('^secret\_', lemma):

  if (lemma == 'secret_supi'):
    for line in lines:
      num = line.split(':')[0]

      if re.match('.*Secret.*', line): rank[90].append(num)
      elif re.match('.*!UE\( .*', line): rank[100].append(num)
      elif re.match('.*St\_.*\_.*', line): rank[90].append(num)
      elif re.match('.*!KU\( \~SUPI.*', line): rank[90].append(num)
      elif re.match('.*RcvS\( .*\~SUPI.*', line): rank[95].append(num)
      elif re.match('.*!KU\( senc\(\<\'MRU\', \~SUPI.*', line): rank[95].append(num)
      else: rank[20].append(num)

  elif (lemma == 'secret_k_seaf'):
    for line in lines:
      num = line.split(':')[0]

      if re.match('.*Secret.*', line): rank[90].append(num)
      elif re.match('.*!UE\( .*', line): rank[100].append(num)
      elif re.match('.*St\_.\_UE\(.*SEAF\.', line): rank[20].append(num)
      elif re.match('.*St\_.*\_UE*', line): rank[95].append(num)
      elif re.match('.*!UE\( .*', line): rank[90].append(num)
      elif re.match('.*!KU\( \~K\_SEAF.*', line): rank[90].append(num)
      elif re.match('.*RcvS\( .*\~K\_SEAF.*', line): rank[95].append(num)
      elif re.match('.*!KU\( senc\(\<\'MRU\', \~K\_SEAF.*', line): rank[95].append(num)
      else: rank[20].append(num)

  elif (lemma == 'secret_k_amf'):
    for line in lines:
      num = line.split(':')[0]

      if re.match('.*Secret.*', line): rank[100].append(num)
      elif re.match('.*X #k.*', line): rank[95].append(num)
      elif re.match('.*#j\. \(Create.*', line): rank[95].append(num)
      elif re.match('.*!UE\( .*', line): rank[95].append(num)
      elif re.match('.*KeyDerived\( .*', line): rank[90].append(num)
      elif re.match('.*!KU\( KDF\(\~K\_SEAF.*', line): rank[90].append(num)
      elif re.match('.*!KU\( \~K\_SEAF.*', line): rank[90].append(num)
      elif re.match('.*!KU\( \~SUPI.*', line): rank[90].append(num)
      elif re.match('.*RcvS\( .*\~K\_SEAF.*', line): rank[95].append(num)
      elif re.match('.*!KU\( senc\(\<\'MRU\', \~K\_SEAF.*', line): rank[95].append(num)
      elif re.match('.*!KU\( senc\(\<\'MRU\', \~SUPI.*', line): rank[95].append(num)
      elif re.match('.*Intermediate.*\<\'NH\', NH.*', line): rank[0].append(num)
      elif re.match('.*Intermediate.*', line): rank[95].append(num)
      elif re.match('.*!KU\( senc\(\<\'ho\_init\', \~SUPI.*', line): rank[95].append(num)
      elif re.match('.*RcvS\(.*\~SUPI.*', line): rank[95].append(num)
      else: rank[20].append(num)

  elif (lemma == 'secret_k_gnb'):
    for line in lines:
      num = line.split(':')[0]

      if re.match('.*Secret.*', line): rank[100].append(num)
      elif re.match('.*X #k.*', line): rank[95].append(num)
      elif re.match('.*#j\. \(Create.*', line): rank[95].append(num)
      elif re.match('.*!UE\( .*', line): rank[95].append(num)
      elif re.match('.*KeyDerived\( .*', line): rank[90].append(num)
      elif re.match('.*!KU\( KDF\(\~K\_SEAF.*', line): rank[90].append(num)
      elif re.match('.*!KU\( \~K\_SEAF.*', line): rank[90].append(num)
      elif re.match('.*!KU\( \~SUPI.*', line): rank[90].append(num)
      elif re.match('.*!KU\( .*\~K\_SEAF\..*', line): rank[0].append(num)
      elif re.match('.*RcvS\( .*\~K\_SEAF.*', line): rank[95].append(num)
      elif re.match('.*!KU\( senc\(\<\'MRU\', \~K\_SEAF.*', line): rank[95].append(num)
      elif re.match('.*!KU\( senc\(\<\'MRU\', \~SUPI.*', line): rank[95].append(num)
      elif re.match('.*!KU\( KDF\(KDF\(\~K\_SEAF.*', line): rank[95].append(num)
      elif re.match('.*Intermediate.*\<\'NH\', NH.*', line): rank[0].append(num)
      elif re.match('.*Intermediate.*', line): rank[95].append(num)
      elif re.match('.*!KU\( senc\(\<\'ho\_init\', \~SUPI.*', line): rank[95].append(num)
      elif re.match('.*RcvS\(.*\~SUPI.*', line): rank[95].append(num)
      else: rank[20].append(num)

  elif (lemma == 'secret_k_gnb_star'):
    for line in lines:
      num = line.split(':')[0]

      if re.match('.*Secret.*', line): rank[100].append(num)
      elif re.match('.*St\_.*\_UE.*MAX.*', line): rank[91].append(num)
      elif re.match('.*St\_.*\_UE.*SUPI\..*', line): rank[90].append(num)
      elif re.match('.*St\_.*\_UE*', line): rank[89].append(num)
      elif re.match('.*Bind\(.*SEAF\..*', line): rank[60].append(num)
      elif re.match('.*Bind\(.*', line): rank[91].append(num)
      elif re.match('.*X #k.*', line): rank[90].append(num)
      elif re.match('.*#j\. \(Create.*', line): rank[90].append(num)
      elif re.match('.*!UE\( .*', line): rank[95].append(num)
      elif re.match('.*KeyDerived\( .*', line): rank[90].append(num)
      elif re.match('.*!KU\( .*\~K\_SEAF\..*', line): rank[0].append(num)
      elif re.match('.*!KU\( KDF\(\~K\_SEAF.*', line): rank[90].append(num)
      elif re.match('.*!KU\( KDF\(KDF\(KDF\(\~K\_SEAF.*', line): rank[90].append(num)
      elif re.match('.*!KU\( \~K\_SEAF.*', line): rank[90].append(num)
      elif re.match('.*!KU\( \~SUPI.*', line): rank[90].append(num)
      elif re.match('.*!KU\( .*\~K\_SEAF\..*', line): rank[0].append(num)
      elif re.match('.*RcvS\( .*\~K\_SEAF.*', line): rank[95].append(num)
      elif re.match('.*!KU\( senc\(\<\'MRU\', \~K\_SEAF.*', line): rank[95].append(num)
      elif re.match('.*!KU\( senc\(\<\'MRU\', \~SUPI.*', line): rank[95].append(num)
      elif re.match('.*!KU\( KDF\(KDF\(\~K\_SEAF.*', line): rank[95].append(num)
      elif re.match('.*Intermediate.*\<\'NH\', NH.*', line): rank[0].append(num)
      elif re.match('.*Intermediate.*', line): rank[95].append(num)
      elif re.match('.*!KU\( senc\(\<\'ho\_init\', \~SUPI.*', line): rank[88].append(num)
      elif re.match('.*RcvS\(.*\~SUPI.*', line): rank[95].append(num)
      else: rank[20].append(num)

## UNEXPECTED LEMMAS
else:
  print "Unexpected lemma: {}".format(lemma)
  exit(0);

for goalList in reversed(rank):
  for goal in goalList:
    sys.stderr.write(goal)
    print goal
