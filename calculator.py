while True:
    var = input('Qual tipo de medida você quer converter para metros? ').lower().strip()
    m = float(input('Quantos metros você quer converter para {} ? ' .format(var)))

    dam = m / 10

    hm =  dam / 10

    km = hm / 10 

    dm = m * 10

    cm = dm * 10 

    mm = cm * 10

    if var == 'dam' or var == 'decametro' or var == 'decâmetro' or var == 'decametros' or var == 'decâmetros':
      print(' {} m são {} {}' .format(m,dam,var))
    elif var == 'hm' or var == 'hectometro' or var == 'hectômetro' or var == 'hectometros' or var == 'hectômetros':
        print(' {} m são {} {}' .format(m,hm,var))
    elif var == 'km' or var == 'quilometro' or var == 'quilômetro' or var == 'quilómetro' or var == 'quilometros' or var == 'quilômetros' or var == 'quilómetros':
          print(' {} m são {} {}' .format(m,km,var))
    elif var == 'dm' or var == 'decimetro' or var == 'decímetro' or var == 'decimetros' or var == 'decímetros':
           print(' {} m são {} {}' .format(m,dm,var))
    elif var ==  'cm' or var == 'centimetro' or var == 'centímetro' or var == 'centimetros' or var == 'centímetros':
        print(' {} m são {} {}' .format(m,cm,var))
    elif var == 'mm' or var == 'milimetro' or var == 'milímetro' or var == 'milimetros' or var == 'milímetros':
        print(' {} m são {} {}' .format(m,mm,var))   
    elif var == 'm' or var == 'metro' or var == 'metros':
        print('Já ta em metro animal!')    
    else:
       print('Tente novamente usando outro tipo de medida!')            
