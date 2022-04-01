def main(x):
    match (x[0]):
        case 2007:
            match (x[2]):
                case 'SMT':
                    match (x[3]):
                        case 'LOGOS':
                            match (x[1]):
                                case 'NCL': return 0
                                case 'POD': return 1
                                case 'AMPL': return 2
                        case 'STATA': return 3
                        case 'KIT':
                            match (x[4]):
                                case 1968: return 4
                                case 1975: return 5
                                case 2011: return 6
                case 'NU': return 7
        case 1977:
            match (x[3]):
                case 'LOGOS': return 8
                case 'STATA':
                    match (x[1]):
                        case 'NCL': return 9
                        case 'POD': return 10
                        case 'AMPL': return 11
                case 'KIT': return 12


print(main([1977, 'AMPL', 'NU', 'KIT', 2011]))
