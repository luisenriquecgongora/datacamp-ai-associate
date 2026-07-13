from openai_client import client

def create_embeddings(texts):
    """Embed a single string OR a list of strings with the OpenAI API.

    The Embeddings endpoint accepts both, which is what makes this helper
    reusable: it always returns a LIST of embedding vectors — one vector
    for a single string, several for a list. Batching a list into one API
    call is cheaper and faster than calling the API once per text.
    """
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    response_dict = response.model_dump()

    return [data['embedding'] for data in response_dict['data']]