import numpy as np
import matplotlib.pyplot as plt

# TODO: Make it work for all possible prompts

def plot_similarities_histogram(similarities: dict,
                                prompts: list[str],
                                *,
                                num_bins: int = 50):

    _, axs = plt.subplots(1, 2, sharex=True, sharey=True)

    axs[0].hist(similarities[prompts[0]], bins=num_bins)
    axs[0].set_title(f"Similarities to \"{prompts[0]}\"")
    axs[0].set_xlabel("Cosine similarity")

    axs[1].hist(similarities[prompts[1]], bins=num_bins)
    axs[1].set_title(f"Similarities to \"{prompts[1]}\"")
    axs[1].set_xlabel("Cosine similarity")

    plt.show()


def plot_similarities_scatter(similarities: dict,
                              prompts: list[str],
                              marginal_idxs: np.ndarray | None = None):

    plt.scatter(similarities[prompts[0]][:1000],
                similarities[prompts[1]][:1000],
                label="Cats")                           # Actual cats
    plt.scatter(similarities[prompts[0]][1000:],
                similarities[prompts[1]][1000:],
                label="Dogs")                           # Actual dogs

    if marginal_idxs is not None:
        plt.scatter(similarities[prompts[0]][marginal_idxs],
                    similarities[prompts[1]][marginal_idxs],
                    label="Marginal")

    plt.xlabel(f"Cosine similarity to \"{prompts[0]}\"")
    plt.ylabel(f"Cosine similarity to \"{prompts[1]}\"")
    plt.legend()

    plt.show()