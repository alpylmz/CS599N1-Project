python3 -m cProfile arm_manipulation_invdyn.py > pythonProfileUnsorted

python3 -m cProfile -s calls arm_manipulation_invdyn.py > pythonProfileSortedCalls

python3 -m cProfile -s cumtime arm_manipulation_invdyn.py > pythonProfileCumtime


python3 -m cProfile -s ncalls arm_manipulation_invdyn.py > pythonProfileNCalls

python3 -m cProfile -s pcalls arm_manipulation_invdyn.py > pythonProfilePcalls

python3 -m cProfile -s line arm_manipulation_invdyn.py > pythonProfileSortedLine

python3 -m cProfile -s nfl arm_manipulation_invdyn.py > pythonProfileNatural

python3 -m cProfile -s time arm_manipulation_invdyn.py > pythonProfileSortedTime

python3 -m cProfile -s tottime arm_manipulation_invdyn.py > pythonProfileTottime



