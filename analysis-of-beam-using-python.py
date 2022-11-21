def start():
    from fpdf import FPDF
    print("--------------------------------------------------------------------------------------------------")
    print("       Claperon's Theorem of Three Moments")
    print("--------------------------------------------------------------------------------------------------")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* INDEX -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("--------------------------------------------------------------------------------------------------")
    print("              1. Two Span Beam")
    print("              2. Three Span Beam")
    print("")
    print("                                                                   Guided By : - Prof.P.B.Kulkarni")
    print("Group Members : -")
    print("261058 - Sagar W. Jadhav  ")
    print("261062 - Suraj B. Gholap  ")
    print("261064 - Sanvidhan C. Pagare  ")
    print("261072 - Roshav V. Jadhav  ")
    print("261074 - Rushikesh M. Kshirsagar  ")

    print("--------------------------------------------------------------------------------------------------")
    menu=int(input("Enter Your Choice : "))
    print("--------------------------------------------------------------------------------------------------")
    def programe():
        def main():
            if (menu==1):
                        #Details for Beam A-B-C
                print("Enter The Details For Beam A-B-C")
                print("1. End Support : ")
                print("                  1. Fixed Support")
                print("                  2. Pinned/Hinged Support")
                print("                  3. Simply Supported")
                print("                  4. Roller Support")
                print("-------------------------------------------------")
                main.end_support=int(input("Enter Your Choice : "))
                print("-------------------------------------------------")
                print("2. Intermediate Support : ")
                print("                  1. Simply Supported")
                print("                  2. Roller Support")
                print("-------------------------------------------------")
                main.intermediate_support=int(input("Enter Your Choice : "))
                print("-------------------------------------------------")
                        #Details of Span 1 (A - B)
                print("Enter The Details For Span AB")
                print("1. Span")
                main.l1=float(input("Enter the Length of Span AB = "))
                print("2. Type of Loading")
                print("                  1. UDL")
                print("                  2. Point Load")
                print("-------------------------------------------------")
                main.load_combination1=int(input("Enter Your Choice : "))
                print("-------------------------------------------------")
                if (main.load_combination1==1):
                    main.wab=float(input("Enter the Magnitude of UDL : "))

                elif (main.load_combination1==2):
                    main.pab=float(input("Enter the Magnitude of Point Load : "))
                    main.aspan1=float(input("Enter the Distance of Point Load From A Support :"))
                    main.bspan1=main.l1-main.aspan1
                print("-------------------------------------------------")
                print("3. EI")
                print("                  1. Value of EI")
                print("                  2. Value of E&I")
                print("-------------------------------------------------")
                main.ei1=int(input("Enter Your Choice : "))
                print("-------------------------------------------------")
                if (main.ei1==1):
                    main.value_EI1=float(input("Enter the Value of EI : "))
                elif (main.ei1==2):
                    main.value_E1=float(input("Enter the Value of E : "))
                    main.value_I1_1=float(input("Enter the Value of I : "))
                    main.value_I1_2=int(input("x10^ : "))
                    main.value_I1_3=10**value_I1_2
                    main.value_I1=value_I1_1*value_I1_3
                    main.value_EI1=main.value_E1*main.value_I2

                        #Details of Span 2 (B - C)
                print("Enter The Details For Span BC")
                print("1. Span")
                main.l2=float(input("Enter the Length of Span BC = "))
                main.l=main.l1+main.l2
                print("2. Type of Loading")
                print("                  1. UDL")
                print("                  2. Point Load")
                print("-------------------------------------------------")
                main.load_combination2=int(input("Enter Your Choice : "))
                print("-------------------------------------------------")
                if (main.load_combination2==1):
                    main.wbc=float(input("Enter the Magnitude of UDL : "))

                elif (main.load_combination2==2):
                    main.pbc=float(input("Enter the Magnitude of Point Load : "))
                    main.aspan2=float(input("Enter the Distance of Point Load From B Support : "))
                    main.bspan2=main.l2-main.aspan2
                print("-------------------------------------------------")
                print("3. EI")
                print("                  1. Value of EI")
                print("                  2. Value of E&I")
                print("-------------------------------------------------")
                main.ei2=int(input("Enter Your Choice : "))
                print("-------------------------------------------------")
                if (main.ei2==1):
                    main.value_EI2=float(input("Enter the Value of EI : "))
                elif (main.ei2==2):
                    main.value_E2=float(input("Enter the Value of E : "))
                    main.value_I2_1=float(input("Enter the Value of I : "))
                    main.value_I2_2=int(input("x10^ : "))
                    main.value_I2_3=10**value_I2_2
                    main.value_I2=value_I2_1*value_I2_3
                    main.value_EI2=main.value_E2*main.value_I2_3

            if (menu==2):
                print("Three Span Beam Section")
                #Details for Beam A - B - C -D
                print("1. Support Condtions : ")
                print("                  1. Fixed Support")
                print("                  2. Pinned/Hinged Support")
                print("                  3. Simply Supported")
                print("                  4. Roller Support")
                main.support_A =int(input("Support A :"))
                main.support_B =int(input("Support B :"))
                main.support_C =int(input("Support C :"))
                main.support_D =int(input("Support D :"))
                print("-------------------------------------------------")

                #Details of Span 1 (A - B)
                print("Enter The Details For Span AB")
                print("1. Span")
                main.l1=float(input("Enter the Length of Span AB = "))
                print("2. Type of Loading")
                print("                  1. UDL")
                print("                  2. Point Load")
                print("-------------------------------------------------")
                main.load_combination1=int(input("Enter Your Choice : "))
                print("-------------------------------------------------")
                if (main.load_combination1==1):
                    main.wab=float(input("Enter the Magnitude of UDL : "))

                elif (main.load_combination1==2):
                    main.pab=float(input("Enter the Magnitude of Point Load : "))
                    main.aspan1=float(input("Enter the Distance of Point Load From A Support :"))
                    main.bspan1=main.l1-main.aspan1
                print("-------------------------------------------------")
                print("3. EI")
                print("                  1. Value of EI")
                print("                  2. Value of E&I")
                print("-------------------------------------------------")
                main.ei1=int(input("Enter Your Choice : "))
                print("-------------------------------------------------")
                if (main.ei1==1):
                    main.value_EI1=float(input("Enter the Value of EI : "))
                elif (main.ei1==2):
                    main.value_E1=float(input("Enter the Value of E : "))
                    main.value_I1_1=float(input("Enter the Value of I : "))
                    main.value_I1_2=int(input("x10^ : "))
                    main.value_I1_3=10**main.value_I1_2
                    main.value_I1=main.value_I1_1*main.value_I1_3
                    main.value_EI1=main.value_E1*main.value_I1

                        #Details of Span 2 (B - C)
                print("Enter The Details For Span BC")
                print("1. Span")
                main.l2=float(input("Enter the Length of Span BC = "))
                print("2. Type of Loading")
                print("                  1. UDL")
                print("                  2. Point Load")
                print("-------------------------------------------------")
                main.load_combination2=int(input("Enter Your Choice : "))
                print("-------------------------------------------------")
                if (main.load_combination2==1):
                    main.wbc=float(input("Enter the Magnitude of UDL : "))

                elif (main.load_combination2==2):
                    main.pbc=float(input("Enter the Magnitude of Point Load : "))
                    main.aspan2=float(input("Enter the Distance of Point Load From B Support :"))
                    main.bspan2=main.l2-main.aspan2
                print("-------------------------------------------------")
                print("3. EI")
                print("                  1. Value of EI")
                print("                  2. Value of E&I")
                print("-------------------------------------------------")
                main.ei2=int(input("Enter Your Choice : "))
                print("-------------------------------------------------")
                if (main.ei2==1):
                    main.value_EI2=float(input("Enter the Value of EI : "))
                elif (main.ei2==2):
                    main.value_E2=float(input("Enter the Value of E : "))
                    main.value_I2_1=float(input("Enter the Value of I : "))
                    main.value_I2_2=int(input("x10^ : "))
                    main.value_I2_3=10**main.value_I2_2
                    main.value_I2=main.value_I2_1*main.value_I2_3
                    main.value_EI2=main.value_E2*main.value_I2


                        #Details of Span 2 (C - D)
                print("Enter The Details For Span CD")
                print("1. Span")
                main.l3=float(input("Enter the Length of Span CD = "))
                main.l = main.l1 + main.l2 + main.l3
                print("2. Type of Loading")
                print("                  1. UDL")
                print("                  2. Point Load")
                print("-------------------------------------------------")
                main.load_combination3=int(input("Enter Your Choice : "))
                print("-------------------------------------------------")
                if (main.load_combination3==1):
                    main.wcd=float(input("Enter the Magnitude of UDL : "))

                elif (main.load_combination3==2):
                    main.pcd=float(input("Enter the Magnitude of Point Load : "))
                    main.aspan3=float(input("Enter the Distance of Point Load From C Support :"))
                    main.bspan3=main.l3-main.aspan3
                print("-------------------------------------------------")
                print("3. EI")
                print("                  1. Value of EI")
                print("                  2. Value of E&I")
                print("-------------------------------------------------")
                main.ei3=int(input("Enter Your Choice : "))
                print("-------------------------------------------------")
                if (main.ei3==1):
                    main.value_EI3=float(input("Enter the Value of EI : "))
                elif (main.ei2==2):
                    main.value_E3=float(input("Enter the Value of E : "))
                    main.value_I3_1=float(input("Enter the Value of I : "))
                    main.value_I3_2=int(input("x10^ : "))
                    main.value_I3_3=10**main.value_I3_2
                    main.value_I3=main.value_I3_1*main.value_I3_3
                    main.value_EI3=main.value_E3*main.value_I3
                def calculation():
                    if (main.support_A==1 and main.support_B==1 and main.support_C==1 and main.support_D==1):
                            print("Combination Not Possible")

                    elif ((main.support_A==2 or main.support_A==3 or main.support_A==4) and (main.support_B==2 or main.support_B==3 or main.support_B==4) and (main.support_C==2 or main.support_C==3 or main.support_C==4) and (main.support_D==2 or main.support_D==3 or main.support_D==4)):
                        #print("")
                        def dlc():
                            if(main.load_combination1==1 and main.load_combination2==1 and main.load_combination3==1):
                                #print("UDL on Entire Span")
                                #100% Completed Done**
                                #For Span AB and BC
                                    #Diagram 2
                                a1 = (2/3)*((main.wab*main.l1**2)/8)*main.l1
                                #print("a1=",a1)
                                x1 = (main.l1)/2
                                #print("x1",x1)
                                za = (main.wab*(main.l1**3))/4
                                #print("za=",za)
                                    #Diagram 3
                                a2 = (2/3)*((main.wbc*main.l2**2)/8)*main.l2
                                #print("a2=",a2)
                                x2 = (main.l2)/2
                                #print("x2",x2)
                                zb = (main.wbc*(main.l2**3))/4
                                #print("zb=",zb)

                                #For Span BC and CD
                                    #Diagram 2
                                a2 = (2/3)*((main.wbc*main.l2**2)/8)*main.l2
                                #print("a2=",a2)
                                x2 = (main.l2)/2
                                #print("x2",x2)
                                zb = (main.wbc*(main.l2**3))/4
                                #print("zb=",zb)
                                    #Diagram 3
                                a3 = (2/3)*((main.wcd*main.l3**2)/8)*main.l3
                                #print("a3=",a3)
                                x3 = (main.l3)/2
                                #print("x3",x3)
                                zc = (main.wcd*(main.l3**3))/4
                                #print("zc=",zc)
                                def momentcal():
                                    #a mb + b mc = c
                                    #d mb + e mc = f
                                    eqn1a=2*((main.l1/main.value_EI1)+(main.l2/main.value_EI2))
                                    #print("Value a =", eqn1a)
                                    eqn1b=(main.l2/main.value_EI2)
                                    #print("Value b =", eqn1b)
                                    eqn2c=-za-zb
                                    #print("Value c =", eqn2c)
                                    eqn2d=(main.l2/main.value_EI2)
                                    #print("Value d =",eqn2d )
                                    eqn2e=2*((main.l2/main.value_EI2)+(main.l3/main.value_EI3))
                                    #print("Value e =",eqn2e)
                                    eqn2f=-zb-zc
                                    #print("Vlaue f =",eqn2f)

                                    n= eqn1a*eqn2e - eqn1b*eqn2d
                                    #print("Values of mb and mc is : ")
                                    if (n!=0):
                                        calculation.mb=((eqn2c*eqn2e) - (eqn1b*eqn2f))/n
                                        calculation.mc=((eqn1a*eqn2f) - (eqn2c*eqn2d))/n
                                        #print("{:.3f} {:.3f}".format(calculation.mb+0,calculation.mc+0))
                                momentcal()
                                calculation.Ra=(calculation.mb+((main.wab*main.l1**2)/2))/main.l1
                                calculation.Rd=(calculation.mc+((main.wcd*main.l3**2)/2))/main.l3
                                def calrb():
                                    calculation.Rba=((-calculation.Ra*(main.l1+main.l2)+calculation.mc))
                                    rba=(round(calculation.Rba, 3))
                                    #print("RBa",rba)

                                    calculation.Rbb=main.wab*main.l1*((main.l1/2)+main.l2)
                                    rbb=(round(calculation.Rbb, 3))
                                    #print("RBb",rbb)

                                    calculation.Rbc=(main.wbc*main.l2**2)/2
                                    rbc=(round(calculation.Rbc, 3))
                                    #print("RBc",rbc)

                                    calculation.Rbd=(calculation.Rba + calculation.Rbb)
                                    rbd=(round(calculation.Rbd, 3))
                                    #print("RBd",rbd)

                                    calrb.rb=(rbd + rbc)/main.l2
                                    calculation.Rb=(round(calrb.rb, 3))
                                    #print("RB" ,calculation.Rb)



                                calrb()
                                calculation.Rc=(main.wab*main.l1)+(main.wbc*main.l2)+(main.wcd*main.l3)-calculation.Ra-calculation.Rb-calculation.Rd



                            elif(main.load_combination1==2 and main.load_combination2==2 and main.load_combination3==2):
                                #print("Point Load on all Spans")
                                #case 100% complete
                                #For Span AB and BC

                                    #Diagram 2
                                mmaxa=((main.pab*main.aspan1*main.bspan1)/main.l1)
                                mmax1=(round(mmaxa, 3))
                                #print("mmax =", mmax1)

                                aa = (1/2)*(mmax1*main.l1)
                                a1=(round(aa, 3))
                                #print("a1 =", a1)

                                xa = ((main.l1 + main.aspan1)/3) #corrected
                                x1=(round(xa, 3))
                                #print("x1 =", x1)


                                z1 = ((6*a1*x1)/(main.value_EI1*main.l1))
                                za=(round(z1, 3))
                                #print("za =", za)

                                    #Diagram 3
                                mmaxb=((main.pbc*main.aspan2*main.bspan2)/main.l2)
                                mmax2=(round(mmaxb, 3))
                                #print("mmax2 =", mmax2)

                                ab = (1/2)*(mmax2*main.l2)
                                a2 =(round(ab, 3))
                                #print("a2 =", a2)

                                xb = ((main.l2 + main.bspan2)/3) #correctd
                                x2 =(round(xb, 3))
                                #print("x2 =", x2)

                                z2 = ((6*a2*x2)/(main.value_EI2*main.l2)) #check this again
                                zb=(round(z2, 3))
                                #print("zb = ", zb)

                                #For Span BC and CD
                                    #Diagram 3
                                mmaxb=((main.pbc*main.aspan2*main.bspan2)/main.l2)
                                mmax2=(round(mmaxb, 3))
                                #print("mmax2 =", mmax2)

                                ab = (1/2)*(mmax2*main.l2)
                                a2 =(round(ab, 3))
                                #print("a2 =", a2)

                                xb = ((main.l2 + main.bspan2)/3) #correctd
                                x2 =(round(xb, 3))
                                #print("x2 =", x2)

                                z2 = ((6*a2*x2)/(main.value_EI2*main.l2)) #check this again
                                zb=(round(z2, 3))
                                #print("zb = ", zb)
                                    #Diagram 4

                                mmaxc=((main.pcd*main.aspan3*main.bspan3)/main.l3) #correction in progress
                                mmax3=(round(mmaxc, 3))
                                #print("mmax3 =", mmax3)

                                ac = (1/2)*(mmax3*main.l3)
                                a3=(round(ac, 3))
                                #print("a3 =", a3)
                                xc = ((main.l3 + main.bspan3)/3)
                                x3 =(round(xc, 3))

                                #print("x3 =", x3)

                                z3 = ((6*a3*x3)/(main.value_EI3*main.l3))
                                zc =(round(z3, 3))
                                #print("zc =", zc)

                                def momentcal():
                                    #a mb + b mc = c
                                    #d mb + e mc = f
                                    eqn1a=2*((main.l1/main.value_EI1)+(main.l2/main.value_EI2))
                                    #print("Value a =", eqn1a)
                                    eqn1b=(main.l2/main.value_EI2)
                                    #print("Value b =", eqn1b)
                                    eqn2c=-za-zb
                                    #print("Value c =", eqn2c)
                                    eqn2d=(main.l2/main.value_EI2)
                                    #print("Value d =",eqn2d )
                                    eqn2e=2*((main.l2/main.value_EI2)+(main.l3/main.value_EI3))
                                    #print("Value e =",eqn2e)
                                    eqn2f=-zb-zc
                                    #print("Vlaue f =",eqn2f)

                                    n= eqn1a*eqn2e - eqn1b*eqn2d
                                    #print("Values of mb and mc is : ")
                                    if (n!=0):
                                        calculation.mb=((eqn2c*eqn2e) - (eqn1b*eqn2f))/n
                                        calculation.mc=((eqn1a*eqn2f) - (eqn2c*eqn2d))/n
                                        #print("{:.3f} {:.3f}".format(calculation.mb+0,calculation.mc+0))
                                momentcal()
                                calculation.Ra=(calculation.mb+((main.pab*main.bspan1)))/main.l1
                                calculation.Rd=(calculation.mc+((main.pcd*main.aspan3)))/main.l3
                                def calrb():
                                    calculation.Rba=((-calculation.Ra*(main.l1+main.l2)+calculation.mc))
                                    rba=(round(calculation.Rba, 3))
                                    #print("RBa",rba)

                                    calculation.Rbb=main.pab*(main.bspan1+main.l2)
                                    rbb=(round(calculation.Rbb, 3))
                                    #print("RBb",rbb)

                                    calculation.Rbc=(main.pbc*main.bspan2)
                                    rbc=(round(calculation.Rbc, 3))
                                    #print("RBc",rbc)

                                    calculation.Rbd=(calculation.Rba + calculation.Rbb)
                                    rbd=(round(calculation.Rbd, 3))
                                    #print("RBd",rbd)
                                    calrb.rb=(rbd + rbc)/main.l2
                                    calculation.Rb=(round(calrb.rb, 3))
                                    #print("RB" ,calculation.Rb)
                                calrb()
                                calculation.Rc=(main.pab)+(main.pbc)+(main.pcd)-calculation.Ra-calculation.Rb-calculation.Rd

                            elif(main.load_combination1==2 and main.load_combination1==1 and main.load_combination1==1 ):
                                #print("pl + udl + udl")
                                #case completed 100%
                            #For span AB and BC

                                #Diagram 2
                                mmaxa=((main.pab*main.aspan1*main.bspan1)/main.l1)
                                mmax1=(round(mmaxa, 3))
                                #print("mmax =", mmax1)

                                aa = (1/2)*(mmax1*main.l1)
                                a1=(round(aa, 3))
                                #print("a1 =", a1)

                                xa = ((main.l1 + main.aspan1)/3) #corrected
                                x1=(round(xa, 3))
                                #print("x1 =", x1)


                                z1 = ((6*a1*x1)/(main.value_EI1*main.l1))
                                za=(round(z1, 3))
                                #print("za =", za)
                                #Diagram 3

                                a2 = (2/3)*((main.wbc*main.l2**2)/8)*main.l2
                                #print("a2=",a2)
                                x2 = (main.l2)/2
                                #print("x2",x2)
                                zb = (main.wbc*(main.l2**3))/4
                                #print("zb=",zb)

                            #For span BC and CD
                                #Diagram 3
                                a2 = (2/3)*((main.wbc*main.l2**2)/8)*main.l2
                                #print("a2=",a2)
                                x2 = (main.l2)/2
                                #print("x2",x2)
                                zb = (main.wbc*(main.l2**3))/4
                                #print("zb=",zb)

                                #Diagram 4
                                a3 = (2/3)*((main.wcd*main.l3**2)/8)*main.l3
                                #print("a3=",a3)
                                x3 = (main.l3)/2
                                #print("x3",x3)
                                zc = (main.wcd*(main.l3**3))/4
                                #print("zc=",zc)

                                def momentcal():
                                    #a mb + b mc = c
                                    #d mb + e mc = f
                                    eqn1a=2*((main.l1/main.value_EI1)+(main.l2/main.value_EI2))
                                    #print("Value a =", eqn1a)
                                    eqn1b=(main.l2/main.value_EI2)
                                    #print("Value b =", eqn1b)
                                    eqn2c=-za-zb
                                    #print("Value c =", eqn2c)
                                    eqn2d=(main.l2/main.value_EI2)
                                    #print("Value d =",eqn2d )
                                    eqn2e=2*((main.l2/main.value_EI2)+(main.l3/main.value_EI3))
                                    #print("Value e =",eqn2e)
                                    eqn2f=-zb-zc
                                    #print("Vlaue f =",eqn2f)

                                    n= eqn1a*eqn2e - eqn1b*eqn2d
                                    #print("Values of mb and mc is : ")
                                    if (n!=0):
                                        calculation.mb=((eqn2c*eqn2e) - (eqn1b*eqn2f))/n
                                        calculation.mc=((eqn1a*eqn2f) - (eqn2c*eqn2d))/n
                                        #print("{:.3f} {:.3f}".format(calculation.mb+0,calculation.mc+0))
                                momentcal()
                                calculation.Ra=(calculation.mb+((main.pab*main.bspan1)))/main.l1
                                calculation.Rd=(calculation.mc+((main.wcd*main.l3**2)/2))/main.l3
                                def calrb():
                                    calculation.Rba=((-calculation.Ra*(main.l1+main.l2)+calculation.mc))
                                    rba=(round(calculation.Rba, 3))
                                    #print("RBa",rba)

                                    calculation.Rbb=main.pab*(main.bspan1+main.l2)
                                    rbb=(round(calculation.Rbb, 3))
                                    #print("RBb",rbb)

                                    calculation.Rbc=(main.wbc*main.l2**2)/2
                                    rbc=(round(calculation.Rbc, 3))
                                    #print("RBc",rbc)

                                    calculation.Rbd=(calculation.Rba + calculation.Rbb)
                                    rbd=(round(calculation.Rbd, 3))
                                    #print("RBd",rbd)
                                    calrb.rb=(rbd + rbc)/main.l2
                                    calculation.Rb=(round(calrb.rb, 3))
                                    #print("RB" ,calculation.Rb)
                                calrb()
                                calculation.Rc=(main.pab)+((main.wbc)*(main.l2))+((main.wcd)*(main.l3))-calculation.Ra-calculation.Rb-calculation.Rd

                                #Support Reactions Remaining
                                #Support Reactions Remaining
                                #Support Reactions Remaining
                                #Support Reactions Remaining
                                #Support Reactions Remaining

                            elif(main.load_combination1==1 and main.load_combination2==2 and main.load_combination3==2):
                                #print("udl + pt + pt")
                                #case complete 100%
                                #For Span AB and BC
                                    #Diagram 2
                                a1 = (2/3)*((main.wab*main.l1**2)/8)*main.l1
                                #print("a1=",a1)
                                x1 = (main.l1)/2
                                #print("x1",x1)
                                za = (main.wab*(main.l1**3))/4
                                #print("za=",za)
                                    #Diagram 3
                                mmaxb=((main.pbc*main.aspan2*main.bspan2)/main.l2)
                                mmax2=(round(mmaxb, 3))
                                #print("mmax2 =", mmax2)

                                ab = (1/2)*(mmax2*main.l2)
                                a2 =(round(ab, 3))
                                #print("a2 =", a2)

                                xb = ((main.l2 + main.bspan2)/3) #correctd
                                x2 =(round(xb, 3))
                                #print("x2 =", x2)

                                z2 = ((6*a2*x2)/(main.value_EI2*main.l2)) #check this again
                                zb=(round(z2, 3))
                                #print("zb = ", zb)

                                #For Span BC and CD
                                    #Diagram 3
                                mmaxb=((main.pbc*main.aspan2*main.bspan2)/main.l2)
                                mmax2=(round(mmaxb, 3))
                                #print("mmax2 =", mmax2)

                                ab = (1/2)*(mmax2*main.l2)
                                a2 =(round(ab, 3))
                                #print("a2 =", a2)

                                xb = ((main.l2 + main.bspan2)/3) #correctd
                                x2 =(round(xb, 3))
                                #print("x2 =", x2)

                                z2 = ((6*a2*x2)/(main.value_EI2*main.l2)) #check this again
                                zb=(round(z2, 3))
                                #print("zb = ", zb)
                                    #Diagram 4

                                mmaxc=((main.pcd*main.aspan3*main.bspan3)/main.l3) #correction in progress
                                mmax3=(round(mmaxc, 3))
                                #print("mmax3 =", mmax3)

                                ac = (1/2)*(mmax3*main.l3)
                                a3=(round(ac, 3))
                                #print("a3 =", a3)
                                xc = ((main.l3 + main.bspan3)/3)
                                x3 =(round(xc, 3))

                                #print("x3 =", x3)

                                z3 = ((6*a3*x3)/(main.value_EI3*main.l3))
                                zc =(round(z3, 3))
                                #print("zc =", zc)

                                def momentcal():
                                    #a mb + b mc = c
                                    #d mb + e mc = f
                                    eqn1a=2*((main.l1/main.value_EI1)+(main.l2/main.value_EI2))
                                    #print("Value a =", eqn1a)
                                    eqn1b=(main.l2/main.value_EI2)
                                    #print("Value b =", eqn1b)
                                    eqn2c=-za-zb
                                    #print("Value c =", eqn2c)
                                    eqn2d=(main.l2/main.value_EI2)
                                    #print("Value d =",eqn2d )
                                    eqn2e=2*((main.l2/main.value_EI2)+(main.l3/main.value_EI3))
                                    #print("Value e =",eqn2e)
                                    eqn2f=-zb-zc
                                    #print("Vlaue f =",eqn2f)

                                    n= eqn1a*eqn2e - eqn1b*eqn2d
                                    #print("Values of mb and mc is : ")
                                    if (n!=0):
                                        calculation.mb=((eqn2c*eqn2e) - (eqn1b*eqn2f))/n
                                        calculation.mc=((eqn1a*eqn2f) - (eqn2c*eqn2d))/n
                                        #print("{:.3f} {:.3f}".format(calculation.mb+0,calculation.mc+0))
                                momentcal()
                                calculation.Ra=(calculation.mb+((main.wab*main.l1**2)/2))/main.l1
                                calculation.Rd=(calculation.mc+((main.pcd*main.aspan3)))/main.l3
                                def calrb():
                                    calculation.Rba=((-calculation.Ra*(main.l1+main.l2)+calculation.mc))
                                    rba=(round(calculation.Rba, 3))
                                    #print("RBa",rba)

                                    calculation.Rbb=main.wab*main.l1*((main.l1/2)+main.l2)
                                    rbb=(round(calculation.Rbb, 3))
                                    #print("RBb",rbb)

                                    calculation.Rbc=(main.pbc*main.bspan2)
                                    rbc=(round(calculation.Rbc, 3))
                                    #print("RBc",rbc)

                                    calculation.Rbd=(calculation.Rba + calculation.Rbb)
                                    rbd=(round(calculation.Rbd, 3))
                                    #print("RBd",rbd)
                                    calrb.rb=(rbd + rbc)/main.l2
                                    calculation.Rb=(round(calrb.rb, 3))
                                    #print("RB" ,calculation.Rb)
                                calrb()
                                calculation.Rc=(calculation.wab*main.l1)+(main.pbc)+(main.pcd)-calculation.Ra-calculation.Rb-calculation.Rd
                                #Support Reactions Remaining
                                #Support Reactions Remaining
                                #Support Reactions Remaining
                                #Support Reactions Remaining
                                #Support Reactions Remaining
                            elif(main.load_combination1==2 and main.load_combination2==1 and main.load_combination3==2):
                                #print("pt + udl + pt")
                                #case completed 100%
                            #For span AB and BC

                                #Diagram 2
                                mmaxa=((main.pab*main.aspan1*main.bspan1)/main.l1)
                                mmax1=(round(mmaxa, 3))
                                #print("mmax =", mmax1)

                                aa = (1/2)*(mmax1*main.l1)
                                a1=(round(aa, 3))
                                #print("a1 =", a1)

                                xa = ((main.l1 + main.aspan1)/3) #corrected
                                x1=(round(xa, 3))
                                #print("x1 =", x1)


                                z1 = ((6*a1*x1)/(main.value_EI1*main.l1))
                                za=(round(z1, 3))
                                #print("za =", za)

                                #Diagram 3

                                a2 = (2/3)*((main.wbc*main.l2**2)/8)*main.l2
                                #print("a2=",a2)
                                x2 = (main.l2)/2
                                #print("x2",x2)
                                zb = (main.wbc*(main.l2**3))/4
                                #print("zb=",zb)

                            #For span BC and CD
                                #Diagram 3

                                a2 = (2/3)*((main.wbc*main.l2**2)/8)*main.l2
                                #print("a2=",a2)
                                x2 = (main.l2)/2
                                #print("x2",x2)
                                zb = (main.wbc*(main.l2**3))/4
                                #print("zb=",zb)

                                #Diagram 4

                                mmaxc=((main.pcd*main.aspan3*main.bspan3)/main.l3) #correction in progress
                                mmax3=(round(mmaxc, 3))
                                #print("mmax3 =", mmax3)

                                ac = (1/2)*(mmax3*main.l3)
                                a3=(round(ac, 3))
                                #print("a3 =", a3)
                                xc = ((main.l3 + main.bspan3)/3)
                                x3 =(round(xc, 3))

                                #print("x3 =", x3)

                                z3 = ((6*a3*x3)/(main.value_EI3*main.l3))
                                zc =(round(z3, 3))
                                #print("zc =", zc)

                                def momentcal():
                                    #a mb + b mc = c
                                    #d mb + e mc = f
                                    eqn1a=2*((main.l1/main.value_EI1)+(main.l2/main.value_EI2))
                                    #print("Value a =", eqn1a)
                                    eqn1b=(main.l2/main.value_EI2)
                                    #print("Value b =", eqn1b)
                                    eqn2c=-za-zb
                                    #print("Value c =", eqn2c)
                                    eqn2d=(main.l2/main.value_EI2)
                                    #print("Value d =",eqn2d )
                                    eqn2e=2*((main.l2/main.value_EI2)+(main.l3/main.value_EI3))
                                    #print("Value e =",eqn2e)
                                    eqn2f=-zb-zc
                                    #print("Vlaue f =",eqn2f)

                                    n= eqn1a*eqn2e - eqn1b*eqn2d
                                    #print("Values of mb and mc is : ")
                                    if (n!=0):
                                        calculation.mb=((eqn2c*eqn2e) - (eqn1b*eqn2f))/n
                                        calculation.mc=((eqn1a*eqn2f) - (eqn2c*eqn2d))/n
                                        #print("{:.3f} {:.3f}".format(calculation.mb+0,calculation.mc+0))
                                momentcal()
                                calculation.Ra=(calculation.mb+((main.pab*main.bspan1)))/main.l1
                                calculation.Rd=(calculation.mc+((main.pcd*main.aspan3)))/main.l3
                                def calrb():
                                    calculation.Rba=((-calculation.Ra*(main.l1+main.l2)+calculation.mc))
                                    rba=(round(calculation.Rba, 3))
                                    #print("RBa",rba)

                                    calculation.Rbb=main.pab*(main.bspan1+main.l2)
                                    rbb=(round(calculation.Rbb, 3))
                                    #print("RBb",rbb)

                                    calculation.Rbc=(main.wbc*main.l2**2)/2
                                    rbc=(round(calculation.Rbc, 3))
                                    #print("RBc",rbc)

                                    calculation.Rbd=(calculation.Rba + calculation.Rbb)
                                    rbd=(round(calculation.Rbd, 3))
                                    #print("RBd",rbd)
                                    calrb.rb=(rbd + rbc)/main.l2
                                    calculation.Rb=(round(calrb.rb, 3))
                                    #print("RB" ,calculation.Rb)
                                calrb()
                                calculation.Rc=main.pab+(main.wbc*main.l2)+main.pcd-calculation.Ra-calculation.Rb-calculation.Rd
                                #Support Reactions Remaining
                                #Support Reactions Remaining
                                #Support Reactions Remaining
                                #Support Reactions Remaining
                                #Support Reactions Remaining
                            elif(main.load_combination1==1 and main.load_combination2==1 and main.load_combination3==2):
                                #print("udl + udl + pt")
                                #case completed 100%
                                #For Span AB and BC
                                    #Diagram 2
                                a1 = (2/3)*((main.wab*main.l1**2)/8)*main.l1
                                #print("a1=",a1)
                                x1 = (main.l1)/2
                                #print("x1",x1)
                                za = (main.wab*(main.l1**3))/4
                                #print("za=",za)
                                    #Diagram 3
                                a2 = (2/3)*((main.wbc*main.l2**2)/8)*main.l2
                                #print("a2=",a2)
                                x2 = (main.l2)/2
                                #print("x2",x2)
                                zb = (main.wbc*(main.l2**3))/4
                                #print("zb=",zb)

                                #FOR SPAN BC AND CD
                                    #Diagram 3

                                a2 = (2/3)*((main.wbc*main.l2**2)/8)*main.l2
                                #print("a2=",a2)
                                x2 = (main.l2)/2
                                #print("x2",x2)
                                zb = (main.wbc*(main.l2**3))/4
                                #print("zb=",zb)
                                #Diagram 4

                                mmaxc=((main.pcd*main.aspan3*main.bspan3)/main.l3) #correction in progress
                                mmax3=(round(mmaxc, 3))
                                #print("mmax3 =", mmax3)

                                ac = (1/2)*(mmax3*main.l3)
                                a3=(round(ac, 3))
                                #print("a3 =", a3)
                                xc = ((main.l3 + main.bspan3)/3)
                                x3 =(round(xc, 3))

                                #print("x3 =", x3)

                                z3 = ((6*a3*x3)/(main.value_EI3*main.l3))
                                zc =(round(z3, 3))
                                #print("zc =", zc)
                                def momentcal():
                                    #a mb + b mc = c
                                    #d mb + e mc = f
                                    eqn1a=2*((main.l1/main.value_EI1)+(main.l2/main.value_EI2))
                                    #print("Value a =", eqn1a)
                                    eqn1b=(main.l2/main.value_EI2)
                                    #print("Value b =", eqn1b)
                                    eqn2c=-za-zb
                                    #print("Value c =", eqn2c)
                                    eqn2d=(main.l2/main.value_EI2)
                                    #print("Value d =",eqn2d )
                                    eqn2e=2*((main.l2/main.value_EI2)+(main.l3/main.value_EI3))
                                    #print("Value e =",eqn2e)
                                    eqn2f=-zb-zc
                                    #print("Vlaue f =",eqn2f)

                                    n= eqn1a*eqn2e - eqn1b*eqn2d
                                    #print("Values of mb and mc is : ")
                                    if (n!=0):
                                        calculation.mb=((eqn2c*eqn2e) - (eqn1b*eqn2f))/n
                                        calculation.mc=((eqn1a*eqn2f) - (eqn2c*eqn2d))/n
                                        #print("{:.3f} {:.3f}".format(calculation.mb+0,calculation.mc+0))
                                momentcal()
                                calculation.Ra=(calculation.mb+((main.wab*main.l1**2)/2))/main.l1
                                calculation.Rd=(calculation.mc+((main.pcd*main.aspan3)))/main.l3
                                def calrb():
                                    calculation.Rba=((-calculation.Ra*(main.l1+main.l2)+calculation.mc))
                                    rba=(round(calculation.Rba, 3))
                                    #print("RBa",rba)

                                    calculation.Rbb=main.wab*main.l1*((main.l1/2)+main.l2)
                                    rbb=(round(calculation.Rbb, 3))
                                    #print("RBb",rbb)

                                    calculation.Rbc=(main.wbc*main.l2**2)/2
                                    rbc=(round(calculation.Rbc, 3))
                                    #print("RBc",rbc)

                                    calculation.Rbd=(calculation.Rba + calculation.Rbb)
                                    rbd=(round(calculation.Rbd, 3))
                                    #print("RBd",rbd)
                                    calrb.rb=(rbd + rbc)/main.l2
                                    calculation.Rb=(round(calrb.rb, 3))
                                    #print("RB" ,calculation.Rb)
                                calrb()
                                calculation.Rc=(main.wab*main.l1)+(main.wbc*main.l2)+main.pcd-calculation.Ra-calculation.Rb-calculation.Rd
                                #Support Reactions Remaining
                                #Support Reactions Remaining
                                #Support Reactions Remaining
                                #Support Reactions Remaining
                                #Support Reactions Remaining

                            elif(main.load_combination1==1 and main.load_combination2==2 and main.load_combination3==1):
                                #print("udl + pt + udl")
                                #case completed 1000%
                                #For Span AB and BC
                                    #Diagram 2
                                a1 = (2/3)*((main.wab*main.l1**2)/8)*main.l1
                                #print("a1=",a1)
                                x1 = (main.l1)/2
                                #print("x1",x1)
                                za = (main.wab*(main.l1**3))/4
                                #print("za=",za)
                                    #Diagram 3
                                mmaxb=((main.pbc*main.aspan2*main.bspan2)/main.l2)
                                mmax2=(round(mmaxb, 3))
                                #print("mmax2 =", mmax2)

                                ab = (1/2)*(mmax2*main.l2)
                                a2 =(round(ab, 3))
                                #print("a2 =", a2)

                                xb = ((main.l2 + main.bspan2)/3) #correctd
                                x2 =(round(xb, 3))
                                #print("x2 =", x2)

                                z2 = ((6*a2*x2)/(main.value_EI2*main.l2)) #check this again
                                zb=(round(z2, 3))
                                #print("zb = ", zb)

                                #For Span BC and CD
                                    #Diagram 3
                                mmaxb=((main.pbc*main.aspan2*main.bspan2)/main.l2)
                                mmax2=(round(mmaxb, 3))
                                #print("mmax2 =", mmax2)

                                ab = (1/2)*(mmax2*main.l2)
                                a2 =(round(ab, 3))
                                #print("a2 =", a2)

                                xb = ((main.l2 + main.bspan2)/3) #correctd
                                x2 =(round(xb, 3))
                                #print("x2 =", x2)

                                z2 = ((6*a2*x2)/(main.value_EI2*main.l2)) #check this again
                                zb=(round(z2, 3))
                                #print("zb = ", zb)

                                    #Diagram 3
                                a3 = (2/3)*((main.wcd*main.l3**2)/8)*main.l3
                                #print("a3=",a3)
                                x3 = (main.l3)/2
                                #print("x3",x3)
                                zc = (main.wcd*(main.l3**3))/4
                                #print("zc=",zc)

                                def momentcal():
                                    #a mb + b mc = c
                                    #d mb + e mc = f
                                    eqn1a=2*((main.l1/main.value_EI1)+(main.l2/main.value_EI2))
                                    #print("Value a =", eqn1a)
                                    eqn1b=(main.l2/main.value_EI2)
                                    #print("Value b =", eqn1b)
                                    eqn2c=-za-zb
                                    #print("Value c =", eqn2c)
                                    eqn2d=(main.l2/main.value_EI2)
                                    #print("Value d =",eqn2d )
                                    eqn2e=2*((main.l2/main.value_EI2)+(main.l3/main.value_EI3))
                                    #print("Value e =",eqn2e)
                                    eqn2f=-zb-zc
                                    #print("Vlaue f =",eqn2f)

                                    n= eqn1a*eqn2e - eqn1b*eqn2d
                                    #print("Values of mb and mc is : ")
                                    if (n!=0):
                                        calculation.mb=((eqn2c*eqn2e) - (eqn1b*eqn2f))/n
                                        calculation.mc=((eqn1a*eqn2f) - (eqn2c*eqn2d))/n
                                        #print("{:.3f} {:.3f}".format(calculation.mb+0,calculation.mc+0))
                                momentcal()
                                calculation.Ra=(calculation.mb+((main.wab*main.l1**2)/2))/main.l1
                                calculation.Rd=(calculation.mc+((main.wcd*main.l3**2)/2))/main.l3
                                def calrb():
                                    calculation.Rba=((-calculation.Ra*(main.l1+main.l2)+calculation.mc))
                                    rba=(round(calculation.Rba, 3))
                                    #print("RBa",rba)

                                    calculation.Rbb=main.wab*main.l1*((main.l1/2)+main.l2)
                                    rbb=(round(calculation.Rbb, 3))
                                    #print("RBb",rbb)

                                    calculation.Rbc=(main.pbc*main.bspan2)
                                    rbc=(round(calculation.Rbc, 3))
                                    #print("RBc",rbc)

                                    calculation.Rbd=(calculation.Rba + calculation.Rbb)
                                    rbd=(round(calculation.Rbd, 3))
                                    #print("RBd",rbd)
                                    calrb.rb=(rbd + rbc)/main.l2
                                    calculation.Rb=(round(calrb.rb, 3))
                                    #print("RB" ,calculation.Rb)

                                calrb()

                                calculation.Rc=(main.wab*main.l1)+main.pbc+(main.wcd*main.l3)-calculation.Ra-calculation.Rb-calculation.Rd
                                #Support Reactions ADDED IN END OF PROGRAM
                                #Support Reactions ADDED IN END OF PROGRAM
                                #Support Reactions ADDED IN END OF PROGRAM
                                #Support Reactions ADDED IN END OF PROGRAM
                                #Support Reactions ADDED IN END OF PROGRAM

                            elif(main.load_combination1==2 and main.load_combination2==2 and main.load_combination3==1):
                                #print("pt + pt + udl")
                                #case completed 100%
                                #For Span AB and BC

                                    #Diagram 2
                                mmaxa=((main.pab*main.aspan1*main.bspan1)/main.l1)
                                mmax1=(round(mmaxa, 3))
                                #print("mmax =", mmax1)

                                aa = (1/2)*(mmax1*main.l1)
                                a1=(round(aa, 3))
                                #print("a1 =", a1)

                                xa = ((main.l1 + main.aspan1)/3) #corrected
                                x1=(round(xa, 3))
                                #print("x1 =", x1)


                                z1 = ((6*a1*x1)/(main.value_EI1*main.l1))
                                za=(round(z1, 3))
                                #print("za =", za)

                                    #Diagram 3
                                mmaxb=((main.pbc*main.aspan2*main.bspan2)/main.l2)
                                mmax2=(round(mmaxb, 3))
                                #print("mmax2 =", mmax2)

                                ab = (1/2)*(mmax2*main.l2)
                                a2 =(round(ab, 3))
                                #print("a2 =", a2)

                                xb = ((main.l2 + main.bspan2)/3) #correctd
                                x2 =(round(xb, 3))
                                #print("x2 =", x2)

                                z2 = ((6*a2*x2)/(main.value_EI2*main.l2)) #check this again
                                zb=(round(z2, 3))
                                #print("zb = ", zb)

                                #For Span BC and CD
                                    #Diagram 3
                                mmaxb=((main.pbc*main.aspan2*main.bspan2)/main.l2)
                                mmax2=(round(mmaxb, 3))
                                #print("mmax2 =", mmax2)

                                ab = (1/2)*(mmax2*main.l2)
                                a2 =(round(ab, 3))
                                #print("a2 =", a2)

                                xb = ((main.l2 + main.bspan2)/3) #correctd
                                x2 =(round(xb, 3))
                                #print("x2 =", x2)

                                z2 = ((6*a2*x2)/(main.value_EI2*main.l2)) #check this again
                                zb=(round(z2, 3))
                                #print("zb = ", zb)

                                    #Diagram 4
                                a3 = (2/3)*((main.wcd*main.l3**2)/8)*main.l3
                                #print("a3=",a3)
                                x3 = (main.l3)/2
                                #print("x3",x3)
                                zc = (main.wcd*(main.l3**3))/4
                                #print("zc=",zc)
                                def momentcal():
                                    #a mb + b mc = c
                                    #d mb + e mc = f
                                    eqn1a=2*((main.l1/main.value_EI1)+(main.l2/main.value_EI2))
                                    #print("Value a =", eqn1a)
                                    eqn1b=(main.l2/main.value_EI2)
                                    #print("Value b =", eqn1b)
                                    eqn2c=-za-zb
                                    #print("Value c =", eqn2c)
                                    eqn2d=(main.l2/main.value_EI2)
                                    #print("Value d =",eqn2d )
                                    eqn2e=2*((main.l2/main.value_EI2)+(main.l3/main.value_EI3))
                                    #print("Value e =",eqn2e)
                                    eqn2f=-zb-zc
                                    #print("Vlaue f =",eqn2f)

                                    n= eqn1a*eqn2e - eqn1b*eqn2d
                                    #print("Values of mb and mc is : ")
                                    if (n!=0):
                                        calculation.mb=((eqn2c*eqn2e) - (eqn1b*eqn2f))/n
                                        calculation.mc=((eqn1a*eqn2f) - (eqn2c*eqn2d))/n
                                        #print("{:.3f} {:.3f}".format(calculation.mb+0,calculation.mc+0))
                                momentcal()
                                calculation.Ra=(calculation.mb+((main.pab*main.bspan1)))/main.l1
                                calculation.Rd=(calculation.mc+((main.wcd*main.l3**2)/2))/main.l3
                                def calrb():
                                    calculation.Rba=((-calculation.Ra*(main.l1+main.l2)+calculation.mc))
                                    rba=(round(calculation.Rba, 3))
                                    #print("RBa",rba)

                                    calculation.Rbb=main.pab*(main.bspan1+main.l2)
                                    rbb=(round(calculation.Rbb, 3))
                                    #print("RBb",rbb)

                                    calculation.Rbc=(main.pbc*main.bspan2)
                                    rbc=(round(calculation.Rbc, 3))
                                    #print("RBc",rbc)

                                    calculation.Rbd=(calculation.Rba + calculation.Rbb)
                                    rbd=(round(calculation.Rbd, 3))
                                    #print("RBd",rbd)
                                    calrb.rb=(rbd + rbc)/main.l2
                                    calculation.Rb=(round(calrb.rb, 3))
                                    #print("RB" ,calculation.Rb)
                                calrb()
                                calculation.Rc=main.pab+main.pbc+(main.wcd*main.l3)-calculation.Ra-calculation.Rb-calculation.Rd

                            else:
                                print("Error!")

                        dlc()
                        print("RA = ",(round(calculation.Ra, 3)), "KN")
                        print("RB = ",(round(calculation.Rb, 3)), "KN")
                        print("RC = ",(round(calculation.Rc, 3)), "KN")
                        print("RD = ",(round(calculation.Rd, 3)), "KN")
                        print("MB = ",(round(calculation.mb, 3)), "KNM")
                        print("MC = ",(round(calculation.mc, 3)), "KNM")
                        raw_input=str(input('PRESS ENTER TO GET PDF!'))
                        def threespan():
                            pdf = FPDF() #Making a PDF Variable
                            pdf.add_page() #Adding a Page
                            pdf.set_font("Arial" , size= 15) #Font ani Size
                            #Actual Printing in PDF Starts here...........
                            pdf.cell(200, 10, txt = "Clapeyron's Theorem of Three Moments",
                                     ln = 1, align = 'C')
                            pdf.cell(200,10, txt = "Three Span Beam",
                                     ln = 2, align = 'C')
                                        #Working on Given Data
                            pdf.cell(200,10, txt = "GIVEN DATA : - ",
                             ln = 4, align = 'L')
                             #Use IF Statement
                            #suppport A
                            if (main.end_support_A==1):
                                pdf.cell(200,10, txt = "    A Supports :  Fixed " ,
                                 ln = 4, align = 'L')
                            elif (main.end_support_A==2):
                                pdf.cell(200,10, txt = "    A Supports :  Pinned/Hinged " ,
                                 ln = 4, align = 'L')

                            elif (main.end_support_A==3):
                                pdf.cell(200,10, txt = "    A Supports :  Simple " ,
                                 ln = 4, align = 'L')

                            elif (main.end_support_A==4):
                                pdf.cell(200,10, txt = "    A Supports :  Roller " ,
                                 ln = 4, align = 'L')
                            #support B
                            if (main.end_support_B==1):
                                pdf.cell(200,10, txt = "    B Supports :  Fixed " ,
                                 ln = 4, align = 'L')
                            elif (main.end_support_B==2):
                                pdf.cell(200,10, txt = "    B Supports :  Pinned/Hinged " ,
                                 ln = 4, align = 'L')

                            elif (main.end_support_B==3):
                                pdf.cell(200,10, txt = "    B Supports :  Simple " ,
                                 ln = 4, align = 'L')

                            elif (main.end_support_B==4):
                                pdf.cell(200,10, txt = "    B Supports :  Roller " ,
                                 ln = 4, align = 'L')
                            #support c

                            if (main.end_support_C==1):
                                pdf.cell(200,10, txt = "    C Supports :  Fixed " ,
                                 ln = 4, align = 'L')
                            elif (main.end_support_C==2):
                                pdf.cell(200,10, txt = "    C Supports :  Pinned/Hinged " ,
                                 ln = 4, align = 'L')

                            elif (main.end_support_C==3):
                                pdf.cell(200,10, txt = "    C Supports :  Simple " ,
                                 ln = 4, align = 'L')

                            elif (main.end_support_C==4):
                                pdf.cell(200,10, txt = "    C Supports :  Roller " ,
                                 ln = 4, align = 'L')

                            #support d

                            if (main.end_support_D==1):
                                pdf.cell(200,10, txt = "    D Supports :  Fixed " ,
                                 ln = 4, align = 'L')
                            elif (main.end_support_D==2):
                                pdf.cell(200,10, txt = "    D Supports :  Pinned/Hinged " ,
                                 ln = 4, align = 'L')

                            elif (main.end_support_D==3):
                                pdf.cell(200,10, txt = "    D Supports :  Simple " ,
                                 ln = 4, align = 'L')

                            elif (main.end_support_D==4):
                                pdf.cell(200,10, txt = "    D Supports :  Roller " ,
                                 ln = 4, align = 'L')

                            pdf.cell(200,10, txt = "    End Supports :   " ,
                             ln = 4, align = 'L')

                            if (main.intermediate_support==1):
                                pdf.cell(200,10, txt = "    Intermediate Supports : Simple ",
                                 ln = 4, align = 'L')
                            elif (main.intermediate_support==2):
                                pdf.cell(200,10, txt = "    Intermediate Supports : Roller ",
                                 ln = 4, align = 'L')
                            else:
                                pdf.cell(200,10, txt = "    Intermediate Supports :  ",
                                 ln = 4, align = 'L')

                            pdf.cell(200,10, txt = "",
                                     ln = 4, align = 'L')

                            pdf.cell(200,10, txt = "    Beam Span Details : - ",
                             ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "        For Span AB : - ",
                             ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "            Length : " +str(main.l1) + " m",
                             ln = 4, align = 'L')
                            if (main.load_combination1==1):
                                pdf.cell(200,10, txt = "            Load :  UDL - " +str(main.wab) + " kN/m",
                                 ln = 4, align = 'L')
                            elif (main.load_combination2==2):
                                pdf.cell(200,10, txt = "            Load :  Point Load - " +str(main.pab) + " kN",
                                 ln = 4, align = 'L')
                            else:
                                pdf.cell(200,10, txt = "            Load :  " ,
                                 ln = 4, align = 'L')
                            if (main.ei1==1):
                                pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI1) + " kN.m^2" ,
                                 ln = 4, align = 'L')
                            elif (main.ei1==2):
                                pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI1) + " kN.m^2",
                                 ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "",
                                     ln = 4, align = 'L')

                            pdf.cell(200,10, txt = "        For Span BC : - ",
                             ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "            Length : " +str(main.l2) + " m",
                             ln = 4, align = 'L')
                            if (main.load_combination2==1):
                                pdf.cell(200,10, txt = "            Load :  UDL - " +str(main.wbc) + " kN/m",
                                 ln = 4, align = 'L')
                            elif (main.load_combination2==2):
                                pdf.cell(200,10, txt = "            Load :  Point Load - " +str(main.pbc) + " kN",
                                 ln = 4, align = 'L')
                            else:
                                pdf.cell(200,10, txt = "            Load :  " ,
                                 ln = 4, align = 'L')
                            if (main.ei2==1):
                                pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI2) + " kN.m^2" ,
                                 ln = 4, align = 'L')
                            elif (main.ei2==2):
                                pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI2) + " kN.m^2",
                                 ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "",
                                     ln = 4, align = 'L')

                            #span cd
                            pdf.cell(200,10, txt = "        For Span CD : - ",
                             ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "            Length : " +str(main.l3) + " m",
                             ln = 4, align = 'L')
                            if (main.load_combination2==1):
                                pdf.cell(200,10, txt = "            Load :  UDL - " +str(main.wcd) + " kN/m",
                                 ln = 4, align = 'L')
                            elif (main.load_combination2==2):
                                pdf.cell(200,10, txt = "            Load :  Point Load - " +str(main.pcd) + " kN",
                                 ln = 4, align = 'L')
                            else:
                                pdf.cell(200,10, txt = "            Load :  " ,
                                 ln = 4, align = 'L')
                            if (main.ei2==1):
                                pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI3) + " kN.m^2" ,
                                 ln = 4, align = 'L')
                            elif (main.ei2==2):
                                pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI3) + " kN.m^2",
                                 ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "",
                                     ln = 4, align = 'L')

                            pdf.cell(200,10, txt = "SOLUTION : - ",
                                     ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "    RA = "+ str(round(calculation.Ra, 3)) + " kN",
                                     ln = 6, align = 'L')
                            pdf.cell(200,10, txt = "    RB = "+ str(round(calculation.Rb, 3)) + " kN",
                                     ln = 7, align = 'L')
                            pdf.cell(200,10, txt = "    RC = "+ str(round(calculation.Rc, 3)) + " kN",
                                     ln = 8, align = 'L')
                            pdf.cell(200,10, txt = "    MB = "+ str(round(calculation.mb, 3)) + " kN.m",
                                     ln = 9, align = 'L')
                            pdf.cell(200,10, txt = "    MC = "+ str(round(calculation.mc, 3)) + " kN.m",
                                     ln = 9, align = 'L')

                            pdf.output("MOS_2_SCE_Group_3_Three Span.pdf")



                        threespan()

                        Repeat = input("Do You Want to Solve another Problem ?")
                        if Repeat == "yes":
                            start()
                        else:
                            print("Thank You....")
                            exit()

                    else :
                        print("Error !")
                calculation()
        main()
        def calculation():
            if (main.end_support==1 and (main.intermediate_support==1 or main.intermediate_support==2)):
                #print("One End Fixed")
                def dlc():
                    if(main.load_combination1==1 and main.load_combination2==2):
                        #for span a'a and ab
                            a1 = (2/3)*((main.wab*main.l1**2)/8)*main.l1
                            #print("a1=",a1)
                            x1 = (main.l1)/2
                            #print("x1",x1)
                            za = (main.wab*main.l1**3)/4
                            #print("za=",za)


                        #for Span ab and bc
                            a1 = (2/3)*((main.wab*main.l1**2)/8)*main.l1
                            #print("a1=",a1)
                            x1 = (main.l1)/2
                            #print("x1",x1)
                            za = (main.wab*main.l1**3)/4
                            #print("za=",za)

                            mmax2=((main.pbc*main.aspan2*main.bspan2)/main.l)
                            #print("mmax2 :",mmax2 )
                            a2 = (1/2)*(mmax2*main.l)
                            #print("a2=",a2)
                            x2 = ((main.l2 + main.bspan2)/3)
                            #print("x2=",x2)
                            zb = ((6*a2*x2)/(main.value_EI2*main.l2))
                            #print("zb=",zb)
                            def momentcal():
                                #a ma + b mb = c
                                #d ma + e mb = f
                                eqn1a=2*((main.l1/main.value_EI1))
                                #print("Value a =", eqn1a)

                                eqn1b=(main.l1/main.value_EI1)
                                #print("Value b =", eqn1b)

                                eqn2c=-za
                                #print("Value c =", eqn2c)

                                eqn2d=(main.l1)
                                #print("Value d =",eqn2d )

                                eqn2e=2*((main.l1/main.value_EI1)+(main.l2/main.value_EI2))
                                #print("Value e =",eqn2e)

                                eqn2f=-za-zb
                                #print("Vlaue f =",eqn2f)

                                n= eqn1a*eqn2e - eqn1b*eqn2d
                                #print("Values of mb and mc is : ")
                                if (n!=0):
                                    calculation.ma=((eqn2c*eqn2e) - (eqn1b*eqn2f))/n
                                    calculation.mb=((eqn1a*eqn2f) - (eqn2c*eqn2d))/n
                                    #print("{:.3f} {:.3f}".format(calculation.ma+0,calculation.mb+0))
                            momentcal()
                            calculation.Ra=((main.wab*main.l1*(main.l1/2))+calculation.ma-calculation.mb)/main.l1
                            print("calculation.Ra = ", calculation.Ra)
                            calculation.Rb1=((main.wab*main.l1)-calculation.Ra)
                            print("calculation.Rb1 = ", calculation.Rb1)
                            calculation.Rb2=(-calculation.mb+(main.pbc*main.bspan2))/main.l2
                            print("calculation.Rb2 = ", calculation.Rb2)
                            calculation.Rb=calculation.Rb1+calculation.Rb2
                            print("calculation.Rb = ", calculation.Rb)
                            calculation.Rc=main.pbc-calculation.Rb2
                            print("calculation.Rc = ", calculation.Rc)
                            print("MA = ", (round(calculation.ma, 3)))
                            print("MB = ", (round(calculation.mb, 3)))
                            raw_input=str(input('PRESS ENTER TO GET PDF!'))
                            def oneendfixed():
                                pdf = FPDF() #Making a PDF Variable
                                pdf.add_page() #Adding a Page
                                pdf.set_font("Arial" , size= 15) #Font ani Size
                                #Actual Printing in PDF Starts here...........
                                pdf.cell(200, 10, txt = "Clapeyron's Theorem of Three Moments",
                                         ln = 1, align = 'C')
                                pdf.cell(200,10, txt = "Two Span Beam",
                                         ln = 2, align = 'C')
                                            #Working on Given Data
                                pdf.cell(200,10, txt = "GIVEN DATA : - ",
                                 ln = 4, align = 'L')
                                 #Use IF Statement
                                if (main.end_support==1):
                                    pdf.cell(200,10, txt = "    End Supports :  Fixed " ,
                                     ln = 4, align = 'L')
                                elif (main.end_support==2):
                                    pdf.cell(200,10, txt = "    End Supports :  Pinned / Hinged " ,
                                     ln = 4, align = 'L')
                                elif (main.end_support==3):
                                    pdf.cell(200,10, txt = "    End Supports :  Simple " ,
                                     ln = 4, align = 'L')
                                elif (main.end_support==4):
                                    pdf.cell(200,10, txt = "    End Supports :  Roller " ,
                                     ln = 4, align = 'L')
                                else:
                                    pdf.cell(200,10, txt = "    End Supports :   " ,
                                     ln = 4, align = 'L')
                                if (main.intermediate_support==1):
                                    pdf.cell(200,10, txt = "    Intermediate Supports : Simple ",
                                     ln = 4, align = 'L')
                                elif (main.intermediate_support==2):
                                    pdf.cell(200,10, txt = "    Intermediate Supports : Roller ",
                                     ln = 4, align = 'L')
                                else:
                                    pdf.cell(200,10, txt = "    Intermediate Supports :  ",
                                     ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "",
                                         ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "    Beam Span Details : - ",
                                 ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "        For Span AB : - ",
                                 ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "            Length : " +str(main.l1) + " m",
                                 ln = 4, align = 'L')
                                if (main.load_combination1==1):
                                    pdf.cell(200,10, txt = "            Load :  UDL - " +str(main.wab) + " kN/m",
                                     ln = 4, align = 'L')
                                elif (main.load_combination2==2):
                                    pdf.cell(200,10, txt = "            Load :  Point Load - " +str(main.pab) + " kN",
                                     ln = 4, align = 'L')
                                else:
                                    pdf.cell(200,10, txt = "            Load :  " ,
                                     ln = 4, align = 'L')
                                if (main.ei1==1):
                                    pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI1) + " kN.m^2" ,
                                     ln = 4, align = 'L')
                                elif (main.ei1==2):
                                    pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI1) + " kN.m^2",
                                     ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "",
                                         ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "        For Span BC : - ",
                                 ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "            Length : " +str(main.l2) + " m",
                                 ln = 4, align = 'L')
                                if (main.load_combination2==1):
                                    pdf.cell(200,10, txt = "            Load :  UDL - " +str(main.wbc) + " kN/m",
                                     ln = 4, align = 'L')
                                elif (main.load_combination2==2):
                                    pdf.cell(200,10, txt = "            Load :  Point Load - " +str(main.pbc) + " kN",
                                     ln = 4, align = 'L')
                                else:
                                    pdf.cell(200,10, txt = "            Load :  " ,
                                     ln = 4, align = 'L')
                                if (main.ei2==1):
                                    pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI2) + " kN.m^2" ,
                                     ln = 4, align = 'L')
                                elif (main.ei2==2):
                                    pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI2) + " kN.m^2",
                                     ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "",
                                         ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "SOLUTION : - ",
                                         ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "    RA = "+ str(round(calculation.Ra, 3)) + " kN",
                                         ln = 6, align = 'L')
                                pdf.cell(200,10, txt = "    RB = "+ str(round(calculation.Rb, 3)) + " kN",
                                         ln = 7, align = 'L')
                                pdf.cell(200,10, txt = "    RC = "+ str(round(calculation.Rc, 3)) + " kN",
                                         ln = 8, align = 'L')

                                pdf.cell(200,10, txt = "    MA = "+ str(round(calculation.ma, 3)) + " kN.m",
                                         ln = 9, align = 'L')
                                pdf.cell(200,10, txt = "    MB = "+ str(round(calculation.mb, 3)) + " kN.m",
                                         ln = 9, align = 'L')
                                #Add Given data info Below

                                #Add Output Data Above

                                #Saving the output in PDF File
                                pdf.output("MOS_2_SCE_Group_3_Fixed.pdf")
                            oneendfixed()
                            Repeat = input("Do You Want to Solve another Problem ?")
                            if Repeat == "yes":
                                start()
                            else:
                                print("Thank You....")
                                exit()


                    elif (main.load_combination1==1 and main.load_combination2==1):
                        #for span a'a and ab
                            a1 = (2/3)*((main.wab*main.l1**2)/8)*main.l1
                            #print("a1=",a1)
                            x1 = (main.l1)/2
                            #print("x1",x1)
                            za = (main.wab*main.l1**3)/4
                            #print("za=",za)

                         #for Span ab and bc
                            a1 = (2/3)*((main.wab*main.l1**2)/8)*main.l1
                            #print("a1=",a1)
                            x1 = (main.l1)/2
                            #print("x1",x1)
                            za = (main.wab*main.l1**3)/4
                            #print("za=",za)

                            a2 = (2/3)*((main.wbc*main.l2**2)/8)*main.l2
                            #print("a2=",a2)
                            x2 = (main.l2)/2
                            #print("x2",x2)
                            zb = (main.wbc*main.l2**3)/4
                            #print("zb=",zb)
                            def momentcal():
                                #a ma + b mb = c
                                #d ma + e mb = f
                                eqn1a=2*((main.l1/main.value_EI1))
                                #print("Value a =", eqn1a)

                                eqn1b=(main.l1/main.value_EI1)
                                #print("Value b =", eqn1b)

                                eqn2c=-za
                                #print("Value c =", eqn2c)

                                eqn2d=(main.l1/main.value_EI1)
                                #print("Value d =",eqn2d )

                                eqn2e=2*((main.l1/main.value_EI1)+(main.l2/main.value_EI2))
                                #print("Value e =",eqn2e)

                                eqn2f=-za-zb
                                #print("Vlaue f =",eqn2f)

                                n= eqn1a*eqn2e - eqn1b*eqn2d
                                #print("Values of ma and mb is : ")
                                if (n!=0):
                                    calculation.ma=((eqn2c*eqn2e) - (eqn1b*eqn2f))/n
                                    calculation.mb=((eqn1a*eqn2f) - (eqn2c*eqn2d))/n
                                    #print("{:.3f} {:.3f}".format(calculation.ma+0,calculation.mb+0))
                            momentcal()
                            calculation.Ra=((main.wab*main.l1*(main.l1/2))+calculation.ma-calculation.mb)/main.l1
                            print("calculation.Ra = ", calculation.Ra)
                            calculation.Rb1=((main.wab*main.l1)-calculation.Ra)
                            print("calculation.Rb1 = ", calculation.Rb1)
                            calculation.Rb2=((-calculation.mb+(main.wbc*main.l2*(main.l2/2)))/main.l2)
                            print("calculation.Rb2 = ", calculation.Rb2)
                            calculation.Rb=calculation.Rb1 + calculation.Rb2
                            print("calculation.Rb = ", calculation.Rb)
                            calculation.Rc=(main.wbc*main.l2)-calculation.Rb2
                            print("calculation.Rc = ", calculation.Rc)
                            raw_input=str(input('PRESS ENTER TO GET PDF!'))
                            def oneendfixed():
                                pdf = FPDF() #Making a PDF Variable
                                pdf.add_page() #Adding a Page
                                pdf.set_font("Arial" , size= 15) #Font ani Size
                                #Actual Printing in PDF Starts here...........
                                pdf.cell(200, 10, txt = "Clapeyron's Theorem of Three Moments",
                                         ln = 1, align = 'C')
                                pdf.cell(200,10, txt = "Two Span Beam",
                                         ln = 2, align = 'C')
                                            #Working on Given Data
                                pdf.cell(200,10, txt = "GIVEN DATA : - ",
                                 ln = 4, align = 'L')
                                 #Use IF Statement
                                if (main.end_support==1):
                                    pdf.cell(200,10, txt = "    End Supports :  Fixed " ,
                                     ln = 4, align = 'L')
                                elif (main.end_support==2):
                                    pdf.cell(200,10, txt = "    End Supports :  Pinned / Hinged " ,
                                     ln = 4, align = 'L')
                                elif (main.end_support==3):
                                    pdf.cell(200,10, txt = "    End Supports :  Simple " ,
                                     ln = 4, align = 'L')
                                elif (main.end_support==4):
                                    pdf.cell(200,10, txt = "    End Supports :  Roller " ,
                                     ln = 4, align = 'L')
                                else:
                                    pdf.cell(200,10, txt = "    End Supports :   " ,
                                     ln = 4, align = 'L')
                                if (main.intermediate_support==1):
                                    pdf.cell(200,10, txt = "    Intermediate Supports : Simple ",
                                     ln = 4, align = 'L')
                                elif (main.intermediate_support==2):
                                    pdf.cell(200,10, txt = "    Intermediate Supports : Roller ",
                                     ln = 4, align = 'L')
                                else:
                                    pdf.cell(200,10, txt = "    Intermediate Supports :  ",
                                     ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "",
                                         ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "    Beam Span Details : - ",
                                 ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "        For Span AB : - ",
                                 ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "            Length : " +str(main.l1) + " m",
                                 ln = 4, align = 'L')
                                if (main.load_combination1==1):
                                    pdf.cell(200,10, txt = "            Load :  UDL - " +str(main.wab) + " kN/m",
                                     ln = 4, align = 'L')
                                elif (main.load_combination2==2):
                                    pdf.cell(200,10, txt = "            Load :  Point Load - " +str(main.pab) + " kN",
                                     ln = 4, align = 'L')
                                else:
                                    pdf.cell(200,10, txt = "            Load :  " ,
                                     ln = 4, align = 'L')
                                if (main.ei1==1):
                                    pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI1) + " kN.m^2" ,
                                     ln = 4, align = 'L')
                                elif (main.ei1==2):
                                    pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI1) + " kN.m^2",
                                     ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "",
                                         ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "        For Span BC : - ",
                                 ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "            Length : " +str(main.l2) + " m",
                                 ln = 4, align = 'L')
                                if (main.load_combination2==1):
                                    pdf.cell(200,10, txt = "            Load :  UDL - " +str(main.wbc) + " kN/m",
                                     ln = 4, align = 'L')
                                elif (main.load_combination2==2):
                                    pdf.cell(200,10, txt = "            Load :  Point Load - " +str(main.pbc) + " kN",
                                     ln = 4, align = 'L')
                                else:
                                    pdf.cell(200,10, txt = "            Load :  " ,
                                     ln = 4, align = 'L')
                                if (main.ei2==1):
                                    pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI2) + " kN.m^2" ,
                                     ln = 4, align = 'L')
                                elif (main.ei2==2):
                                    pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI2) + " kN.m^2",
                                     ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "",
                                         ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "SOLUTION : - ",
                                         ln = 4, align = 'L')
                                pdf.cell(200,10, txt = "    RA = "+ str(round(calculation.Ra, 3)) + " kN",
                                         ln = 6, align = 'L')
                                pdf.cell(200,10, txt = "    RB = "+ str(round(calculation.Rb, 3)) + " kN",
                                         ln = 7, align = 'L')
                                pdf.cell(200,10, txt = "    RC = "+ str(round(calculation.Rc, 3)) + " kN",
                                         ln = 8, align = 'L')

                                pdf.cell(200,10, txt = "    MA = "+ str(round(calculation.ma, 3)) + " kN.m",
                                         ln = 9, align = 'L')
                                pdf.cell(200,10, txt = "    MB = "+ str(round(calculation.mb, 3)) + " kN.m",
                                         ln = 9, align = 'L')
                                #Add Given data info Below

                                #Add Output Data Above

                                #Saving the output in PDF File
                                pdf.output("MOS_2_SCE_Group_3_Fixed.pdf")
                            oneendfixed()
                            Repeat = input("Do You Want to Solve another Problem ?")
                            if Repeat == "yes":
                                start()
                            else:
                                print("Thank You....")
                                exit()
                    elif (main.load_combination1==2 and main.load_combination2==2):

                        mmax1=((main.pab*main.aspan1*main.bspan1)/main.l)
                        #print("mmax1 :",mmax1 )
                        a1 = (1/2)*(mmax1*main.l)
                        #print("a1=",a1)
                        x1 = ((main.l1 + main.aspan1)/3)
                        #print("x1=",x1)
                        za = ((6*a1*x1)/(main.value_EI1*main.l1))
                        #print("za=",za)
                        #Diagram 3
                        mmax2=((main.pbc*main.aspan2*main.bspan2)/main.l)
                        #print("mmax2 :",mmax2 )
                        a2 = (1/2)*(mmax2*main.l)
                        #print("a2=",a2)
                        x2 = ((main.l2 + main.bspan2)/3)
                        #print("x2=",x2)
                        zb = ((6*a2*x2)/(main.value_EI2*main.l2))
                        #print("zb=",zb)
                        def momentcal():
                                #a ma + b mb = c
                                #d ma + e mb = f
                                eqn1a=2*((main.l1/main.value_EI1))
                                #print("Value a =", eqn1a)

                                eqn1b=(main.l1/main.value_EI1)
                                #print("Value b =", eqn1b)

                                eqn2c=-za
                                #print("Value c =", eqn2c)

                                eqn2d=(main.l1/main.value_EI1)
                                #print("Value d =",eqn2d )

                                eqn2e=2*((main.l1/main.value_EI1)+(main.l2/main.value_EI2))
                                #print("Value e =",eqn2e)

                                eqn2f=-za-zb
                                #print("Vlaue f =",eqn2f)

                                n= eqn1a*eqn2e - eqn1b*eqn2d
                                #print("Values of ma and mb is : ")
                                if (n!=0):
                                    calculation.ma=((eqn2c*eqn2e) - (eqn1b*eqn2f))/n
                                    calculation.mb=((eqn1a*eqn2f) - (eqn2c*eqn2d))/n
                                    #print("{:.3f} {:.3f}".format(calculation.ma+0,calculation.mb+0))
                        momentcal()
                        calculation.Ra=((main.pab*main.bspan2)+calculation.ma-calculation.mb)/main.l1
                        print("calculation.Ra = ", calculation.Ra)
                        calculation.Rb1=((main.pab)-calculation.Ra)
                        print("calculation.Rb1 = ", calculation.Rb1)
                        calculation.Rb2=(-calculation.mb+(main.pbc*main.bspan2))/main.l2
                        print("calculation.Rb2 = ", calculation.Rb2)
                        calculation.Rb=calculation.Rb1+calculation.Rb2
                        print("calculation.Rb = ", calculation.Rb)
                        calculation.Rc=main.pbc-calculation.Rb2
                        print("calculation.Rc = ", calculation.Rc)
                        print("MA = ", (round(calculation.ma, 3)))
                        print("MB = ", (round(calculation.mb, 3)))
                        raw_input=str(input('PRESS ENTER TO GET PDF!'))
                        def oneendfixed():
                            pdf = FPDF() #Making a PDF Variable
                            pdf.add_page() #Adding a Page
                            pdf.set_font("Arial" , size= 15) #Font ani Size
                            #Actual Printing in PDF Starts here...........
                            pdf.cell(200, 10, txt = "Clapeyron's Theorem of Three Moments",
                                     ln = 1, align = 'C')
                            pdf.cell(200,10, txt = "Two Span Beam",
                                     ln = 2, align = 'C')
                                        #Working on Given Data
                            pdf.cell(200,10, txt = "GIVEN DATA : - ",
                             ln = 4, align = 'L')
                             #Use IF Statement
                            if (main.end_support==1):
                                pdf.cell(200,10, txt = "    End Supports :  Fixed " ,
                                 ln = 4, align = 'L')
                            elif (main.end_support==2):
                                pdf.cell(200,10, txt = "    End Supports :  Pinned / Hinged " ,
                                 ln = 4, align = 'L')
                            elif (main.end_support==3):
                                pdf.cell(200,10, txt = "    End Supports :  Simple " ,
                                 ln = 4, align = 'L')
                            elif (main.end_support==4):
                                pdf.cell(200,10, txt = "    End Supports :  Roller " ,
                                 ln = 4, align = 'L')
                            else:
                                pdf.cell(200,10, txt = "    End Supports :   " ,
                                 ln = 4, align = 'L')
                            if (main.intermediate_support==1):
                                pdf.cell(200,10, txt = "    Intermediate Supports : Simple ",
                                 ln = 4, align = 'L')
                            elif (main.intermediate_support==2):
                                pdf.cell(200,10, txt = "    Intermediate Supports : Roller ",
                                 ln = 4, align = 'L')
                            else:
                                pdf.cell(200,10, txt = "    Intermediate Supports :  ",
                                 ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "",
                                     ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "    Beam Span Details : - ",
                             ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "        For Span AB : - ",
                             ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "            Length : " +str(main.l1) + " m",
                             ln = 4, align = 'L')
                            if (main.load_combination1==1):
                                pdf.cell(200,10, txt = "            Load :  UDL - " +str(main.wab) + " kN/m",
                                 ln = 4, align = 'L')
                            elif (main.load_combination2==2):
                                pdf.cell(200,10, txt = "            Load :  Point Load - " +str(main.pab) + " kN",
                                 ln = 4, align = 'L')
                            else:
                                pdf.cell(200,10, txt = "            Load :  " ,
                                 ln = 4, align = 'L')
                            if (main.ei1==1):
                                pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI1) + " kN.m^2" ,
                                 ln = 4, align = 'L')
                            elif (main.ei1==2):
                                pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI1) + " kN.m^2",
                                 ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "",
                                     ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "        For Span BC : - ",
                             ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "            Length : " +str(main.l2) + " m",
                             ln = 4, align = 'L')
                            if (main.load_combination2==1):
                                pdf.cell(200,10, txt = "            Load :  UDL - " +str(main.wbc) + " kN/m",
                                 ln = 4, align = 'L')
                            elif (main.load_combination2==2):
                                pdf.cell(200,10, txt = "            Load :  Point Load - " +str(main.pbc) + " kN",
                                 ln = 4, align = 'L')
                            else:
                                pdf.cell(200,10, txt = "            Load :  " ,
                                 ln = 4, align = 'L')
                            if (main.ei2==1):
                                pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI2) + " kN.m^2" ,
                                 ln = 4, align = 'L')
                            elif (main.ei2==2):
                                pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI2) + " kN.m^2",
                                 ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "",
                                     ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "SOLUTION : - ",
                                     ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "    RA = "+ str(round(calculation.Ra, 3)) + " kN",
                                     ln = 6, align = 'L')
                            pdf.cell(200,10, txt = "    RB = "+ str(round(calculation.Rb, 3)) + " kN",
                                     ln = 7, align = 'L')
                            pdf.cell(200,10, txt = "    RC = "+ str(round(calculation.Rc, 3)) + " kN",
                                     ln = 8, align = 'L')

                            pdf.cell(200,10, txt = "    MA = "+ str(round(calculation.ma, 3)) + " kN.m",
                                     ln = 9, align = 'L')
                            pdf.cell(200,10, txt = "    MB = "+ str(round(calculation.mb, 3)) + " kN.m",
                                     ln = 9, align = 'L')
                            #Add Given data info Below

                            #Add Output Data Above

                            #Saving the output in PDF File
                            pdf.output("MOS_2_SCE_Group_3_Fixed.pdf")
                        oneendfixed()
                        Repeat = input("Do You Want to Solve another Problem ?")
                        if Repeat == "yes":
                            start()
                        else:
                            print("Thank You....")
                            exit()

                    elif (main.load_combination1==2 and main.load_combination2==1):
                        mmax1=((main.pab*main.aspan1*main.bspan1)/main.l)
                        #print("mmax1 :",mmax1 )
                        a1 = (1/2)*(mmax1*main.l)
                        #print("a1=",a1)
                        x1 = ((main.l1 + main.aspan1)/3)
                        #print("x1=",x1)
                        za = ((6*a1*x1)/(main.value_EI1*main.l1))
                        #print("za=",za)

                        a2 = (2/3)*((main.wbc*main.l2**2)/8)*main.l2
                        #print("a2=",a2)
                        x2 = (main.l2)/2
                        #print("x2",x2)
                        zb = (main.wbc*main.l2**3)/4
                        #print("zb=",zb)

                        def momentcal():
                                #a ma + b mb = c
                                #d ma + e mb = f
                                eqn1a=2*((main.l1/main.value_EI1))
                                #print("Value a =", eqn1a)

                                eqn1b=(main.l1/main.value_EI1)
                                #print("Value b =", eqn1b)

                                eqn2c=-za
                                #print("Value c =", eqn2c)

                                eqn2d=(main.l1/main.value_EI1)
                                #print("Value d =",eqn2d )

                                eqn2e=2*((main.l1/main.value_EI1)+(main.l2/main.value_EI2))
                                #print("Value e =",eqn2e)

                                eqn2f=-za-zb
                                #print("Vlaue f =",eqn2f)

                                n= eqn1a*eqn2e - eqn1b*eqn2d
                                #print("Values of ma and mb is : ")
                                if (n!=0):
                                    calculation.ma=((eqn2c*eqn2e) - (eqn1b*eqn2f))/n
                                    calculation.mb=((eqn1a*eqn2f) - (eqn2c*eqn2d))/n
                                    #print("{:.3f} {:.3f}".format(calculation.ma+0,calculation.mb+0))
                        momentcal()
                        calculation.Ra=((main.pab*main.bspan1)+calculation.ma-calculation.mb)/main.l1
                        print("calculation.Ra = ", calculation.Ra)
                        calculation.Rb1=((main.pab)-calculation.Ra)
                        print("calculation.Rb1 = ", calculation.Rb1)
                        calculation.Rb2=((-calculation.mb+(main.wbc*main.l2*(main.l2/2)))/main.l2)
                        print("calculation.Rb2 = ", calculation.Rb2)
                        calculation.Rb=calculation.Rb1 + calculation.Rb2
                        print("calculation.Rb = ", calculation.Rb)
                        calculation.Rc=(main.wbc*main.l2)-calculation.Rb2
                        print("calculation.Rc = ", calculation.Rc)
                        print("MA =",calculation.ma)
                        print("MB =",calculation.mb)
                        raw_input=str(input('PRESS ENTER TO GET PDF!'))
                        def oneendfixed():
                            pdf = FPDF() #Making a PDF Variable
                            pdf.add_page() #Adding a Page
                            pdf.set_font("Arial" , size= 15) #Font ani Size
                            #Actual Printing in PDF Starts here...........
                            pdf.cell(200, 10, txt = "Clapeyron's Theorem of Three Moments",
                                     ln = 1, align = 'C')
                            pdf.cell(200,10, txt = "Two Span Beam",
                                     ln = 2, align = 'C')
                                        #Working on Given Data
                            pdf.cell(200,10, txt = "GIVEN DATA : - ",
                             ln = 4, align = 'L')
                             #Use IF Statement
                            if (main.end_support==1):
                                pdf.cell(200,10, txt = "    End Supports :  Fixed " ,
                                 ln = 4, align = 'L')
                            elif (main.end_support==2):
                                pdf.cell(200,10, txt = "    End Supports :  Pinned / Hinged " ,
                                 ln = 4, align = 'L')
                            elif (main.end_support==3):
                                pdf.cell(200,10, txt = "    End Supports :  Simple " ,
                                 ln = 4, align = 'L')
                            elif (main.end_support==4):
                                pdf.cell(200,10, txt = "    End Supports :  Roller " ,
                                 ln = 4, align = 'L')
                            else:
                                pdf.cell(200,10, txt = "    End Supports :   " ,
                                 ln = 4, align = 'L')
                            if (main.intermediate_support==1):
                                pdf.cell(200,10, txt = "    Intermediate Supports : Simple ",
                                 ln = 4, align = 'L')
                            elif (main.intermediate_support==2):
                                pdf.cell(200,10, txt = "    Intermediate Supports : Roller ",
                                 ln = 4, align = 'L')
                            else:
                                pdf.cell(200,10, txt = "    Intermediate Supports :  ",
                                 ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "",
                                     ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "    Beam Span Details : - ",
                             ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "        For Span AB : - ",
                             ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "            Length : " +str(main.l1) + " m",
                             ln = 4, align = 'L')
                            if (main.load_combination1==1):
                                pdf.cell(200,10, txt = "            Load :  UDL - " +str(main.wab) + " kN/m",
                                 ln = 4, align = 'L')
                            elif (main.load_combination2==2):
                                pdf.cell(200,10, txt = "            Load :  Point Load - " +str(main.pab) + " kN",
                                 ln = 4, align = 'L')
                            else:
                                pdf.cell(200,10, txt = "            Load :  " ,
                                 ln = 4, align = 'L')
                            if (main.ei1==1):
                                pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI1) + " kN.m^2" ,
                                 ln = 4, align = 'L')
                            elif (main.ei1==2):
                                pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI1) + " kN.m^2",
                                 ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "",
                                     ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "        For Span BC : - ",
                             ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "            Length : " +str(main.l2) + " m",
                             ln = 4, align = 'L')
                            if (main.load_combination2==1):
                                pdf.cell(200,10, txt = "            Load :  UDL - " +str(main.wbc) + " kN/m",
                                 ln = 4, align = 'L')
                            elif (main.load_combination2==2):
                                pdf.cell(200,10, txt = "            Load :  Point Load - " +str(main.pbc) + " kN",
                                 ln = 4, align = 'L')
                            else:
                                pdf.cell(200,10, txt = "            Load :  " ,
                                 ln = 4, align = 'L')
                            if (main.ei2==1):
                                pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI2) + " kN.m^2" ,
                                 ln = 4, align = 'L')
                            elif (main.ei2==2):
                                pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI2) + " kN.m^2",
                                 ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "",
                                     ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "SOLUTION : - ",
                                     ln = 4, align = 'L')
                            pdf.cell(200,10, txt = "    RA = "+ str(round(calculation.Ra, 3)) + " kN",
                                     ln = 6, align = 'L')
                            pdf.cell(200,10, txt = "    RB = "+ str(round(calculation.Rb, 3)) + " kN",
                                     ln = 7, align = 'L')
                            pdf.cell(200,10, txt = "    RC = "+ str(round(calculation.Rc, 3)) + " kN",
                                     ln = 8, align = 'L')

                            pdf.cell(200,10, txt = "    MA = "+ str(round(calculation.ma, 3)) + " kN.m",
                                     ln = 9, align = 'L')
                            pdf.cell(200,10, txt = "    MB = "+ str(round(calculation.mb, 3)) + " kN.m",
                                     ln = 9, align = 'L')
                            #Add Given data info Below

                            #Add Output Data Above

                            #Saving the output in PDF File
                            pdf.output("MOS_2_SCE_Group_3_Fixed.pdf")
                        oneendfixed()
                        Repeat = input("Do You Want to Solve another Problem ?")
                        if Repeat == "yes":
                            start()
                        else:
                            print("Thank You....")
                            exit()
                dlc()



            elif ((main.end_support==2 or main.end_support==3 or main.end_support==4) and (main.intermediate_support==1 or main.intermediate_support==2)):
                #print("Pined")

                #print("Contineous Beams with UDL on Entire Span")
                #im = Image.open(r"C:\Users\HP\Desktop\MOS 2 SCE\Data\Images\case1.jpeg")
                #im.show()
                #print("Programme will give Values of : Ra , Rb , Rc & Mb")
                #print(" # Note : End moments Ma = Mc = 0, because A & C are simple supports")

                #print("1. Dividing the beam in two simply supported beams....")
                #print("and Find ((6.a1.x1)/(l1)) & ((6.a2.x2)/(l2))....")
                def dlc():
                    if (main.load_combination1==2 and main.load_combination2==2):
                        #print("Point Load on Both Spans")
                        #Case completed 100%
                        #Diagram 2
                        #M.Max(h)
                        mmax1=((main.pab*main.aspan1*main.bspan1)/main.l)
                        #print("mmax1 :",mmax1 )
                        a1 = (1/2)*(mmax1*main.l)
                        #print("a1=",a1)
                        x1 = ((main.l1 + main.aspan1)/3)
                        #print("x1=",x1)
                        za = ((6*a1*x1)/(main.value_EI1*main.l1))
                        #print("za=",za)
                        #Diagram 3
                        mmax2=((main.pbc*main.aspan2*main.bspan2)/main.l)
                        #print("mmax2 :",mmax2 )
                        a2 = (1/2)*(mmax2*main.l)
                        #print("a2=",a2)
                        x2 = ((main.l2 + main.bspan2)/3)
                        #print("x2=",x2)
                        zb = ((6*a2*x2)/(main.value_EI2*main.l2))
                        #print("zb=",zb)
                        calculation.mb = (-za-zb)/(2*((main.l1/main.value_EI1)+(main.l2/main.value_EI2)))
                        #Support Reactions
                        calculation.Ra =(main.pab*main.bspan1+calculation.mb)/(main.l1)
                        calculation.Rc =((main.pbc*main.aspan2)+calculation.mb)/(main.l2)
                        calculation.Rb =(main.pab+main.pbc)-calculation.Ra-calculation.Rc


                    elif (main.load_combination1==1 and main.load_combination2==1):
                        #print("UDL on Both Spans")
                        #Case Completed 100%
                        #Code Here
                        #Diagram 2
                        a1 = (2/3)*((main.wab*main.l1**2)/8)*main.l1
                        #print("a1=",a1)
                        x1 = (main.l1)/2
                        #print("x1",x1)
                        za = (main.wab*main.l1**3)/4
                        #print("za=",za)
                        #Diagram 3
                        a2 = (2/3)*((main.wbc*main.l2**2)/8)*main.l2
                        #print("a2=",a2)
                        x2 = (main.l2)/2
                        #print("x2",x2)
                        zb = (main.wbc*main.l2**3)/4
                        #print("zb=",zb)
                        calculation.mb = (-za-zb)/(2*((main.l1/main.value_EI1)+(main.l2/main.value_EI2)))
                        #Support Reactions
                        calculation.Ra=((main.wab*(main.l1**2)/2)+calculation.mb)/main.l1
                        calculation.Rc=(((main.wbc*(main.l2**2))/2)+calculation.mb)/(main.l2)
                        Rb1 = (main.wab*main.l1) - calculation.Ra
                        Rb2 = (main.wbc*main.l2) - calculation.Rc
                        calculation.Rb = Rb1 + Rb2
                    elif (main.load_combination1==1 and main.load_combination2==2):
                        #print("UDL + Point Load")
                        #Case Completed 100%
                        #Code Here
                        #Diagram 2
                        a1 = (2/3)*((main.wab*main.l1**2)/8)*main.l1
                        #print("a1=",a1)
                        x1 = (main.l1)/2
                        #print("x1",x1)
                        za = (main.wab*main.l1**3)/4
                        #print("za=",za)
                        #Diagram 3
                        mmax2=((main.pbc*main.aspan2*main.bspan2)/main.l)
                        #print("mmax2 :",mmax2 )
                        a2 = (1/2)*(mmax2*main.l)
                        #print("a2=",a2)
                        x2 = ((main.l2 + main.bspan2)/3)
                        #print("x2=",x2)
                        zb = ((6*a2*x2)/(main.value_EI2*main.l2))
                        #print("zb=",zb)
                        calculation.mb = (-za-zb)/(2*((main.l1/main.value_EI1)+(main.l2/main.value_EI2)))
                        #Support Reactions
                        calculation.Ra =((((main.wab)*(main.l1**2))/2)+calculation.mb)/main.l1
                        calculation.Rc =(((main.pbc*main.aspan2)+calculation.mb)/main.l2)
                        calculation.Rb =((main.wab*main.l1)+main.pbc-calculation.Ra-calculation.Rc)
                    elif (main.load_combination1==2 and main.load_combination2==1):
                        #print("Point Load + UDL")
                        #Case Completed 100%
                        #Diagram 2
                        mmax1=((main.pab*main.aspan1*main.bspan1)/main.l)
                        #print("mmax1 :",mmax1 )
                        a1 = (1/2)*(mmax1*main.l)
                        #print("a1=",a1)
                        x1 = ((main.l1 + main.aspan1)/3)
                        #print("x1=",x1)
                        za = ((6*a1*x1)/(main.value_EI1*main.l1))
                        #print("za=",za)
                        #Diagram 3
                        a2 = (2/3)*((main.wbc*main.l2**2)/8)*main.l2
                        #print("a2=",a2)
                        x2 = (main.l2)/2
                        #print("x2",x2)
                        zb = (main.wbc*main.l2**3)/4
                        #print("zb=",zb)
                        calculation.mb = (-za-zb)/(2*((main.l1/main.value_EI1)+(main.l2/main.value_EI2)))
                        #Support Reactions
                        #check code below
                        calculation.Ra = ((main.pab*main.bspan1)+(calculation.mb))/main.l1
                        #print(main.wbc)
                        #print(main.l2)
                        #print(calculation.mb)
                        #print(main.l2)
                        calculation.Rc = (-(((main.wbc)*(main.l2**2))/2)-(calculation.mb))/(-main.l2)


                        calculation.Rb = main.pab+(main.wbc*main.l2)-calculation.Ra-calculation.Rc
                    else :
                        print ("Error")
                dlc()
                print("RA = ",(round(calculation.Ra, 3)), "KN")
                print("RB = ",(round(calculation.Rb, 3)), "KN")
                print("RC = ",(round(calculation.Rc, 3)), "KN")
                print("MB = ",(round(calculation.mb, 3)), "KNM")
                raw_input=str(input('PRESS ENTER TO GET PDF!'))
                Repeat = input("Do You Want to Solve another Problem ?")
                if Repeat == "yes":
                    start()
                else:
                    print("Thank You....")


        calculation()
        def outputpdf():
            def twospan():
                pdf = FPDF() #Making a PDF Variable
                pdf.add_page() #Adding a Page
                pdf.set_font("Arial" , size= 15) #Font ani Size
                #Actual Printing in PDF Starts here...........
                pdf.cell(200, 10, txt = "Clapeyron's Theorem of Three Moments",
                         ln = 1, align = 'C')
                pdf.cell(200,10, txt = "Two Span Beam",
                         ln = 2, align = 'C')
                            #Working on Given Data
                pdf.cell(200,10, txt = "GIVEN DATA : - ",
                 ln = 4, align = 'L')
                 #Use IF Statement
                if (main.end_support==1):
                    pdf.cell(200,10, txt = "    End Supports :  Fixed " ,
                     ln = 4, align = 'L')
                elif (main.end_support==2):
                    pdf.cell(200,10, txt = "    End Supports :  Pinned / Hinged " ,
                     ln = 4, align = 'L')
                elif (main.end_support==3):
                    pdf.cell(200,10, txt = "    End Supports :  Simple " ,
                     ln = 4, align = 'L')
                elif (main.end_support==4):
                    pdf.cell(200,10, txt = "    End Supports :  Roller " ,
                     ln = 4, align = 'L')
                else:
                    pdf.cell(200,10, txt = "    End Supports :   " ,
                     ln = 4, align = 'L')
                if (main.intermediate_support==1):
                    pdf.cell(200,10, txt = "    Intermediate Supports : Simple ",
                     ln = 4, align = 'L')
                elif (main.intermediate_support==2):
                    pdf.cell(200,10, txt = "    Intermediate Supports : Roller ",
                     ln = 4, align = 'L')
                else:
                    pdf.cell(200,10, txt = "    Intermediate Supports :  ",
                     ln = 4, align = 'L')
                pdf.cell(200,10, txt = "",
                         ln = 4, align = 'L')
                pdf.cell(200,10, txt = "    Beam Span Details : - ",
                 ln = 4, align = 'L')
                pdf.cell(200,10, txt = "        For Span AB : - ",
                 ln = 4, align = 'L')
                pdf.cell(200,10, txt = "            Length : " +str(main.l1) + " m",
                 ln = 4, align = 'L')
                if (main.load_combination1==1):
                    pdf.cell(200,10, txt = "            Load :  UDL - " +str(main.wab) + " kN/m",
                     ln = 4, align = 'L')
                elif (main.load_combination2==2):
                    pdf.cell(200,10, txt = "            Load :  Point Load - " +str(main.pab) + " kN",
                     ln = 4, align = 'L')
                else:
                    pdf.cell(200,10, txt = "            Load :  " ,
                     ln = 4, align = 'L')
                if (main.ei1==1):
                    pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI1) + " kN.m^2" ,
                     ln = 4, align = 'L')
                elif (main.ei1==2):
                    pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI1) + " kN.m^2",
                     ln = 4, align = 'L')
                pdf.cell(200,10, txt = "",
                         ln = 4, align = 'L')
                pdf.cell(200,10, txt = "        For Span BC : - ",
                 ln = 4, align = 'L')
                pdf.cell(200,10, txt = "            Length : " +str(main.l2) + " m",
                 ln = 4, align = 'L')
                if (main.load_combination2==1):
                    pdf.cell(200,10, txt = "            Load :  UDL - " +str(main.wbc) + " kN/m",
                     ln = 4, align = 'L')
                elif (main.load_combination2==2):
                    pdf.cell(200,10, txt = "            Load :  Point Load - " +str(main.pbc) + " kN",
                     ln = 4, align = 'L')
                else:
                    pdf.cell(200,10, txt = "            Load :  " ,
                     ln = 4, align = 'L')
                if (main.ei2==1):
                    pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI2) + " kN.m^2" ,
                     ln = 4, align = 'L')
                elif (main.ei2==2):
                    pdf.cell(200,10, txt = "            EI :  " +str(main.value_EI2) + " kN.m^2",
                     ln = 4, align = 'L')
                pdf.cell(200,10, txt = "",
                         ln = 4, align = 'L')
                pdf.cell(200,10, txt = "SOLUTION : - ",
                         ln = 4, align = 'L')
                pdf.cell(200,10, txt = "    RA = "+ str(round(calculation.Ra, 3)) + " kN",
                         ln = 6, align = 'L')
                pdf.cell(200,10, txt = "    RB = "+ str(round(calculation.Rb, 3)) + " kN",
                         ln = 7, align = 'L')
                pdf.cell(200,10, txt = "    RC = "+ str(round(calculation.Rc, 3)) + " kN",
                         ln = 8, align = 'L')
                pdf.cell(200,10, txt = "    MB = "+ str(round(calculation.mb, 3)) + " kN.m",
                         ln = 9, align = 'L')
                #Add Given data info Below

                #Add Output Data Above

                #Saving the output in PDF File
                pdf.output("MOS_2_SCE_Group_3.pdf")
            twospan()
        outputpdf()

    programe()
start()


