for i in range(100):    
    local_filename=f"{i}/kernprof_output.txt"
    file = open(local_filename, "r")
    lines = file.readlines()
    # print(lines[115])

    # for line in lines:
    #     if "solver.solve()" in line:
    #         print(line)
    #         break

    #write a new line after the previous line
    file2 = open("kernprof_SolverIntro_solve_loop1.txt", "a")
    file2.write(f"{lines[23]}")
    file2.close()
    file.close()
