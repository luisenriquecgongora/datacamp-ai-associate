# Import the necessary libraries
import pandas as pd
from openai_client import client
import json

# Load the data
df = pd.read_csv("data/transcriptions.csv")
df.head()

## Start coding here, use as many cells as you need
## Generate a table with age, medical specialty and recommended treatment

import pandas as pd
import json

system_message = """
    You are an expert on data analysis. You are going to receive a transcription. Extract the age, medical specialty and match the recommended treament with a corresponding International Classification of Diseases (ICD) code.
"""

function_definition = [
    {
        "type": "function",
        "function": {
            "name": "extract_medical_data",
            "description": "Get the age, medical_specialty and ICD code fro the transcript",
            "parameters": {
                "type": "object",
                "properties": {
                    "age": {
                        "type": "string",
                        "description": "Age of the patient",
                    },
                    "recommended_treatment": {
                        "type": "string",
                        "description": "Recommended Treatment",
                    },
                    "icd_code": {
                        "type": "string",
                        "description": "International Classification of Diseases matching the recommended treatment described in the transcript",
                    },
                },
                "required": ["age", "recommended_treatment", "icd_code"],
            },
        },
    }
]

def getStructuredTranscript(transcription):
    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
          {
            "role": "system",
            "content": system_message
          },
          {
            "role": "user",
            "content": transcription
          }
      ],
        tools=function_definition,
        tool_choice={'type': 'function', 'function': {'name': 'extract_medical_data'}},
    )
    # The arguments are returned as a JSON string, so we need to parse them
    arguments = response.choices[0].message.tool_calls[0].function.arguments
    return json.loads(arguments)

rows = []

for _, row in df.iterrows():
    response = getStructuredTranscript(row['transcription'])
    rows.append({
        "age": response["age"],
        "medical_specialty": row["medical_specialty"],
        "recommended_treatment": response["recommended_treatment"],
        "icd_code": response["icd_code"],
    })

df_structured = pd.DataFrame(rows, columns=["age", "medical_specialty", "recommended_treatment", "icd_code"])

df_structured.head()
print(df_structured)