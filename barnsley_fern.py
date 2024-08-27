def compute_and_plot_barnsley_fern(
    *,
    stepcount: int = int(1e6),
    scatter_size: int | float = 1e-3,
    color: str = "purple",
    x=[0],
    y=[0]
) -> None:
    import matplotlib.pyplot as plt
    from random import randint

    for i in range(stepcount):
        random_int = randint(1, 100)

        if random_int == 1:
            "generating the stems with P=1%"
            x.append(0)
            y.append(0.16 * (y[i]))
        elif random_int <= 86:
            "generating succcessive sub-ferns with P=85%"
            x.append(0.85 * (x[i]) + 0.04 * (y[i]))
            y.append(-0.04 * (x[i]) + 0.85 * (y[i]) + 1.6)
        elif random_int <= 93:
            "generating first left sub-fern with P=7%"
            x.append(0.2 * (x[i]) - 0.26 * (y[i]))
            y.append(0.23 * (x[i]) + 0.22 * (y[i]) + 1.6)
        else:
            "generating first right sub-fern with P=7%"
            x.append(-0.15 * (x[i]) + 0.28 * (y[i]))
            y.append(0.26 * (x[i]) + 0.24 * (y[i]) + 0.44)
    plt.scatter(x, y, s=scatter_size, edgecolor=color)
    plt.show()


if __name__ == "__main__":
    "https://en.wikipedia.org/wiki/Barnsley_fern"
    compute_and_plot_barnsley_fern()
