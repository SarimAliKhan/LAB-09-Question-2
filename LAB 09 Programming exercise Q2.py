print("SARIM ALI KHAN")
print("18B-043-CS(A)")
print("LAB 09")
def stats(filename):
    infile = open(filename,'r')
    content = infile.read()
    infile.close()
    words = content.split()
    A_plus = 0
    A_minus = 0
    B_plus = 0
    B_minus = 0
    C_plus = 0
    C_minus = 0
    F = 0
    for i in words:
        if i == "A+":
            A_plus += 1
        elif i == "A-":
            A_minus += 1
        elif i == "B+":
            B_plus += 1
        elif i == "B-":
            B_minus += 1
        elif i == "C+":
            C_plus += 1
        elif i == "C-":
            C_minus += 1
        elif i == "F":
            F += 1
    print("\n",A_plus,"Students got A+\n",A_minus,"Students got A-\n"
          ,B_plus,"Students got B+\n",B_minus,"students got B-\n",C_plus,"Students got C+\n",C_minus,"students got C-\n",F,"students got F\n")





print(stats('sarim.txt'))

