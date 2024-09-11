from utils import *
from plots import *
from scipy.spatial.distance import cosine
from pathlib import Path



# TODO: Batch images?  --  should work normally due to np.stack
# TODO: Make GPU support better  --  use more GPU
# TODO: TD-1: Is this the best way to define marginal points?


def run_experiment(prompts: list[str], path: Path = Path('./dataset/'), download=False):

    # Loading dataset, CLIP pre-processor and CLIP model
    ds = load_dataset(path, target_type="category", download=download)
    processor = load_processor()
    model = load_model()


    # Sampling 1000 images of cats and dogs (cats come first)
    images = sample_equally(ds)


    # Running model and saving necessary information
    logits_image = []
    logits_text  = []

    embeds_image = []
    embeds_text  = None

    for img in tqdm(images, desc="Processing images"):
        output = run_model(processor, model, [img], prompts)

        logits_image.append( output.logits_per_image.cpu().detach().numpy() )
        logits_text.append(  output.logits_per_text.cpu().detach().numpy()  )

        embeds_image.append( output.image_embeds.cpu().detach().numpy()     )

        # Since the texts are the same, their embeddings are also the same
        if embeds_text is None:
            embeds_text = output.text_embeds.cpu().detach().numpy()


    logits_image = np.stack(logits_image, axis=0)
    logits_text  = np.stack(logits_text, axis=0)

    embeds_image = np.stack(embeds_image, axis=0).squeeze()


    # Calculating cosine similarity between images and texts embeddings

    # Defining cat and dog indexes for better readability
    CAT_IDX = 0
    DOG_IDX = 1

    similarities = {
        prompts[0]: np.array([ cosine(img, embeds_text[CAT_IDX]) for img in embeds_image ]),
        prompts[1]: np.array([ cosine(img, embeds_text[DOG_IDX]) for img in embeds_image ])
    }

    # Calculating marginal points - points that have low similarity for both prompts
    NUM_MARGINAL = 10
    marginal_indexes = (similarities[prompts[0]] * similarities[prompts[1]]).argsort()[:NUM_MARGINAL]   # TD-1

    plot_similarities_histogram(similarities, prompts)
    plot_similarities_scatter(similarities, prompts)
    plot_similarities_scatter(similarities, prompts, marginal_indexes)


    # Plotting marginal images
    marginal_images = [ images[m_idx] for m_idx in marginal_indexes ]
    for img in marginal_images:
        img.show()


def run_accuracy_experiment(path: Path = Path('./dataset/'), download=False):

    # Loading dataset, CLIP pre-processor and CLIP model
    ds = load_dataset(path, target_type="category", download=download)
    processor = load_processor()
    model = load_model()


    # Creating prompts
    class_names = [
        "Abyssinian", "American Bulldog", "American Pit Bull Terrier", "Basset Hound",
        "Beagle", "Bengal", "Birman", "Bombay", "Boxer", "British Shorthair", "Chihuahua",
        "Egyptian Mau", "English Cocker Spaniel", "English Setter", "German Shorthaired",
        "Great Pyrenees", "Havanese", "Japanese Chin", "Keeshond", "Leonberger", "Maine Coon",
        "Miniature Pinscher", "Newfoundland", "Persian", "Pomeranian", "Pug", "Ragdoll", 
        "Russian Blue", "Saint Bernard", "Samoyed","Scottish Terrier", "Shiba Inu", "Siamese", 
        "Sphynx", "Staffordshire Bull Terrier", "Wheaten Terrier", "Yorkshire Terrier"
    ]
    prompts = [ f"A photo of a {c}, a type of pet" for c in class_names ]


    # Running model and saving necessary information
    logits_image = []
    labels = []

    for img, label in tqdm(ds, desc="Processing images"):
        output = run_model(processor, model, [img], prompts)

        logits_image.append( output.logits_per_image.cpu().detach().numpy() )
        labels.append(       label                                          )


    # Transforming logit activation in a probabilistic distribution
    logits_image = np.stack(logits_image, axis=0).squeeze()
    preds = logits_image.argmax(axis=1)

    
    # Calculating and printing accuracy
    acc = (preds == labels).mean()
    print(f"CLIP accuracy on Oxford-IIIT Pets: {acc * 100:.3f}%")
