print(
    sum(
        e * all(
            list(
                map(
                    eval,
                    l.strip()
                    .replace(" blue", "<15")
                    .replace(" green", "<14")
                    .replace(" red", "<13")
                    .replace(", ", " and ")
                    .split(": ")[-1]
                    .split("; "),
                )
            )
        )
        for e, l in enumerate(open("day2.txt"), 1)
    )
)
