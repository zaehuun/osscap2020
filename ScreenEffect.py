




def WhenCrush():
    Carray=arrayScreen[:37]
    iCarray=Matrix(Carray)
    oCarray=Matrix(iCarray)
    draw_matrix(oCarray)
    time.sleep(0.5)

    for i in range(len(Carray)):
        for j in range(len(Carrary[0])):
            if (Carray[i][j]==5) or (Carray[i][j]==1):
                Carray[i][j]=0
    for i in range(11):
        for j in range(len(Carray)):            
            f0=Carray[j].index(0)
            e1=Carray[j][f0+1:].index(10)+f1+1
            Carray[j][f0-1]=0
            Carray[j][e1]=0
        iCarray=Matrix(Carray)
        oCarray=Matrix(iCarray)
        draw_matrix(oCarray)
        time.sleep(0.5)






