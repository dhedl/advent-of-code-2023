print(
    sum(
        list(
            eval(
                str(
                    tuple(
                        dict(
                            map(
                                lambda x: (x[0], len(x)), 
                                sorted(
                                    map(
                                        eval, 
                                        l.strip()
                                        .replace(" blue","*'b'")
                                        .replace(" green","*'g'")
                                        .replace(" red","*'r'")
                                        .replace(";", ",")
                                        .split(": ")[-1]
                                        .split(",")
                                        )
                                    )
                                )
                            ).values()
                                
                        )
                    ).replace(',','*')
                                        
                ) 
            for l in open("day2.txt")
        )
    )
)