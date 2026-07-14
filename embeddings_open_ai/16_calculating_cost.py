import tiktoken

# Sample of Netflix title descriptions (preloaded as `documents` on DataCamp)
documents = ["In his hometown of Wilmington, Delaware, comedian Kevin Hart takes the stage for a stand-up special full of laughs and personal stories.",
             "A talented batch of amateur bakers face off in a 10-week competition, whipping up their best dishes in the hopes of being named the U.K.'s best.",
             "After a devastating earthquake hits Mexico City, trapped survivors from all walks of life wait to be rescued while trying desperately to stay alive.",
             "When an army recruit is found dead, his fellow soldiers are forced to confront a terrifying secret that's haunting their jungle island training camp."]

# Load the encoder for the OpenAI text-embedding-3-small model
enc = tiktoken.encoding_for_model("text-embedding-3-small")

# Encode each text in documents and calculate the total tokens
total_tokens = sum(len(enc.encode(document)) for document in documents)

cost_per_1k_tokens = 0.00002

# Display number of tokens and cost
print('Total tokens:', total_tokens)
print('Cost:', total_tokens*cost_per_1k_tokens/1000)