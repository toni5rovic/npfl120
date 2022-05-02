sl = "/home/toni/repos/npfl120/hw08-tree-translation/parallel/sl.s"
hr = "/home/toni/repos/npfl120/hw08-tree-translation/parallel/hr.s"

with open(sl) as sl_file, open(hr) as hr_file, open(sl + ".mod", "w") as sl_out, open(hr + ".mod", "w") as hr_out:
    for i in range(149605):
        sl_line = sl_file.readline().strip()
        hr_line = hr_file.readline().strip()
        
        if sl_line == "" or len(sl_line) == 0:
            continue
        
        if hr_line == "" or len(hr_line) == 0:
            continue

        sl_out.write(sl_line + "\n")
        hr_out.write(hr_line + "\n")