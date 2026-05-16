# PART F – Vector DB & Semantic Search
## F1 – Theory

# 1. What are Embeddings?
Embeddings are numerical vector representations of text, images, or other data.

Purpose:

Capture semantic meaning
Convert unstructured text into machine-readable vectors
Enable similarity comparison
Example: Product descriptions with similar meanings generate similar embeddings.

Applications:

Semantic search
Recommendation systems
Chatbots
NLP systems

# 2. Why Cosine Similarity Works?
Cosine similarity measures similarity between vectors based on angle rather than magnitude.

Formula: Cosine Similarity = cosine(angle between vectors)

Why it works:

Similar text produces vectors pointing in similar directions
Independent of vector size
Effective for semantic comparison
Interpretation:

Value near 1 → highly similar
Value near 0 → unrelated
Value near -1 → opposite meaning

# 3. Keyword Search vs Semantic Search
Keyword Search
Searches exact matching words.

Characteristics:

Fast
Simple
Fails on synonyms/context
Example: Searching “phone” may not match “smartphone”.

Semantic Search
Understands contextual meaning using embeddings.

Characteristics:

Context-aware
Handles synonyms
Better search relevance
Example: “Gaming device” may match “Gaming Console”.

# 4. What is ANN (Approximate Nearest Neighbour)?
ANN is an optimized search technique for finding similar vectors efficiently.

Purpose:

Speed up similarity search
Avoid brute-force comparison
Handle large vector datasets

Applications:

Vector databases
Recommendation systems
Semantic search engines

Popular ANN libraries:

FAISS
ChromaDB
Annoy
Pinecone

## EMBEDDING CODE

product_data = [

    {
        "product_id": 1,
        "product_name": "Gaming Laptop",
        "category": "Electronics",
        "description": "High performance laptop designed for gaming and graphics intensive applications"
    },

    {
        "product_id": 2,
        "product_name": "Wireless Headphones",
        "category": "Audio",
        "description": "Noise cancelling wireless headphones with premium sound quality"
    },

    {
        "product_id": 3,
        "product_name": "Smartphone",
        "category": "Mobile",
        "description": "Android smartphone with high resolution camera and fast processor"
    },

    {
        "product_id": 4,
        "product_name": "Gaming Console",
        "category": "Entertainment",
        "description": "Next generation gaming console with immersive graphics"
    },

    {
        "product_id": 5,
        "product_name": "Smartwatch",
        "category": "Wearable",
        "description": "Fitness tracking smartwatch with heart rate monitoring"
    }

]

import pandas as pd

products_df = pd.DataFrame(product_data)

products_df

## ChromaDB code
%pip install sentence-transformers chromadb

from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

product_data = [

    {
        "product_id": 1,
        "product_name": "Gaming Laptop",
        "category": "Electronics",
        "description": "High performance laptop designed for gaming and graphics intensive applications"
    },

    {
        "product_id": 2,
        "product_name": "Wireless Headphones",
        "category": "Audio",
        "description": "Noise cancelling wireless headphones with premium sound quality"
    },

    {
        "product_id": 3,
        "product_name": "Smartphone",
        "category": "Mobile",
        "description": "Android smartphone with high resolution camera and fast processor"
    },

    {
        "product_id": 4,
        "product_name": "Gaming Console",
        "category": "Entertainment",
        "description": "Next generation gaming console with immersive graphics"
    },

    {
        "product_id": 5,
        "product_name": "Smartwatch",
        "category": "Wearable",
        "description": "Fitness tracking smartwatch with heart rate monitoring"
    }

]

import pandas as pd

products_df = pd.DataFrame(product_data)

embeddings = model.encode(
    products_df["description"].tolist()
)

client = chromadb.Client()

collection = client.create_collection(
    name="smartgear_products"
)

for idx, row in products_df.iterrows():

    collection.add(

        ids=[str(row["product_id"])],

        embeddings=[embeddings[idx].tolist()],

        documents=[row["description"]],

        metadatas=[

            {
                "product_name": row["product_name"],
                "category": row["category"]
            }

        ]
    )


    def semantic_search(query_text):

    query_embedding = model.encode([query_text])

    results = collection.query(

        query_embeddings=query_embedding.tolist(),

        n_results=3

    )

    return results


    results = semantic_search(
    "high performance gaming device"
)

results



for i in range(len(results["documents"][0])):

    print("\nResult", i + 1)

    print(
        "Product:",
        results["metadatas"][0][i]["product_name"]
    )

    print(
        "Category:",
        results["metadatas"][0][i]["category"]
    )

    print(
        "Description:",
        results["documents"][0][i]
    )


    Result 1
Product: Gaming Laptop
Category: Electronics
Description: High performance laptop designed for gaming and graphics intensive applications

Result 2
Product: Gaming Console
Category: Entertainment
Description: Next generation gaming console with immersive graphics

Result 3
Product: Smartphone
Category: Mobile
Description: Android smartphone with high resolution camera and fast processor