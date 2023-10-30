import numpy as np

time=[]
# percent=[]
sample_min=[]
sample_avg=[]
sample_max=[]
filename="kernprof_SolverIntro_solve_loop1.txt"
file = open(filename,'r')
lines=file.readlines()
n=0
for line in lines[:-1]:
    # print(line.split())
    # print(line.split()[2])
    # print(line.split()[4])
    # n+=1
    # if n>10:
    #     break
    time.append(float(line.split()[-1]))
    # percent.append(float(line.split()[4]))
    sample_min.append(float(line.split()[1]))
    sample_avg.append(float(line.split()[2]))
    sample_max.append(float(line.split()[3]))

file.close()

sample_min_min=np.min(sample_min)
sample_min_max=np.max(sample_min)
sample_min_avg=np.mean(sample_min)
sample_min_std=np.std(sample_min)

sample_avg_min=np.min(sample_avg)
sample_avg_max=np.max(sample_avg)
sample_avg_avg=np.mean(sample_avg)
sample_avg_std=np.std(sample_avg)

sample_max_min=np.min(sample_max)
sample_max_max=np.max(sample_max)
sample_max_avg=np.mean(sample_max)
sample_max_std=np.std(sample_max)

time_min=np.min(time)
time_max=np.max(time)
time_avg=np.mean(time)
time_std=np.std(time)

# percent_min=np.min(percent)
# percent_max=np.max(percent)
# percent_avg=np.mean(percent)
# percent_std=np.std(percent)

file2 = open("kernprof_SolverIntro_solve_loop1.txt",'a')
file2.write(f"Total time: time_min:{time_min}, time_max:{time_max}, time_avg:{time_avg}, time_std:{time_std}\n")
file2.write(f"sample_min_min:{sample_min_min}, sample_min_max:{sample_min_max}, sample_min_avg:{sample_min_avg}, sample_min_std:{sample_min_std}\n")
file2.write(f"sample_avg_min:{sample_avg_min}, sample_avg_max:{sample_avg_max}, sample_avg_avg:{sample_avg_avg}, sample_avg_std:{sample_avg_std}\n")
file2.write(f"sample_max_min:{sample_max_min}, sample_max_max:{sample_max_max}, sample_max_avg:{sample_max_avg}, sample_max_std:{sample_max_std}\n")
# file2.write(f"percent_min:{percent_min}, percent_max:{percent_max}, percent_avg:{percent_avg}, percent_std:{percent_std}\n")
file2.close()

# str="   119         1     415187.8 415187.8     21.6      solver.solve()"
# print(str.split())