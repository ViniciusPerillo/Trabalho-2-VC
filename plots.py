import matplotlib.pyplot as plt

# TODO: Make it work for all possible prompts

def plot_similarities_histogram(similarities: dict):
    NUM_BINS = 50

    _, axs = plt.subplots(1, 2, sharex=True, sharey=True)

    axs[0].hist(similarities["Cat"], bins=NUM_BINS)
    axs[0].set_title("Similarities to \"Cat\"")
    axs[0].set_xlabel("Cosine similarity")

    axs[1].hist(similarities["Dog"], bins=NUM_BINS)
    axs[1].set_title("Similarities to \"Dog\"")
    axs[1].set_xlabel("Cosine similarity")

    plt.show()


# TODO: Add legend to the scatterplot
def plot_similarities_scatter(similarities: dict):
    points_color = [0]*1000 + [1]*1000

    plt.scatter(similarities["Cat"], similarities["Dog"], c=points_color)
    plt.xlabel("Cosine similarity to \"Cat\"")
    plt.ylabel("Cosine similarity to \"Dog\"")
    # plt.legend(labels=["Cat", "Dog"])

    plt.show()