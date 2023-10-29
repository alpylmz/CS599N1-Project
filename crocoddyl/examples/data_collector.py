import os
import sys

#source_commands = ". /opt/ros/noetic/setup.bash; . /ws/devel/setup.bash"

#os.system(source_commands)

# open a folder called data if it does not exists:
if not os.path.exists("data"):
    os.makedirs("data")

#for i in range(100):
#    os.system("kernprof -l arm_manipulation_invdyn.py")


# run kernprof -l arm_manipulation_invdyn.py 100 times and save the output to a file
for i in range(100):

    # open folder i in folder data if it does not exist
    if not os.path.exists("data/" + str(i)):
        os.makedirs("data/" + str(i))
 
    os.system("kernprof -l arm_manipulation_invdyn.py > data/" + str(i) + "/kernprof_output.txt")
    os.system("python3 -m line_profiler arm_manipulation_invdyn.py.lprof > data/" + str(i) + "/line_profiler_output.txt")






