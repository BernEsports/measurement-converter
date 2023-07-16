#           Measurement fun project
#                 Made by Bern
# =====================================

print("Hello, write a number what you want to convert?")
print("1. Kilometers to metres\n"
      "2. Kilometers to cantimetres\n"
      "3. Kilometers to milimetres\n"
      "4. Metres to kilometres\n"
      "5. Metres to cantimetres\n"
      "6. Metres to milimetres\n"
      "7. Kilometers to miles\n"
      "8. Kilometers to yards\n"
      "9. Kilometers to foots\n"
      "0. Next page (1/7)")
first_pginput = input("")

if first_pginput == "1":
      km = input("Enter kilometres: ")
      x = int(km) * 1000
      print(f"{str(km)} is {x} metres")
elif first_pginput == "2":
      km = input("Enter kilometres: ")
      x = int(km) * 100_000
      print(f"{str(km)} is {x} cantimetres")
elif first_pginput == "3":
      km = input("Enter kilometres: ")
      x = int(km) * 1_000_000
      print(f"{str(km)} is {x} milimetres")
elif first_pginput == "4":
      metrs = input("Enter metres: ")
      x = int(metrs) / 1000
      print(f"{str(metrs)} is {x} kilometres")
elif first_pginput == "5":
      metrs = input("Enter metres: ")
      x = int(metrs) * 100
      print(f"{str(metrs)} is {x} cantimetres")
elif first_pginput == "6":
      metrs = input("Enter metres: ")
      x = int(metrs) * 1000
      print(f"{str(metrs)} is {x} milimetres")
elif first_pginput == "7":
      km = input("Enter kilometres: ")
      x = int(km) / 1.609
      print(f"{str(km)} is {x:.2f} miles")
elif first_pginput == "8":
      km = input("Enter kilometres: ")
      x = int(km) * 1094
      print(f"{str(km)} is {x:.2f} yards")
elif first_pginput == "9":
      km = input("Enter kilometres: ")
      x = int(km) * 3281
      print(f"{str(km)} is {x:.2f} foots")

elif first_pginput == "0":
      print("1: Kilometers to inches\n"
          "2. Metres to miles\n"
          "3. Metres to yards\n"
          "4. Metres to foots\n"
          "5. Metres to inches\n"
          "6. Metres to nautical miles\n"
          "7. Cantimetres to miles\n"
          "8. Cantimetres to yards\n"
          "9. Cantimetres to foots\n"
          "0. Next page (2/7)")
      second_pginput = input("")
      if second_pginput == "1":      
            km = input("Enter kilometres: ")
            x = int(km) * 39370
            print(f"{str(km)} is {x:.2f} inches")
      elif second_pginput == "2":      
            metrs = input("Enter metres: ")
            x = int(metrs) / 1609
            print(f"{str(metrs)} is {x:.2f} miles")
      elif second_pginput == "3":      
            metrs = input("Enter metres: ")
            x = int(metrs) * 1.094
            print(f"{str(metrs)} is {x:.2f} yards")
      elif second_pginput == "4":      
            metrs = input("Enter metres: ")
            x = int(metrs) * 3,281
            print(f"{str(metrs)} is {x:.2f} foots")
      elif second_pginput == "5":      
            metrs = input("Enter metres: ")
            x = int(metrs) * 39.37
            print(f"{str(metrs)} is {x:.2f} inches")
      elif second_pginput == "6":      
            metrs = input("Enter metres: ")
            x = int(metrs) / 1852
            print(f"{str(metrs)} is {x:.2f} nautical miles")
      elif second_pginput == "7":      
            cmtr = input("Enter cantimetres: ")
            x = int(cmtr) / 160900
            print(f"{str(cmtr)} is {x:.2f} miles")
      elif second_pginput == "8":      
            cmtr = input("Enter cantimetres: ")
            x = int(cmtr) / 91.44
            print(f"{str(cmtr)} is {x:.2f} yards")
      elif second_pginput == "9":      
            cmtr = input("Enter cantimetres: ")
            x = int(cmtr) / 30.48
            print(f"{str(cmtr)} is {x:.2f} foots")

      elif second_pginput == "0":
            print("1. Cantimetres to inches\n"
              "2. Milimeters to miles\n"
              "3. Milimeters to yards\n"
              "4. Milimeters to foots\n"
              "5. Milimeters to inches\n"
              "6. Miles to kilometers\n"
              "7. Miles to Cantimetres\n"
              "8. Miles to Metres\n"
              "9. Miles to yards\n"
              "0. Next page (3/7)")
            third_pginput = input("")
            if third_pginput == "1":
                  cmtr = input("Enter cantumetres: ")
                  x = int(cmtr) / 2.54
                  print(f"{str(cmtr)} is {x:.2f} inches")
            elif third_pginput == "2":
                  mlmtr = input("Enter milimeters: ")
                  x = int(mlmtr) / 1_609_000
                  print(f"{str(mlmtr)} is {x:.2f} miles")
            elif third_pginput == "3":
                  mlmtr = input("Enter milimeters: ")
                  x = int(mlmtr) / 914.4
                  print(f"{str(mlmtr)} is {x:.2f} yards")
            elif third_pginput == "4":
                  mlmtr = input("Enter milimeters: ")
                  x = int(mlmtr) / 304.8
                  print(f"{str(mlmtr)} is {x:.2f} foots")
            elif third_pginput == "5":
                  mlmtr = input("Enter milimeters: ")
                  x = int(mlmtr) / 25.4
                  print(f"{str(mlmtr)} is {x:.2f} inches")
            elif second_pginput == "6":      
                  miles = input("Enter miles: ")
                  x = int(miles) * 1.609
                  print(f"{str(miles)} is {x:.2f} kilometres")
            elif second_pginput == "7":      
                  miles = input("Enter miles: ")
                  x = int(miles) * 160_900
                  print(f"{str(miles)} is {x:.2f} cantimetres")
            elif second_pginput == "8":      
                  miles = input("Enter miles: ")
                  x = int(miles) * 1609
                  print(f"{str(miles)} is {x:.2f} metres")
            elif second_pginput == "9":      
                  miles = input("Enter miles: ")
                  x = int(miles) * 1760
                  print(f"{str(miles)} is {x:.2f} yards")
                  
            elif third_pginput == "0":
                  print("1. Miles to inches\n"
                  "2. Miles to foots\n"
                  "3. Yards to kilometres\n"
                  "4. Yards to metres\n"
                  "5. Yards to cantimetres"
                  "6. Yards to millimetres\n"
                  "7. Yards to miles\n"
                  "8. Yards to foots\n"
                  "9. Yards to inches\n"
                  "0. Next page (4/6)")
                  fourth_pginput = input("")
                  if fourth_pginput == "1":
                        miles = input("Enter miles: ")
                        x = int(miles) * 63360
                        print(f"{str(miles)} is {x:.2f} inches")
                  elif fourth_pginput == "2":
                        miles = input("Enter miles: ")
                        x = int(miles) * 5280
                        print(f"{str(miles)} is {x:.2f} foots")
                  elif fourth_pginput == "3":
                        yards = input("Enter yards: ")
                        x = int(yards) / 1094
                        print(f"{str(yards)} is {x:.2f} kilometres")
                  elif fourth_pginput == "4":
                        yards = input("Enter yards: ")
                        x = int(yards) / 1.094
                        print(f"{str(yards)} is {x:.2f} metres")
                  elif fourth_pginput == "5":
                        yards = input("Enter yards: ")
                        x = int(yards) * 91.44
                        print(f"{str(yards)} is {x:.2f} cantimetres")
                  elif fourth_pginput == "6":
                        yards = input("Enter yards: ")
                        x = int(yards) * 914.4
                        print(f"{str(yards)} is {x:.2f} milimetres")
                  elif fourth_pginput == "7":
                        yards = input("Enter yards: ")
                        x = int(yards) / 1760
                        print(f"{str(yards)} is {x:.2f} miles")
                  elif fourth_pginput == "8":
                        yards = input("Enter yards: ")
                        x = int(yards) * 3
                        print(f"{str(yards)} is {x:.2f} foots")
                  elif fourth_pginput == "9":
                        yards = input("Enter yards: ")
                        x = int(yards) * 36
                        print(f"{str(yards)} is {x:.2f} inches")

                  elif fourth_pginput == "0":
                        print("1. Foots to kilometres\n"
                      "2. Foots to metres\n"
                      "3. Foots to cantimetres\n"
                      "4. Foots to milimetres\n"
                      "5. Foots to miles\n"
                      "6. Foots to yards\n"
                      "7. Foots to inches\n"
                      "8. Inches to kilometres\n"
                      "9. Inches to metres\n"
                      "0. Next page (5/7)")
                        fifth_pginput = input("")
                        if fifth_pginput == "1":
                              foots = input("Enter foots: ")
                              x = int(foots) / 3281
                              print(f"{str(foots)} is {x:.6f} kilometres")
                        elif fifth_pginput == "2":
                              foots = input("Enter foots: ")
                              x = int(foots) / 3.281
                              print(f"{str(foots)} is {x:.2f} metres")
                        elif fifth_pginput == "3":
                              foots = input("Enter foots: ")
                              x = int(foots) * 30.48
                              print(f"{str(foots)} is {x:.2f} cantimetres")
                        elif fifth_pginput == "4":
                              foots = input("Enter foots: ")
                              x = int(foots) * 304.8
                              print(f"{str(foots)} is {x:.2f} milimetres")
                        elif fifth_pginput == "5":
                              foots = input("Enter foots: ")
                              x = int(foots) / 5280
                              print(f"{str(foots)} is {x:.6f} miles")
                        elif fifth_pginput == "6":
                              foots = input("Enter foots: ")
                              x = int(foots) / 3
                              print(f"{str(foots)} is {x:.2f} yards")
                        elif fifth_pginput == "7":
                              foots = input("Enter foots: ")
                              x = int(foots) * 36
                              print(f"{str(foots)} is {x:.2f} inches")
                        elif fifth_pginput == "8":
                              inches = input("Enter inches: ")
                              x = int(inches) / 39370
                              print(f"{str(inches)} is {x:.2f} kilometres")
                        elif fifth_pginput == "9":
                              inches = input("Enter inches: ")
                              x = int(inches) / 39.37
                              print(f"{str(inches)} is {x:.2f} metres")

                        elif fifth_pginput == "0":
                              print("1. Inches to cantimetres\n"
                          "2. Inches to milimetres\n"
                          "3. Inches to miles\n"
                          "4. Inches to yards\n"
                          "5. Inches to foots\n"
                          "6. Cantimetres to metres\n"
                          "7. Milimetres to metres\n"
                          "8. Kilometres to nautical miles\n"
                          "9. Miles to nautical miles\n"
                          "0. Next page (6/7)")
                        sixth_pginput = input("")
                        if sixth_pginput == "1":
                              inches = input("Enter inches: ")
                              x = int(inches) * 2.54
                              print(f"{str(inches)} is {x:.2f} cantimetres")
                        elif sixth_pginput == "2":
                              inches = input("Enter inches: ")
                              x = int(inches) * 25.4
                              print(f"{str(inches)} is {x:.2f} milimetres")
                        elif sixth_pginput == "3":
                              inches = input("Enter inches: ")
                              x = int(inches) / 63360
                              print(f"{str(inches)} is {x:.2f} miles")
                        elif sixth_pginput == "4":
                              inches = input("Enter inches: ")
                              x = int(inches) / 36
                              print(f"{str(inches)} is {x:.2f} yards")
                        elif sixth_pginput == "5":
                              inches = input("Enter inches: ")
                              x = int(inches) / 12
                              print(f"{str(inches)} is {x:.2f} foots")
                        elif sixth_pginput == "6":
                              cmtr = input("Enter cantimetres: ")
                              x = int(cmtr) / 100
                              print(f"{str(cmtr)} is {x:.2f} metres")
                        elif sixth_pginput == "7":
                              mlmtr = input("Enter milimetres")
                              x = int(mlmtr) / 1000
                              print(f"{str(mlmtr)} is {x:.2f} metres")
                        elif sixth_pginput == "8":
                              km = input("Enter kilometres")
                              x = int(km) / 1.852
                              print(f"{str(km)} is {x:.2f} nautical miles")
                        elif sixth_pginput == "9":
                              miles = input("Enter miles")
                              x = int(miles) / 1.852
                              print(f"{str(miles)} is {x:.2f} nautical miles")


                        elif sixth_pginput == "0":
                              print("1. Yards to nautical miles\n"
                                    "2. Nautical miles to kilometres\n"
                                    "3. Nautical miles to metres\n"
                                    "4. Nautical miles to miles\n"
                                    "5. Nautical miles to yards")
                              seventh_pginput = input("")
                              if seventh_pginput == "1":
                                    yards = input("Enter yards: ")
                                    x = int(yards) / 2025
                                    print(f"{str(yards)} is {x:.2f} nautical miles")
                              elif seventh_pginput == "2":
                                    naut_miles = input("Enter nautical miles: ")
                                    x = int(naut_miles) * 1.852
                                    print(f"{str(naut_miles)} is {x:.2f} kilometres")
                              elif seventh_pginput == "3":
                                    naut_miles = input("Enter nautical miles: ")
                                    x = int(naut_miles) * 1852
                                    print(f"{str(naut_miles)} is {x:.2f} metres")
                              elif seventh_pginput == "4":
                                    naut_miles = input("Enter nautical miles: ")
                                    x = int(naut_miles) * 1.151
                                    print(f"{str(naut_miles)} is {x:.2f} miles")
                              elif seventh_pginput == "5":
                                    naut_miles = input("Enter nautical miles: ")
                                    x = int(naut_miles) * 2025
                                    print(f"{str(naut_miles)} is {x:.2f} yards")